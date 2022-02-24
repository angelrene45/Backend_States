import os
import json
import urllib3
import urllib.parse

from app import app
from app.module_states.pdf_state import PDF_STATE

http = urllib3.PoolManager()

def generate_pdf( state_object ):
    id_state = state_object.id
    name = state_object.name
    geojson = state_object.geojson

    data_geojson = json.loads(geojson)
    type_geom  = data_geojson.get('type')

    pdf = PDF_STATE('P', 'mm', 'Letter')
    pdf.title_header = name
    pdf.set_title(name)
    pdf.set_author('angel.calzada')
    pdf.add_page()
    pdf.print_attribute(f'ID: {id_state}')
    pdf.print_attribute(f'Type Geometry: {type_geom}')

    path_image = request_image_mapbox( id_state, data_geojson )
    if not path_image: return None
    else: pdf.setImageGeoJSON( path_image )
    
    return pdf.output(dest="S", name=name).encode('latin-1') # generate pdf in memory


def request_image_mapbox( id_state, data_geojson ):
    path_image = os.path.join( app.config['STATIC_FOLDER'], 'states', f'{id_state}.png' )
    
    geojson =  {
            "type": "FeatureCollection",
            "features": [
                {
                    "type": "Feature",
                    "properties": {
                        "stroke": "#000000",
                        "fill": "#005776",
                        "fill-opacity": 1
                    },
                    "geometry": data_geojson
                }
            ]
        }
    geojson = json.dumps(geojson).replace(" ", "") # convert diccionary in string and replace spaces
    geojson = urllib.parse.quote( geojson ) # convert string json in url encoded
    token_mapbox = os.getenv('MAPBOX_TOKEN') # get token from env 
    api_request = f"""https://api.mapbox.com/styles/v1/mapbox/streets-v11/static/geojson({geojson})/auto/630x360?access_token={token_mapbox}"""
    bytes_image = make_request_api( api_request )
    if not bytes_image: return False
    path_image = save_image(path_image, bytes_image)
    if not path_image: return False
    return path_image 

def make_request_api( api_request ):
    try:
        response = http.request("GET", api_request, timeout=4.0)
        if response.status != 200: return None
        bytes_image = response.data # reponse is Image PNG
        return bytes_image
    except Exception as e:
        print(f"Error in request API ")
        print(f"{e}")
        return None

def save_image( path_image, bytes_image ):
    with open(path_image, 'wb') as f: # Save image in static files 
        f.write(bytes_image)

    if os.path.exists( path_image ): return path_image
    else: return False
        
   

