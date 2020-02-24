#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# THou, 2020-Feb-18, replaced lstRow with lstDicRow
# THou, 2020-Feb-20, added delete, load functions; modified save function
# THou, 2020-Feb-23, added autogenerating for CD ID
#------------------------------------------#

# Declare variables
strChoice = ''  # User input from menu
lstTbl = []  # list of dictionaries to hold data
dicRow = {'id': '', 'title': '', 'artist':''} # dictionary to hold CD entry
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object
strInputID = ''  # collect the CD ID from user input
intCDID = ''  # CD ID variable
strRow = '' # string variable for CD row

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('\n')
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print('\n\n')


    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        print('Goodbye')
        break


    if strChoice == 'l':
        # load data from file; appends to existing data
        #generate unique ID based on table length
        intCDID = len(lstTbl) + 1 #proposed CD ID based on table length
        while any(intCDID == row['id'] for row in lstTbl) is True: #check if ID already exists
            intCDID = intCDID + 1 #increment until ID is unique
            
        #load line from file
        objFile = open(strFileName, 'r')
        for row in objFile:
            strRow = row.strip().split(sep=',')
            dicRow = {'id': intCDID, 'title': strRow[1], 'artist': strRow[2]}
            lstTbl.append(dicRow)
            dicRow = {'id': '', 'title': '', 'artist':''}
            intCDID = intCDID + 1
        objFile.close()
        print('Load complete')


    elif strChoice == 'a':
        # 2. Add data to the table (2d-list of dictionaries) each time the user wants to add data
        #generate unique ID based on table length
        intCDID = len(lstTbl) + 1
        while any(intCDID == row['id'] for row in lstTbl) is True:
            intCDID = intCDID + 1
        dicRow['id'] = intCDID
        print('ID: ', intCDID)
        
        #get title and artist inputs
        dicRow['title'] = input('Enter the CD\'s Title: ')
        dicRow['artist'] = input('Enter the Artist\'s Name: ')
        
        #append to 2D list
        lstTbl.append(dicRow)
        dicRow = {'id': '', 'title': '', 'artist':''}
        print('Entry saved')


    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist')
        for row in lstTbl:
            print(*row.values(), sep = ', ')


    elif strChoice == 'd':
        #get id input from user, find matching entry, delete
        strInputID = input('Enter the CD ID of the entry you want to delete: ')
        try:
            intCDID = int(strInputID)
            if any(intCDID == row['id'] for row in lstTbl) is True: #check each row's ID value to see if intID exists
                for row in lstTbl: #find and remove entry with matching ID
                    if intCDID == row['id']:
                        print('Removing entry:')
                        print(*row.values(), sep = ', ')
                        lstTbl.remove(row)
            else:
                print('No such ID')
        except ValueError:
            print('Invalid input')


    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'w') #overwrite file with memory table
        for row in lstTbl:
            strRow = ''
            for dicValue in row.values():
                strRow += str(dicValue) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(str(strRow))
        objFile.close()
        print('Save complete')


    else:
        print('Please choose either l, a, i, d, s or x!')