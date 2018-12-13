import os


def inspectors():
    current_stateinfo = os.stat('test.txt')
    while (True):
        new_stateinfo = os.stat('test.txt')
        if new_stateinfo != current_stateinfo:
           current_stateinfo=new_stateinfo
           print("File has been modified. Reloding credentials")
           return True
		
        else:
            return False