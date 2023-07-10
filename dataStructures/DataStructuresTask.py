#stack demo application
def inputValidator(inputString):
  '''returns numeric user choice'''
  while True:
    try:
      choice = int(input(f"Enter a {inputString}:"))
      return choice
    except ValueError:
      print('Enter a numeric value')

def stackOperation():
  '''stack demo'''
  stackItems = []
  while True:
    print('-'*30)
    print('Choose Stack operations\n1. Push\n2. Pop\n3. View\n4. Return to main menu')
    operation =inputValidator("stack operation")
    print('-'*15)
    print()
    if operation ==1:
      print(f'Original Stack status: {stackItems}')
      toPush = inputValidator("value to push onto the stack")
      print(f'Original Stack: {stackItems}')
      stackItems.insert(0,toPush)
      print(f'Updated Stack status: {stackItems}')
      continue
    elif operation == 2:
      if len(stackItems) ==0:
        print('No items to pop! Stack is empty')
        continue
      else:
        print(f'Original Stack: {stackItems}')
        del stackItems[0]
        print(f'Updated Stack status: {stackItems}')
        continue
    elif operation ==3:
      print(f'Current Stack status: {stackItems}')
      continue
    elif operation == 4:
      break
    else:
      print('Invalid menu option')
def queueOperation():
  '''queue demo'''
  queueItems = []
  while True:
    print('-'*30)
    print('Choose Queue operation: \n1. Push\n2. Pop\n3. View\n4. Return to main menu')
    operation =inputValidator("queue operation")
    print('-'*30)
    print()
    if operation ==1:
      print(f'Original Queue status: {queueItems}')
      toPush = inputValidator("value to push onto the queue")
      print(f'Original Queue: {queueItems}')
      queueItems.append(toPush)
      print(f'Updated Queue status: {queueItems}')
      continue
    elif operation == 2:
      if len(queueItems) ==0:
        print('No items to pop! Queue is empty')
        continue
      else:
        print(f'Original Queue: {queueItems}')
        del queueItems[0]
        print(f'Updated Queue status: {queueItems}')
        continue
    elif operation ==3:
      print(f'Current Queue status: {queueItems}')
      continue
    elif operation == 4:
      break   
    else:
     print('Invalid menu option')    
  
def main():
  '''Menu to demo a stack'''
  while True:
    print("Choose a structure to test:")
    print('1. Stack\n2. Queue\n3. Quit')
    userChoice = inputValidator("menu choice")
    if userChoice == 1:
      stackOperation()
    if userChoice == 2:
      queueOperation()
    elif userChoice == 3:
      quit()
      break