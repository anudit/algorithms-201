import math

input_matrix = [
    [0, -1, 1],
    [-1, 0, -1],
    [1, -1, 0 ]
]

freq_table={}
for i in range(len(input_matrix)):
    freq_table[i] = {
        'correct':0,
        'fault':0
    }

for rb_ind in range(len(input_matrix)):
    for dp_ind in range(len(input_matrix[rb_ind])):
        if (dp_ind!=rb_ind):
            if(input_matrix[rb_ind][dp_ind]==-1):
                freq_table[dp_ind]['fault']+=1
            elif(input_matrix[rb_ind][dp_ind]==1):
                freq_table[dp_ind]['correct']+=1

consensus_cnt = math.floor(len(input_matrix)/2)

# print(freq_table)
# print(consensus_cnt)

for key in freq_table:
    if (freq_table[key]['correct'] >= consensus_cnt):
        print(f"{key} is functioning correctly")
