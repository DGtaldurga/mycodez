def multiplyList(fruit_list):
    result = 1
    for x in fruit_list:
        result = result * x
    return result
fruit_list=[5,4,3,9,8,7]
print(multiplyList(fruit_list))