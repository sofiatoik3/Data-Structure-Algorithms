def findMedianSortedArrays(self, nums1, nums2):
    Arr = nums1 + nums2
    Arr = sorted(Arr)
    
    if (len(Arr)%2 == 0):
        Position1 = int((round(len(Arr))/2))
        Position2 =  Position1 - 1 
        Median = (Arr[Position1] + Arr[Position2]) / 2
        return Median
    else:
        Position = len(Arr)/2
        Median = Arr[Position]
        return Median