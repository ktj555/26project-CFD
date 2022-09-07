class module:
    def __init__(self,info):
        self.TEM=info['TEM']
        self.hot_side=info['Hot_Side']
        self.cold_side=info['Cold_Side']
    
    # 조건 부여
    def set_inout(self,hot_in,hot_out,cold_in,cold_out):
        self.hot_in=hot_in
        self.hot_out=hot_out
        self.cold_in=cold_in
        self.cold_out=cold_out
    
    # 조건 검증
    def valid(self,I):
        self.R_h=self.hot_side.Thermal_Resistence(self.hot_in)
        self.R_c=self.cold_side.Thermal_Resistence(self.cold_in)

        hot_flow=self.hot_in['fluid']
        cold_flow=self.cold_in['fluid']

        try:
            hot_state={'T':(self.hot_in['state']['T']+self.hot_out['state']['T'])*0.5,'P':(self.hot_in['state']['P']+self.hot_out['state']['P'])*0.5}
        except:
            hot_state={'T':(self.hot_in['state']['T']+self.hot_out['state']['T'])*0.5}
        try:
            cold_state={'T':(self.cold_in['state']['T']+self.cold_out['state']['T'])*0.5,'P':(self.cold_in['state']['P']+self.cold_out['state']['P'])*0.5}
        except:
            cold_state={'T':(self.cold_in['state']['T']+self.cold_out['state']['T'])*0.5}
        C_h=self.hot_in['velocity']*hot_flow.rho(hot_state)*self.hot_side.config.Area*hot_flow.Cp(hot_state)
        C_c=self.cold_in['velocity']*cold_flow.rho(cold_state)*self.cold_side.config.Area*cold_flow.Cp(cold_state)

        T_TEM_h=hot_state['T']-self.R_h*C_h*(self.hot_in['state']['T']-self.hot_out['state']['T'])
        T_TEM_c=cold_state['T']-self.R_c*C_c*(self.cold_in['state']['T']-self.cold_out['state']['T'])
        del_T=T_TEM_h-T_TEM_c

        if(self.TEM.material.SeebeckType=='average'):
            T_a=0.5*(T_TEM_h+T_TEM_c)
        elif(self.TEM.material.SeebeckType=='diff'):
            T_a=del_T
        else:
            T_a=0
        if(self.TEM.material.ResistivityType=='average'):
            T_R=0.5*(T_TEM_h+T_TEM_c)
        elif(self.TEM.material.ResistivityType=='diff'):
            T_R=del_T
        else:
            T_R=0
        if(self.TEM.material.ConductivityType=='average'):
            T_k=0.5*(T_TEM_h+T_TEM_c)
        elif(self.TEM.material.ConductivityType=='diff'):
            T_k=del_T
        else:
            T_k=0

        a=self.TEM.material.s(T_a)
        R=self.TEM.material.r(T_R)
        k=self.TEM.material.k(T_k)
        A=self.TEM.config.Area
        L=self.TEM.config.h

        q_h_H=C_h*(self.hot_in['state']['T']-self.hot_out['state']['T'])
        q_c_H=C_c*(self.cold_out['state']['T']-self.cold_in['state']['T'])
        q_h_E=a*I*T_TEM_h+k*A/L*del_T-0.5*I**2*R
        q_c_E=a*I*T_TEM_c+k*A/L*del_T+0.5*I**2*R

        error_h=(q_h_H-q_h_E)**2
        error_c=(q_c_H-q_c_E)**2

        return [error_h,error_c]

    # 조건에 대한 전압 및 저항 산출
    def voltage_and_Resistence(self):
        hot_flow=self.hot_in['fluid']
        cold_flow=self.cold_in['fluid']

        self.R_h=self.hot_side.Thermal_Resistence(self.hot_in)
        self.R_c=self.cold_side.Thermal_Resistence(self.cold_in)

        try:
            hot_state={'T':(self.hot_in['state']['T']+self.hot_out['state']['T'])*0.5,'P':(self.hot_in['state']['P']+self.hot_out['state']['P'])*0.5}
        except:
            hot_state={'T':(self.hot_in['state']['T']+self.hot_out['state']['T'])*0.5}
        try:
            cold_state={'T':(self.cold_in['state']['T']+self.cold_out['state']['T'])*0.5,'P':(self.cold_in['state']['P']+self.cold_out['state']['P'])*0.5}
        except:
            cold_state={'T':(self.cold_in['state']['T']+self.cold_out['state']['T'])*0.5}
        C_h=self.hot_in['velocity']*hot_flow.rho(hot_state)*self.hot_side.config.Area*hot_flow.Cp(hot_state)
        C_c=self.cold_in['velocity']*cold_flow.rho(cold_state)*self.cold_side.config.Area*cold_flow.Cp(cold_state)

        T_TEM_h=hot_state['T']-self.R_h*C_h*(self.hot_in['state']['T']-self.hot_out['state']['T'])
        T_TEM_c=cold_state['T']-self.R_c*C_c*(self.cold_in['state']['T']-self.cold_out['state']['T'])
        del_T=T_TEM_h-T_TEM_c

        if(self.TEM.material.SeebeckType=='average'):
            T_a=0.5*(T_TEM_h+T_TEM_c)
        elif(self.TEM.material.SeebeckType=='diff'):
            T_a=del_T
        else:
            T_a=0
        if(self.TEM.material.ResistivityType=='average'):
            T_R=0.5*(T_TEM_h+T_TEM_c)
        elif(self.TEM.material.ResistivityType=='diff'):
            T_R=del_T
        else:
            T_R=0
        
        a=self.TEM.material.s(T_a)
        R=self.TEM.material.r(T_R)
        V=a*del_T

        return {'V':V,'R':R}