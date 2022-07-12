a= int(input("how many numbers do you want to enter"))
sum=0
for i in range(0,a):
    b = int(input("number"))
    sum+=b
    print(sum)
print(sum/a)