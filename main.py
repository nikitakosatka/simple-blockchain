from flask import *

from block import *

app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def index():

    if request.method == 'POST':

        sender = request.form['sender']
        amount = request.form['amount']
        recipient = request.form['recipient']

        create_genesis()
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
