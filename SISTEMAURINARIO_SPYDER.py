"""
Proyecto: Sistema Urinario

Departamento de Ingeniería Eléctrica y Electrónica, Ingeniería Biomédica
Tecnológico Nacional de México [TecNM - Tijuana]
Blvd. Alberto Limón Padilla s/n, C.P. 22454, Tijuana, B.C., México

Nombre del alumno: Marla Espinoza Bedoy, Abraham Gómez Aguilar, Jesus Zamora Cervantes
Número de control: 21212152, 21212158, 21212185
Correo institucional: l21212152@tectijuana.edu.mx, l21212158@tectijuana.edu.mx, l21212185@tectijuana.edu.mx

Asignatura: Modelado de Sistemas Fisiológicos
Docente: Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx
"""
# Instalar librerias en consola
#!pip install control
#!pip install slycot

# Librerías para cálculo numérico y generación de gráficas
import numpy as np
import math as m 
import matplotlib.pyplot as plt
import control as ctrl



# Datos de la simulación
x0, t0, tF, dt, w, h = 0, 0, 10, 1E-3, 6, 3
N = round((tF-t0)/dt) + 1 
t = np.linspace (t0, tF, N)
u1 = np.zeros(N); u1[round(1/dt):round(2/dt)] = 1 #Impulso
signals = {
    "Sistema Urinario": u1,
}

# Componentes del circuito RLC y función de transferencia
L=4.7E-3
R1=10E3
R2=1000E3


#Parámetros de individuo sano 
C=440E-6
R3=20E3
num = [R2*R3*C, 0]
den = [L*C*R1+L*C*R2, R1*R2*C+R2*R3*C+R1*R2*C, R1+R2]
sys = ctrl.tf(num,den)  # Función de transferencia (persona saludable)
print('Individuo sano (control):')
print(sys)


#Parametros del individuo con incontinencia
C_1=110E-6
R3_1=5E3
num = [R2*R3_1*C_1, 0]
den = [L*C_1*R1+L*C_1*R2, R1*R2*C_1+R2*R3_1*C_1+R1*R2*C_1, R1+R2]
sysE = ctrl.tf(num,den)  # Función de transferencia (persona no saludable)
print('Individuo enfermo (caso):')
print(sysE)

#Parametros del controlador
Cr = 1E-6
Re = 759.04
numPID = [1]
denPID = [Re*Cr, 0]
PID = ctrl.tf(numPID,denPID)


# Sistema de control de tratamiento 
X2 = ctrl.series(PID,sys)
sysPID=ctrl.feedback(X2,1,sign=-1)
print('Sistema con tratamiento (individuo enfermo):')
print(sysPID)

#Graficación paciente sano 
    
for label, signal in signals.items():
    fig, ax = plt.subplots()
       
    # Respuesta del sistema sin tratamiento (persona saludable)
    ts, Pex = ctrl.forced_response(sys, t, signal, x0)
    ax.plot(t, Pex, "-", color=[1, 0, 0], label='$P_e(t):(Control)$')
    
    # Respuesta del sistema sin tratamiento (persona enferma)
    ts, Pey = ctrl.forced_response(sysE, t, signal, x0)
    ax.plot(t, Pey, "-", linewidth=2, color=[0.5, 0, 0.5], label='$P_e(t): (Caso)$')
    
    # Respuesta del sistema con tratamiento aplicado (control PID)
    ts, Pez = ctrl.forced_response(sysPID, t, Pex, x0)
    ax.plot(t, Pez, ":", linewidth=2, color=[0.25, 0.75, 0.25], label='$P_e(t):(Tratamiento)$')


    # Configuración de la gráfica
    ax.grid(False)
    ax.set_xlim(0, 10)
    ax.set_xticks(np.arange(0, 11, 1))
    ax.set_ylim(-0.1, 0.6)
    ax.set_yticks(np.arange(-0.1, 0.7, 0.1))
    ax.set_xlabel("$t$ [s]")
    ax.set_ylabel("$P (t)$ $[V]$")
    #ax.set_title(f"{label.upper()}")
    ax.legend(bbox_to_anchor=(0.5, -0.37), loc='center', ncol=4)

   # Guardar gráfica con nombre dinámico según la etiqueta de la señal
    fig.set_size_inches(w, h)
    fig.tight_layout()
    namepng = f'python_{label.replace(" ", "_")}.png'
    namepdf = f'python_{label.replace(" ", "_")}.pdf'
    fig.savefig(namepng, dpi=600, bbox_inches='tight')
    fig.savefig(namepdf, bbox_inches='tight')
    plt.show()
