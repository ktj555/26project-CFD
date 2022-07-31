def find_key(dict,value):
    for k,v in dict.items():
        if(v==value):
            return k
    return False

class node:
    def __init__(self,voltage,resistence):
        self.v=voltage
        self.r=resistence
        self.In={'V':None,'I':None}
        self.Out={'V':None,'I':None}

    def set_In_I(self,I):
        self.In['I']=I
    def set_In_V(self,V):
        self.In['V']=V
    def set_Out_I(self,I):
        self.Out['I']=I
    def set_Out_V(self,V):
        self.Out['V']=V
    
    def __str__(self):
        return 'Voltage : {}\nResistence : {}'.format(self.v,self.r)

class circuit:
    def __init__(self,nodes,edges):
        self.node={}
        self.edge=[]
        i=0
        for n in nodes:
            self.node[i]=n
            self.edge.append([])
            i+=1
        for s, e in edges:
            s_index=find_key(self.node,s)
            e_index=find_key(self.node,e)
            start=min(s_index,e_index)
            end=max(s_index,e_index)
            self.edge[start].append(end)

    def set_in_out(self):
        for index in self.BFS_path_list():
            if(index==0):
                self.node[index].set_In_I()
                self.node[index].set_In_V(0)

    def BFS_path_list(self):
        result=[]
        path=[]
        pos=0
        is_go=[0 for _ in range(len(self.node))]
        while(1):
            is_go[pos]=1
            if(pos not in result):
                result.append(pos)
            for i in self.edge[pos]:
                if(is_go[i]==0):
                    path.append(i)
            if(len(path)==0):
                break
            pos=path[0]
            del path[0]
        return result

    def __str__(self):
        string='Nodes : '+str(list(self.node.keys()))+'\n'
        string+='Edges\n  start  |   end\n'
        for i in range(len(self.edge)):
            string+='  {:5}  |  '.format(i)
            for j in self.edge[i]:
                string+='{} '.format(j)
            string+='\n'
        return string

a=node(1,1)
b=node(2,2)
c=node(3,3)
d=node(4,4)
e=node(5,5)
f=node(6,6)
g=node(7,7)
h=node(8,8)
I=node(9,9)

C=circuit([a,b,c,d,e,f,g,h,I],[(a,b),(a,c),(a,f),(b,d),(b,h),(c,d),(c,g),(d,e),(f,e),(e,I),(g,I),(h,I)])
print(C.BFS_path_list())