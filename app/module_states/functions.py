import os
import json
import datetime
import urllib3
import urllib.parse

from app import app
from app.module_states.pdf_state import PDF_STATE

http = urllib3.PoolManager()

def generate_pdf( state_object ):
    """
        Method that generate PDF from state
    """
    id_state = state_object.id
    name = state_object.name
    geojson = state_object.geojson

    data_geojson = json.loads(geojson) # convert string to diccionary
    type_geom  = data_geojson.get('type') # get type of geometry 

    pdf = PDF_STATE('P', 'mm', 'Letter') # crate Object from PDF
    pdf.title_header = name
    pdf.set_title(name)
    pdf.set_author('angel.calzada')
    pdf.add_page()
    pdf.print_attribute(f'ID: {id_state}')
    pdf.print_attribute(f'Type Geometry: {type_geom}')

    path_image = request_image_mapbox( id_state, data_geojson ) # Call API mapbox to create image from GeoJSON
    if not path_image: return None
    else: pdf.setImageGeoJSON( path_image )

    delete_image( path_image )
    
    return pdf.output(dest="S", name=name).encode('latin-1') # generate pdf in memory


def request_image_mapbox( id_state, data_geojson ):
    """
        Method that do request to API mapbox 
        Create and image from GeoJSON
    """
    # path where image save
    suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S") # create at unique suffix
    path_image = os.path.join( app.config['STATIC_FOLDER'], 'states', f'{id_state}_{suffix}.png' )
    
    # geojson request from mapbox API
    geojson =  {
            "type": "FeatureCollection",
            "features": [
                {
                    "type": "Feature",
                    "properties": {
                        "stroke": "#000000",
                        "fill": "#005776",
                        "fill-opacity": 0.5
                    },
                    "geometry": data_geojson
                }
            ]
    }

    # Convert diccionary to url encoded
    geojson = json.dumps(geojson).replace(" ", "") # convert diccionary in string and replace spaces
    geojson = urllib.parse.quote( geojson ) # convert string json in url encoded
    # Get mapbox token for request
    token_mapbox = os.getenv('MAPBOX_TOKEN')
    # Full url from api request
    api_request = f"""https://api.mapbox.com/styles/v1/mapbox/streets-v11/static/geojson({geojson})/auto/550x360?access_token={token_mapbox}"""
    # Do request 
    bytes_image = make_request_api( api_request )
    # Validate response 
    if not bytes_image: return False
    # save image in static files 
    path_image = save_image(path_image, bytes_image)
    # Validate exist path_image
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

def delete_image( path_image ):
    try:
        os.remove( path_image )
        return True
    except Exception as e:
        print(f"Error to remove image {path_image}")
        print(e)
        return False
        
   

