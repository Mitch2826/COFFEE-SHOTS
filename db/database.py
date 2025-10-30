from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


# instance of SQLAlchemy with custom base class
db = SQLAlchemy(model_class=Base)
