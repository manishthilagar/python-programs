def merge_sorted(nums1,nums2):
    """
        Input:
            nums1 = [1,2,3], m = 3
            nums2 = [2,5,6],       n = 3
        Output: 
            [1,2,2,3,5,6]
    """
    ind1=0
    ind2=0
    res=[]
    while(ind1<len(nums1) and ind2<len(nums2)):
        if(nums1[ind1]>nums2[ind2]):
            res.append(nums2[ind2])
            ind2+=1
        else:
            res.append(nums1[ind1])
            ind1+=1
    while(ind1<len(nums1)):
        res.append(nums1[ind1])
        ind1+=1
    while(ind2<len(nums2)):
        res.append(nums2[ind2])
        ind2+=1
    return res

if(__name__ == "__main__"):
    nums1=[1,2,3]
    nums2=[2,5,6]
    print("Sorted merged array is: "+str(merge_sorted(nums1,nums2)))