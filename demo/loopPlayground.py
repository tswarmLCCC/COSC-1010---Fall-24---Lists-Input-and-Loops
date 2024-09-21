
#Sentinel Values
items = ['pen', 'notebook', 'pencil', 'lunch box']
index = 0
items_len = len(items)

while (index < items_len):

    print(items[index])
    #there's a problem here!  Let's use the debugger to figure out some things!
    if items[index] == 'pencil':
        print ("Found it!")
        break
    index += 1