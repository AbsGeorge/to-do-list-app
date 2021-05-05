from application import app, db
from application.models import Tasks

@app.route('/add')
def add():
    new_todo = Tasks(description="New Task")
    db.session.add(new_todo)
    db.session.commit()
    return "Added new to-do task"


@app.route('/')
@app.route('/home')
def home():
    all_task = Tasks.query.all()
    message = ""
    for task in all_task:
        message += task.description + "\n"
    return message

@app.route('/complete/<int:id>')
def complete(id):
    task = Tasks.query.filter_by(id=id).first()
    task.completed = True
    db.session.commit()
    return "Task is now complete"

@app.route('/incomplete/<int:id>')
def incomplete(id):
    task = Tasks.query.filter_by(id=id).first()
    task.completed = False
    db.session.commit()
    return "Task is incomplete"

@app.route('/update/<new_description>')
def update(new_description):
    task = Tasks.query.order_by(Task.id.desc).first()
    task.description = new_description
    db.session.commit()
    return f"Most recent task was updated with the description: {new_description}"

@app.route('/delete/<int:id>')
def delete(id):
    task = Tasks.query.filter_by(id=id).first()
    db.session.delete(task)
    db.session.commit()
    return f"Task {id} deleted"
