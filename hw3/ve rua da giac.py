from turtle import*
shape("arrow")
colors = ["red","blue","brown","yellow","grey"]
for i in range(3,8):
    goc = 180-((i - 2) * 180/i)
    color(colors[i-3])
    for j in range(i):
        left(goc)
        forward(100)

mainloop()