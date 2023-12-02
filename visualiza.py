#!/usr/bin/env python3

import matplotlib.pyplot as plt

with open('r14.dat') as f:
    lines = f.readlines()

N = len(lines)#int(lines[0])
i = 0
j = 0
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
x = []
y = []
z = []
for data in lines[2:]:
    print(data)
    coordinates = data.split()
    x.append(float(coordinates[3]))
    y.append(float(coordinates[4]))
    z.append(float(coordinates[5]))
    i = i+1
    if (i!=N):
        i = 0
        ax.scatter(x,y,z)
        nn = '{0:03}'.format(j)
        plt.savefig(f"output14/frame-"+nn+".png")
        #plt.cla()
        ax.set_xlim([80,95])
        ax.set_ylim([25,64])
        ax.set_zlim([0, 2])
        j = j+1
        x = []
        y = []
        z = []