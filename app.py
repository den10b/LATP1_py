from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db = SQLAlchemy(app)


class Student(db.Model):
    __tablename__ = 'Student'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


@app.route('/<int:student_id>')
def index(student_id):
    student = Student.query.filter_by(id=student_id).first()
    print(student.name)
    return render_template('index.html', student_name=student.name)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5767)
