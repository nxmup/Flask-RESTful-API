from . import api


@api.route('/', methods=['GET'])
def index():
    return 'Hello World!'
