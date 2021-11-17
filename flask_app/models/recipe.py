from flask_app.config.mysqlconnection import connectToMySQL

class Recipe:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instruction = data['instruction']
        self.under30 = data['under30']
        self.user_id = data['user_id']

    @classmethod
    def save_recipe( cls , data ):
        query = "INSERT INTO users.recipe ( name, description, instruction, under30, user_id ) VALUES (%(name)s, %(description)s, %(instruction)s, %(under30)s, %(user_id)s);"
        return connectToMySQL('users').query_db( query, data)

    @classmethod
    def get_from_id(cls, data:dict):
        query = "SELECT * FROM users.recipe WHERE id = %(user_id)s;"
        results = connectToMySQL('users').query_db(query, data)
        recipesid = []
        for recipe in results:
            recipesid.append(cls(recipe))
        return recipesid
        
    @classmethod
    def get_each_id(cls, data:dict):
        query = "SELECT * FROM users.recipe WHERE user_id = %(user_id)s AND id = %(id)s;"
        results = connectToMySQL('users').query_db(query, data)
        recipes = []
        for recipe in results:
            recipes.append(cls(recipe))
        return recipes    
        
    @classmethod
    def delete_byid(cls, data):
        query = "DELETE FROM users.recipe WHERE id = %(id)s;"
        return connectToMySQL('users').query_db(query, data)

    @classmethod
    def update(cls, data ):
        query = "UPDATE recipe SET( name , description , instruction , under30, updated_at ) VALUES ( %(name)s , %(description)s , %(instruction)s , %(under30)s, NOW() ) WHERE id = %(id)s;"
        return connectToMySQL('users').query_db( query, data )     
    
    # @classmethod
    # def get_from_author(cls, data:dict):
    #     query = "SELECT * FROM users JOIN messages ON users.id = messages.user_id JOIN users ON messages.id = messages.receiver_id WHERE receiver_id = %(receiver_id)s;"
    #     results = connectToMySQL('users').query_db(query, data)
    #     messages = []
    #     for message in results:
    #         messages.append(cls(message))
    #     print (messages)
    #     return messages


    # @classmethod
    # def get_byid(cls, data:dict):
    #     query = "SELECT * FROM authors JOIN favorite ON authors.id = favorite.author_id JOIN books ON books.id = favorite.book_id WHERE author_id = %(author_id)s;"
    #     results = connectToMySQL('authorsbooks').query_db(query, data)
    #     favorites = []
    #     for favorite in results:
    #         favorites.append(cls(favorite))
    #     return favorites




    # @classmethod
    # def save(cls, data ):
    #     query = "INSERT INTO favorite ( name, created_at , updated_at) VALUES ( %(name)s, NOW() , NOW() );"
    #     return connectToMySQL('authorsbooks').query_db( query, data )

    # @classmethod
    # def update(cls, data ):
    #     query = "UPDATE authors SET( name ) VALUES ( %(name)s , NOW() , NOW() ) WHERE id = %(id)s;"
    #     return connectToMySQL('authorsbooks').query_db( query, data )        