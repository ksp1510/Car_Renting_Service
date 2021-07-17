import json
import os.path

import pymongo as pymongo
from werkzeug.utils import secure_filename

from flask import Flask, render_template, request, redirect, url_for, flash, abort, session, jsonify,request, redirect
from form import SignUpForm, LoginForm


app = Flask(__name__)
app.secret_key = "kjjjgjgkjlhuaiy7u"
conn_string = "mongodb+srv://ksp1510:kishan@cluster0.syoit.mongodb.net/db_rental?ssl=true&ssl_cert_reqs=CERT_NONE&retryWrites=true&w=majority"
my_client = pymongo.MongoClient(conn_string)
db = my_client["users"]





@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login',methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('All fields are required.')
    return render_template('login.html', form=form)


@app.route('/signup')
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        flash('All fields are required.')
    return render_template('sign_up.html', form=form)


@app.route('/success', methods=['GET', 'POST'])
def success():
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        add = request.form['add']
        city = request.form['city']
        pin = request.form['pin']
        contact = request.form['contact']
        email = request.form['email']
        userid = request.form['userid']
        password = request.form['password']
        lic_num = request.form['lic_num']
        lic_val = request.form['lic_val']
        rto = request.form['rto']



    return render_template('success.html')


@app.route('/aboutus', methods=['GET', 'POST'])
def aboutus():
    form = SignUpForm()
    if form.validate_on_submit():
        flash('All fields are required.')
    return render_template('aboutus.html', form=form)


@app.route('/cars')
def cars():
    return render_template("cars.html")

'''Including SQLAlchemy Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


#car schedulr database
class Todo(db.Model):
    __tablename__ = "Task"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500), nullable=False)
    #completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')

        except:
            return 'Sorry, task not added'

    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('template.html', tasks=tasks)

@app.route('/delete/<int:id')
def delete(id):
    task_to_delete = Todo.guery.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return ' Problem identified '


@app.route('/upadte/<int:id', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'sorry , update action not done'

    else:
        return render_template('update.html', task=task)

# Press the green button in the gutter  to run the script.'''
if __name__ == '__main__':
    app.run(debug=True)

