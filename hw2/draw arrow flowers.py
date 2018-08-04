favorites =["xem phim","choi","an"]
print(favorites)
print("what location  you like update?")
index = int(input("index="))
print("what thing you like update?")
thing = input("thing=")
favorites[index] = thing
print(favorites)

menu = ["thit xien", "pho cuon","bun cha"]
# index = 2
# new_values = "banh bao"
# menu[index] = new_values
#
# print(menu)
# no = 1
# for item in menu:
#     # print(no,".",item,sep="")
#     text = "{0}. {1} ". format(no, item)
#     print(text)
#     no += 1
# for index , item in enumerate(menu):
#     print(index,item)
# menu.remove("thit xien")
# print(menu)
menu.pop(-1)
