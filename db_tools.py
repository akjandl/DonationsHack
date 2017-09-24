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
        WHERE UPPER(Name)=?
    '''
    cursor.execute(sql, (name.upper(),))
    return cursor.fetchone()


def get_cat_id(cursor, name):
    sql = '''
        SELECT ID
        FROM Categories
        WHERE UPPER(CategoryName)=?
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


def add_match_rec_to_db(cursor, cat_id, loc_id):

    sql = '''
        INSERT INTO Matches
        (ID, Category_ID, Location_ID)
        VALUES
        (?, ?, ?)
    '''
    cursor.execute(sql, (None, cat_id, loc_id))


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def match_loc_data(category):
    con = sqlite3.connect('donations_hack.db')
    con.row_factory = dict_factory
    cur = con.cursor()
    sql = '''
        SELECT Name, Phone, Hours, Website, Address
        FROM Locations JOIN Matches ON Locations.ID = Matches.Location_ID
        WHERE Matches.Category_ID= (
          SELECT ID 
          FROM Categories
          WHERE UPPER(CategoryName)=?
        )
    '''
    cur.execute(sql, (category.upper(),))
    return cur.fetchall()


def get_categories():
    con = sqlite3.connect('donations_hack.db')
    cur = con.cursor()
    sql = '''
        SELECT CategoryName
        FROM Categories
        ORDER BY CategoryName
    '''
    cur.execute(sql)
    return [i[0] for i in cur.fetchall()]


def main():
    pass


if __name__ == '__main__':
    main()