from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'AWS CICD Pipline for a python based Flask app'

'if __name__ == "__main__":
    app.run()
