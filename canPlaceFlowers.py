def canPlaceFlowers(flower,n):
    count=0
    length=len(flower)

    for i in range (length):
        if flower[i]==0:
            if(i==0 or flower[i-1]==0) and (i==length-1 or flower[i+1]==0):
                flower[i]=1
                count+=1
        if count >=n:
            return True
    return False
flower=[1,0,0,0,1]
n=2
print(canPlaceFlowers(flower,n))