import numpy as np

# Definir la función f(x) = (sin(x))^2 * e^x
def f(x):
    return (np.sin(x))**2 * np.exp(x)

# Método de trapecios
def trapecios(a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)  # Generar los puntos entre a y b con n subintervalos
    y = f(x)  # Evaluar la función en esos puntos
    integral = (h / 2) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])  # Aplicar la fórmula de trapecios
    return integral

# Límites de integración
a, b = 0, 2

# Calcular para diferentes valores de n
n_values = [2, 8, 16]
for n in n_values:
    resultado = trapecios(a, b, n)
    print(f"Para n = {n} subintervalos, la aproximación es: {resultado}")
