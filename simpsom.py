import numpy as np

# Definir la función f(x) = (sin(x))^2 * e^x
def f(x):
    return (np.sin(x))**2 * np.exp(x)

# Regla de Simpson 1/3
def simpson(a, b, n):
    if n % 2 == 1:
        raise ValueError("n debe ser un número par para aplicar la regla de Simpson")
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)  # Generar los puntos
    y = f(x)  # Evaluar la función en esos puntos
    integral = (h / 3) * (y[0] + 4 * np.sum(y[1:n:2]) + 2 * np.sum(y[2:n-1:2]) + y[-1])  # Aplicar fórmula de Simpson
    return integral

# Límites de integración
a, b = 0, 2

# Calcular para diferentes valores de n (deben ser pares)
n_values = [2, 8, 16]
for n in n_values:
    resultado = simpson(a, b, n)
    print(f"Para n = {n} subintervalos, la aproximación es: {resultado}")
