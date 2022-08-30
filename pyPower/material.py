class Material:
    def __init__(self,info,need=['Density','Conductivity','Specificheat','DensityType','ConductivityType','SpecificheatType']):
        for key,value in info.items():
            setattr(self,key,value)

        for i in need:
            try:
                getattr(self,i)
            except:
                setattr(self,i,None)
                print(i,'is not defined')

    def set_prop(self,info):
        l=dir(self)
        for key,value in info.items():
            if(key in l):
                setattr(self,key,value)

    def check_prop(self):
        for i in dir(self):
            if (i not in dir(Material)):
                print(i,'is',getattr(self,i))

    def rho(self,state):
        if(self.DensityType=='const'):
            return self.Density
        else:
            if(self.DensityType=='Temperature_dependent'):
                return self.Density(T=state['T'])
            elif(self.DensityType=='Pressure_dependent'):
                return self.Density(P=state['P'])
            elif(self.DensityType=='Temperature_Pressure_dependent'):
                return self.Density(T=state['T'],P=state['P'])
        return False

    def k(self,state):
        if(self.ConductivityType=='const'):
            return self.Conductivity
        else:
            if(self.ConductivityType=='Temperature_dependent'):
                return self.Conductivity(T=state['T'])
            elif(self.ConductivityType=='Pressure_dependent'):
                return self.Conductivity(P=state['P'])
            elif(self.ConductivityType=='Temperature_Pressure_dependent'):
                return self.Conductivity(T=state['T'],P=state['P'])

    def Cp(self,state):
        if(self.SpecificheatType=='const'):
            return self.Specificheat
        else:
            if(self.SpecificheatType=='Temperature_dependent'):
                return self.Specificheat(T=state['T'])
            elif(self.SpecificheatType=='Pressure_dependent'):
                return self.Specificheat(P=state['P'])
            elif(self.Specificheat=='Temperature_Pressure_dependent'):
                return self.Specificheat(T=state['T'],P=state['P'])

class Fluid(Material):
    def __init__(self,info):
        '''
        info : dict
        info's key : ['Density', 'Conducitivity', 'Specificheat', 'Viscosity', each type]
        '''

        need=['Density','Conductivity','Specificheat','Viscosity','DensityType','ConductivityType','SpecificheatType','ViscosityType']

        super().__init__(info,need)

    def mu(self,state):
        if(self.ViscosityType=='const'):
            return self.Viscosity
        else:
            if(self.ViscosityType=='Temperature_dependent'):
                return self.Viscosity(T=state['T'])
            elif(self.ViscosityType=='Pressure_dependent'):
                return self.Viscosity(P=state['P'])
            elif(self.ViscosityType=='Temperature_Pressure_dependent'):
                return self.Viscosity(T=state['T'],P=state['P'])

class Solid(Material):
    def __init__(self,info):
        '''
        info : dict
        info's key : ['Density', 'Conducitivity', 'Specificheat', 'SeeBeck', 'Resistivity', each type]
        '''

        need=['Density','Conductivity','Specificheat','Seebeck','Resistivity','DensityType','ConductivityType','SpecificheatType','SeebeckType','ResistivityType']

        super().__init__(info,need)

    def s(self,state):
        if(self.SeebeckType=='const'):
            return self.Seebeck
        else:
            if(self.SeeBeckType=='Temperature_dependent'):
                return self.Seebeck(T=state['T'])
            elif(self.SeebeckType=='Pressure_dependent'):
                return self.Seebeck(P=state['P'])
            elif(self.SeebeckType=='Temperature_Pressure_dependent'):
                return self.Seebeck(T=state['T'],P=state['P'])

    def r(self,state):
        if(self.ResistivityType=='const'):
            return self.Resistivity
        else:
            if(self.ResistivityType=='Temperature_dependent'):
                return self.Resistivity(T=state['T'])
            elif(self.ResistivityType=='Pressure_dependent'):
                return self.Resistivity(P=state['P'])
            elif(self.ResistivityType=='Temperature_Pressure_dependent'):
                return self.Resistivity(T=state['T'],P=state['P'])

Air=Fluid({'Density':1.225,'Conductivity':0.025,'Specificheat':1030,'Viscosity':1.81e-5,'DensityType':'const','ConductivityType':'const','SpecificheatType':'const','ViscosityType':'const'})
Water=Fluid({'Density':998,'Conductivity':0.5918,'Specificheat':4182,'Viscosity':1e-3,'DensityType':'const','ConductivityType':'const','SpecificheatType':'const','ViscosityType':'const'})

Steel=Solid({'Density':7750,'Conductivity':14,'Specificheat':490,'Seebeck':0,'Resistivity':89e-9,'DensityType':'const','ConductivityType':'const','SpecificheatType':'const','SeebeckType':'const','ResistivityType':'const'})
Aluminum=Solid({'Density':2710,'Conductivity':237,'Specificheat':898.8,'Seebeck':0,'Resistivity':26.5e-9,'DensityType':'const','ConductivityType':'const','SpecificheatType':'const','SeebeckType':'const','ResistivityType':'const'})