#8.8
#Permutations with Dups:
#Write a method to compute all permutations of a string whose characters are not necessarily unique.
#The list of permutations should not have duplicates.

def permutations(string):
    return partial_permutations("", sorted(string))

def partial_permutations(partial, letters):
    if len(letters) == 0:
        return [partial]
    permutations = []
    previous_letter = None
    for i, letter in enumerate(letters):
        if letter == previous_letter:
            continue
        next_partial = partial + letter
        next_letters = letters[:i] + letters[(i+1):]
        permutations += partial_permutations(next_partial, next_letters)
        previous_letter = letter
    return permutations
