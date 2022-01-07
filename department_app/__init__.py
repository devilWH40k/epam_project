from flask import Flask, render_template

app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route("/")
@app.route("/home")
def home():
    return "<h1>Test run</h1>"


@app.route("/test")
def test():
    return render_template('departments.html')


if __name__ == '__main__':
    app.run(debug=True)