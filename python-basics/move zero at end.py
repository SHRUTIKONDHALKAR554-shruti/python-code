def move_zero(number):
    result=[]
    for num in number:
        if num!=0:
            result.append(num)
    for num in number:
         if num==0:
             result.append(num)
    return result
number=[0,1,0,3,12,0,5]
print(move_zero(number))