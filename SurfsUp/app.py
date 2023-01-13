import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

engine = create_engine("sqlite:///../Resources/hawaii.sqlite", echo=False)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save reference to the table
Percipitation = Base.classes.measurement

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

# defining the index route (Home Page)
@app.route("/")
def home():
    print("List all available api routes")
    return(
        f"Hello, Welcome to the Home Page!<br/>"
        f"Available routes :<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )

@app.route("/api/v1.0/precipitation")
def percipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of """
    # Query all 
    results = session.query(Percipitation.pcrp,Percipitation.date).all()

    session.close()

    # Convert list of tuples into normal list
    all_percipitation = list(np.ravel(results))

    return jsonify(all_percipitation)

@app.route("/api/v1.0/stations")
def percipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of """
    # Query all 
    results = session.query(Stations).all()

    session.close()

    # Convert list of tuples into normal list
    all_stations = list(np.ravel(results))

    return jsonify(all_stations)

    if __name__ == '__main__':
        app.run(debug=True)