# x=int(input())
# y=int(input())
# z=int(input())
# n=int(input())
# list=[]
# for i in range(x):
#     for j in range(y):
#         for k in range(z):
n = int(input())
arr = map(int, input().split())
# [2,3,1,2,1]
l=list(arr)
print(l)
for i in range(n):
    # print(i)
    for j in range(i+1,n):
        # print(j)
        if l[i]>l[j]:
            l[i],l[j]=l[j],l[i]
        else:
            pass
print(l)
print(l[-2])