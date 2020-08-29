# SWAMI KARUPPASWAMI THUNNAI

import secrets
from flask import Flask
from flask import redirect
from inventory.inventory import inventory,url_for



app = Flask(__name__)
app.secret_key = "THIRUVALLUVAN"

app.register_blueprint(inventory)


@app.route("/")
def index():
    return redirect("/contest")


if __name__ == "__main__":
    app.run(debug=True)