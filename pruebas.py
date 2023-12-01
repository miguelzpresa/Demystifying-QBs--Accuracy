import simulator
from simulator import Particle,N_body_system,Integrator


"""
bajarle el delta t 
verificar que la constante de gravitacion no este en cm
cuando z se haga negativa cortala


"""
dt = 1e-3 #sec
v_x= 0#7.69
v_y= 7.7572
earth = Particle(5.9736e24, 6371.0e3 ,  [0.0,0.0,-6371.0e3], [0, 0, 0])
ball = Particle(.450, 0.025, [84.582,32.9184, 1.85], [v_x, v_y, 0])



parabolic_system =  N_body_system()

parabolic_system.add_particle(earth)
parabolic_system.add_particle(ball)

newton = Integrator(parabolic_system, dt)

parabolic_system.Header()
skip = 0

for j in range(100): #300*.7 = 210 sec > 300 sec
    parabolic_system,collition = newton.compute()
    #if (skip % 1 == 0):
    print(parabolic_system)
    print()
    print(collition)
    if collition:
        break
    parabolic_system.Print()