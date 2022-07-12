
solution=[]

def divisible_by_3_5(a):
    for i in range(0,a):
        if i%3==0 and i%5==0:
            solution.append(i)
            continue
        else:
            continue

a = int(input("enter a number"))
divisible_by_3_5(a)
print(solution)        