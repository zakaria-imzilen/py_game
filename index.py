import random

andrewTateMatrix = [
    [
        0, 0, 0,0, 0, 0, 0
    ],
    [
        0, 0, 0,0, 0, 0, 0
    ],
    [
        0, 0, 0,0, 0, 0, 0
    ],
    [
        0, 0, 0,0, 0, 0, 0
    ],
    [
        0, 0, 0,0, 0, 0, 0
    ],
    [
        0, 0, 0,0, 0, 0, 0
    ],
    [
        0, 0, 0,0, 0, 0, 0
    ],
]

# --- FUNCTIONS
def check_num_db_ex (arr, x, num, y):
    status = True

    if num < 1 or num > 49:
        status = False

    counter = 0
    for nX in range(7):
        for number in range(7):
            if arr[nX][number] == num:
                counter += 1
                if counter == 2:
                    status = False
                    print('EXISTS')
                    break

    return status

def check_num_ex(num):
    numToDeleteIndexes = []

    for x in range(7):
        for y in range(7):
            if andrewTateMatrix[x][y] == num:
                numToDeleteIndexes.append([x, y])
        
    return numToDeleteIndexes

def generate_random_num():
    return random.randrange(1, 50)

def is_game_over():
    sum = 0

    for x in range(7):
        for y in range(7):
            sum += andrewTateMatrix[x][y]

    return sum == 0

def deleteNbrsFromMtx(nbrs):
    for number in nbrs:
        andrewTateMatrix[number[0]][number[1]] = 0

# Fill the matrix in
for x in range(7):
    for y in range(7):
        result = False
        
        while(result == False):
            val = input('Enter a value for: ('+ str(x)+ ':'+ str(y)+ ')')
            result = check_num_db_ex(andrewTateMatrix, x, int(val), y)

        andrewTateMatrix[x][y] = int(val)

print(andrewTateMatrix)

# Save the players names
firstPlayer = input("Enter the first player name")
secondPlayer = input("Enter the second player name")

currentPlayer = firstPlayer
winner = None

while (is_game_over() == False):
    # Generate a Random Number
    random_number = generate_random_num()
    print(random_number)

    checking = check_num_ex(random_number)
    
    # IF NUM EXISTS --> REMOVE IT PAIRS FROM THE ARR
    if (len(checking) > 0):
        deleteNbrsFromMtx(checking)

    if currentPlayer == firstPlayer:
        currentPlayer = secondPlayer
    else:
        currentPlayer = firstPlayer

    print(andrewTateMatrix)

print("The Winner is: ", currentPlayer)