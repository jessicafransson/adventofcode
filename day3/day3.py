with open("03data.txt") as file:
    # to get the numbers along with the rows and columns numbers they occupy
    # as well as get the symbols along with rows and columns
    numbers = []
    symbols = []
    for rowNumber, line in enumerate(file.readlines()):
        number = 0
        columns = []
        for columnNumber, c in enumerate(line.strip() + '.'):
            if c >= '0' and c <= '9':
                number = (10 * number) + int(c)
                columns.append(columnNumber)
            else:
                if number > 0:
                    numbers.append((rowNumber, columns, number))
                if c != '.':
                    symbols.append((rowNumber, columnNumber, c))
                number = 0
                columns = []
                
# process each of the numbers to check for symbols nearby
    total = 0
    offsets = [[-1, -1], [-1, 0], [-1, 1],[0, -1],[0, 0],[0, 1],[1, -1],[1, 0], [1, 1]]
    for number in numbers:
        found = False
        for symbol in symbols:
            for offset in offsets:
                location = [symbol[0] + offset[0], symbol[1] + offset[1]]
                if number[0] == location[0] and location[1] in number[1]:
                    found = True
                    total += number[2]
                    break

    print("Day 3 - solution pt1:", total)
            