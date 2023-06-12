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



## Find Path

### Request

`POST /path`


{
    "start": 출발지점 (float),
    "end": 도착지점
}
#### example
{
    "start": 416,
    "end": 406
}


### Response



{
    "path": [] distance => 거리, angle => 회전각
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

