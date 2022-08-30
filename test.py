import pyPower

air=pyPower.material.Air
water=pyPower.material.Water
aluminum=pyPower.material.Aluminum

thermoelectricmaterial=pyPower.material.Solid(
    {'Density':7000,
    'Conductivity':1.5/0.003,
    'Specificheat':4182,
    'Seebeck':0.123,
    'Resistivity':2/0.003,
    'DensityType':'const',
    'ConductivityType':'const',
    'SpecificheatType':'const',
    'SeebeckType':'const',
    'ResistivityType':'const'}
)

hot_side_config=pyPower.config.plate({'Width':0.06,'Depth':0.06,'Height':0.003,'duct height':0.04})
cold_side_config=pyPower.config.plate({'Width':0.06,'Depth':0.06,'Height':0.003,'duct height':0.01})
generator=pyPower.config.cubic({'Width':0.06,'Depth':0.06,'Height':0.003})

hot_side=pyPower.part.hot_side(hot_side_config,aluminum)
cold_side=pyPower.part.cold_side(cold_side_config,aluminum)
tem=pyPower.part.TEM(generator,thermoelectricmaterial)

module=pyPower.module.module({'TEM':tem,'Hot_Side':hot_side,'Cold_Side':cold_side})

hot_flow_path=pyPower.path.mass_flow([0,1,2,3,4],[(0,1),(1,2),(2,3),(3,4)])
cold_flow_path=pyPower.path.mass_flow([0,1,2,3,4],[(4,3),(3,2),(2,1),(1,0)])

system=pyPower.system.system()
system.set_module(module)
system.set_flow_path(hot_flow_path,cold_flow_path)
system.set_circuit([[0,1],[1,2],[2,3],[3,4]])
system.set_fluid(air,water)
system.set_in({'hot':0,'cold':4})
system.set_mass({'hot':0.01,'cold':0.06})
system.set_in_state({'hot':{'T':550},'cold':{'T':300}})
system.set_chain([[0,0,4],[1,1,3],[2,2,2],[3,3,1],[4,4,0]])

system.compile()



# system.solve(first_step=1e-3,step_decrease=0.9,print_b=True)