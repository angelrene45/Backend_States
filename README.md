# ![logo](/app/static/logo.png) Mexico States (Flask Project)

Mexico states is a API that download pdf from state or get GEOJSON from all states

## Example PDF 
For create the PDF use PyFPDF and the picture is a static image that generate with a GeoJSON in the API Mapbox  
![PDF](/app/static/pdf_test.png)

## Installation

You need to create .env file inside env folder and set the enviroment variables MAPBOX_TOKEN and SECRET_KEY:

```env
SECRET_KEY=<here_write_super_secret_key>
MAPBOX_TOKEN=<here_write_mapbox_token>
```

## Get PDF form State

`GET /states/pdf/:id_state`

    curl -G -o test.pdf http://angelrene45.pythonanywhere.com/states/pdf/5

    # -G is get Request
    # -o is the path from output pdf 


## Get GeoJSON from all states

`GET /states/`

    curl -G http://angelrene45.pythonanywhere.com/states/

## Register new User

`POST /users/signup`

    curl -d '{"name":"juan","email":"exampgmail.com","password":"mypassword"}' -H "Content-Type: application/json" -X POST http://angelrene45.pythonanywhere.com/users/signup

## Login User

`POST /users/login`

    curl -d '{"email":"exampgmail.com","password":"mypassword"}' -H "Content-Type: application/json" -X POST http://angelrene45.pythonanywhere.com/users/login

## Logout User

`POST /users/logout`

    curl -G http://angelrene45.pythonanywhere.com/users/logout


