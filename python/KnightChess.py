"""
    A situation is given. Determine if white king is in checkmate or not.
    The white king is in checkmate if and only if it is in check and it is
    not able to move to any of its neighboring positions which is not in check.

    The first line will contain T number of test cases.
    Then the test cases follow.
    The first line of each test case contains a single integer N
    The next N line contains 2 space-separated integers Xi and Yi
    denoting the position of knights.
    The next line contains 2 space-separated integers A and B
    denoting the position of king

"""

"""
   returns a 3x3 array filled with false 
"""
def resetThreatendSquares() :
    square = []
    line = [False, False, False]
    square.append(line)
    square.append(line)
    square.append(line)
    return square



"""
    takes a list of strings and returns the list of int representation
"""
def listToInt(stringList) :
    answer = []
    for i in range(0, len(stringList)) :
        answer.append(int(stringList[i]))
    return answer



"""
    Returns true if the knight is threatening a relevent square false otherwise
    input: 2 2x1 arrays listing knights and kings paoition
"""
def isThreat(knightPosition, kingPosition) :
    xDisplacement = abs(knightPosition[0] - kingPosition[0])
    yDisplacement = abs(knightPosition[1] - kingPosition[1])
    if xDisplacement > 3 :
        return False
    if yDisplacement > 3 :
        return False
    if xDisplacement == 3 and yDisplacement == 3 :
        return False
    return True


"""
    returns true if the input square coresponds to checkmate
"""
def checkmate(square):
    for i in range(0,3) :
        for j in range(0,3) :
            if square[i][i] == False :
                return False
    return True
    

numberOfTests = int(input())
moves = [(1,2), (2,1), (-1,2), (2,-1), (1,-2), (-2,1), (-1,-2), (-2,-1)]
for i in range(0, numberOfTests):
    #threatendSquares = resetThreatendSquares()
    threatendSquares =[[False, False, False], [False, False, False], [False, False, False]]
    numberOfKnights = int(input())
    knights = []
    # load knights
    for j in range(0, numberOfKnights):
        knights.append(listToInt(str.split(input())))
    kingPosition = listToInt(str.split(input()))
    for j in range(0, numberOfKnights):
        if isThreat(knights[j], kingPosition):
            for k in range(0,8) :
                #calculate the squares in threatend square
                #the knight threatens with the given move
                xThreat = knights[j][0] - kingPosition[0]+ moves[k][0] + 1
                yThreat = knights[j][1] - kingPosition[1]+ moves[k][1] + 1
                if xThreat >=0 and xThreat <= 2 and yThreat >=0 and yThreat <= 2:
                    threatendSquares[xThreat][yThreat] = True
    #print (threatendSquares)
    if(checkmate(threatendSquares)) :
        print("YES")
    else :
        print("NO")
    

