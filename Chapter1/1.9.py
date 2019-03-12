
#String Rotation; Assume you have a method i s S u b s t r i n g which checks if one word is a substring of another.
#Given two strings, si and s2, write code to check if s2 is a rotation of si using only one call to isSubstring
# [e.g., "waterbottle" is a rotation oP'erbottlewat"),

def string_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    else:
        return s1 in (s2 + s2)      #lets say we are calling substring like substring(s1,s2+s2)


def main():
    print(string_rotation('waterbottle','erbottlewat'))
    
if __name__ == "__main__":
    main()
