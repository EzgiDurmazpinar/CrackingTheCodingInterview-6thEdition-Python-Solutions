#8.4 Power Set: Write a method to return all subsets of a set.

def getSubsets(set):
    allSubsets = []  #result array to return all subsets
    max = 1 << len(set) #len = 4 if do left shift it is 16
    for k in range(max):
        subset = convertIntToSet(k, set)
        allSubsets.append(subset)
    return allSubsets

def convertIntToSet(x, set):
    subset = []
    index = 0
    k = x
    while k > 0:
        if k & 1 == 1 and set[index] not in subset:
            subset.append(set[index])
        index += 1
        k >>= 1
    return subset
def main():
    s = ['a', 'b', 'c', 'd']
    print(getSubsets(s))

if __name__ == '__main__':
    main()
