# Mexico States 

Mexico states is a API that download pdf from state or get GEOJSON from all states

## Installation

you can set the enviroment variable MAPBOX_TOKEN manually:

In windows
```bash
set MAPBOX_TOKEN=<token-key>
```

In Linux
```bash
export MAPBOX_TOKEN=<token-key>
```

## Usage

```python
import os

# get token from envs
token_mapbox = os.getenv('MAPBOX_TOKEN')

```

## Get PDF form State

### Request

`GET /states/pdf/:id_state`

    curl -G -o test.pdf http://localhost:8080/states/pdf/5/

    # -G is get Request
    # -o is the path from output pdf 

### Response

    % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                    Dload  Upload   Total   Spent    Left  Speed
    100 40198  100 40198    0     0   219k      0 --:--:-- --:--:-- --:--:--  220k

## Get GeoJSON from all states

### Request

`GET /states/`

    curl -G http://localhost:8080/states/

### Response

    GET /states/ HTTP/1.1
    Host: localhost:8080
    User-Agent: curl/7.79.1
    Accept: */*

    HTTP 1.0, assume close after body
    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 116802
    Server: Werkzeug/2.0.2 Python/3.7.11
    Date: Thu, 24 Feb 2022 19:05:54 GMT

    {}

