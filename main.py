# Telegram: @Mortys3

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
        two = text[::-1]  # slice
        three = "".join([x for x in reversed(text)])  # comprehension

        return f'Reversed text: {one}, Slice: {two},Comprehension: {three}'


@app.route('/third', methods=["GET", "POST"])
def third():
    pass


def function(in1, in2):
    list1 = []
    for i in range(int(in1), int(in2)):
        if i % 3 == 0:
            list1.append(int(i))
    return list1


@app.route('/fourth/1', methods=["GET", "POST"])
def fourth():
    if request.method == 'GET':
        return render_template('41.html')

    if request.method == 'POST':
        in1 = request.form.get('in1')
        in2 = request.form.get('in2')
        list1 = function(in1, in2)

    return f'{" ".join(str(list1))}'


def checker(x):
    for i in x:

        if ( i.isalpha() and i != ' ' ):
            a = True
        elif i != '  ':
            a = False
        else:
            a = False
    return f'{a}'


@app.route('/fourth/2', methods=["GET", "POST"])
def fourth2():
    if request.method == 'GET':
        return render_template('42.html')

    if request.method == 'POST':
        string1 = str(request.form.get('string1'))

        otvet = checker(string1)
    return f'{" ".join(otvet)}'


if __name__ == '__main__':
    app.run('127.0.0.1')
