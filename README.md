# iot5_backend

### MAIN - https://github.com/Yoon-Hae-Min/Introduction-to-Internet-of-Things-team-5


## Train location

### Request

`POST /train`

{
  "name": "location_name",
  "data": [
    {
      "ssid": "AP3",
      "bssid": "94:64:24:9f:03:A9",
      "quality": 20
    },
    {
      "ssid": "AP3",
      "bssid": "AA:BB:CC:DD:EE:A9",
      "quality": 10
    }
  ]
}


### Response

    HTTP/1.1 200 OK
    Server: Werkzeug/2.3.4 Python/3.8.9
    Date: Sun, 28 May 2023 08:49:53 GMT
    Content-Type: application/json
    Content-Length: 40
    Connection: close

    {"message":"Point added successfully."}



## Predict my location

### Request

`POST /predict`

{
  "data": [
    {
      "ssid": "AP3",
      "bssid": "94:64:24:9f:03:A9",
      "quality": 20
    },
    {
      "ssid": "AP3",
      "bssid": "AA:BB:CC:DD:EE:A9",
      "quality": 10
    }
  ]
}


### Response

    HTTP/1.1 200 OK
    Server: Werkzeug/2.3.4 Python/3.8.9
    Date: Sun, 28 May 2023 08:51:21 GMT
    Content-Type: application/json
    Content-Length: 18
    Connection: close

    {"location":"p3"}



## GET LOCATIONS LIST

### Request
`GET /locations`


### Response
{"locations":["433","426","514","435","406","504","428","5\uce35\uacc4\ub2e85","427","421","414f","512","529","5\uce35\uc5d8\ubca03","430","405","532","412f","409b","403f","5\uce35\uacc4\ub2e82","418","524","521","425","533","432","507","5\uce35\uc5d8\ubca02","501","525","531","407A","429","403b","516","508","404","416","434","404f","423","530","411","5\uce35\uacc4\ub2e82 ","522","404b","414b","539","503","419","431","5\uce35\uacc4\ub2e83","405b","519","405f","409f","420","408f","518","51p","528","cube_s","402","526","523","407","505","527","513","520","413f","415f","5\uce35\uacc4\ub2e84","512f","515","cube","","408b","424","415b","5\uce35\uc5d8\ubca01","422","cube_n","410b","509","417","413b","507A","511","506","5\uce35\uacc4\ub2e81","510","502","410f","412b","401","517"]}
## Find Path

### Request

`POST /path`


{
    "start": 출발지점 (string),<br>
    "end": 도착지점
}
#### example

{
    "start": "416",
    "end": "406"
}


### Response



{
    "path": [] distance => 거리, angle => 회전각, <br>
    "start_direction": "right" or "left" or 개발중 - "top" or "bottom"
}

#### example
{
    "path": [
        {
            "distance": 36
        },
        {
            "angle": 90.0
        },
        {
            "distance": 23
        },
        {
            "angle": 302.2756443145776
        },
        {
            "distance": 4
        },
        {
            "angle": 342.31327441829706
        },
        {
            "distance": 4
        }
    ],
    "start_direction": "right"
}

