#The Seive of Ertosthenes
def generate_list_of_primes(max):
    prime = 2
    flags = [True]*max+1
    while(prime <= math.sqrt(max)):
        #cross list with values that has multiplier of this prime
        cross_list(flags,prime)
        #get the nex primw number
        prime = get_next_prime(flass,prime)

def cross_list(flags,prime):
    i = prime*prime
    while(i<len(flags)):
        flags[i] = False
        i +=prime

def get_next_prime(flags,prime):
    next = prime+1
    while(next<len(flags) and flags[next]!=True):
        next +=1
    return next
