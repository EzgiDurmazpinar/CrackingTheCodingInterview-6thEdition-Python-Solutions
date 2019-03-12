#Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
#A palindrome is a word or phrase that is the same forwards and backwards.
#A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.


#First I need to preprocess the strings to eliminate things like case and spaces so we can just focus on the letters that
#are present in the string

def is_perm_plindrome(string):
    #Deal with case
    input_string = string.lower()
    #Deal with spaces
    input_string = input_string.replace(" ", "")

    my_dict = dict() #the syntax is: mydict[key] = "value" --> mydict[t] = 2

    for char in input_string:  #Adding values as how many time that key is occured
        if char in my_dict:
            my_dict[char] +=1
        else:
            my_dict[char] = 1
#Algorithm works like this : If we have ANNA OR TACT COA --> HER harften iki tane veya toplam bir hafrten 1 tane var eger boyle olursa perm of palindrome
    even_ctr = 0
    one_ctr = 0
    odd_ctr = 0
    for key, value in my_dict.items():
        if value%2 == 0:
            even_ctr+=1
        elif value == 1:
            one_ctr+=1
        else:
            odd_ctr+=1

    if(one_ctr>1 or odd_ctr>0):
        return False
    else:
        return True

def main():
    my_string = 'This is not a palindrome permutation'
    print(is_perm_plindrome(my_string ))

if __name__ == '__main__':
    main()
