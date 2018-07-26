for row in range(1, 10):
    for col in range(1, 10):
        num = row * col
        if num < 10:
            space = "  "
        else:
            if num < 100:
                space  = " "
        print(space, num, end = '')
    print()
input("enter to exit")
