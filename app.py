from flask import Flask, render_template, request
from flask import jsonify
import execute

app = Flask(__name__, static_url_path="/static") 

@app.route('/message', methods=['POST'])
def reply():
    return jsonify( { 'text': execute.response(request.form['msg']) } )

@app.route("/")
def index(): 
    return render_template("index.html")

if __name__ == '__main__': 
    app.run(port = 9000) 
