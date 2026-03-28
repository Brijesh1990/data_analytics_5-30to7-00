file=open("module.txt","r")
if file:
    print('file opened successfully')
else:
    print('file not found')

file.close()
    