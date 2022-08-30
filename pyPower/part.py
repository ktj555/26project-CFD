class part:
    def __init__(self,config,material):
        self.config=config
        self.material=material

class heat_exchanger(part):
    def __init__(self,config,material):
        super().__init__(config,material)
    
    def Thermal_Resistence(self,inlet):
        return self.config.Thermal_Resistence(self.material,inlet)

class hot_side(heat_exchanger):
    def __init__(self,config,material):
        super().__init__(config,material)
    
class cold_side(heat_exchanger):
    def __init__(self,config,material):
        super().__init__(config,material)

class TEM(part):
    def __init__(self,config,material):
        super().__init__(config,material)