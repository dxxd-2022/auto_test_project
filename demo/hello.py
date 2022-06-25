from flask import Flask, request

app = Flask (__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route("/request", methods=['POST', 'GET'])
def get_diff_post():
    #拿到request参数
    query = request.args
    #El request form
    post = request.form
    #分别打印拿到的参数和form
    return f"query: {query}\n"\
           f"post: {post}"