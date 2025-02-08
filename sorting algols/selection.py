# get min and swap with first index
# increment index and repeat s1
arr=list(map(int,input().split()))
for i in range(len(arr)):
    krr=arr[i::]
    m=min(krr)
    j=i+krr.index(m)
    arr[i],arr[j]=arr[j],arr[i]
print(arr)

'''
# with out fun()
arr=list(map(int,input().split()))
for i in range(len(arr)):
    krr=arr[i::]
    m=krr[0]
    for k in krr:
        if k<m:
            m=k
    j=i+krr.index(m)
    arr[i],arr[j]=arr[j],arr[i]
print(arr)
'''