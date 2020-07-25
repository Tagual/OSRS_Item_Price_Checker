
import requests
import json
import urllib

#Open the database 
def open_database():
    """Open the database. """
    with urllib.request.urlopen("https://raw.githubusercontent.com/osrsbox"
    "/osrsbox-db/master/docs/items-summary.json") as url:
        osrs_database = json.loads(url.read().decode())
        return osrs_database

def request_item_name(osrs_database):
    """Obtain the item ID. """
    item_requested = input('Enter your item here: ')
    for x in osrs_database.values():
        new_values = list(x.values())

        if item_requested.capitalize() in new_values:
            item_id = (new_values[0])
            return item_id

def get_item_price(id):
    """Use the OSRS API to get the item price on the GE. """
    url = (
        f"http://services.runescape.com/m=itemdb_oldschool/"
        f"api/catalogue/detail.json?item={id}"
    )
    r = requests.get(url)
    response_url = r.json()
    response_url = response_url['item']
    price = response_url['current']['price']
    item_name = response_url['name']
    return(f"A {item_name} costs {price} gp.")

def get_the_cost_of_item():
    try:
        new_database = open_database()
        item_id = request_item_name(new_database)
        final_response = get_item_price(item_id)
        print(final_response)
    except ValueError:
        print("You spelt the item incorrectly, or the item "
        "is not tradeable.")


get_the_cost_of_item()
    
while True:
    user_input = input("Do you still want to find the price of "
    "items? (y/n) ")
    if user_input.lower() == 'y':
        get_the_cost_of_item()
    else: 
        break
print("Thanks, see you soon")
