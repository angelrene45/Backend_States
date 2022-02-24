import json

from  app.module_states.pdf_state import PDF_STATE

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
    
    return pdf.output(dest="S", name=name).encode('latin-1') # generate pdf in memory