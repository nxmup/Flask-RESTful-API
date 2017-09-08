from . import api
from .. import db
from flask import jsonify, abort, make_response, request
# jsonify -- 格式化响应给客户端的数据
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


@api.route('/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = Tasks(title=request.json['title'],
                 description=request.json.get('description', ''),
                 done=False)
    db.session.add(task)
    db.session.commit()
    return jsonify({'task': task.get_json()})


@api.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = Tasks.query.filter_by(id=task_id).first()
    if not task:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) is not str:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not str:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    task.title = request.json.get('title', task.title)
    task.description = request.json.get('description', task.description)
    task.done = request.json.get('done', task.done)
    db.session.commit()
    return jsonify({'task': task.get_json()})


@api.app_errorhandler(404)
def page_not_found(error):
    return make_response(jsonify({'error': "Not Found"}), 404)
