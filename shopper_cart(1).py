#greeting
print("Hi!!! Welcome to JED'S UNIVERSAL SHOPPING MARKET! Here you can shop anything!")
print("(type buy to stop shopping and pay,type show cart to see cart, type show bill to see bill, type remove to remove from cart)")
#ill put all of these ^^^^ in a while with ifs for each
items = []
#there'll be an items^ and item
prices = []
#prices and price too
bill = 0.000000000000000000000000000000000000000000000000000000000000000 #its gonna be bill += price
#I had to make sure you knew that the bill truly starts at 0 and im not overcharging ;)
while True:
  item = input("Add an Item to your cart!")
  if item == "buy": #stop the shoppin (saves you money foreal)
        break
  elif item == "remove":
      remove = items(input("What item would you like to remove(you better buy something in its place)"))
      items.remove(remove)
      price.remove(remove)
#this is honestly the only place i had trouble thank the Lord it worked
  elif item == "show bill":
    print(f"Here's your bill(next time dont skip math) {bill}")
  elif item == "show cart":
    print(f"Here's what you have in your cart(no way you cant remember) {items}")
  elif item:
      price = float(input(f"What's the price of {item}: $"))
      items.append(item)
      #.append() adds the value you put in to the list you put in fronna the .
      prices.append(price)
  else:
    print("love you")
print("")#putting a space in between what theyre inputting and when they quit
print("<<<<JUSM CART>>>>")#after they type quit and it breaks, now its not an endless nothingness
for item in items:
  print(item)
for price in prices:
  bill += price
  bill = bill*1.13 #taxing them so i can make profit (buggin if u think im giving that to sum1)
print(f"So your bill comes out to ${bill}")
print("Hope your card doesnt decline lol, otherwise we gonna have issues :(")
