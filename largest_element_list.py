
def largest_element(list):
    largest = list[0]
    for i in list:
        if i >largest:
            largest = i
    return largest

list=[3,2,4,8]
result = largest_element(list)
print(result)