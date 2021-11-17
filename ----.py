from flask_app.config.mysqlconnection import connectToMySQL

class Book:
    def __init__( self , data ):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL('authorsbooks').query_db(query)
        books = []
        for book in results:
            books.append( cls(book) )
        return books
    
    @classmethod
    def get_from_dojo(cls, data:dict):
        query = "SELECT * FROM books WHERE dojo_id = %(dojo_id)s;"
        results = connectToMySQL('authorsbooks').query_db(query, data)
        books = []
        for book in results:
            books.append(cls(book))
        return books


    @classmethod
    def get_byid(cls, data:dict):
        query = "SELECT * FROM books WHERE id = %(id)s;"
        results = connectToMySQL('authorsbooks').query_db(query, data)
        return cls (results[0])

    @classmethod
    def delete_byid(cls, data):
        query = "DELETE FROM books WHERE id = %(id)s;"
        return connectToMySQL('authorsbooks').query_db(query, data)

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO books ( title, num_of_pages , created_at , updated_at ) VALUES (%(title)s, %(num_of_pages)s,NOW(),NOW());"
        return connectToMySQL('authorsbooks').query_db( query, data )

    @classmethod
    def update(cls, data ):
        query = "UPDATE books SET( first_name, last_name , age, created_at , updated_at ) VALUES (%(fname)s, %(lname)s, %(age)s,NOW(),NOW()) WHERE id = %(id)s;"
        return connectToMySQL('authorsbooks').query_db( query, data )        