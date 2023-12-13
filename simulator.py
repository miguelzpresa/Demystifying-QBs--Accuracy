#!/usr/bin/env python3
#https://youtu.be/U7rPIg7ZNQ8
#import numpy as np
import math

# MKS
G = 6.67e-11  #N m**2/kg**2

epsilon = 0.128 #m

class Particle():
    def __init__(self, m=0.0, radii=1.0, r=[0.0,0.0,0.0], v = [0.0,0.0,0.0]):
        self.m = m # [kg]
        self.r = r # [m, m, m]
        self.v = v # [m/s, m/s, m/s]
        self.i = 0 # index in the n-body-system
        self.radii = radii
        
    def Print(self):
        #print (self.i,self.m, self.radii, self.r[0], self.r[1],self.r[2],self.v[0],self.v[1],self.v[2])
        print ( self.r[0], self.r[1],self.r[2])
    def sPrint(self):
        #return [str(self.i), str(self.m), str(self.radii), str(self.r[0]), str(self.r[1]),str(self.r[2]),str(self.v[0]),str(self.v[1]),str(self.v[2])]
        return print ( self.r[0], self.r[1],self.r[2])
    #def __repr__():
     #   return self.r

class N_body_system():
    def __init__(self):
        self.N = 0  #number of particles
        self.p = [] # set of particles

    def add_particle(self, p):
        self.N = self.N + 1
        p.i = self.N
        self.p.append(p)

    def Print(self):
        self.p[1].Print()
        #for p in self.p:
            #p.Print()

    def fPrint(self,out):
        for p in self.p:
            out.write(" ".join(p.sPrint())+"\n")

    def Header(self):
        print(self.N)
        print("#index","mass", "radii","x","y","z","vx","vy","vz")

    def fHeader(self, out):
        out.write(str(self.N)+"\n")
        out.write("#index mass radii x y z vx vy vz\n")


class Integrator():
    def __init__(self, n_body_system,dt):
        self.n_body_system = n_body_system
        self.dt = dt
        

    def E(self,m,r):
        #suma = 0.0
        #for p in self.n_body_system.p: #for all particles
        #    m = p.m
        #    if (p.i != n):
        #        suma = suma+ m*dt/r**3
        return m/(r**3)
                
    def U(self, r_i, r_n):
        r_x = r_i[0] - r_n[0]
        r_y = r_i[1] - r_n[1]
        r_z = r_i[2] - r_n[2]
        return [r_x, r_y, r_z]

    def norm(self, r):
        a = math.sqrt(r[0]**2 + r[1]**2 + r[2]**2)
        #if a <= epsilon:
        #    print("#Warning, distance of particles very close!!!")
        #    exit(1)
        #    #return epsilon
        #else:
        return a
    
    def compute(self):
        #print("DEB2",self.n_body_system.N)
        for p in self.n_body_system.p: #for all particles
            n = p.i
            vx = 0.0
            vy = 0.0
            vz = 0.0
            for q in self.n_body_system.p: #lista de ls particulas 
                #print("DEB3",q.i,n)
                #print(f"coordenadas de particula{q.r}")
                if (q.i != n):
                    u = self.U(q.r,p.r)
                    r = self.norm(u)
                    if (r <= q.radii +  p.radii):
                        print("Warning! collision!")
                        return self.n_body_system, True                        
                    vx = vx + self.E(q.m, r)*self.dt*u[0]
                    vy = vy + self.E(q.m, r)*self.dt*u[1]
                    vz = vz + self.E(q.m, r)*self.dt*u[2]
                    #print("DEB1",vx,vy,vz)
            
            p.v[0] = G*vx + p.v[0]
            p.v[1] = G*vy + p.v[1]
            p.v[2] = G*vz + p.v[2]
            
            
        for p in self.n_body_system.p: #for all particles
            p.r[0] = p.v[0]*self.dt + p.r[0]
            p.r[1] = p.v[1]*self.dt + p.r[1]
            p.r[2] = p.v[2]*self.dt + p.r[2]            
            #print(f"hello{p.r}")
        return self.n_body_system, False #no collition

    def __repr__():
        return 
                
#m_sun = 1.98847e30 #Kg4

#0.1sec
#1sec
def main():

    dt = 1e-2 #sec
    #v_x= 7.69
    #v_y= 7.7572
    v_x= 5.18#10.45
    v_y = 14.19 #10.91
    earth = Particle(5.9736e24, 6371.0e3 ,  [0.0,0.0,-6371.0e3], [0, 0, 0])
    ball = Particle(.450, 0.025, [84.582,32.9184, 1.85], [v_x, v_y, 0])
    #coordenadas de llegada x=91.44,y= 31.089 z= 1.88
    #hipo= 7.03


    #theta = grados
    #ancho=64.008 =64.008*.5 -.9144
    #64.008*.5 +.9144 = 32.9184
    # 64.008*.5 -.9144 = 31.089


    #En este código, math.asin(valor) calcula el arcseno del valor en radianes. Luego, math.degrees(arcseno_radianes)
    parabolic_system =  N_body_system()

    parabolic_system.add_particle(earth)
    parabolic_system.add_particle(ball)

    newton = Integrator(parabolic_system, dt)

    #parabolic_system.Header()
    skip = 0

    for j in range(100): #300*.7 = 210 sec > 300 sec
        parabolic_system,collition = newton.compute()
        #if (skip % 1 == 0):
        if collition:
            break
        parabolic_system.Print()
    #earth_acceleration.fPrint(out)
    #skip=skip+1
if __name__ == "__main__" :
    main()



