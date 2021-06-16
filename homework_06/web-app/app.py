from flask import Flask,render_template
from web_app.models import db
from web_app.views.users import users_app
from flask_migrate import Migrate

app = Flask(__name__)
app.register_blueprint(users_app)
app.config.from_object('config.ProductionConfig')
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

db.init_app(app)
migrate = Migrate(app, db)



@app.route('/')
def index():
    print("hello")
    return render_template('index.html')


@app.route('/about/')
def about():
    hello = "Осваиваем новые горизонты"
    return render_template('about.html', hello=hello)

if __name__ == '__main__':
    app.run(debug=True)