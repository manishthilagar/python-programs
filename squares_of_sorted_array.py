def squares(li):
    """
        Input: [-4,-1,0,3,10]
        Output: [0,1,9,16,100]
    """
    res=[]
    for i in li:
        res.append(i*i)
    return sorted(res)

if(__name__=="__main__"):
    li=[-4,-1,0,3,10]
    print("Squares of sorted array is: "+str(squares(li)))