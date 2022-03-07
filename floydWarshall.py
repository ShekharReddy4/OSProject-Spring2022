import math
import random
import os
import psutil
import shutil
import json
import time

data=[{}]

def osinfo(p):
    # print("process cpu util in percentage is while in for loop : ",p.cpu_times()._asdict())
    # print("process cpu util excluding the IO/Blockstate while in for loop : ",round(sum(p.cpu_times()[:2]),2))
    data[0]['cpu times'] = round(sum(p.cpu_times()[:2]),2)
    #print("process memory in percentage is while in for loop : ", p.memory_info() )
    #print("process cpu_percent in percentage is : ", p.cpu_percent(interval=1.0) )
    #print("process IO counters : ", p.io_counters())
    #print("Number of cpu s : ", p.cpu_num() )
    #print("process number of context switches is : ", p.num_ctx_switches()._asdict()['voluntary'] )
    data[0]['voluntary ctx switch'] = p.num_ctx_switches()._asdict()['voluntary']
    #print("process memory_full info : ", p.memory_full_info() )
    #print("process RSS(aka Resident Set Size) memory in percentage is : ", round(p.memory_percent(memtype="rss"),2))
    data[0]['RSS'] = round(p.memory_percent(memtype="rss"),2)
    #print("process VMS(aka Virtual Memory Size) memory in percentage is : ", round(p.memory_percent(memtype="vms"),2))
    data[0]['VMS'] = round(p.memory_percent(memtype="vms"),2)
    data[0]['Pgfaults'] = round(p.memory_percent(memtype="pfaults"),2)
    
    #print("process USS(aka Unique Set Size) memory in percentage is : ", round(p.memory_percent(memtype="uss"),2))
    data[0]['memory%'] = round(p.memory_percent(memtype="uss"),2)

    #print("process memory maps : ", p.memory_maps() )
    #print("Number of open files : ", p.open_files() )
    #print("=====================================================================")
    #print("process memory in percentage is : ",  )
    total, used, free = shutil.disk_usage("/")
    data[0]["HDUsage"]= (0)

def insert(originalfile,string):
    with open(originalfile,'r') as f:
        with open('./data/newfdata.json','w') as f2: 
            f2.write(string)
            f2.write(f.read())

def FloydWarshall(G, n, p):
    start_time = time.time()
    print("================================== START OF FLOYDWARSHALL ALGORITHM ===================================")
    W = [[[math.inf for j in range(n)] for i in range(n)] for k in range(n+1)]

    for i in range(n):
        for j in range(n):
            W[0][i][j] = G[i][j]

    for k in range(1,n+1):
        for i in range(n):
            for j in range(n):
                W[k][i][j] = min(W[k-1][i][j], (W[k-1][i][k-1]+W[k-1][k-1][j]) )

    osinfo(p)
    timetaken = (time.time() - start_time)
    data[0]['timetaken'] = round(timetaken,6)
    with open('./data/fdata.json', 'w') as f:
        json.dump(data, f)
    print("================================== End OF FLOYDWARSHALL ALGORITHM ===================================")

    return W[n]

def main():
    pid = os.getpid()
    p = psutil.Process(pid)
    #print("Enter space separated values")
    #n, m = map(int, input("No. of Vertices, Edges: ").split())
    n, m = 10, 100

    G = [[math.inf for column in range(n)]  for row in range(n)]
    for i in range(n):
        G[i][i] = 0

    #print("For each edge (U -> V) \n\nU V W")
    for x in range(1, n+1):
        for y in range(1, n+1):
            #x = random.randint(-100,100)
            u, v, = x, y
            w = random.randint(-5,100)
            G[u-1][v-1] = w

    sp = FloydWarshall(G, n, p)
    #print("\nU -> V : W")
    # for i in range(n):
    #     for j in range(n):
    #         if(i!=j):
    #             print(f"{i+1} -> {j+1} : {sp[i][j]}")
    #print()
    insert("./data/fdata.json", "fdata=")

if __name__ == "__main__":
    main()