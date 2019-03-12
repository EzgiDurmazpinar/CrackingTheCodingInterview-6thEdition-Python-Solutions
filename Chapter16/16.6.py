#16.6
#smallestDifferences

#First Approach Brute Force
def find_smallest_diff(arr1,arr2):
    min_diff = 1000000
    for a in arr1:
        for b in arr2:
            min_diff = min(min_diff,abs(a-b))
    return min_diff


#Solution2
#sort arrays First

def find_smallest_diff2(arr1,arr2):
    min_diff = 1000000
    arr1.sort()
    arr2.sort()
    i = j = 0
    while(i<len(arr1) and j<len(arr2)):
        min_diff = = min(min_diff,abs(arr1[i]-arr2[j]))
        if arr1[i] < arr2[j]:
            i+=1
        else:
            j+=1
    return min_diff
