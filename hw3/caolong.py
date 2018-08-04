sizes = [5,10,100,300,250,200,20,30]
print ("Hello my name is Dang Anh and here is my sheep size")
print (sizes)
m= int(input("Months="))
for i in range (m):
    print ("Month",m)
    new_sizes = [s + 50 for s in sizes]
    print("One month has passed, now here is my flock")
    sizes = new_sizes
    print(sizes)
    x = max(sizes)
    max_index = sizes.index(x)
    print ("Now my biggest size is", x,"let's shear it")
    sizes[max_index]=8
    print ("After shearing, here is my flock")
    print (sizes)
total = sum(sizes)
print ("My flock has size in total", total)
price = total*2
print ("I would get", total, "*2$ =",price)
input("Enter to exit")