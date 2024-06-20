import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math

N = 2
R = 20
R_particula = 1

#___________________Función para generar posiciones aleatorias___________________________

def Posiciones_random(N, R):
    phi_N = np.random.uniform(0, 2*np.pi, N)
    omega_N = np.random.rand(N) - 0.5
    z_N = R * np.exp(1j*phi_N)
    return z_N, phi_N, omega_N


#___________________Proxima función para implementar cargas aleatorias_______________

carga = 1 


#___________________Próxima función para generar velocidades aleatorias_________________

def Velocidad_random(N, z_N):    
    return  1j * z_N * omega_N    

z_N, phi_N, omega_N = Posiciones_random(N, R)
v_N = Velocidad_random(N, z_N)
#___________________Función para actualizar velocidades y colisiones ________________________________

def actualizar_posiciones(z_N, phi_N, v_N, delta_t):
    phi_N += omega_N * delta_t
    
    
    z_N = R * np.exp(1j * phi_N)
    #v_N = 1j * z_N * omega_N
    
    for i in range(len(z_N)):
        for j in range(i + 1, len(z_N)):
            if np.abs(z_N[i] - z_N[j]) <= 2 * R_particula:
                direccion_impacto = z_N[j] - z_N[i]

                v_rel = v_N[i] - v_N[j]
                v_N[i] -=  np.dot(v_rel, direccion_impacto) * direccion_impacto / np.abs(direccion_impacto)**2
                v_N[j] -=  np.dot(v_rel, direccion_impacto) * direccion_impacto / np.abs(direccion_impacto)**2
                print("chocaron")
                

    
    return z_N, phi_N, v_N



#___________________Generar gráfico de las partículas_________________

def Circulo(z_N, R_particula):
    fig, ax = plt.subplots()
    circle = plt.Circle((0, 0), R, color='black', fill=False)
    ax.add_artist(circle)

    for i in range(N):
        x, y = np.real(z_N[i]), np.imag(z_N[i])
        particle_circle = plt.Circle((x, y), R_particula, color=colores[i], fill=True)
        ax.add_artist(particle_circle)

    ax.set_xlim(-R-0.1, R+0.1)
    ax.set_ylim(-R-0.1, R+0.1)
    ax.set_aspect('equal')

    plt.show()
    


#_____________________Animación________________________________________

colores = np.random.rand(N, 3)

def animacion(i):
    global z_N, v_N, phi_N, omega_N
    delta_t = 0.1  
    
    z_N, phi_N, v_N = actualizar_posiciones(z_N, phi_N, v_N, delta_t)
    
    ax.clear()
    circle = plt.Circle((0, 0), R, color='black', fill=False)
    ax.add_artist(circle)
    
    x_N = np.real(z_N)
    y_N = np.imag(z_N)

    for i in range(N):
        ax.scatter(x_N[i], y_N[i], color=colores[i],s=R_particula*R)

    ax.set_xlim(-R-0.5, R+0.5)
    ax.set_ylim(-R-0.5, R+0.5)
    ax.set_aspect('equal')

fig, ax = plt.subplots()

ani = FuncAnimation(fig, animacion, frames=100, interval=20)

plt.show()
