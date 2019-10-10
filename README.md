# MP Vehicle Search API
<h4> NOTE: </h4>

> * The repository & code is for educational purpose only. <br>
> * The terms of MP Transport Website prohibits the use of automated tools such as any spider,
robot, or automated searching or "scraping" tool) to monitor, access or copy any
content from their website. <br>

> * Use at your own risk.
<br>
>
<h2> Usage </h2>

<code>pip install -r requirements.txt</code><br>
<code>python app.py </code>

## API Usage
### API Base URL: 'http://mp-vehicle.herokuapp.com/'

## Endpoint
 GET: [`/regis-num/<registrationnum>`]
 
#### Example
Example usage: `GET http://mp-vehicle.herokuapp.com/regis-num/MP12MA1222` <br>

Example result:
```json
{
    message: "Record found!",
    status: "200",
    veh_chassis_no: "05G29F03874",
    veh_class: "MOTOR CYCLE",
    veh_colour: "P BLACK",
    veh_engine_no: "05G29E03219",
    veh_maker: "HERO HONDA MOTORS",
    veh_manufacture_year: "2005",
    veh_model: "CD DAWN DLX",
    veh_owner_name: "AMIT KUMAR  ",
    veh_recent_owner_count: "1",
    veh_regis_date: "01-04-2006",
    veh_regis_num: "MP12MA1222",
    veh_rto_name: "KHANDWA",
}
```

