print("enter '0' for exit.")
ch = input("enter your character:")
if ch == '0':
  exit();
else:
  if((ch>= 'a' and ch<= 'z') or (ch>= 'A' and ch<= 'Z')):
    print(ch, "is an alphabet");
  else:
    print(ch, "is not an alphabet");
  
  
