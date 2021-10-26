from imports_and_constants import *

app = Flask(__name__)
app.secret_key = SECRET_KEY


@app.route('/', methods=['GET'])
def hello_menu():
    return render_template('main.html')


if __name__ == '__main__':
    app.run(debug=True)
