from flask import Flask
from flask import request
from flask import g
from flask import render_template
from flask import redirect

from cocktaildata import Data

app = Flask(__name__)
app.secret_key = 'very secret string'

data = None

@app.teardown_appcontext
def close_connection(exception):
    data.close_connection()


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', opskrifter = data.get_recipes())

@app.route("/visopskrift")
def vis_opskrift():
    recipe = request.args['recipe']
    return render_template('opskrift.html', opskrift=recipe, ingredients = data.get_ingredients(recipe))


@app.route("/addrecipe")
def add_recipe():
    return render_template("newrecipe.html")

@app.route('/inputingredient', methods=['POST'])
def input_ingredient():
    recipe = request.form['recipe']
    name = request.form['name']
    amount = request.form['amount']
    note = request.form['note']
    data.add_ingredient(recipe, name, amount, note)
    return redirect("/visopskrift?recipe={}".format(recipe))

@app.route('/inputrecipe', methods=['POST'])
def input_recipe():
    recipe = request.form['navn']
    data.add_recipe(recipe)
    return redirect("/")


if __name__ == "__main__":
    with app.app_context():
        data = Data()

    app.run(debug=True)
