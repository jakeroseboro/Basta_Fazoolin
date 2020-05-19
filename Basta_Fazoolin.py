#Defining the classes
class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  def __repr__(self):
    return (self.address)
  def available_menus(self, time):
    available_menus = []
    for i in self.menus:
      if time >= i.start_time and time <= i.end_time:
        available_menus.append(i)
    return available_menus

class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  def __repr__(self):
    return (self.name +" menu available from " + str(self.start_time) + " to " + str(self.end_time))
  def calculate_bill(self, purchased_items):
    total = 0 
    for i in purchased_items:
      if i in self.items:
        total += self.items[i] 
    return total

class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises
#Defining the items and keys
brunchItems = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
earlyBird = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
dinnerItems = {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
kidItems = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
arepas_menu = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
#Creating Menus
brunch = Menu("Brunch", brunchItems, 1100, 1600)
early_bird = Menu("Early-bird Dinner", earlyBird, 1500, 1800)
dinner = Menu("Dinner", dinnerItems, 1700, 2300)
kids = Menu("Kids", kidItems, 1100, 2100)
arepasMenu = Menu("Take a' Arepa", arepas_menu, 1000, 2000)
#Creating lists for franchises
menus = [brunch, early_bird, dinner, kids]
arepa = [arepasMenu]
#Creating Franchises and Businesses
flagship_store = Franchise("1232 West End Road", menus)

new_installment = Franchise("12 East Mulberry Street", menus)

arepas_place = Franchise("189 Fitzgerald Avenue", arepa)

business1 = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

Arepas = Business("Take a' Arepa", arepas_place)


























