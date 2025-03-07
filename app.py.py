from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, CI/CD!"

# New status route
@app.route('/status')
def status():
    return "OKkk", 200

if __name__ == "__main__":
    app.run()
