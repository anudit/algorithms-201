def knapSack(B, cost, rating, n): 
    K = [[0 for x in range(B + 1)] for x in range(n + 1)]  
    for i in range(n + 1): 
        for w in range(B + 1): 
            if i == 0 or B == 0: 
                K[i][B] = 0
            elif cost[i-1] <= B: 
                K[i][B] = max(rating[i-1] + K[i-1][B-cost[i-1]],  K[i-1][B]) 
            else: 
                K[i][B] = K[i-1][B] 
  
    return K[n][B] 
  
rating = [24, 13, 23, 15, 16]     ####rating array 
cost = [ 12, 7, 11, 8, 9]         ####cost array 
B = 26                            #### B
n = len(rating)                   #### n
print(knapSack(B, cost, rating, n)) #### ANS