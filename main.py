from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')

def hello():
    name = request.args.get("name", "World")
    return f'Andrey Pedko, TZ-61'
@app.route('/first')
def function():
    name = request.args.get("age", "country", "classroom")
    age = None
    country = 'Ukraine'
    classroom == 25
    print ("age, country, classroom")
    pass


if __name__ == '__main__':
    app.run('0.0.0.0')
