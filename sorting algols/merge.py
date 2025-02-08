def mergesort(arr,start,end):
    if start>=end:
        return ; 
    mid=(start+end)//2
    mergesort(arr,start,mid)
    mergesort(arr,mid+1,end)
    merge(arr,start,mid,end)
def merge(arr,start,mid,end):
    lef=start
    rig=mid+1
    temp=[]
    while lef<=mid and rig<=end:
        if arr[lef] < arr[rig]:
            temp.append(arr[lef])
            lef+=1
        else:
            temp.append(arr[rig])
            rig+=1
    if lef<=mid:
        temp.extend(arr[lef:mid+1])
    if rig <= end:
        temp.extend(arr[rig:end+1])
    '''
    for i in range(start,end+1):
        arr[i]=temp[i-start]
    '''
    arr[start:end+1]=temp    
arr=list(map(int,input().split()))
mergesort(arr,0,len(arr)-1)
print(arr)