import glob, sys, time



for argument in sys.argv[1:]:
    N = 0
    result = 0

    f = open(argument)

    points = []

    for line in f:
        line = str(line)

        found = line.find("DIMENSION") != -1

        if(found):
            split = line.split(":")
            N = int(split[1].strip())

        found = line.find("NODE_COORD_SECTION") != -1

        if(found):
            for i in range(N):
                values = tuple([float(x) for x in f.readline().split()][1:])
                points.append(values)
                # print(values)
            break
    
    print(f"../{argument}: {N} {result}")