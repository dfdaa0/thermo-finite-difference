import numpy as np
import matplotlib.pyplot as plt


k = 60.5
h = 100
x = 0.3
y = 0.3
dx = 0.06
dy = 0.06
Tinf = 750
alpha = 17.7e-06
iteracoes = 33
dt = 0.3
criterioEstabilidade = (((-2*((alpha*dt)/(dy**2))) + ((alpha*dt)/(dx**2)) + 1))

print(criterioEstabilidade >= 0)

comportamentoCentral = np.array([300])

x = np.array([[750, 750, 750, 750, 750, 750, 750],
			  [750, 300, 300, 300, 300, 300, 750],
			  [750, 300, 300, 300, 300, 300, 750],
			  [750, 300, 300, 300, 300, 300, 750],
			  [750, 300, 300, 300, 300, 750, 750],
			  [750, 300, 300, 300, 750, 750, 750],
			  [750, 750, 750, 750, 750, 750, 750]])



x = x.astype(float)
y = x.astype(float)


tiposCelulas = np.array([[0,  0,  0,  0,  0,  0,  0],
			             [0,  8,  3,  3,  3,  7,  0],
			             [0,  2,  5,  5,  5,  1,  0],
			             [0,  2,  5,  5,  6,  10, 0],
			             [0,  2,  5,  6,  10, 0,  0],
			             [0,  9,  4,  10, 0,  0,  0],
			             [0,  0,  0,  0,  0,  0,  0]])

linhas, colunas = x.shape


print("Perfil de temperatura inicial da barra (os valores 750 se referem ao ar quente)")
print(x)

while(x[3,3] < 600):
    for m in range(linhas):
        for n in range(colunas):
            
            if tiposCelulas[m,n] == 0:  # ar quente
                y[m,n] = Tinf
            
            if tiposCelulas[m,n] == 1:  # lateral direita
                y[m,n] = ((2*x[m-1,n] + x[m,n+1] + x[m,n-1]) + Tinf*(2*h*dx)/k) / (2*((h*dx/k)+2))
            
            if tiposCelulas[m,n] == 2:  # lateral esquerda
                y[m,n] = ((2*x[m+1,n] + x[m,n+1] + x[m,n-1]) + Tinf*(2*h*dx)/k) / (2*((h*dx/k)+2))
            
            if tiposCelulas[m,n] == 3:  # lateral cima
                y[m,n] = ((2*x[m,n-1] + x[m+1,n] + x[m-1,n]) + Tinf*(2*h*dx)/k) / (2*((h*dx/k)+2))
            
            if tiposCelulas[m,n] == 4:  # lateral baixo
                y[m,n] = ((2*x[m,n+1] + x[m+1,n] + x[m-1,n]) + Tinf*(2*h*dx)/k) / (2*((h*dx/k)+2))
            
            if tiposCelulas[m,n] == 5:  # interna
                y[m,n] = (x[m,n+1] + x[m,n-1] + x[m+1,n] + x[m-1,m]) / 4
            
            if tiposCelulas[m,n] == 6:  # vulco inferior direito
                y[m,n] = ((2*(x[m-1,n] + x[m,n+1]) + (x[m+1,n] + x[m,n-1]) + (2*Tinf*h*dx)/k)) / (2*((h*dx/k)+3))
            
            if tiposCelulas[m,n] == 7:  # canto superior direito
                y[m,n] = (x[m,n-1] + x[m-1,n] + (Tinf*(2*(h*dx)))/k) / (2*((h*dx/k)+1)) 
            
            if tiposCelulas[m,n] == 8:  # canto superior esquerdo
                y[m,n] = (x[m,n-1] + x[m+1,n] + (Tinf*(2*(h*dx)))/k) / (2*((h*dx/k)+1)) 
            
            if tiposCelulas[m,n] == 9:  # canto inferior esquerdo
                y[m,n] = (x[m,n+1] + x[m+1,n] + (Tinf*(2*(h*dx)))/k) / (2*((h*dx/k)+1)) 
            
            if tiposCelulas[m,n] == 10:  # canto inferior direito
                y[m,n] = (x[m,n+1] + x[m-1,n] + (Tinf*(2*(h*dx)))/k) / (2*((h*dx/k)+1))

				
    x += dt * (y - x)
    print(x[3,3])

print(np.round(x, 3))


i, j = np.meshgrid(np.arange(x.shape[0]), np.arange(x.shape[1]))

plt.imshow(x, cmap='plasma', interpolation='nearest')
