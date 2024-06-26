inpfile=open("input4.txt","r")
outfile=open("output4.txt","w")

N=inpfile.readline()
N=N.split(" ")

node=int(N[0])
edge=int(N[1])

lstt=[0]*(node+1)

start,end=inpfile.readline().split(" ")
start=int(start)
lstt[start]=[int(end)]

for i in range(edge-1):
    line=inpfile.readline()
    line=line.split(" ")
    num1=int(line[0])
    num2=int(line[1])

    if lstt[num1]==0:
        lstt[num1]=[num2]
    else:
        if num2 not in lstt[num1]:
            lstt[num1].append(num2)

visited=[]
def DFS(start, visited, lstt):
    if start in visited:
        return "YES"
    visited.append(start)
    if lstt[start] != 0:
        for i in lstt[start]:
            d = DFS(i, visited, lstt)
            if d == "YES":
                return "YES"

    for i in range(len(visited)):
        if visited[i]==start:
            visited.pop(i)
    return "NO"

fin=DFS(start,visited,lstt)

outfile.write(f"{fin}")

inpfile.close()
outfile.close()