def csvReader():
  '''read in the csv file'''
  f = open ("PeopleTrainingData.csv", 'r')
  f_contents =f.read().splitlines()
  print(f_contents)
  f.close()