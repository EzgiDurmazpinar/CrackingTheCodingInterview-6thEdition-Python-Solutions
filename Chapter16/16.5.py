#16.5
#Write an algorithm which computes the number of trailing zeros in n factorial
#There will always be more of 2 than 5, though , so simply counting the number of 5 is sufficient.
def factors_of_5(num):
    count = 0
    while (i%5 == 0):
        count +=1
        i = i//5
    return count
def count_trailing_zeros(num):
    if num<0:
        return False
    else:
        count = 0
        i=2
        while(i<=num):
            count+=factors_of_5(i)
            i+=1
    return count
