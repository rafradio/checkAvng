from flask import Flask
from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config.ProdConfig')
# app.config['SQLALCHEMY_DATABASE_URI']  = app.config['MYSQL_OBJECT']
db = SQLAlchemy(app)

@app.get('/')
def index():
    newName = app.config['MY_TEST_VAR']
    context = {
        'name': newName
    }
    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run(debug=True)

