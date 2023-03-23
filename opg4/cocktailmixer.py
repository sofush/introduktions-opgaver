#!/usr/bin/env python
import tkinter as tk
import tkinter.ttk as ttk
from cocktaildata import Data

class Cocktail_mixer(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)

        self.data = Data()

        self.build_GUI()
        self.update_ui()

    def on_recipe_selected(self, event):
        self.update_ui()

    def update_ui(self):
        recipes = self.data.get_recipes()
        self.cb_recipes['values'] = self.data.get_recipes()
        ingredients = self.data.get_ingredients(self.recipe_value.get())
        self.recipe_grid.delete(*self.recipe_grid.get_children())
        for ingredient in ingredients:
            self.recipe_grid.insert("", tk.END, values=ingredient)
        rating = self.data.get_rating(self.cb_recipes.get())
        if rating == None:
            rating = "ukendt"
        self.lbl_rating.config(text = f"Rating: {rating}")


    def delete_recipe(self):
        recipe = self.cb_recipes.get()
        self.data.delete_recipe(recipe)
        self.cb_recipes.selection_clear()
        self.cb_recipes.set('')
        self.update_ui()


    def new_recipe(self):
        def insert():
            name = edNavn.get()
            rating = edRating.get()
            self.data.add_recipe(name, rating)
            self.update_ui()
            dialog.destroy()
            dialog.update()

        def cancel():
            dialog.destroy()
            dialog.update()

        dialog = tk.Toplevel()

        edNavn = tk.Entry(dialog)
        edRating = tk.Scale(dialog, from_=1, to=5, tickinterval=10)

        lblNavn = ttk.Label(dialog, text="Navn")
        lblRating = ttk.Label(dialog, text="Rating")

        butCancel = ttk.Button(dialog, text="Annuller", command=cancel)
        butOK = ttk.Button(dialog, text="OK", command=insert)

        lblNavn.grid(column = 0, row = 0, columnspan=1)
        lblRating.grid(column = 1, row = 0, columnspan=1)
        edNavn.grid(column = 0, row = 1, columnspan=1)
        edRating.grid(column = 1, row = 1, columnspan=1)

        butCancel.grid(column = 0, row = 2)
        butOK.grid(column = 1, row = 2)

    def new_ingredient(self):
        def insert():
            name = ed_navn.get()
            amount = sl_amount.get()
            note = text_note.get("1.0",tk.END)
            recipe = self.cb_recipes.get()
            self.data.add_ingredient(recipe, name, amount, note)
            self.update_ui()
            dialog.destroy()
            dialog.update()

        def cancel():
            dialog.destroy()
            dialog.update()

        dialog = tk.Toplevel()

        lbl_navn = ttk.Label(dialog, text="Navn")
        ed_navn = tk.Entry(dialog)

        lbl_note = ttk.Label(dialog, text="Note")
        text_note = tk.Text(dialog, height=4)

        lbl_amount = ttk.Label(dialog, text="Mængde")
        sl_amount = tk.Scale(dialog, from_=1, to=10, tickinterval=10, orient=tk.HORIZONTAL)

        but_cancel = ttk.Button(dialog, text="Annuller", command=cancel)
        but_ok = ttk.Button(dialog, text="OK", command=insert)

        lbl_navn.grid(column = 0, row = 0)
        ed_navn.grid(column = 1, row = 0)

        lbl_note.grid(column=0, row=1)
        text_note.grid(column=1, row=1)

        lbl_amount.grid(column=0, row = 2)
        sl_amount.grid(column=1, row = 2)

        but_cancel.grid(column = 0, row = 3)
        but_ok.grid(column = 1, row = 3)

    def build_GUI(self):
        self.pack(side = tk.BOTTOM)
        self.overskrift = tk.Label(self, text = "Bland nogle lækre cocktails")
        self.overskrift.grid(column=0,row=0,columnspan = 2)

        lbl_recipes = ttk.Label(self, text="Opskrifter")
        self.lbl_rating = ttk.Label(self, text="Rating: Ukendt")
        self.recipe_value=tk.StringVar()
        self.cb_recipes = ttk.Combobox(self, values = [], textvariable=self.recipe_value)
        self.cb_recipes.bind("<<ComboboxSelected>>", self.on_recipe_selected)

        lbl_recipes.grid(column=0,row=1)
        self.lbl_rating.grid(column=0,row=2)
        self.cb_recipes.grid(column=0,row=3)

        self.but_new_recipe = tk.Button(self, text = "Tilføj ny opskrift", command=self.new_recipe)
        self.but_new_recipe.grid(column=0, row=4)

        self.but_new_ingredient = tk.Button(self, text = "Tilføj ny ingrediens", command=self.new_ingredient)
        self.but_new_ingredient.grid(column=0, row=5)

        self.but_delete_recipe = tk.Button(self, text = "Slet opskrift", command=self.delete_recipe)
        self.but_delete_recipe.grid(column=0, row=6)

        self.recipe_grid = ttk.Treeview(self, column=("columnIngredient", "columnAmount", "columnNote"), show='headings')
        self.recipe_grid.heading("#1", text="Ingrediens")
        self.recipe_grid.heading("#2", text="Mængde")
        self.recipe_grid.heading("#3", text="Note")
        self.recipe_grid["displaycolumns"]=("columnIngredient", "columnAmount", "columnNote")
        ysb = ttk.Scrollbar(self, command=self.recipe_grid.yview, orient=tk.VERTICAL)
        self.recipe_grid.configure(yscrollcommand=ysb.set)
        self.recipe_grid.grid(column=1, row = 1, rowspan=5)



app = Cocktail_mixer()

app.mainloop()
