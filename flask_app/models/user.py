from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash



EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.pw = data['pw']
        self.pwconfirmation = data['pwconfirmation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_user( user ):
        is_valid = True
        if len(user['first_name']) < 2:
            flash("Name must be at least 2 characters.")
            is_valid = False
        if len(user['last_name']) < 2:
            flash("Bun must be at least 3 characters.")
            is_valid = False
        if (user['pw']) != (user['pwconfirmation']):
            flash("Password must match")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!")
            is_valid = False
        return is_valid

    @classmethod
    def get_byid(cls, data:dict):
        query = "SELECT * FROM users WHERE id = %(user_id)s;"
        results = connectToMySQL('users').query_db(query, data)
        return cls (results[0])

    @classmethod
    def get_all_names(cls, data):
        query = "SELECT * FROM users.users JOIN users.messages ON users.users.id = users.messages.user_id WHERE receiver_id = %(user_id)s;"
        results = connectToMySQL('users').query_db(query, data)
        names = []
        for name in results:
            names.append( cls(name) )
        return names

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users').query_db(query)
        users = []
        for email in results:
            users.append( cls(email) )
        return users
    
    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL("users").query_db(query,data)
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users ( first_name, last_name, email, pw, created_at, updated_at ) VALUES ( %(first_name)s, %(last_name)s, %(email)s, %(pw)s , NOW() , NOW() );"

        return connectToMySQL('users').query_db( query, data )