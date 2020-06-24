from flask import (Flask, render_template)

app = Flask("__main__")

@app.route("/", methods=['GET', 'POST'])
def my_index():
    return render_template("index.html", flask_token="Allahuabha+")

app.run(debug=True)
