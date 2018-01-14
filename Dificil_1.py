mult_3_5 = []

for x in range(1000):
    if (x%3==0):
        if(x not in mult_3_5):
            mult_3_5.append(x)
    if (x%5==0):
        if(x not in mult_3_5):
            mult_3_5.append(x)

#for x in mult_3_5:
#    print(x)
   
total = 0
for x in mult_3_5:
    total=total+x

print(total)
