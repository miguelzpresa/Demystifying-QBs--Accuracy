#!/usr/bin/env python3

import matplotlib.pyplot as plt


def myplot(plot, filename, dt, n_particle):
    #dt = 0.1 #sec
    with open(filename) as f:
        lines = f.readlines()

    #N = int(lines[0]) # number of particles
    N=1
    i = 0
    j = 0
    x = []
    y = []
    z = []
    v_x = []
    v_y = []
    v_z = []

    t= []
    n = 0

    for data in lines[2:]:
        coordinates = data.split()
        i = i+1
        if (i == n_particle):
            #print(data)
            x.append(float(coordinates[3])-6371e3)
            y.append(float(coordinates[4]))
            z.append(float(coordinates[5]))
            v_x.append(float(coordinates[6]))
            v_y.append(float(coordinates[7]))
            v_z.append(float(coordinates[8]))
        if (i==N):
            i = 0
            t.append(n*dt)
            n = n +1

    plt.plot(y, x,label=str(dt)+"sec")
    
    #derivative (acceleration)

    #Y1 = []
    #
    #for i in range(len(v_x)-1):
    #    y1 = (v_x[i+1] - v_x[i]) / dt
    #    print(y1)
    #    Y1.append(y1)
    #    
    #plt.plot(t[:-1], Y1,label=str(dt)+"sec")


    
fig = plt.figure()
ax = fig.add_subplot()
n_particle = 2 # the particle that I want to observe

myplot(ax , "res.dat", 1e-2, 1)

ax.set_aspect('equal')
ax.legend()
plt.show()

