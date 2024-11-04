from flask import Flask
from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy
from models import db, MyUser, Valuty

app = Flask(__name__)
app.config.from_object('config.ProdConfig')
# app.config['SQLALCHEMY_DATABASE_URI']  = app.config['MYSQL_OBJECT']
db.init_app(app)

@app.get('/')
def index():
    newName = app.config['MY_TEST_VAR']
    context = {
        'name': newName
    }
    db.create_all()
    return render_template('index.html', **context)

@app.cli.command("init-db")
def init_db():
    db.create_all()
    print(app.config['SQLALCHEMY_DATABASE_URI'])
    print('OK')

@app.cli.command("find-curr")
def find_curr():
    currencies = Valuty.query.all()
    for cur in currencies: print(cur.currency_name)




if __name__ == '__main__':
    app.run(debug=True)

