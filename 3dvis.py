#!/usr/bin/env python3

import matplotlib.pyplot as plt

with open('res.dat') as f:
    lines = f.readlines()
#print(lines)
#N = float(lines[0])
N= float

i = 0
j = 0
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
x = []
y = []
z = []
print(lines[7:15])
for data in lines[2:]:
    print(data)
    coordinates = data.split()
    print(coordinates)
    x.append(float(coordinates[2]))
    y.append(float(coordinates[3]))
    z.append(float(coordinates[4]))
    i = i+1
    if (i==N):
        i = 0
        print(f"x len {len(x)}, y len {len(y)},z len {len(z)}")
        ax.scatter(x,y,z)
        nn = '{0:03}'.format(j)
        plt.savefig(f"output/frame-"+nn+".png")
        plt.cla()
        ax.set_xlim([0.0, 90.0])
        ax.set_ylim([0.0, 90.0])
        ax.set_zlim([-7.0, 7.0])
        j = j+1
        x = []
        y = []
        z = []
