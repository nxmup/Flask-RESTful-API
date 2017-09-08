from . import api
from flask import jsonify, abort
from app.models import Tasks


@api.route('/tasks', methods=['GET'])
def index():
    tasks = Tasks.query.all()
    return jsonify({'tasks': list(map(lambda task: task.get_json(), tasks))})


@api.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = Tasks.query.filter_by(id=task_id).first()
    if not task:
        abort(404)
    return jsonify({'task': task.get_json()})
