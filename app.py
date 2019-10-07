from flask import Flask, jsonify
from werkzeug.exceptions import HTTPException
from http.cookiejar import LWPCookieJar
from bs4 import BeautifulSoup
import mechanize
from proj_constants import BASE_URL
app = Flask(__name__)


@app.route('/regis-num/<reg_num>')
def api_article(reg_num):
    data = {}
    br = mechanize.Browser()
    # Cookie Jar
    cj = LWPCookieJar()
    br.set_cookiejar(cj)

    # Browser options
    br.set_handle_equiv(True)
    br.set_handle_gzip(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)

    # Follows refresh 0 but not hangs on refresh > 0
    br.set_handle_refresh(mechanize.HTTPRefreshProcessor(), max_time=1)

    # User-Agent (this is cheating, ok?)
    br.addheaders = [('User-agent',
                      'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 '
                      'Firefox/3.0.1')]

    br.set_handle_robots(False)
    br.open(BASE_URL)
    br.select_form(name='aspnetForm')
    br["ctl00$ContentPlaceHolder1$txtRegNo"] = reg_num
    res = br.submit()
    content = res.read()
    soup = BeautifulSoup(content)
    table = soup.find("table", {"border": "1", "id": "ctl00_ContentPlaceHolder1_grvSearchSummary"})
    # Extracting useful information
    for row in table.findAll('tr', {'class': 'GridItem'}):
        col = row.findAll('td')
        reg_num = col[2].find('a').string
        chassis_no = col[3].string
        eng_no = col[4].string
        owner = col[5].string
        rto = col[6].string
        man_year = col[7].string
        reg_date = col[8].string
        owner_count = col[9].string
        color = col[11].string
        veh_class = col[12].string
        maker = col[13].string
        model = col[14].string

        # Constructing json
        data = {
            'status': '200',
            'message': 'Record found!',
            'veh_regis_num': reg_num,
            'veh_model': model,
            'veh_owner_name': owner,
            'veh_rto_name': rto,
            'veh_regis_date': reg_date,
            'veh_chassis_no': chassis_no,
            'veh_engine_no': eng_no,
            'veh_manufacture_year': man_year,
            'veh_colour': color,
            'veh_class': veh_class,
            'veh_maker': maker,
            'veh_recent_owner_count': owner_count
        }

    # If The reg_num was invalid
    message = None
    for row in table.findAll('tr', {'class': 'GridEmpty'}):
        col = row.findAll('td')
        message = col[0].string

        # Constructing JSON
        invalid_data = {
            'status': '999',
            'message': message
        }
    response = jsonify(data)
    if message == "No record found......":
        response = jsonify(invalid_data)

    return response


@app.errorhandler(HTTPException)
def page_not_found(e):
    data = {
        'status': str(e.code),
        'message': str(e.description)
    }
    return jsonify(data)


if __name__ == '__main__':
    app.run()
