output_file = input("output file :")
file = open(output_file)

cdf = []
flits27 = 0
flits28 = 0
flits35 = 0
flits36 = 0
inductiveNoise = 0
currentTime = 0

high27 = False
low27 = True
was_high27 = False
was_low27 = True

high28 = False
low28 = True
was_high28 = False
was_low28 = True

high35 = False
low35 = True
was_high35 = False
was_low35 = True

high36 = False
low36 = True
was_high36 = False
was_low36 = True

for line in file:
    if line.startswith('Time: '):
        data = line.split(' ')
        if(currentTime != int(data[1])):
            if((was_high27 == True and low27 == True) or (was_low27 == True and high27 == True)):
                inductiveNoise = inductiveNoise + 1
            if((was_high28 == True and low28 == True) or (was_low28 == True and high28 == True)):
                inductiveNoise = inductiveNoise + 1
            if((was_high35 == True and low35 == True) or (was_low35 == True and high35 == True)):
                inductiveNoise = inductiveNoise + 1
            if((was_high36 == True and low36 == True) or (was_low36 == True and high36 == True)):
                inductiveNoise = inductiveNoise + 1
            
            cdf.insert(currentTime, inductiveNoise)
            currentTime = int(data[1])
            
            was_high27 = high27
            was_low27 = low27
            low27 = True
            high27 = False
            
            was_high28 = high28
            was_low28 = low28
            low28 = True
            high28 = False
            
            was_high35 = high35
            was_low35 = low35
            low35 = True
            high35 = False
            
            was_high36 = high36
            was_low36 = low36
            low36 = True
            high36 = False
            
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
            high27 = True
        if(flits28 == 3):
            high28 = True
        if(flits35 == 3):
            high35 = True
        if(flits36 == 3):
            high36 = True
        
        if(not(flits27 == 0)):
            low27 = False
        if(not(flits28 == 0)):
            low28 = False
        if(not(flits35 == 0)):
            low35 = False
        if(not(flits36 == 0)):
            low36 = False

for i in range(0,len(cdf)):
    print(i, end="")
    print(", ", end="")
    print(cdf[i])

