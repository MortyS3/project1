from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
@app.route('/first')
def hello():
    name = request.args.get("name", "World")
    return f'Andrey Pedko, TZ-61'
def function():
    name = request.args.get("age", "country", "classroom")
    return f'age, country, classroom' 
    pass


if __name__ == '__main__':
    app.run('0.0.0.0')
