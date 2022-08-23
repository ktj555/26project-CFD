class system:
    def __init__(self):
        self.hot_temperature=[]
        self.cold_temperature=[]
        self.flow=None
        self.circuit_list=None
        self.module=None

    def initialize(self):
        for i in self.map:
            for j in i:
                self.hot_temperature.append(self.hot_in_state['T'])
                self.cold_temperature.append(self.cold_in_state['T'])
    
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

    def compile(self):
        self.initialize()
        self.mass={}
        self.flow['hot'].set_in({self.flow_in['hot']:self.mass_in['hot']})
        self.flow['cold'].set_in({self.flow_in['cold']:self.mass_in['cold']})
        self.mass['hot']=self.flow['hot'].solve()
        self.mass['cold']=self.flow['cold'].solve()

    def solve(self,error=1e-3,first_step=1,step_decrease=0.5,print_b=False):
        index_list=self.flow['hot'].BFS_path_list()
        for pos in index_list:
            self