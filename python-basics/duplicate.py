def find_duplicate(num):
    duplicate=[]
    for i in range(len(num)):
        for j in range(i+1,len(num)):
            if num[i]==num[j]:
             if num[i] not in duplicate:
              duplicate.append(num[i])
              return duplicate
num=[10,20,30,40,20]
print("duplicate",find_duplicate(num))
