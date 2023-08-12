from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template("index.html")

@app.route('/game.html', methods=['POST'])
def game():
    name = request.form.get('name')
    return render_template("game.html", name=name)

@app.route('/end.html', methods=['GET', 'POST'])  # 添加 'POST' 方法
def end():
    score = request.form.get('score')
    print("Received score:", score)
    return render_template('end.html', score=score)

if __name__ == '__main__':
    app.run(debug=True)
