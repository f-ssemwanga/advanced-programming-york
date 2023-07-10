from conversionModule import *

def conversionCalculator():
  
  print("Choose an option from the menu")
  displayMenu =""
  while displayMenu!=10:
    print("1. Convert Length\n2. Convert Mass\n3. Convert Temperature\n4. Convert Time \n5. Quit ")
    option = inputValidator("menu")
    if option ==1:
      lengthConverter()
    elif option ==2:
     massConverter()
    elif option ==3:
     tempConverter()
    elif option ==4:
     timeConverter()
    elif option ==5:
      quit()