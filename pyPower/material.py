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

class Fluid(Material):
    def __init__(self,info):
        '''
        info : dict
        info's key : ['Density', 'Conducitivity', 'Specificheat', 'Viscosity', each type]
        '''

        need=['Density','Conductivity','Specificheat','Viscosity','DensityType','ConductivityType','SpecificheatType','ViscosityType']

        super().__init__(info,need)

class Solid(Material):
    def __init__(self,info):
        '''
        info : dict
        info's key : ['Density', 'Conducitivity', 'Specificheat', 'SeeBeck', 'Resistivity', each type]
        '''

        need=['Density','Conductivity','Specificheat','Seebeck','Resistivity','DensityType','ConductivityType','SpecificheatType','SeebeckType','ResistivityType']

        super().__init__(info,need)

Air=Fluid({'Density':1.225,'Conductivity':0.025,'Specificheat':1030,'Viscosity':1.81e-5,'DensityType':'const','ConductivityType':'const','SpecificheatType':'const','ViscosityType':'const'})
Water=Fluid({'Density':998,'Conductivity':0.5918,'Specificheat':4182,'Viscosity':1e-3,'DensityType':'const','ConductivityType':'const','SpecificheatType':'const','ViscosityType':'const'})

Steel=Solid({'Density':7750,'Conductivity':14,'Specificheat':490,'Seebeck':0,'Resistivity':89e-9,'ConductivityType':'const','SpecificheatType':'const','SeebeckType':'const','ResistivityType':'const'})
Aluminum=Solid({'Density':2710,'Conductivity':237,'Specificheat':898.8,'Seebeck':0,'Resistivity':26.5e-9,'DensityType':'const','ConductivityType':'const','SpecificheatType':'const','SeebeckType':'const','ResistivityType':'const'})