# Code completed by Sarthak Mittal
# Roll Number 200050129

File = open("HarryPotterAndTheSorcerersStone.txt",'r')
DictionaryOfWords = {}
Novel = []

i = 0
for line in File.readlines():
  line = line.replace(".","").replace(",","").replace('?','').replace('!','').replace('[','').replace(']','')\
  .replace('(','').replace(')','').replace('%','').replace('/','')

  for word in line.split(' '): 
    if word in DictionaryOfWords.keys():
      DictionaryOfWords[word].append(i)
    else:
      DictionaryOfWords[word] = [i]
    Novel.append(word)
    i += 1

def GetQuery():
  word = input()
  Number = int(input())
  return (word,Number)   

def PrintContext(index):
  global Novel
  for i in range(-5,5):
    print(Novel[index + i], end = ' ')
  print('\n')

def PrintResult(word, NumQuery):
  global DictionaryOfWords
  L = DictionaryOfWords[word] 
  for i in range(0,min(len(L),NumQuery)):
    PrintContext(DictionaryOfWords[word][i])
  
while True:   
  Choice = input('Press Y in order to Continue with the next query or N to end. Please press Enter after entering your choice!\n')
  if Choice == 'Y':
    t = GetQuery()
    PrintResult(t[0],t[1])
  else:
    break          