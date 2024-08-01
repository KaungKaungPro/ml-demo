from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to Fit Focus Machine Learning API!'

if __name__ == "__main__":
    app.run()