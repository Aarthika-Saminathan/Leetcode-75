def reverseWords(s):
    s=s.strip()
    words=s.split()
    words.reverse()     
    return ' '.join(words)

s="hi im aarthika"
print(reverseWords(s))