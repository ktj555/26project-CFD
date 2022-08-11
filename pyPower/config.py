from math import tanh

class config:
    def __init__(self):
        pass

class cubic(config):
    def __init__(self,info):
        self.w=info['Width']
        self.d=info['Depth']
        self.h=info['Height']

class plate(cubic):
    def __init__(self, info):
        super.__init__(info)

    def Thermal_Resistence(self,material,inlet):
        fluid=inlet['fluid']
        v=inlet['velocity']
        Pr=fluid.mu(inlet['state'])*fluid.Cp(inlet['state'])/fluid.k(inlet['state'])
        f_Pr=0.564/(1+(1.1664*Pr**(1/6))**4.5)**(2/9)
        L=2*self.w*self.h/(self.w+self.h)
        Re_L=v*L*fluid.rho(inlet['state'])/fluid.mu(inlet['state'])
        z_star=self.d/(L*Re_L*Pr)
        Nu_l=4/z_star*f_Pr
        h=Nu_l*fluid.k(inlet['state'])/L
        return 1/(h*self.w*self.h)

class heatsink(config):
    def __init__(self,info):
        pass

class Plate_fin_heatsink(heatsink):
    def __init__(self,info):
        self.base=info['base']
        self.fin=info['fin']
        self.Area=(self.base['Width']-self.fin['Width']*self.fin['N_fin'])*self.fin['Height']

    def Thermal_Resistence(self,material,inlet):
        fluid=inlet['fluid']
        v=inlet['velocity']
        b=(self.base['Width']-self.fin['N_fin']*self.fin['Width']-2*self.fin['Side'])/(self.fin['N_fin']-1)
        Re=v*b*fluid.rho(inlet['state'])/fluid.mu(inlet['state'])
        Re_star=Re*b/self.base['Depth']
        Pr=fluid.mu(inlet['state'])*fluid.Cp(inlet['state'])/fluid.k(inlet['state'])
        Nu_b=((Re_star*Pr/2)**(-3)+(0.664*Re_star**0.5*Pr**(1/3)*(1+3.65/Re_star**0.5)**0.5)**(-3))**(-1/3)
        h=Nu_b*fluid.k(inlet['state'])/b
        P_L=(self.fin['Width']+self.fin['Height'])*2
        A_c=self.fin['Width']*self.fin['Height']
        m=(h*P_L/material.k(inlet['state'])/A_c)**0.5
        R_fin=1/((h*P_L*material.k(inlet['state'])*A_c)**0.5*tanh(m*self.fin['Height']))
        return 1/(self.fin['N_fin']/R_fin+h*(self.fin['N_fin']-1)*b*self.base['Depth'])