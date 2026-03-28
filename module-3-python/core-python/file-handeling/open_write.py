file=open("module.txt","w")
if file:
    print('file opened successfully')
else:
    print('file not found')

file.close()
    