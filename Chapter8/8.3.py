#8.3 Magic Index :A magic index in an arrayA[0...n-1] is defined to be an index such that A[i] = i.
# Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in array A.

#first brute force
def mgc_idx(array):
    for i in range(len(array)):
        if array[i] == i:
            return i
    return -1

#Faster Approach in a sorted array
def magic_index(array):
    idx = find_magic_index(array,0,len(array)-1)
    #idx = find_not_distinct_magic_idx(array,0,len(array)-1)
    print(idx)

def find_magic_index(array,start,end):
    if end < start:
        return -1
    middle = (start+end)//2
    if array[middle] == middle:
        return middle
    elif array[middle]>middle:
        return find_magic_index(array,start,middle-1)
    else:
        return find_magic_index(array,middle+1,end)
#if array's element is not distinct
def find_not_distinct_magic_idx(array,start,end):
    if end<start:
        return -1
    middle = (start+end) //2
    middle_value = array[middle]
    if middle_value == array[middle]:
        return middle
    #search left
    left_idx = min(middle-1,middle_value)
    left = find_not_distinct_magic_idx(array,start,left_idx)
    if left >= 0:
        return left
    #search right
    right_idx - max(middle+1,middle_value)
    right = find_not_distinct_magic_idx(array,start,right_idx)
    return right
def main():
    array = [-40,-20,-1,1,2,3,5,7,9,12,13]
    magic_index(array)
    #print(mgc_idx(array))

if __name__ == '__main__':
    main()
