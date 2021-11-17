from flask import render_template, request, redirect
from flask.globals import session
from flask_app import app
from flask_app.models.user import User
from flask_app.models.message import Message


@app.route('/addtomessages', methods= ["POST"])
def add_book_to_author():
    data = {
        "user_id": session["user_id"],
        "message": request.form["message"],
        "receiver_id": request.form["receiver_id"]
    }
    Message.save_message(data)
    return redirect("/dashboard")

# @app.route('/dashboard')
# def messages_show():
#     data = {
#         "user_id": session["user_id"]
#     }
#     messages = Message.get_all_messages(data)
#     names = User.get_all_names(data)

#     return render_template('dashboard.html', messages=messages, names = names)