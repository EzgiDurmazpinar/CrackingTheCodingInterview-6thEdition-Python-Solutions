#One Away: There are three types of edits that can be performed on strings:
#insert a character, remove a character, or replace a character.
#Given two strings, write a function to check if they are one edit (or zero edits) away.


#We can start comparing lengths of two strings if the difference is more than 1 it cant be one awayself.
def one_away(string1,string2):

    size1 = len(string1)
    size2 = len(string2)

    if(abs(size1 - size2) > 1): #If difference between m an n is more than 1, return false.
        print('sizedan dolayi dondu')
        return False

    total_edit_ctr = 0  #Initialize count of edits as 0.
    i=0
    j=0

    while(i<size1 and j<size2): #Start traversing both strings from first character.

        if(string1[i] != string2[j]):  #If current characters don't match, then
            total_edit_ctr +=1 #Increment count of edits

            if(total_edit_ctr > 1): #If count becomes more than 1, return false
                return False
            #If length of one string is  more, move ahead in larger string.
            if size1>size2:
                i+=1
            elif size2>size1:
                j+=1
                #If length is same, then only possible edit is to  change a character. Therefore, move ahead in both strings.
            else:
                i+=1
                j+=1

        else:              #if current characters match go ahead both
            i+=1
            j+=1

    if total_edit_ctr>1: #if it is edited more than 1 return false
        return False
    else:
        return True #otherwise return true


def main():
    print(one_away('pales','pale'))

if __name__ == '__main__':
    main()
