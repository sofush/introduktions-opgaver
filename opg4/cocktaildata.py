import sqlite3

class Data():

    def __init__(self):
        self.DATABASE = 'mixer_data.db'

        self.db = sqlite3.connect(self.DATABASE)

        self._create_db_tables()



    def add_recipe(self, name, rating):
        if name in self.get_recipes():
            print("Opskriften findes allerede")
        c = self.db.cursor()
        c.execute("""INSERT INTO Recipes (name, rating) VALUES (?,?)""", [name, rating])
        self.db.commit()

    def delete_recipe(self, name):
        c = self.db.cursor()
        c.execute("""DELETE FROM Recipes WHERE name IS (?)""", [name])
        self.db.commit()

    def add_ingredient(self, recipe, name, amount, note):
        c = self.db.cursor()
        c.execute("""INSERT INTO Ingredients (recipe, name, amount, note) VALUES (?,?,?,?)""", [recipe,name, amount,note])
        self.db.commit()

    def get_recipes(self):
        c = self.db.cursor()
        c.execute("""SELECT * FROM Recipes""")

        recipes = []
        for recipe in c:
            recipes.append(recipe[1])

        return recipes

    def get_rating(self, recipe):
        c = self.db.cursor()
        c.execute("""SELECT rating FROM Recipes WHERE name = ?""",[recipe])
        for recipe in c:
            return recipe[0]



    def get_ingredients(self, recipe):
        c = self.db.cursor()
        c.execute("""SELECT name,amount,note FROM Ingredients WHERE recipe = ?""",[recipe])
        ingredients = []

        for ingredient in c:
            ingredients.append((ingredient[0],ingredient[1],ingredient[2]))

        return ingredients




    def _create_db_tables(self):
        c = self.db.cursor()
        try:
            c.execute("""CREATE TABLE Recipes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                rating INTEGER,
                name TEXT);""")
        except Exception as e:
            print(e)
        try:
            c.execute("""CREATE TABLE Ingredients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                recipe TEXT,
                name TEXT,
                amount INTEGER,
                note TEXT);""")
        except Exception as e:
            print(e)

        self.db.commit()
        return 'Data tables created'
