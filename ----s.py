from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.author import Author
from flask_app.models.book import Book

@app.route('/create_book', methods= ["POST"])
def create_ninja():
    data = {
        "title": request.form["title"],
        "num_of_pages": request.form["num_of_pages"],
    }
    Book.save(data)
    return redirect("/add_book")

@app.route('/add_book')
def add_book():
    books = Book.get_all()
    return render_template("create_book.html", books=books)


@app.route('/go_to_add_book')
def go_to_add_book():
    return redirect("/add_book")

# @app.route('/go_to_home')
# def go_to_home():
#     return redirect("/")



# @app.route('/overview/<int:dojo_id>')
# def overview_dojo(dojo_id):
#     data = {
#         "dojo_id": dojo_id
#     }
#     ninjas = Ninja.get_from_dojo(data)
#     return render_template("overview.html", ninjas = ninjas)