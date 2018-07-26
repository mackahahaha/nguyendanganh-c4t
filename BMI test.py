n = float(input("height(cm)="))
l = float(input("weight(kg)="))
c = n / 100
print(c,"m")
b = l/(c*c)
print("BMI=",b)
if b<16 :
    print("you are Severely underweight")
if  b <= 18.5:
    print("you are Underweight")
if  b <= 25:
    print("you are Normal ")
elif b <=30:
    print("you are Overweight ")
else :
    print("you are Obese ")
input("press enter to exit")