def issubsequence(s,t):
    i=0
    for char in t:
        if i <len(s) and char==s[i]:
            i+=1
    return i==len(s)
