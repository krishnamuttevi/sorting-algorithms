arr=list(map(int,input().split()))
'''
for i in range(len(arr)):
    key = arr[i]
    j=i-1
    while arr[j]>key and j>=0:
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=key
print(arr)
''' 
for i in range(len(arr)):
    j=i
    while j>0 and arr[j-1]>arr[j]:
        arr[j-1],arr[j]=arr[j],arr[j-1]
        j-=1
        print(arr)
print('end')
print(arr)