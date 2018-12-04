def ReadFileWords (inputFileName) :
    inputFile = open(inputFileName, "r")
    lines = []
    for line in inputFile:
        lines.append(line.split())
    return lines


lines = ReadFileWords("input.txt")
for a in range(0, len(lines)):
    print("line")
    for b in range(0, len(lines[a])):
        print("word", lines[a][b])



