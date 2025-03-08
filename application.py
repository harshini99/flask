from flask import Flask ,requests


#creating app like flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


app.app_context().push()

class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.name} - {self.description}"
#route 

@app.route('/')
def method():
    return "Hello"

@app.route('/drinks')
def get_drinks():
    drinks = Drink.query.all()
    output=[]
    for drink in drinks:
        drink_data = {'name':drink.name, 'description': drink.description}
        output.append(drink_data)
    return {"drinks":output}



