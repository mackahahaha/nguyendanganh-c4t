prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3

}
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
for  keys, values in prices.items():
    print (keys)
    print("price:",values)
    print("stock:",stock[keys])
    print()
total=0
for k,v in prices.items():
    p = v*stock[k]
    print(k,"'s price:",p)
    total=total+p
print()
print("total prices",total)
input("enter to escape")