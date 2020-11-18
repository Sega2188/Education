from flask import Flask

app = Flask(__name__)


@app.route('/hello/<user1>')
def home(user1):
    return 'hello, user: ' + user1


@app.route('/summa/<x>/<y>')
def home2(x, y):
    result = int(x) + int(y)
    return str(result)


@app.route('/long/<str1>/<str2>/<str3>')
def home3(str1, str2, str3):
    maxlen = len(str1)
    result = str1
    if len(str2) > maxlen:
        maxlen = len(str2)
        result = str2
    if len(str3) > maxlen:
        maxlen = len(str3)
        result = str3
    return result


if __name__ == '__main__':
    app.run()