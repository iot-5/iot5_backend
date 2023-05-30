# iot5_backend


## Add Point

### Request

`POST /train`

{
  "name": "location_name",
  "data": [
    {
      "ssid": "AP3",
      "mac": "94:64:24:9f:03:A9",
      "quality": 20
    },
    {
      "ssid": "AP3",
      "mac": "AA:BB:CC:DD:EE:A9",
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



## Get My Point

### Request

`POST /predict`

{
  "data": [
    {
      "ssid": "AP3",
      "mac": "94:64:24:9f:03:A9",
      "quality": 20
    },
    {
      "ssid": "AP3",
      "mac": "AA:BB:CC:DD:EE:A9",
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

