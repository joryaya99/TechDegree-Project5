from flask import Flask, render_template, request, redirect, url_for
from model import db, Project
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)

@app.route('/projects/new', methods=['GET', 'POST'])
def create_project():
    if request.method == 'POST':
        return render_template('create.html')

@app.route('/projects/<int:id>')
def project_detail(id):
    project = Project.query.get(id)
    return render_template('detail.html', project=project)

@app.route('/projects/<int:id>/edit', methods=['GET', 'POST'])
def edit_project(id):
    project = Project.query.get(id)
    if request.method == 'POST':
        return render_template('edit.html', project=project)

@app.route('/projects/<int:id>/delete')
def delete_project(id):
    project = Project.query.get(id)
