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


## Get GeoJSON from all states

### Request

`GET /states/`

    curl -G http://localhost:8080/states/

## Register new User

### Request

`POST /users/signup`

    curl -d '{"name":"juan","email":"exampgmail.com","password":"mypassword"}' -H "Content-Type: application/json" -X POST http://localhost:8080/users/signup

## Login User

### Request

`POST /users/login`

    curl -d '{"email":"exampgmail.com","password":"mypassword"}' -H "Content-Type: application/json" -X POST http://localhost:8080/users/login


