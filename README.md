# iot5_backend


## Add Point

### Request

`POST /addpoint/`

{
  "name": "p3",
  "data": [
    {
      "91:9f:33:5c:23:09": 30
    },
    {
      "95:1f:33:ac:35:3a": 50
    },
    {
      "96:7f:23:55:29:87": 70
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

`POST /addpoint/`

{
  "name": "p2",
  "data": [
    {
      "mac": "95:1f:33:ac:35:11",
      "rssi": 40
    },
    {
      "mac": "91:9f:33:5c:23:02",
      "rssi": 20
    },
    {
      "mac": "96:7f:23:55:29:11",
      "rssi": 50
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

