def check_power(N,K);
if N <= 0 or k <=0:
        print "not a valid input"
    else:
        for i in range (1,20):
            x = k**i
            if x == N :
                print " True "
                print k, "power ", i , "is", N
                break
            elif x> N:
                print "false"
                break
check_power(244140625,5)
check_power(4096,16)
check_power(0,16)
check_power(1,1)
