# arr = [['silent disco', 15, 100000],
# 	['Bonfire', 15, 500000],
# 	['Street Play', 15, 60000],
# 	['Dancing competition', 15, 75000],
# 	['Short Film screening', 20, 45000],
#     ['Rangoli',20 ,50000]]

# sort = sorted(arr,key=lambda arr: (arr[1], arr[2]))

# cur_time = 12
# penalty = 0
# for index, event in enumerate(sort):
#     event_time = event[1]
#     print(f"{event} at {cur_time} - {cur_time+1}")
#     if cur_time >= event_time:
#         penalty+= event[2]
#     cur_time+=1

# print(f"Penalty : {penalty}")


import numpy as np

data = [("Silent Disco", 15,100000),
("Bonfire", 15,500000),
("Street Play", 15,60000),
("Dancing Competition", 15,75000),
("Short Film", 20, 45000),
( "Rangoli",20 ,50000)]

# data = [("Silent Disco", 13,10),
# ("Bonfire", 14,50),
# ("Street Play", 14,60)]

a = np.array(data,dtype=[('name',np.dtype('U25')), ('x',int),('y',int)])
sort = list(a[np.lexsort((-a['y'], a['x']))])

cur_time = 12
penalty = 0
for index, event in enumerate(sort):
    event_time = event[1]
    print(f"{event} at {cur_time} - {cur_time+1}")
    if cur_time >= event_time:
        penalty+= event[2]
    cur_time+=1

print(f"Penality : {penalty}")
