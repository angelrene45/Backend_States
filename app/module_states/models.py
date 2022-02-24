from app import db
from sqlalchemy.ext.automap import automap_base

Base = automap_base()

# reflect the tables
Base.prepare(db.engine, reflect=True)

# mapped classes are now created with names by default
# matching that of the table name.
State = Base.classes.state
