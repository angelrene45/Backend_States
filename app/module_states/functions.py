import json
from fpdf import FPDF

def generate_pdf( state_object ):
    id_state = state_object.id
    name = state_object.name
    geojson = state_object.geojson

    data_geojson = json.loads(geojson)
    type_geom  = data_geojson.get('type')

    # variable pdf
    pdf = FPDF('P', 'mm', 'Letter')
    # Add a page
    pdf.add_page()
    # set style and size of font 
    pdf.set_font("Arial",  'B', size = 15)
    # create a cell
    pdf.cell(0, 10, txt = name, 
            ln = 1, align = 'C')
    pdf.cell(0, 10, txt = f'ID: {id_state}', border = 0, ln = 1, 
          align = '', fill = False, link = '')
    pdf.cell(0, 10, txt = f'Type Geometry: {type_geom}', border = 0, ln = 1, 
          align = '', fill = False, link = '')

    pdf.multi_cell(w=0, h=10, txt='', border = 1, 
                align= 'J', fill = False)
    
    return pdf.output(dest="S", name=name).encode('latin-1') # generate pdf in memory