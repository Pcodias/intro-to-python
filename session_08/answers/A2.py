# A2 - Read the file 'austen.txt' and print the amount of lines in the file

#Option 1
total = 0
for x in open("austen.txt"):
    total += 1

print(total)

#Option 2 
total=0
file = open (text_files/"austen.txt, "r"")"
for line in file:
  total +=1
  print(total)
