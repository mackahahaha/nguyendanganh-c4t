shop_item = ["T-shirt" ,"Sweater"]
temp_string = shop_item

while 1>0:
    print("Welcome to our shop, what do you want(C,R,U,D)?", end = ' ')
    item = str(input(""))
    position = -1
    if item == "C":
        new = str(input("enter new item:"))
        temp_string.append(new)
    if item == "U":
        position = int(input("Update position?"))
        another = str(input("Enter new item:"))
        if position < 0: break
        if position > len(shop_item): break
        temp_string[position - 1] = another
    if item == "D":
        position = int(input("delete position?"))
        if position < 0: break
        if position > len(shop_item): break
        temp_string.__delitem__(position - 1)
    if item != "C" and item != "D" and item != "R" and item != "U": break

    shop_item = temp_string
    print("our_items", shop_item)

input("enter to exit")
