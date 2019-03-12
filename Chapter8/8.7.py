#8.7
#Permutations without Dups: Write a method to compute all permutations of a string of unique characters.
def calculate_permutation(lst):
    if len(lst) == 0 :
        return []
    elif len(lst) == 1:
        return [lst]
    else:
        l = []
        for i in range(len(lst)):
            x = lst[i]
            xs = lst[:i] + lst[i+1:]
            for p in calculate_permutation(xs):
                l.append([x]+p)
        return l
def main():
    la = list('abc')
    print(calculate_permutation(la))
if __name__ == '__main__':
    main()
