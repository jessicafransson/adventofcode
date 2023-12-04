with open("01data.txt") as file:
    data = []
    for line in file.readlines():
        line = line.replace('one', 'o1ne')
        line = line.replace('two', 't2wo')
        line = line.replace('three', 'thr3ee')
        line = line.replace('four', 'fou4r')
        line = line.replace('five', 'fi5ve')
        line = line.replace('six', 'si6x')
        line = line.replace('seven', 'sev7en')
        line = line.replace('eight', 'eigh8t')
        line = line.replace('nine', 'ni9ne')
        line = line.replace('zero', 'zer0o')
        item = []
        for character in line:
            if character >= '0' and character <= '9':
                item.append(int(character))
        data.append(item)
        
total = 0
for item in data:
    total += (10 * item[0])
    total += item[-1]
    
print("PART 2 SOLUTION:", total)