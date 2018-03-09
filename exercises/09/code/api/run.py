from . import create_app
from .database import db

app = create_app()


@app.before_first_request
def setup_db():
    db.create_all()
