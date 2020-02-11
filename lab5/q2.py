import numpy as np

data = [("Silent Disco", 24,120),
    ("Bonfire", 24,120),
    ("Street Play", 14,60),
    ("Dancing Competition", 20,60),
    ("Short Film", 22, 30),
    ("Rangoli",16 ,30),
    ("scavenger hunt",17 ,90),
    ("face art",16 ,30),
    ("solo music",19 ,30),
    ("group music",19 ,60),
    ("Mime",23 ,60),
    ("poetry recitation",23 ,60)]

a = np.array(data,dtype=[('name',np.dtype('U25')), ('x',int),('y',int)])
sort = list(a[np.lexsort((a['y'], a['x']))])

cur_time = 12
penalty = 0
for index, event in enumerate(sort):
    event_time = event[1]
    print(f"{event} at {cur_time} - {cur_time+(event[2]/60)}")
    cur_time+=(event[2]/60)
    if cur_time >= event_time:
        penalty+= 50000

print(f"Penality : {penalty}")
