from flask import Blueprint, render_template, redirect, url_for, request
from .models import Task, db

main = Blueprint("main", __name__)

@main.route("/")
def index():
    tasks = Task.query.all()
    return render_template("index.html", tasks=tasks)

@main.route("/add", methods=["POST"])
def add_task():
    title = request.form.get("title")
    new_task = Task(title=title)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for("main.index"))

@main.route("/update/<int:task_id>")
def update_task(task_id):
    task = Task.query.get_or_404(task_id)
    task.completed = not task.completed
    db.session.commit()
    return redirect(url_for("main.index"))

@main.route("/delete/<int:task_id>")
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("main.index"))
