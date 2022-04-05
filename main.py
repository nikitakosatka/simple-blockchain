from flask import Flask, render_template, request, redirect, url_for

from block import *

app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def index():
    create_genesis()

    if request.method == 'POST':

        sender = request.form['sender']
        amount = request.form['amount']
        recipient = request.form['recipient']

        write_block(sender, amount, recipient)
        return redirect(url_for('index'))

    return render_template('index.html')


@app.route('/check', methods=['GET'])
def check():
    create_genesis()
    results = check_integrity()
    return render_template('index.html', results=results)


if __name__ == '__main__':
    app.run(debug=True)
