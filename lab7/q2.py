import sys
def count1(arr,i,j):
    if(i==j):return 0
    sup = sys.maxsize 
    for k in range(i,j):
        count=count1(arr,i,k)+count1(arr,k+1,j)+(arr[i-1]*arr[k]*arr[j])
        if(count<sup):sup=count
    return sup
arr=[1,2,3,4,2]
print(count1(arr,1,len(arr)-1))