
import requests
import json


#Open the database 
def open_database():
    """Open the database. """
    filename = 'data/objects_osrs.json'
    with open(filename) as f:
        osrs_database = json.load(f)
        return osrs_database


def request_item_name(osrs_database):
    """Obtain the item ID. """
    item_requested = input('Enter your item here: ')
    for item_osrs in osrs_database:
        if item_osrs['name'] == item_requested:
            return(item_osrs['id'])

def get_item_price(id):
    """Use the OSRS API to get the item price on the GE. """
    base_url = 'http://services.runescape.com/m=itemdb_oldschool'
    end_url = f"/api/catalogue/detail.json?item={id}"
    url = base_url + end_url

    r = requests.get(url)
    # print(f"Status Code: {r.status_code}")
    response_url = r.json()

    response_url = response_url['item']
    price = response_url['current']['price']
    item_name = response_url['name']
    return(f"A {item_name} costs {price} gp.")
    
try:
    new_database = open_database()
    item_id = request_item_name(new_database)
    final_response = get_item_price(item_id)
    print(final_response)
except ValueError:
    print("You spelt the item incorrectly, or the item is not tradeable.")

