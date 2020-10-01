import math
def even_digs(nums):
    """    
    Input: nums = [12,345,2,6,7896]
    Output: 2
    Explanation: 
        12 contains 2 digits (even number of digits). 
        345 contains 3 digits (odd number of digits). 
        2 contains 1 digit (odd number of digits). 
        6 contains 1 digit (odd number of digits). 
        7896 contains 4 digits (even number of digits). 
        Therefore only 12 and 7896 contain an even number of digits.
    """
    res=0
    for i in range(len(nums)):
        digits=1+int(math.log10(nums[i]))
        if(digits%2==0):
            res+=1
    return res;

if(__name__ == "__main__"):
    nums=[10,232,143,7021]
    print("Number of elements with even digits are "+str(even_digs(nums)))
