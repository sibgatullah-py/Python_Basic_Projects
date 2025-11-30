from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)
#<----- Flask setup complete ----->

class Drinks(db.Model): # row column setup of database 
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), unique = True, nullable = False)
    description = db.Column(db.String(120))
    
    def __repr__(self): # This method setups the models kinda
        return f"{self.name} - {self.description}"


@app.route('/') # a route 
def index(): # a method that we want to hit when someone use this route
    return 'Hello!'

@app.route('/drinks') # show all the drink
def get_drinks():
    drinks = Drinks.query.all()
    
    output = []
    
    for drink in drinks:
        drink_data = {'name': drink.name, 'description': drink.description} # taking the values in dictionary format
        
        output.append(drink_data)
    
    return {'drinks': output}


@app.route('/drinks/<id>') # view a spacific drink
def get_drink(id):
    drink = Drinks.query.get_or_404(id)
    return {"name":drink.name,'description':drink.description}

@app.route('/drinks', methods =['POST']) # add a drink in the database
def add_drink():
    drink = Drinks(name = request.json['name'], description = request.json['description'])
    if drink is None:
        return {"error":"drink doesn't exists"}
    db.session.add(drink)
    db.session.commit()
    return {'id':drink.id}

@app.route('/drinks/<id>', methods=['DELETE']) # delete a drink from the database 
def delete_drink(id):
    drink = Drinks.query.get(id)
    if drink is None:
        return {"error":"not found"}
    db.session.delete(drink)
    db.session.commit()
    return {"message": "deleted!"}


if __name__ == '__main__':
    app.run(debug=True)
    
    
    

# from application import app, db, Drinks
# with app.app_context():