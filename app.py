from flask import Flask, render_template, request, redirect, url_for
from model import db, Project
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
db.init_app(app)

with app.app_context():
    db.create_all()

    if not Project.query.first():
        project1 = Project(title='Sample Project 1', date=datetime.now(), description='This is a sample project.', skills='Flask, SQLAlchemy', repo_link='https://github.com/sample_project1')
        project2 = Project(title='Sample Project 2', date=datetime.now(), description='Another sample project.', skills='HTML, CSS, Python', repo_link='https://github.com/sample_project2')
        db.session.add_all([project1, project2])
        db.session.commit()

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

@app.route('/populate')
def populate_database():
    return 'Database is already populated with sample projects.'

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='127.0.0.1')
