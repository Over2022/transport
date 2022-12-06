from flask import Flask, render_template
from models import db, Add
from flask import request, redirect
from decouple import config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///transport.db'

db.init_app(app)


@app.route('/', methods=['POST', 'GET'])
@app.route('/home',  methods=['POST', 'GET'])
def index():
    # api_key = config('api_key', default='')
    # url = 'http://htmlweb.ru/geo/api.php?location=&json&charset=windows-1251&fields=id,name&api_key=' + api_key
    # url_city = 'https://htmlweb.ru/json/geo/city/1?api_key=' + api_key
    # res = requests.get(url.format()).json()
    # res_city = requests.get(url_city.format())
    # print(res_city.text)

    if request.method == 'POST':
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        price = request.form['price']
        add = Add(start_date=start_date, end_date=end_date, price=price)

        try:
            db.session.add(add)
            db.session.commit()
            return redirect('/cargo')

        except:
            return 'Error'

    else:
        return render_template('index.html')


@app.route('/cargo')
def cargo():
    add = Add.query.order.by().all()
    return render_template('cargo.html', add=add)

@app.route('/create')
def create():
    db.create_all()
    return 'All tables created'


if __name__ == '__main__':
    app.run(debug=True)
