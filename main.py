from flask import Flask, jsonify
from flask_migrate import Migrate
from db.database import db
from db.config import DATABASE_URL

from controllers.customers_controller import get_all_customers

# an instance of the class
app = Flask(__name__)

# configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
db.init_app(app)

migrate = Migrate(app, db)

# register the models we have
from models.customer import Customer


# setup a route
@app.route('/')
def home():
    return "Hello, Flask!"


@app.route('/customers')
def fetch_all_customers():
    customers = jsonify(get_all_customers())
    return customers


# run the app
if __name__ == '__main__':
    app.run(debug=True)
