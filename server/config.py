# Standard library imports

# Remote library imports
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_bcrypt import Bcrypt
from marshmallow import (
    Schema,
    fields,
    ValidationError,
    validate,
    validates_schema,
    validates,
)
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemySchema, SQLAlchemyAutoSchema
from dotenv import load_dotenv
from os import environ
import os


# Local imports

# Instantiate app, set attributes
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

load_dotenv(".env")
app.secret_key = environ.get("SECRET_KEY")

# Define metadata, instantiate db
metadata = MetaData(
    naming_convention={
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    }
)
db = SQLAlchemy(metadata=metadata)
migrate = Migrate(app, db)
db.init_app(app)

# Instantiate REST API
api = Api(app)

# Instantiate CORS
CORS(app)

bcrypt = Bcrypt(app)
ma = Marshmallow(app)
