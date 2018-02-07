from Algorithm.Propose_1 import Algorithm

def main():                                         #the original alogrithm

    propose1 = Algorithm()
    runtime, skyline = propose1.DHSQA("1")

    print("Final Output")
    for i in range(0, len(skyline), 1):
        for j in range(0, len(skyline[i]), 1):
            print("ID:", skyline[i][j].ID)
            # print("MaxSchedule(same)", skyline[i][j].maxSchedule)
            print("MinSchedule", skyline[i][j].minSchedule)
            print("AvgSchedule", skyline[i][j].avgSchedule)
            print("MaxArrive", skyline[i][j].maxArrive)
            # print("MinArrive(same)", skyline[i][j].minArrive)
            print("AvgArrive", skyline[i][j].avgArrive)
            # print("MaxDelay(same)", skyline[i][j].maxDelay)
            # print("MinDelay(same)", skyline[i][j].minDelay)
            print("AvgDelay", skyline[i][j].avgDelay)
            print("----------------------------------------")
    print("runtime", runtime)
    for length in skyline:
        print("length", len(length))
    print('\ncheck_End......')

if __name__ == '__main__':
    main()