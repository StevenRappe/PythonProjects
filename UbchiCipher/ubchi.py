'''
    Steven Rappe
    Ubchi Cipher Encryption

    This program is a representation of the Ubchi cipher system that the
    German military used during much of World War One. It is a double transposition
    cipher, that first transposes the message based on the key, then transposes that
    message again using the same key.
'''

def encrypt(message, key):
    
    newMessage = message.upper()
    newKey = key.upper()

    print("Message: " + newMessage)
    print("Key: " + newKey)
    
    k = len(key)
    msgCntr = 0
    intKey = []

    # Make int representation of key
    for char in range(k):
        intKey.append(ord(newKey[char]))

    # check message length modulo k
    if (len(message)%k)== 0:
        l = len(message)//k
    else:
        l = (len(message)//k) + 1

    # create transposition grid
    transGrid = []
    for i in range(l):
        transGrid.append([])
        for j in range(k):
            transGrid[i].append(newMessage[msgCntr])
            msgCntr += 1
            
    print(" ")
        
    # create new grid
    orderedGrid = []
    for i in range(l):
        orderedGrid.append([])

    # rearrange columns in new grid
    curMin = 0
    minIndex = 0
    indexTracker = []
    
    for s in range(k):
        pastMin = 10000
        for i in range(k):
            if (intKey[i] < pastMin) and (intKey[i] >= curMin):
                if i not in indexTracker:
                    pastMin = intKey[i]
                    minIndex = i
                
        curMin = pastMin
        indexTracker.append(minIndex)
                
        for j in range(l):
            orderedGrid[j].append(transGrid[j][minIndex])
            
    result = []
    for i in range(l):
        print(orderedGrid[i])

    for i in range(k):
        for j in range(l):
    
            result.append(orderedGrid[j][i])
        
    return result


# Run program

selectProgramOption = raw_input("Choose option a or b: a = use test input, b = enter own input: ")
while (selectProgramOption != "a") and (selectProgramOption != "b"):
    selectProgramOption = raw_input("Invalid input. Choose option a or b: a = use test input, b = enter own input: ")        

# Use given test key
if selectProgramOption == "a":
    testMessage = "EnemyShipMEnTDepArTstomoRroWMoRnIng"
    testKey = "alpha"

    solution = encrypt(testMessage, testKey)
    midStrSol = ''.join(solution)
    print("Mid-Point Solution")
    print(midStrSol)
    print(" ")

    finalSolution = encrypt(midStrSol, testKey)
    finStrSol = ''.join(finalSolution)
    print("Final Solution")
    print(finStrSol)

# Use user-chosen test key
elif selectProgramOption == "b":
    inputMessage = raw_input("Choose message so that key divides message with no remainder: ")
    inputKey = raw_input("Choose key so that key divides message with no remainder: ")

    while ((len(inputMessage))%(len(inputKey))) != 0:
        print("Invalid message-key combination.")
        inputMessage = raw_input("Choose message so that key divides message with no remainder: ")
        inputKey = raw_input("Choose key so that key divides message with no remainder: ") 

    solution = encrypt(inputMessage, inputKey)
    midStrSol = ''.join(solution)
    print("Mid-Point Solution")
    print(midStrSol)
    print(" ")

    finalSolution = encrypt(midStrSol, inputKey)
    finStrSol = ''.join(finalSolution)
    print("Final Solution")
    print(finStrSol)

