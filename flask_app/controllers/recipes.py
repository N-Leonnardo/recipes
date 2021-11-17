from flask import render_template, request, redirect
from flask.globals import session
from flask_app import app
from flask_app.models.user import User
from flask_app.models.recipe import Recipe


@app.route('/dashboard')
def dashboard():
    data = {
        "user_id": session['user_id']
    }
    users = User.get_byid(data)
    recipes = Recipe.get_from_id(data)
    return render_template('dashboard.html', recipes = recipes, users = users)

@app.route('/create_recipe')
def create_recipe():
    return render_template('createrecipe.html')


@app.route('/add_recipe', methods= ["POST"])
def add_recipe():
    data = {
        "name" : request.form["name"],
        "description" : request.form["description"],
        "instruction" : request.form["instruction"],
        "under30" : request.form["under30"],
        "user_id": session['user_id']
    }
    Recipe.save_recipe(data)
    return redirect('/dashboard')

@app.route("/edit/<int:id>")
def edit(id):
    data = {
        "id": id,
        "user_id": session['user_id']
    }
    recipes = Recipe.get_each_id(data)
    return render_template("edit.html", recipes=recipes)

@app.route("/add_recipe/<int:id>", methods = ["POST"])
def editit(id):
    data = {
        "name" : request.form["name"],
        "description" : request.form["description"],
        "instruction" : request.form["instruction"],
        "under30" : request.form["under30"],
        "id": id
    }
    Recipe.update(data)
    return redirect("/users")

@app.route('/delete/<int:id>')
def delete_recipe(id):
    data = {
        "id" : id
    }
    Recipe.delete_byid(data)
    return redirect('/dashboard')

# @app.route('/dashboard')
# def messages_show():
#     data = {
#         "user_id": session["user_id"]
#     }
#     messages = Message.get_all_messages(data)
#     names = User.get_all_names(data)

#     return render_template('dashboard.html', messages=messages, names = names)