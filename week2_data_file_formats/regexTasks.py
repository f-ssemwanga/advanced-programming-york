import re
def regularExpExercises():
  '''solutions to the above'''
  try:
    file =open("The_Raven.txt", 'r', encoding="utf-8")
    file_contents = [line.strip() for line in file.readlines()] # remove new line characters
    result =re.search(r'\bshrieked\b',''.join(file_contents)) #second argument must be a string
    if result is not None:
      print("Found")
    else:
      print("not found")
    file.close()
  except FileNotFoundError:
    print('Not able to open file - check if it exists')
  except TypeError:
    print('file was found but not able to search it')
regularExpExercises()