output_file = input("output file :")
file = open(output_file)

cdf = []
flits27 = 0
flits28 = 0
flits35 = 0
flits36 = 0
resistiveNoise = 0
currentTime = 0

for line in file:
    if line.startswith('Time: '):
        data = line.split(' ')
        if(currentTime != int(data[1])):
            cdf.insert(currentTime, resistiveNoise)
            currentTime = int(data[1])
            flits27 = 0
            flits28 = 0
            flits35 = 0
            flits36 = 0
        
        if(data[8] == "27"):
            flits27 = flits27 + 1
        elif(data[8] == "28"):
            flits28 = flits28 + 1
        elif(data[8] == "35"):
            flits35 = flits35 + 1
        elif(data[8] == "36"):
            flits36 = flits36 + 1
        
        if(flits27 > 3 or flits28 > 3 or flits35 > 3 or flits36 > 3):
            print(flits27)
            print(flits28)
            print(flits35)
            print(flits36)
            print(line)

        if(flits27 == 3):
            resistiveNoise = resistiveNoise + 1
            flits27 = 0
        if(flits28 == 3):
            resistiveNoise = resistiveNoise + 1
            flits28 = 0
        if(flits35 == 3):
            resistiveNoise = resistiveNoise + 1
            flits35 = 0
        if(flits36 == 3):
            resistiveNoise = resistiveNoise + 1
            flits36 = 0

for i in range(0,len(cdf)):
    print(i, end="")
    print(", ", end="")
    print(cdf[i])

