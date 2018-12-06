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
        return false
    if yDisplacement > 3 :
        return false
    if xDisplacement == 3 and yDisplacement == 3 :
        return false
    return true
    

numberOfTests = int(input())
for i in range(0, numberOfTests):
    threatendSquares = resetThreatendSquares()
    numberOfKnights = int(input())
    knights = []
    # load knights
    for j in range(0, numberOfKnights):
        knights.append(listToInt(str.split(input())))
    kingPosition = listToInt(str.split(input()))
    


