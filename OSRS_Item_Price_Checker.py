
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
    item_ids = []
    for item in osrs_database.values():
        if item_requested.lower() in item['name'].lower():
            item_ids.append(item['id'])
    return item_ids
    

def get_item_price(item_ID):
    for object_ID in item_ID:
        """Use the OSRS API to obtain item price on the GE. """
        try:
            url = (
                f"http://services.runescape.com/m=itemdb_oldschool/"
                f"api/catalogue/detail.json?item={object_ID}"
            )
            r = requests.get(url)
            response_url = r.json()
            response_url = response_url['item']
            price = response_url['current']['price']
            item_name = response_url['name']
            (print(f"{item_name} costs {price} gp."))
        except: 
            pass
    return

def get_the_cost_of_item():
    try:
        new_database = open_database()
        item_id = request_item_name(new_database)
        if item_id == []:
            return print("You have spelt the item incorrectly or it is not "
            "tradeable")
        get_item_price(item_id)
    except ValueError:
        pass
        print("You spelt the item incorrectly, or the item "
        "is not tradeable.")
    return


get_the_cost_of_item()
    
while True:
    user_input = input("Do you still want to find the price of "
    "items? (y/n) ")
    if user_input.lower() == 'y':
        get_the_cost_of_item()
    else: 
        break
print("Thanks, see you soon")



