from flask_app.config.mysqlconnection import connectToMySQL

class Message:
    def __init__( self , data ):
        self.user_id = data['user_id']
        self.message = data['message']
        self.receiver_id = data['receiver_id']

    @classmethod
    def save_message( cls , data ):
        query = "INSERT INTO messages ( user_id, receiver_id, message ) VALUES (%(user_id)s,%(receiver_id)s, %(message)s);"
        return connectToMySQL('users').query_db( query, data)

    @classmethod
    def get_all_messages(cls, data):
        query = "SELECT * FROM users.messages WHERE receiver_id = %(user_id)s;"
        results = connectToMySQL('users').query_db(query, data)
        messages = []
        for message in results:
            messages.append( cls(message) )
        return messages

    
    @classmethod
    def get_from_author(cls, data:dict):
        query = "SELECT * FROM users JOIN messages ON users.id = messages.user_id JOIN users ON messages.id = messages.receiver_id WHERE receiver_id = %(receiver_id)s;"
        results = connectToMySQL('users').query_db(query, data)
        messages = []
        for message in results:
            messages.append(cls(message))
        print (messages)
        return messages


    # @classmethod
    # def get_byid(cls, data:dict):
    #     query = "SELECT * FROM authors JOIN favorite ON authors.id = favorite.author_id JOIN books ON books.id = favorite.book_id WHERE author_id = %(author_id)s;"
    #     results = connectToMySQL('authorsbooks').query_db(query, data)
    #     favorites = []
    #     for favorite in results:
    #         favorites.append(cls(favorite))
    #     return favorites


    @classmethod
    def delete_byid(cls, data):
        query = "DELETE FROM favorite WHERE book_id = %(book_id)s AND author_id = %(author_id)s;"
        return connectToMySQL('authorsbooks').query_db(query, data)

    # @classmethod
    # def save(cls, data ):
    #     query = "INSERT INTO favorite ( name, created_at , updated_at) VALUES ( %(name)s, NOW() , NOW() );"
    #     return connectToMySQL('authorsbooks').query_db( query, data )

    # @classmethod
    # def update(cls, data ):
    #     query = "UPDATE authors SET( name ) VALUES ( %(name)s , NOW() , NOW() ) WHERE id = %(id)s;"
    #     return connectToMySQL('authorsbooks').query_db( query, data )        