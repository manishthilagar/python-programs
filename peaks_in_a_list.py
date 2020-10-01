def num_peaks(li):
    """
        peaks(li) to find the number of peaks in the array
        parameters: 
            li: list of numbers
        returns: 
            number representing the number of peaks
    """
    mx=0;
    peaks=0
    for i in range(1,len(li)-1):
        if(li[i]>li[i-1] and li[i]>li[i+1]):
            peaks+=1
    return peaks

if(__name__=='__main__'):
    li=[1,2,1,2,1]
    print("Number of Peaks in list is "+str(num_peaks(li)))