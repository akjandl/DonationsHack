import os
import sqlite3
import db_tools
from flask import Flask, render_template, g

app = Flask(__name__)

def populate_categories():
    return db_tools.get_categories()

def match_loc_data(category):
    return db_tools.match_loc_data(category)

@app.route('/')
def index():
    categories = populate_categories()
    locations = db_tools.get_location_list()
    return render_template('index.html', categories=categories,
                        locations=locations)

@app.route('/<category>')
def retrieve_page(category):
    categories = populate_categories()
    if category not in categories:
        # Not a known category
        return render_template('index.html', categories=categories)
    locations = match_loc_data(category)
    return render_template('category_template.html', category=category,
                           locations=locations)

if __name__ == '__main__':
    app.run()
