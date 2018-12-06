lines = []
amountOfLines = int(input())
for line in range(amountOfLines):
    line = input()
    lines.append(line.split())
for testCase in lines:
    if (int(testCase[2]) % 2 == 0 ):
        a = abs(int(testCase[0]))
        b = abs(int(testCase[1]))
    else :
        a = int(testCase[0])
        b = int(testCase[1])
    if (a > b) :
        print('1')
    elif (a < b):
        print ('2')
    else :
        print ('0')
