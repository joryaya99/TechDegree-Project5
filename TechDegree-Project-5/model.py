from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    date = db.Column(db.Date)
    description = db.Column(db.Text)
    skills = db.Column(db.Text)
    repo_link = db.Column(db.String(255))