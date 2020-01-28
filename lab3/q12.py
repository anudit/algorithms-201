import math

input_matrix = [
    [0, -1, 1],
    [-1, 0, -1],
    [1, -1, 0 ]
]

def check_con(ele):
    tr = 0
    fa = 0
    for i in range(len(input_matrix)):
        if (input_matrix[ele][i] == -1):
            fa +=1
        else:
            tr +=1
    if(tr>fa):
        return True
    else:
        return False

def test(r, x, y):
    if(input_matrix[r][x] == input_matrix[r][y]): # 1,1 -1,-1
        return x
    else:
        return -1

res = []

for t_ind in range(len(input_matrix)):
    ind=0
    while ( ind < len(input_matrix[t_ind])-1):

        d = 0
        if t_ind==ind:
            d = [ind+1, ind+2]
            ind +=3
        elif t_ind==ind+1:
            d = [ind, ind+2]
            ind +=3
        else:
            d = [ind, ind+1]
            ind +=2

        # print(t_ind, d[0], d[1])
        tr = test(t_ind, d[0], d[1])
        if tr != -1:
            # print("appended")
            res.append([t_ind, tr])

wrong = []
for inde in res:
    if (check_con(inde[0]) == False):
        wrong.append(inde[0])


for rbs in range(len(input_matrix)):
    if (rbs not in wrong):
        print(str(rbs) + " is right")

# consensus_cnt = math.floor(len(input_matrix)/2)

# # print(freq_table)
# # print(consensus_cnt)

# for key in freq_table:
#     if (freq_table[key]['correct'] >= consensus_cnt):
#         print(f"{key} is functioning correctly")
