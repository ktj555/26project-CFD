class module:
    def __init__(self,info):
        self.TEM=info['TEM']
        self.hot_side=info['Hot_Side']
        self.cold_side=info['Cold_Side']
    
    def set_inlet(self,hot_side,cold_side):
        self.hot_in=hot_side
        self.cold_in-cold_side
    
    def make_eqn(self):
        R_h=self.hot_side.Thermal_Resistence(self.hot_in)