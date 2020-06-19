def tictactoe():
    game = [[0,0,0],
            [0,0,0],
            [0,0,0]]
    
    mycount = 1
    myMap = {}
    for i in range(3):
        for j in range(3):
            myMap[mycount] = (i,j)
            mycount += 1
    print(myMap)
    myGame = True
    visited = {i : 0 for i in range(1,10)}
    user1 = True
    count = 1     
    while myGame:
        for row in game:
            print(row)
        if len(visited.keys()) >= 5:
            if visited[1] == visited[2] == visited[3]  or visited[4] == visited[5] == visited[5] or visited[7] == visited[8] == visited[9]:
                if visited[1] == 'X' or visited[4] == 'X' or visited[7] == 'X':
                    print("Player1 WOn")
                    break
                elif visited[1] == 'Y' or visited[4] == 'Y' or visited[7] == 'Y':
                    print("Player 2 won")
                    break
            elif visited[1] == visited[5] == visited[9] or visited[3] == visited[5] == visited[7]:
                if visited[1] == 'X' or visited[3] == 'X':
                    print("Player1 WOn")
                    break
                elif visited[1] == 'Y' or visited[3] == 'Y':
                    print("Player 2 won")
                    break
            elif visited[1] == visited[4] == visited[7] or visited[2] == visited[5] == visited[8] or visited[3] == visited[6] == visited[9]:
                if visited[1] == 'X' or visited[2] == 'X' or visited[3] == 'X':
                    print("Player1 WOn")
                    break
                elif visited[1] == 'Y' or visited[2] == 'Y' or visited[3] == 'Y':
                    print("Player 2 won")
                    break


        if count == 9:
            print("Its Draw")
            myGame = False
            break
        inputNumber = 0
        if user1:
            inputNumber = int(input("User 1 enter your position 1 to 9 : "))
        else:
            inputNumber = int(input("User 2 enter your position 1 to 9 : "))
        if 1 <= inputNumber <=9 and inputNumber and visited[inputNumber] == 0: 
            if user1:
                game[myMap[inputNumber][0]][myMap[inputNumber][1]] = 'X'
                visited[inputNumber] = 'X'
                user1 = False
            else:
                game[myMap[inputNumber][0]][myMap[inputNumber][1]] = 'Y'
                visited[inputNumber] = 'Y'
                user1 = True
        else:
            print("Wrong Input")
        count += 1

tictactoe()