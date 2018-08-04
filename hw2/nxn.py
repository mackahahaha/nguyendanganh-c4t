n = int(input("n="))
for row in range(1, n+1):
    for col in range(1, n+1):
        num = row * col
        if num < 10:
            space = "  "
        else:
            if num < 100:
                space  = " "
        print(space, num, end = '')
    print()
input("enter to exit")
