    my_list = []
    count = int(input("How many numbers you want to add : "))
    for i in range(1,count+1):
      my_list.append(int(input("Enter number {} : ".format(i))))
    print("Input Numbers : ")
    print(my_list)
    min = my_list[0]
    max = my_list[0]
    for no in my_list:
      if no < min : min = no elif no > max :
        max = no
    print("Minimum number : {}, Maximum number : {}".format(min,max))
