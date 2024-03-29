from flask import Blueprint, make_response

from app.module_states.models import State
from app.module_states.functions import generate_pdf
from app import db

states = Blueprint('states', __name__, url_prefix='/states')

@states.route("/", methods=['GET'])
def home():
    """
        Method return json from all states in database
    """
    # Get all states from database
    results = db.session.query(State).all()
    results_dict = { obj.id : { 'id': obj.id, 'name': obj.name, 'geojson': obj.geojson }  for obj in results  }
    return results_dict

@states.route("/<id_state>", methods=['GET'])
def get_state( id_state ):
    """
        Method return json from state request
    """
    # Get one record
    obj = db.session.query(State).get( id_state )
    if not obj: return f'State not found with id {id_state} ', 400
    results_dict =  { 'id': obj.id, 'name': obj.name, 'geojson': obj.geojson } 
    return results_dict

@states.route("/pdf/<id_state>", methods=['GET'])
def get_pdf( id_state ):
    """
        Method return PDF file from state 
    """
    state_object = db.session.query(State).get( id_state )
    if not state_object: return f'State not found with id {id_state} ', 400
    pdf = generate_pdf( state_object )
    if not pdf: return f'Problem to generate PDF {id_state} ', 500
    response = make_response( pdf )
    response.headers['Content-Disposition'] = f'attachment; filename="{state_object.name}.pdf"'
    response.headers['Content-Type'] = 'application/pdf'
    return response