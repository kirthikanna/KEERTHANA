# You have been given a list of N integers which represents the number of Mangoes in a bag. Each bag has a variable numbers of Mangoes. There are M students in a Guvi class.your task is to distribute the Mangoes in such a way that each student gets one Bag. The difference between the number of Mangoes in a bag with maximum Mangoes and Bags with minimum Mangoes givento the student is minimum?

# m mangoes
# p people
def distribution(p,m):
    res = 1
    if m>p-m:
       m=p-m
    for i in range(0,m):
        res*=(p-i)
        res/=(i+1)

    return res
# helper function for generating no of ways
# to distribute m mangoes amongst p people    
def calculate_ways(m,p):
     # not enough mangoes to be distributed    
    if m<p:
        return 0
 
    # ways  -> (p + m-1)C(p-1)
    ways = distribution(p + m-1, p-1)
    return int(ways)
 
# Driver function
if __name__ == '__main__':
 
    # m represents number of mangoes 
    # n represents number of people
    m = 8 ;p = 5
 
    result = calculate_ways(m, p)
    print(result)