import math
def gcd_of_strings(str1,str2):
    if str1+str2 !=str2+str1:
       return  ""
    gcd_len=math.gcd(len(str1),len(str2))
    return str1[ :gcd_len]

str1="abcabc"
str2="abc"
print(gcd_of_strings(str1,str2))