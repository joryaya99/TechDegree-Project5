from flask import Flask, render_template, request, redirect, url_for
from model import db, Project
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
db.init_app(app)

with app.app_context():
    db.create_all()

    if not Project.query.first():
        project1 = Project(title='The Number Guessing Game', date=datetime.now(), description='Built a console number guessing game that prompts the player to choose a number between a specified range of numbers. After the user guesses the correct number, the program will display the number of attempts it took them to guess correctly.', skills='Python', repo_link='https://github.com/joryaya99/TechDegree-Project-1')
        project2 = Project(title='Basketball Stats Tool', date=datetime.now(), description='Built a console-based basketball team statistics tool to help divide up a group of players into teams.', skills='Python', repo_link='https://github.com/joryaya99/TechDegree-Project-2')
        db.session.add_all([project1, project2])
        db.session.commit()

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects/<int:id>')
def project_detail(id):
    project = Project.query.get(id)
    if project is None:
        return render_template('404.html'), 404
    else:
        return render_template('detail.html', project=project)

@app.route('/projects/<int:id>/delete', methods=['GET', 'POST'])
def delete_project(id):
    project = Project.query.get(id)
    if request.method == 'POST':
        if project:
            db.session.delete(project)
            db.session.commit()
        return redirect(url_for('index'))
    return render_template('delete_confirm.html', project=project)

@app.route('/')
def index():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)

@app.route('/projects/new', methods=['GET', 'POST'])
def create_project():
    if request.method == 'POST':
        return redirect(url_for('index'))
    else:
        return render_template('create.html')

@app.route('/projects/<int:id>/edit', methods=['GET', 'POST'])
def edit_project(id):
    project = Project.query.get(id)
    if project:
        if request.method == 'POST':
            return redirect(url_for('project_detail', id=id))  # Redirect to the project detail page after successful edit
        else:
            return render_template('edit.html', project=project)
    else:
        return render_template('404.html'), 404

@app.route('/populate')
def populate_database():
    return 'Database is already populated with sample projects.'

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='127.0.0.1')
