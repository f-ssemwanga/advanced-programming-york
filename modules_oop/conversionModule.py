
def inputValidator(param):
  '''returns a validated menu option'''
  while True:
    if param =="menu":
      try:
        choice =int(input('Enter a menu choice: '))
        return choice
      except ValueError:
        print('Entered choice must be a number')
    elif param=="data":
      try:
        choice =float(input('Enter a value to convert: '))
        if choice >0:
          return choice
        else:
          print('input must be more than 0')
          continue
      except ValueError:
        print('Entered choice must be a number')

def lengthConverter():
  '''takes the length and returns a unit'''
  print('---------------- Length Conversion Calculator --------------')
  print("1. Feet to Metres\n2. Inches to Metres")
  
  while True:
    option = inputValidator("menu")
    if option ==1:
      feet = inputValidator("data")
      meters = feet/3.28
      print(f'{feet}\' is equivalent to {meters:.2f}M')
    elif option == 2:
      inches = inputValidator("data")
      meters = inches/39.37
      print(f'{inches}" is equivalent to {meters:.2f}M')
    else:
      break
   
def massConverter():
  '''takes the weight in pounds and returns equivalent in KG'''
  print('---------------- Mass Conversion Calculator --------------')
  pounds = inputValidator("data")
  kgs = pounds/2.20462
  print(f'{pounds}lbs is equivalent to {kgs:.2f}KG')
    
def tempConverter():
  '''takes the temp in Kelvin and returns temp in celsius'''
  print('---------------- Kelvin to Celcius Calculator --------------')
  K = inputValidator("data")
  c= K - 273.15
  print(f'{K}K is equivalent to {c}C')
def timeConverter():
  print('---------------- Seconds Calculator --------------')
  print("1. Hours to Seconds\n2. Minutes to Seconds")
  
  while True:
    option = inputValidator("menu")
    if option ==1:
      hours = inputValidator("data")
      seconds = hours*3600
      print(f'{hours} is equivalent to {seconds} seconds')
    elif option == 2:
      minutes = inputValidator("data")
      seconds = minutes*60
      print(f'{minutes}" is equivalent to {seconds} seconds')
    else:
      break