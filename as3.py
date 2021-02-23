import re 
def rem_vowel(string): 
    return (re.sub("[aeiouAEIOU]","",string))             
string =input("Enter a string :")
print(rem_vowel(string))