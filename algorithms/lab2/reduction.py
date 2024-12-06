
def read_from_file(filename):
    f = open(filename,"r")
    v = int(f.readline())
    e = int(f.readline())
    m = int(f.readline())
    line = f.readline()
    #print(type(line))
    edges = []
    while (line):
        line = line.strip().split(" ")
        edges.append((int(line[0]), int(line[1])))
        line = f.readline()


    return v,e,m,edges



def read_from_stdio():
    v = int(input())
    e = int(input())
    m = int(input())
    edges = []
    countv = 0
    seenv = set()
    seene = set()
    for i in range(e):
        line = input().strip().split(" ")
        v1 = int(line[0])
        v2 = int(line[1])
        if ((v1,v2) in seene) or ((v2,v1) in seene): continue
        edges.append((v1,v2))
        seenv.add(v1)
        seenv.add(v2)
        seene.add((v1,v2))
    
    return len(seenv),len(seene),m,edges


def reduce_to_casting(v,e,m,edges):
    #basecase = "3\n2\n3\n1 1\n1 2\n1 3\n2 1 3\n2 2 3"
    if (m >= v): 
        print("3")
        print("2")
        print("3")
        print("1 1\n1 2\n1 3")
        print("2 1 3\n2 2 3")
        return
    
    s = e + 2
    k = m + 3
    n = 3

    roles = {}  # each vertex corresponds to a role but they start after n =3 because the first 3 roles are reserved 
    scenes = [] # each scene in the casting problem is an edge in the coloring graph problem. And the roles for the scene are its verticies
    for edge in edges:
        if edge[0] == edge[1]: continue
        for i in range(2):
            if edge[i] not in roles:
                n+=1
                roles[edge[i]] = n
        
        scenes.append("2 {} {}".format(roles[edge[0]],roles[edge[1]]))

            
    
    # we make constrains of type 1 as that any actor after the 3rd one can play every role after the 3rd one

    constrains1 = str(m)
    for i in range(3,k):
        constrains1+= " " + str(i+1)

    # we make constrains of type 2 as that in each scene the corresponding actors-verticies play 
    constrains2 = ""
    for i  in  range(len(scenes)):
        constrains2 += "{}\n".format(scenes[i])
    constrains2 = constrains2[:-1]
    print(n)
    print(s)
    print(k)
    print("1 1\n1 2\n1 3") #first 2 roles are reserved.
    for i in range(3,n):  #all the rest roles can be played by all actors
        print(constrains1)
    print("2 1 3\n2 2 3") #first 2 scenes are reserved
    
    print(constrains2)
    

    


if __name__ == "__main__":
    v,e,m,edges = read_from_stdio()
    #v,e,m,edges = read_from_file('in.txt')
    reduce_to_casting(v,e,m,edges)