#DIVISIBILITY
#Requirements: python3

#Made by: SvenAzari
#http://www.github.com/svenazari

def divisi ():
  x = input("x = ") #number that enters the test
  a = [] #list of numbers x is divisible with
  try:
    xi = int(x) #convert x to integer
  except ValueError:
    print ("You must input integers only! Run script again an input and integer!")
    exit()
  else:
    try:
      if x == "0":
        print ("If 0 is devided with any number, result is 0.")
        exit()
      elif x == "1":
        print("Number 1 is divisible with number 1.")
        exit()
      else:
        for c in range(1, xi+1, 1):
          d = xi % c
          if d == 0:
            a.append(str(c))
    except KeyboardInterrupt: #if user aborts calculation
      print("\n" + "ABORTED BY USER!")
    else:
      print("Number " + x + " is divisible with numbers " + ", ".join(a) + ".") #print results

divisi () #call function
