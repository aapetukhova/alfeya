m = float (input ("Weight(kg): "))
h = float (input( "Height(cm): "))
i= (m*10000)/(h*h)
print(i)
if i < 16:
    print ("Very severely underweight")
elif i > 16 and i <= 18.5:
    print ("Underweight")
elif i > 18.5 and i < 25:
    print ("Normal")
elif i >= 25 and i < 30:
    print ("Overweight")
elif i >= 30 and i < 35:
    print ("Obesety 1")
elif i >=35 and i < 40:
    print ("Obesety 2")
elif i >= 40:
    print ("Obesety 3")
