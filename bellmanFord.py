# Bellman Ford Algorithm in Python
import os
import random
import psutil
import shutil
import json
import time

# r = {'is_claimed': 'True', 'rating': 3.5}
# r = json.dumps(r)
# loaded_r = json.loads(r)
# loaded_r['rating'] #Output 3.5
# type(r) #Output str
# type(loaded_r) #Output dict

class Graph:
    data=[{}]

    def __init__(self, vertices):
        self.V = vertices   # Total number of vertices in the graph
        self.graph = []     # Array of edges

    def insert(self,originalfile,string):
        with open(originalfile,'r') as f:
            with open('./data/newbdata.json','w') as f2: 
                f2.write(string)
                f2.write(f.read())
        
    def osinfo(self, p):
        
        # print("process cpu util in percentage is while in for loop : ",p.cpu_times()._asdict())
        # print("process cpu util excluding the IO/Blockstate while in for loop : ",round(sum(p.cpu_times()[:2]),2))
        self.data[0]['cpu times'] = round(sum(p.cpu_times()[:2]),2)
        #print("process memory in percentage is while in for loop : ", p.memory_info() )
        #print("process cpu_percent in percentage is : ", p.cpu_percent(interval=1.0) )
        #print("process IO counters : ", p.io_counters())
        #print("Number of cpu s : ", p.cpu_num() )
        #print("process number of context switches is : ", p.num_ctx_switches()._asdict()['voluntary'] )
        self.data[0]['voluntary ctx switch'] = p.num_ctx_switches()._asdict()['voluntary']
        #print("process memory_full info : ", p.memory_full_info() )
        #print("process RSS(aka Resident Set Size) memory in percentage is : ", round(p.memory_percent(memtype="rss"),2))
        self.data[0]['RSS'] = round(p.memory_percent(memtype="rss"),2)
        #print("process VMS(aka Virtual Memory Size) memory in percentage is : ", round(p.memory_percent(memtype="vms"),2))
        self.data[0]['VMS'] = round(p.memory_percent(memtype="vms"),2)
        self.data[0]['Pgfaults'] = round(p.memory_percent(memtype="pfaults"),2)
        
        #print("process USS(aka Unique Set Size) memory in percentage is : ", round(p.memory_percent(memtype="uss"),2))
        self.data[0]['memory%'] = round(p.memory_percent(memtype="uss"),2)

        #print("process memory maps : ", p.memory_maps() )
        #print("Number of open files : ", p.open_files() )
        #print("=====================================================================")
        #print("process memory in percentage is : ",  )
        total, used, free = shutil.disk_usage("/")
        self.data[0]["HDUsage"]= (0)
        
        

    # Add edges
    def add_edge(self, s, d, w):
        self.graph.append([s, d, w])

    
    def bellman_ford(self, src, p):
        start_time = time.time()
        print("================================== START OF BELLMANFORD ALGORITHM ===================================")

        # Step 1: fill the distance array and predecessor array
        dist = [float("Inf")] * self.V
        # Mark the source vertex
        dist[src] = 0

        # Step 2: relax edges |V| - 1 times
        for _ in range(self.V - 1):
            for s, d, w in self.graph:
                if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w
            
        # Step 3: detect negative cycle
        # if value changes then we have a negative cycle in the graph
        # and we cannot find the shortest distances
        for s, d, w in self.graph:
            if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                print("Graph contains negative weight cycle")
                return
        print("================================== END OF BELLMANFORD ALGORITHM ===================================")
        self.osinfo(p)
        # print("================================== END OF THE FUNCTION ===================================")
        # print("process cpu util in percentage is : ",p.cpu_times())
        # print("process memory in percentage is : ", p.memory_info() )
        # print("process memory in percentage is : ", p.cpu_percent(interval=1.0) )
        # print("process USS(aka Unique Set Size) memory in percentage is : ", p.memory_percent(memtype="uss"))
        timetaken = (time.time() - start_time)
        self.data[0]['timetaken'] = round(timetaken,6)
        with open('./data/bdata.json', 'w') as f:
            json.dump(self.data, f)


# g.add_edge(0, 1, 5)
# g.add_edge(0, 2, -4)
# g.add_edge(1, 3, 3)
# g.add_edge(2, 1, 6)
# g.add_edge(3, 2, 2)
n=10
g = Graph(n)
for x in range(1, n+1):
    for y in range(1, n+1):
        #x = random.randint(-100,100)
        u, v, = x, y
        w = random.randint(1,100)
        g.add_edge(u-1, v-1, w)

pid = os.getpid()
p = psutil.Process(pid)

# print("================================== BEFORE START OF THE PROGRAM ===================================")
# print("process cpu util in percentage is : ",p.cpu_times())
# print("process memory in percentage is : ", p.memory_info() )
# print("process memory in percentage is : ", p.cpu_percent(interval=1.0) )

# start_time = time.time()
g.bellman_ford(0,p)
# print("================================== TOTAL RUNNING TIMEPROGRAM ===================================")
# print("--- %s seconds ---" % (time.time() - start_time))
# print("================================== END OF THE PROGRAM ===================================")


# total, used, free = shutil.disk_usage("/")

# print("Total: %d GiB" % (total // (2**30)))
# print("Used: %d GiB" % (used // (2**30)))
# print("Free: %d GiB" % (free // (2**30)))

g.insert("./data/bdata.json", "data=")
