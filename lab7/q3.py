time_consume=[[3,3,5,7,9,10,14,16],[4,4,6,5,11,6,15,22]]
switch_time=[[2,1,3,3,2,1,3,3,2],[2,1,2,2,3,2,4,3,1]]
def self1(t,s):
    # take any sublist of above given array
    i=len(time_consume[0])
    path1_time=[0 for k in range(i)]
    path2_time=[0 for k in range(i)]
    #Initial time of both paths
    path1_time[0]=time_consume[0][0]+switch_time[0][0]
    path2_time[0]=time_consume[1][0]+switch_time[1][0]
    for l in range(1,i):
        path1_time[l]=min(path1_time[l-1]+time_consume[0][l],path2_time[l-1]+switch_time[1][l]+time_consume[0][l])
        path2_time[l]=min(path2_time[l-1]+time_consume[1][l],path1_time[l-1]+switch_time[0][l]+time_consume[1][l])
    a=path1_time[i-1]
    b=path2_time[i-1]
    return(min(a,b))
print(self1(time_consume,switch_time))