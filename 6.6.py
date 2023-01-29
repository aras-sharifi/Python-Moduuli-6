def unitprice(diameter,price):
    radius = diameter / 2
    area = 3.14 * radius**2
    unitprice = price / area
    return unitprice


diameter1 = float(input("Add pizza 1 diameter: "))
price1 = float(input("Add pizza 1 price: "))
diameter2 = float(input("Add pizza 2 diameter:"))
price2 = float(input("Add pizza 2 price: "))
unit_price1 = unitprice(diameter1, price1)
unit_price2 = unitprice(diameter2, price2)
if unit_price1 < unit_price2:
    print("First pizza")
else:
    print("Second pizza")



