from flask import Flask

app = Flask(__name__)


@app.route('/search', methods=['GET'])
def get_list():
    return 


