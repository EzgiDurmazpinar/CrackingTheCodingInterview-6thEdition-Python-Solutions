#String Compression: Implement a method to perform basic string compression using the counts of repeated characters.
#For example, the string aabcccccaaa would become a2blc5a3,
#If the "compressed" string would not become smaller than the original string,
#your method should return the original string. You can assume the string has only uppercase and lowercase letters (a - z).

def string_compression(string):

    result = [] #For Result string
    counter = 0 #For the count how many repeated letter
    current = string[0] #set up current to first char of an array

    for char in string:  #iterate through all chars in string

        if char == current: #if char is equal to current count it
            counter += 1
        else:                #if they are not equal
            result.append('{}{}'.format(current, counter)) #append the letter which repeated and append also how many times
            current = char #now make current char
            counter = 1 #and make counter 1 again

    result.append('{}{}'.format(current, counter))
    result = ''.join(result)

    if len(result) > len(string): #if original string is smaller then compressed one return original
        return string
    else:                           #otherwise return the compressed one
        return result

def main():
    my_string = 'aaabbbvcgggaa'
    print(string_compression(my_string))

if __name__ == '__main__':
    main()
