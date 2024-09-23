import numpy as np
# Definir la función a integrar
def f(x):
    return (np.sin(x))**2 * np.exp(x)

# Regla de Simpson 3/8
def simpson38(a, b, n):
    if n % 3 != 0:
        raise ValueError("n debe ser múltiplo de 3 para aplicar la regla de Simpson 3/8")
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    # Aplicar la fórmula de Simpson 3/8
    integral = (3 * h / 8) * (y[0] + 3 * np.sum(y[1:n:3]) + 3 * np.sum(y[2:n:3]) + 2 * np.sum(y[3:n-1:3]) + y[-1])
    return integral

# Límites de integración
a, b = 0, 2
# Calcular para diferentes valores de n (múltiplos de 3)
n_values_simpson38 = [3, 9, 18]
# Mostrar resultados
for n in n_values_simpson38:
    resultado = simpson38(a, b, n)
    print(f"Para n = {n} subintervalos, la aproximación es: {resultado}")
