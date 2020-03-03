#Telegram: @Mortys3

from flask import Flask, escape, request, render_template

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
    classroom = 25
    return f"{age}, {country}, {classroom}"


@app.route('/second', methods=['GET', 'POST'])
def second():

    if request.method == 'GET':
        return render_template('second.html')

    if request.method == 'POST':
        text = request.form.get('text')
        one = "".join(list(reversed(text)))  # reversed text
        two = text[::-1] #slice
        three = "".join([x for x in reversed(text)])  # comprehension

        return f'Reversed text: {one}, Slice: {two},Comprehension: {three}'


if __name__ == '__main__':
    app.run('127.0.0.1')
