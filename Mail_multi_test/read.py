

def receipient_updater():
	
	try:
		fhand= open('testfile.txt', 'r')

	except:
		print("File is not available or cannot be read at the moment")
		exit()
	count=0
	firstList=["",""]
	lastList=["",""]
	emailList=["",""]
	for line in fhand:
		line=line.rstrip()
		if line.startswith('user'):
			count=count+1
		if line.startswith('first Name'):
			firstList[count]= line[12:]
			#print (First_Name)
		if line.startswith('Last Name'):
			lastList[count] = line[11:]
			#print (Last_Name)
		if line.startswith('Email'):
			emailList[count]= line[7:]
			#print (Email)
	print(firstList)
	print(lastList)
	print(emailList)
	return emailList
receipient_updater()