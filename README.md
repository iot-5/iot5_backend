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
  "data": [
    {
      "mac": "91:9f:33:5c:23:09",
      "rssi": 30
    },
    {
      "mac": "95:1f:33:ac:35:3a",
      "rssi": 50
    },
    {
      "mac": "96:7f:23:55:29:87",
      "rssi": 69
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
