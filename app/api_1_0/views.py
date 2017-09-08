from . import api
from flask import jsonify, abort, make_response
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


@api.app_errorhandler(404)
def page_not_found(error):
    return make_response(jsonify({'error': "Not Found"}), 404)
