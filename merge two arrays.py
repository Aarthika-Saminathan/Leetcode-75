def merged_two_array(arr1,arr2):
      merged=[]
      i,j=0,0,
      while i <len(arr1) and j <len(arr2):
            merged.append(arr1[i])
            merged.append(arr2[j])
            i+=1
            j+=1
      merged.append(arr1[i: ])
      merged.append(arr2[j: ])
      return ''.join(merged)
arr1=("abc")
arr2=("pqr")
print(merged_two_array(arr1,arr2))