from copy import deepcopy
import numpy as np

def find_key(dict,value):
    for k,v in dict.items():
        if(v==value):
            return k
    return False

class node:
    def __init__(self,voltage,resistence):
        self.v=voltage
        self.r=resistence
        self.In=[]
        self.Out=[]

    def __str__(self):
        return 'Voltage : {}\nResistence : {}'.format(self.v,self.r)

class circuit:
    def __init__(self,nodes,edges):
        self.node={}
        self.edge=[]
        self.reverse=[]
        i=0
        self.setup=False
        self.d=None
        for n in nodes:
            self.node[i]=n
            self.edge.append([])
            self.reverse.append([])
            i+=1
        for s, e in edges:
            start=find_key(self.node,s)
            end=find_key(self.node,e)
            self.edge[start].append(end)
            self.reverse[end].append(start)

    def set_in_out(self):
        path=self.BFS_path_list()
        diff=[]
        for index in path:
            if(index==0):
                self.node[index].In=[]
                self.node[index].Out=[0]
            else:
                if(len(self.reverse[index])>1):
                    diff.append(index)
                for i in self.reverse[index]:
                    self.node[index].In.append(self.node[i].Out)
                self.node[index].Out+=self.node[index].In[0]+[index]
        self.setup=True
        self.d=diff
        return diff

    def make_eqn(self):
        if(self.setup):
            diff=self.d
        else:
            diff=self.set_in_out()
        A=[]
        B=[]
        node_list=[i for i in range(len(self.node))]

        for i in range(len(self.edge)):
            if(len(self.edge[i])>1):
                pre=[0 for _ in range(len(self.node))]
                for index in self.edge[i]:
                    pre[index]=1
                pre[i]=-1
                A.append(pre)
                B.append([0])
                if(i in node_list):
                    node_list.remove(i)
        for i in range(len(self.reverse)):
            if(len(self.reverse[i])>1):
                pre=[0 for _ in range(len(self.node))]
                for index in self.reverse[i]:
                    pre[index]=1
                    if(index in node_list):
                        node_list.remove(index)
                pre[i]=-1
                A.append(pre)
                B.append([0])
        for i in node_list:
            pre=[0 for _ in range(len(self.node))]
            pre[self.edge[i][0]]=1
            pre[i]=-1
            A.append(pre)
            B.append([0])
        for i in diff:
            in_list=self.node[i].In
            for i in range(len(in_list)-1):
                first=in_list[i]
                second=in_list[i+1]
                pre=[0 for _ in range(len(self.node))]
                pre_b=[0]
                for j in first:
                    if(j not in second):
                        pre[j]=self.node[j].r
                        pre_b[0]+=self.node[j].v
                for j in second:
                    if(j not in first):
                        pre[j]=-self.node[j].r
                        pre_b[0]-=self.node[j].v
                A.append(pre)
                B.append(pre_b)
        pre=[0 for _ in range(len(self.node))]
        pre_b=[0]
        for i in self.node[len(self.node)-1].Out:
            pre[i]=self.node[i].r
            pre_b[0]+=self.node[i].v
        A.append(pre)
        B.append(pre_b)
        
        return [np.array(A),np.array(B)]

    def solve(self):
        A,B=self.make_eqn()
        return np.dot(np.linalg.pinv(A),B)

    def calculate_load_resistence(self):
        new_circuit=deepcopy(self)
        for i,j in new_circuit.node.items():
            j.v=0
        new_circuit.node[0].v=1
        new_circuit.node[len(new_circuit.node)-1].r=0
        
        A,B=new_circuit.make_eqn()
        I=np.dot(np.linalg.pinv(A),B)
        return 1/I[0][0]

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

class mass_flow:
    def __init__(self,nodes,edges):
        self.node={}
        self.edge=[]
        self.reverse=[]
        i=0
        self.setup=False
        self.d=None
        for n in nodes:
            self.node[i]=n
            self.edge.append([])
            self.reverse.append([])
            i+=1
        for s,e in edges:
            start=find_key(self.node,s)
            end=find_key(self.node,e)
            self.edge[start].append(end)
            self.reverse[end].append(start)

    def next(self,index):
        return self.edge[index]

    def previous(self,index):
        return self.reverse[index]

    def set_in(self,in_):
        self.mass={}
        self.mass['in']=in_
    
    def DFS_path_list(self,start):
        result=[]
        path=[]
        pos=start
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
            pos=path[-1]
            del path[-1]

        return result

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

    def solve(self,start):
        path=self.DFS_path_list(start)
        mass={}
        for index,m in self.mass['in'].items():
            mass[index]=m
        for pos in path[1:]:
            if(find_key(mass,pos)):
                continue
            else:
                mass[pos]=0
                for i in self.reverse[pos]:
                    mass[pos]+=mass[i]
        return mass