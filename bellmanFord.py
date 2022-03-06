# Bellman Ford Algorithm in Python
import os
import psutil

class Graph:

    def __init__(self, vertices):
        self.V = vertices   # Total number of vertices in the graph
        self.graph = []     # Array of edges

    # Add edges
    def add_edge(self, s, d, w):
        self.graph.append([s, d, w])

    # Print the solution
    # def print_solution(self, dist):
    #     print("Vertex Distance from Source")
    #     for i in range(self.V):
    #         print("{0}\t\t{1}".format(i, dist[i]))

    def bellman_ford(self, src, p):
        print("================================== START OF THE FUNCTION ===================================")

        # Step 1: fill the distance array and predecessor array
        dist = [float("Inf")] * self.V
        # Mark the source vertex
        dist[src] = 0

        # Step 2: relax edges |V| - 1 times
        for _ in range(self.V - 1):
            for s, d, w in self.graph:
                if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w
            print("process cpu util in percentage is while in for loop : ",p.cpu_times())
            print("process cpu util excluding the IO/Blockstate while in for loop : ",sum(p.cpu_times()[:2]))
            print("process memory in percentage is while in for loop : ", p.memory_info() )
            print("process cpu_percent in percentage is : ", p.cpu_percent(interval=1.0) )
            #print("process IO counters : ", p.io_counters())
            #print("Number of cpu s : ", p.cpu_num() )
            print("process number of context switches is : ", p.num_ctx_switches() )
            print("process memory_full info : ", p.memory_full_info() )
            print("process RSS(aka Resident Set Size) memory in percentage is : ", p.memory_percent(memtype="rss"))
            print("process VMS(aka Virtual Memory Size) memory in percentage is : ", p.memory_percent(memtype="vms"))
            print("process USS(aka Unique Set Size) memory in percentage is : ", p.memory_percent(memtype="uss"))
            #print("process memory maps : ", p.memory_maps() )
            print("Number of open files : ", p.open_files() )
            print("=====================================================================")
            #print("process memory in percentage is : ",  )

            
        # Step 3: detect negative cycle
        # if value changes then we have a negative cycle in the graph
        # and we cannot find the shortest distances
        for s, d, w in self.graph:
            if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                print("Graph contains negative weight cycle")
                return
        
        print("================================== END OF THE FUNCTION ===================================")
        print("process cpu util in percentage is : ",p.cpu_times())
        print("process memory in percentage is : ", p.memory_info() )
        print("process memory in percentage is : ", p.cpu_percent(interval=1.0) )
        

        # No negative weight cycle found!
        # Print the distance and predecessor array
        # self.print_solution(dist)


g = Graph(5)
g.add_edge(0, 1, 5)
g.add_edge(0, 2, -4)
g.add_edge(1, 3, 3)
g.add_edge(2, 1, 6)
g.add_edge(3, 2, 2)

pid = os.getpid()
p = psutil.Process(pid)

print("================================== BEFORE START OF THE PROGRAM ===================================")
print("process cpu util in percentage is : ",p.cpu_times())
print("process memory in percentage is : ", p.memory_info() )
print("process memory in percentage is : ", p.cpu_percent(interval=1.0) )
import time
start_time = time.time()
g.bellman_ford(0,p)
print("================================== TOTAL RUNNING TIMEPROGRAM ===================================")
print("--- %s seconds ---" % (time.time() - start_time))
print("================================== END OF THE PROGRAM ===================================")


