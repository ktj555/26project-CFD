from copy import deepcopy
from pyPower.path import *

class system:
    def __init__(self):
        self.hot_temperature={}
        self.cold_temperature={}
        self.flow={}
        self.circuit_list=None
        self.module=None

    def initialize(self):
        for index,module in self.flow['hot'].node.items():
            self.hot_temperature[index]=deepcopy(self.hot_in_state['T'])
        for index,module in self.flow['cold'].node.items():    
            self.cold_temperature[index]=deepcopy(self.cold_in_state['T'])
        self.hot_temperature[-1]=deepcopy(self.hot_in_state['T'])
        self.cold_temperature[-1]=deepcopy(self.cold_in_state['T'])
    
    def set_flow_path(self,hot_path,cold_path):
        self.flow['hot']=hot_path
        self.flow['cold']=cold_path

    def set_module(self,module):
        self.module=module
    
    def set_circuit(self,path):
        self.circuit_list=path

    def set_fluid(self,hot,cold):
        self.hot_fluid=hot
        self.cold_fluid=cold

    def set_in(self,in_):
        self.flow_in=in_

    def set_mass(self,in_):
        self.mass_in=in_
    
    def set_in_state(self,in_):
        self.hot_in_state=in_['hot']
        self.cold_in_state=in_['cold']

    def set_chain(self,indexes):
        self.chain=indexes

    def compile(self):
        self.initialize()
        self.mass={}
        self.flow['hot'].set_in({self.flow_in['hot']:self.mass_in['hot']})
        self.flow['cold'].set_in({self.flow_in['cold']:self.mass_in['cold']})
        self.mass['hot']=self.flow['hot'].solve(self.flow_in['hot'])
        self.mass['cold']=self.flow['cold'].solve(self.flow_in['cold'])

    def solve(self,error=1e-3,first_step=1,step_decrease=0.5,print_b=False,load=False):

        step=first_step
        
        total_error=1e100
        last_error=1e00

        iter=0

        while(total_error>error):
            Node=[]
            path=[]
            num=[]
            for i in self.chain:
                module_num=i[0]
                hot_num=i[1]
                cold_num=i[2]
                try:
                    hot_next=self.flow['hot'].next(hot_num)[0]
                except:
                    hot_next=-1
                try:
                    cold_next=self.flow['cold'].next(cold_num)[0]
                except:
                    cold_next=-1
                hot_in={'state':{'T':self.hot_temperature[hot_num]},'fluid':self.hot_fluid,'velocity':self.mass['hot'][module_num]/self.module.hot_side.config.Area/self.hot_fluid.rho({'T':self.hot_temperature[hot_num]})}
                hot_out={'state':{'T':self.hot_temperature[hot_next]},'fluid':self.hot_fluid}
                cold_in={'state':{'T':self.cold_temperature[cold_num]},'fluid':self.cold_fluid,'velocity':self.mass['cold'][module_num]/self.module.cold_side.config.Area/self.cold_fluid.rho({'T':self.cold_temperature[cold_num]})}
                cold_out={'state':{'T':self.cold_temperature[cold_next]},'fluid':self.cold_fluid}
                self.module.set_inout(hot_in,hot_out,cold_in,cold_out)

                V_R=self.module.voltage_and_Resistence()
                Node.append(node(V_R['V'],V_R['R']))
                num.append(module_num)
            Node.append(node(0,0))
            num.append(-1)
            for s,e in self.circuit_list:
                path.append([Node[num.index(s)],Node[num.index(e)]])
            path.append([Node[num.index(e)],Node[num.index(-1)]])
            path.append([Node[num.index(-1)],self.circuit_list[0][0]])
            self.circuit=circuit(Node,path)
            if(not load):
                self.circuit.node[len(self.circuit.node)-1].r=self.circuit.calculate_load_resistence()
            else:
                self.circuit.node[len(self.circuit.node)-1].r=load
            I=self.circuit.solve()

            result=[]

            for i in self.chain:
                module_num=i[0]
                hot_num=i[1]
                cold_num=i[2]
                try:
                    hot_next=self.flow['hot'].next(hot_num)[0]
                except:
                    hot_next=-1
                try:
                    cold_next=self.flow['cold'].next(cold_num)[0]
                except:
                    cold_next=-1
                hot_in={'state':{'T':self.hot_temperature[hot_num]},'fluid':self.hot_fluid,'velocity':self.mass['hot'][module_num]/self.module.hot_side.config.Area/self.hot_fluid.rho({'T':self.hot_temperature[hot_num]})}
                hot_out={'state':{'T':self.hot_temperature[hot_next]},'fluid':self.hot_fluid}
                cold_in={'state':{'T':self.cold_temperature[cold_num]},'fluid':self.cold_fluid,'velocity':self.mass['cold'][module_num]/self.module.cold_side.config.Area/self.cold_fluid.rho({'T':self.cold_temperature[cold_num]})}
                cold_out={'state':{'T':self.cold_temperature[cold_next]},'fluid':self.cold_fluid}
                self.module.set_inout(hot_in,hot_out,cold_in,cold_out)

                result.append(self.module.valid(I[num.index(module_num)][0]))

            total_error=0

            for i in result:
                total_error+=i[0]+i[1]

            if(total_error>last_error):
                step*=step_decrease

            last_error=deepcopy(total_error)

            Total_error_h={}
            size_h=0

            for j in self.hot_temperature.keys():
                if(j == self.flow_in['hot']):
                    continue
                self.hot_temperature[j]+=0.01

                Node=[]
                path=[]
                num=[]
                for i in self.chain:
                    module_num=i[0]
                    hot_num=i[1]
                    cold_num=i[2]
                    try:
                        hot_next=self.flow['hot'].next(hot_num)[0]
                    except:
                        hot_next=-1
                    try:
                        cold_next=self.flow['cold'].next(cold_num)[0]
                    except:
                        cold_next=-1
                    hot_in={'state':{'T':self.hot_temperature[hot_num]},'fluid':self.hot_fluid,'velocity':self.mass['hot'][module_num]/self.module.hot_side.config.Area/self.hot_fluid.rho({'T':self.hot_temperature[hot_num]})}
                    hot_out={'state':{'T':self.hot_temperature[hot_next]},'fluid':self.hot_fluid}
                    cold_in={'state':{'T':self.cold_temperature[cold_num]},'fluid':self.cold_fluid,'velocity':self.mass['cold'][module_num]/self.module.cold_side.config.Area/self.cold_fluid.rho({'T':self.cold_temperature[cold_num]})}
                    cold_out={'state':{'T':self.cold_temperature[cold_next]},'fluid':self.cold_fluid}
                    self.module.set_inout(hot_in,hot_out,cold_in,cold_out)

                    V_R=self.module.voltage_and_Resistence()
                    Node.append(node(V_R['V'],V_R['R']))
                    num.append(module_num)
                Node.append(node(0,0))
                num.append(-1)
                for s,e in self.circuit_list:
                    path.append([Node[num.index(s)],Node[num.index(e)]])
                path.append([Node[num.index(e)],Node[num.index(-1)]])
                path.append([Node[num.index(-1)],self.circuit_list[0][0]])
                self.circuit=circuit(Node,path)
                if(not load):
                    self.circuit.node[len(self.circuit.node)-1].r=self.circuit.calculate_load_resistence()
                else:
                    self.circuit.node[len(self.circuit.node)-1].r=load
                I=self.circuit.solve()

                result=[]

                for i in self.chain:
                    module_num=i[0]
                    hot_num=i[1]
                    cold_num=i[2]
                    try:
                        hot_next=self.flow['hot'].next(hot_num)[0]
                    except:
                        hot_next=-1
                    try:
                        cold_next=self.flow['cold'].next(cold_num)[0]
                    except:
                        cold_next=-1
                    hot_in={'state':{'T':self.hot_temperature[hot_num]},'fluid':self.hot_fluid,'velocity':self.mass['hot'][module_num]/self.module.hot_side.config.Area/self.hot_fluid.rho({'T':self.hot_temperature[hot_num]})}
                    hot_out={'state':{'T':self.hot_temperature[hot_next]},'fluid':self.hot_fluid}
                    cold_in={'state':{'T':self.cold_temperature[cold_num]},'fluid':self.cold_fluid,'velocity':self.mass['cold'][module_num]/self.module.cold_side.config.Area/self.cold_fluid.rho({'T':self.cold_temperature[cold_num]})}
                    cold_out={'state':{'T':self.cold_temperature[cold_next]},'fluid':self.cold_fluid}
                    self.module.set_inout(hot_in,hot_out,cold_in,cold_out)

                    result.append(self.module.valid(I[num.index(module_num)][0]))

                te=0

                for i in result:
                    te+=i[0]+i[1]

                Total_error_h[j]=(te-total_error)/0.01
                size_h+=Total_error_h[j]**2

                self.hot_temperature[j]-=0.01

            Total_error_c={}
            size_c=0

            for j in self.cold_temperature.keys():
                if(j == self.flow_in['cold']):
                    continue
                self.cold_temperature[j]+=0.01

                Node=[]
                path=[]
                num=[]
                for i in self.chain:
                    module_num=i[0]
                    hot_num=i[1]
                    cold_num=i[2]
                    try:
                        hot_next=self.flow['hot'].next(hot_num)[0]
                    except:
                        hot_next=-1
                    try:
                        cold_next=self.flow['cold'].next(cold_num)[0]
                    except:
                        cold_next=-1
                    hot_in={'state':{'T':self.hot_temperature[hot_num]},'fluid':self.hot_fluid,'velocity':self.mass['hot'][module_num]/self.module.hot_side.config.Area/self.hot_fluid.rho({'T':self.hot_temperature[hot_num]})}
                    hot_out={'state':{'T':self.hot_temperature[hot_next]},'fluid':self.hot_fluid}
                    cold_in={'state':{'T':self.cold_temperature[cold_num]},'fluid':self.cold_fluid,'velocity':self.mass['cold'][module_num]/self.module.cold_side.config.Area/self.cold_fluid.rho({'T':self.cold_temperature[cold_num]})}
                    cold_out={'state':{'T':self.cold_temperature[cold_next]},'fluid':self.cold_fluid}
                    self.module.set_inout(hot_in,hot_out,cold_in,cold_out)

                    V_R=self.module.voltage_and_Resistence()
                    Node.append(node(V_R['V'],V_R['R']))
                    num.append(module_num)
                Node.append(node(0,0))
                num.append(-1)
                for s,e in self.circuit_list:
                    path.append([Node[num.index(s)],Node[num.index(e)]])
                path.append([Node[num.index(e)],Node[num.index(-1)]])
                path.append([Node[num.index(-1)],self.circuit_list[0][0]])
                self.circuit=circuit(Node,path)
                if(not load):
                    self.circuit.node[len(self.circuit.node)-1].r=self.circuit.calculate_load_resistence()
                else:
                    self.circuit.node[len(self.circuit.node)-1].r=load
                I=self.circuit.solve()

                result=[]

                for i in self.chain:
                    module_num=i[0]
                    hot_num=i[1]
                    cold_num=i[2]
                    try:
                        hot_next=self.flow['hot'].next(hot_num)[0]
                    except:
                        hot_next=-1
                    try:
                        cold_next=self.flow['cold'].next(cold_num)[0]
                    except:
                        cold_next=-1
                    hot_in={'state':{'T':self.hot_temperature[hot_num]},'fluid':self.hot_fluid,'velocity':self.mass['hot'][module_num]/self.module.hot_side.config.Area/self.hot_fluid.rho({'T':self.hot_temperature[hot_num]})}
                    hot_out={'state':{'T':self.hot_temperature[hot_next]},'fluid':self.hot_fluid}
                    cold_in={'state':{'T':self.cold_temperature[cold_num]},'fluid':self.cold_fluid,'velocity':self.mass['cold'][module_num]/self.module.cold_side.config.Area/self.cold_fluid.rho({'T':self.cold_temperature[cold_num]})}
                    cold_out={'state':{'T':self.cold_temperature[cold_next]},'fluid':self.cold_fluid}
                    self.module.set_inout(hot_in,hot_out,cold_in,cold_out)

                    result.append(self.module.valid(I[num.index(module_num)][0]))

                te=0

                for i in result:
                    te+=i[0]+i[1]

                Total_error_c[j]=(te-total_error)/0.01
                size_c+=Total_error_c[j]**2

                self.cold_temperature[j]-=0.01

            for i in self.hot_temperature.keys():
                if(i == self.flow_in['hot']):
                    continue
                self.hot_temperature[i]-=Total_error_h[i]/size_h**0.5*step

            for i in self.cold_temperature.keys():
                if(i == self.flow_in['cold']):
                    continue
                self.cold_temperature[i]-=Total_error_c[i]/size_c**0.5*step

            iter+=1

            if(print_b and iter%100 == 0):
                print('iteration : {}'.format(iter))
                print('hot temperature :',self.hot_temperature)
                print('cold temperature :',self.cold_temperature)
                print("Error : {}".format(total_error))