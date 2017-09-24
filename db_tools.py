import sqlite3


def add_category_to_db(cursor, category_name):

    sql = '''
        INSERT INTO Categories
        (ID, CategoryName)
        VALUES
        (?, ?);
    '''
    cursor.execute(sql, (None, category_name))


def get_loc_id(cursor, name):

    sql = '''
        SELECT ID
        FROM Locations
        WHERE Name=UPPER(?)
    '''
    cursor.execute(sql, (name.upper(),))
    return cursor.fetchone()


def get_cat_id(cursor, name):
    sql = '''
        SELECT ID
        FROM Categories
        WHERE CategoryName=UPPER(?)
    '''
    cursor.execute(sql, (name.upper(),))
    return cursor.fetchone()


def add_loc_to_db(cursor, name, phone, hours, website, address):

    sql = '''
        INSERT INTO Locations(
          ID,
          Name,
          Phone,
          Hours,
          Website,
          Address
        )
        VALUES 
        (?, ?, ?, ?, ?, ?)
    '''
    cursor.execute(sql, (None, name, phone, hours, website, address))


def add_match_rec_to_db(cursor, loc_id, cat_id):
    pass
