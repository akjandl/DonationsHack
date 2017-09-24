import os
import sqlite3
import db_tools
# TODO: import statements from Andy's API
from flask import Flask, render_template, g

app = Flask(__name__)

# TODO: Dummy data; get rid of this once merged
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'test.db'),
    SECRET_KEY='dev',
    CATEGORIES=['shoes', 'bicycles'],
    LOCATIONS=[('Me', 'My phone', 'Always', 'My URL', 'My address'),
               ('Poirot', 'Unlisted', 'Monday-Thursday', 'None', '221B Baker St')
              ]
))

# TODO: Mock: Remove later
def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = sqlite3.connect(app.config['DATABASE'])
        g.sqlite_db.row_factory = sqlite3.Row
    return g.sqlite_db

# TODO: Mock: Replace call with DB connection
def populate_categories():
    # return g.sqlite_db.get_categories()
    return app.config['CATEGORIES'] 

def match_loc_data(category):
    return db_tools.match_loc_data(category)

@app.route('/')
def index():
    # TODO: Mock: Replace call later
    get_db()
    categories = populate_categories()
    # TODO: Replace with call to DB
    locations = app.config['LOCATIONS']
    return render_template('index.html', categories=categories,
                        locations=locations)

@app.route('/<category>')
def retrieve_page(category):
    categories = populate_categories()
    if category not in categories:
        # Not a known category
        # TODO: What to render in this case?
        return render_template('index.html', categories=categories)
    locations = match_loc_data(category)
    return render_template('category_template.html', category=category,
                           locations=locations)

if __name__ == '__main__':
    app.run()
