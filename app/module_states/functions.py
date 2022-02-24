
from os import stat_result


def generate_pdf( state_object ):
    id_state = state_object.id
    name = state_object.name
    geojson = state_object.geojson

    print( id_state, name )

    pass