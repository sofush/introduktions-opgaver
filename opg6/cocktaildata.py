import sqlite3
from flask import g

class Data():

    def __init__(self):
        self.DATABASE = '_data.db'

        self._create_db_tables()


    def _get_db(self):
        db = g.get('_database', None)
        if db is None:
            db = g._databdase = sqlite3.connect(self.DATABASE)
        return db

    def close_connection(self):
        db = getattr(g, '_database', None)
        if db is not None:
            db.close()

    def add_recipe(self, name):
        if name in self.get_recipes():
            print("Opskriften findes allerede")
        db = self._get_db()
        c = db.cursor()
        c.execute("""INSERT INTO Recipes (name) VALUES (?)""", [name])
        db.commit()

    def add_ingredient(self, recipe, name, amount, note):
        db = self._get_db()
        c = db.cursor()
        c.execute("""INSERT INTO Ingredients (recipe, name, amount, note) VALUES (?,?,?,?)""", [recipe,name, amount,note])
        db.commit()

    def get_recipes(self):
        db = self._get_db()
        c = db.cursor()
        c.execute("""SELECT * FROM Recipes""")

        recipes = []
        for recipe in c:
            print(".")
            recipes.append(recipe[1])

        return recipes


    def get_ingredients(self, recipe):
        db = self._get_db()
        c = db.cursor()
        c.execute("""SELECT name,amount,note FROM Ingredients WHERE recipe = ?""",[recipe])
        ingredients = []

        for ingredient in c:
            ingredients.append((ingredient[0],ingredient[1],ingredient[2]))

        return ingredients

    def get_all_ingredients(self):
        db = self._get_db()
        c = db.cursor()
        c.execute("""SELECT name,amount,note FROM Ingredients""")
        ingredients = []

        for ingredient in c:
            ingredients.append((ingredient[0],ingredient[1],ingredient[2]))

        return ingredients




    def _create_db_tables(self):
        db = self._get_db()
        c = db.cursor()
        try:
            c.execute("""CREATE TABLE Recipes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT);""")
            self.add_recipe("White russian")
        except Exception as e:
            print(e)
        try:
            c.execute("""CREATE TABLE Ingredients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                recipe TEXT,
                name TEXT,
                amount INTEGER,
                note TEXT);""")
            self.add_ingredient("White russian", "vodka", "1", "")
            self.add_ingredient("White russian", "mælk", "2", "")
            self.add_ingredient("White russian", "kahlua", "1", "")
            self.add_ingredient("White russian", "is", "3", "isterninger")
        except Exception as e:
            print(e)

        db.commit()
        return 'Data tables created'
