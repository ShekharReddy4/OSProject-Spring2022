import math
import random

def FloydWarshall(G, n):

    W = [[[math.inf for j in range(n)] for i in range(n)] for k in range(n+1)]

    for i in range(n):
        for j in range(n):
            W[0][i][j] = G[i][j]

    for k in range(1,n+1):
        for i in range(n):
            for j in range(n):
                W[k][i][j] = min(W[k-1][i][j], (W[k-1][i][k-1]+W[k-1][k-1][j]) )

    return W[n]


def main():

    #print("Enter space separated values")
    #n, m = map(int, input("No. of Vertices, Edges: ").split())
    n, m = map(int, "100 10000".split())

    G = [[math.inf for column in range(n)]  for row in range(n)]
    for i in range(n):
        G[i][i] = 0

    #print("For each edge (U -> V) \n\nU V W")
    for i in range(5):
        for j in range(5):
            ux=number = random.randint(i,5)
            uy=number = random.randint(j,5)
            uz=number = random.randint(1,100)
            u, v, w =  ux,uy,uz
            G[u-1][v-1] = w

    sp = FloydWarshall(G, n)
    print("\nU -> V : W")
    for i in range(n):
        for j in range(n):
            if(i!=j):
                print(f"{i+1} -> {j+1} : {sp[i][j]}")
    print()

if __name__ == "__main__":
    main()