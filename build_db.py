import sqlite3
import json

from db_tools import *


def get_categories(file):

    categories = set()
    with open(file, 'r') as data:
        for l in data.readlines():
            row = l.split('\t')
            dt = row[1]
            if dt == 'category':
                categories.add(row[2].strip())
    return categories


def get_location_data(file):

    locations = {}
    with open(file, 'r') as data:
        for l in data.readlines():
            row = l.split('\t')
            name = row[0].strip()
            dt = row[1].strip()
            val = row[2].strip()
            if dt == 'category':
                continue
            if not locations.get(name):
                locations[name] = {}
            locations[name][dt] = val
    print(json.dumps(locations, indent=4))
    return locations



def main():
    con = sqlite3.connect('donations_hack.db')
    cursor = con.cursor()
    file = 'DonationData.tsv'
    loc_data = get_location_data(file)
    for key, data in loc_data.items():
        name = key
        phone = data.get('phone')
        hours = data.get('hours')
        website = data.get('website')
        address = data.get('address')
        add_loc_to_db(cursor, name, phone, hours, website, address)
    con.commit()


if __name__ == '__main__':
    main()