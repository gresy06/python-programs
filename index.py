def reorder(arr,index, n): 
  
    temp = [0] * n; 
  
    # arr[i] should be 
        # present at index[i] index 
    for i in range(0,n): 
        temp[index[i]] = arr[i] 
  
    # Copy temp[] to arr[] 
    for i in range(0,n): 
        arr[i] = temp[i] 
        index[i] = i 
