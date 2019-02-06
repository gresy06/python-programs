def minimum(a, n):  
    minpos = a.index(min(a))  
    maxpos = a.index(max(a))   
    print "The maximum is at position", maxpos + 1  
    print "The minimum is at position", minpos + 1
a = [3, 4, 1, 3, 4, 5]  
minimum(a, len(a)) 
