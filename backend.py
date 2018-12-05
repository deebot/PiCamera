import fileHistoryCheck

while (True):
    status = fileHistoryCheck.inspectors()
    if status == True:
       fhand = open("test.txt")
       for line in fhand:
          emailAddress=line
          print(emailAddress)

