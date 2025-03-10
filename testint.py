from scipy.integrate import quad
from functools import partial

# Définir la fonction à intégrer avec a et b
def integrand(x, a, b):
    return a * x**2 + b


a = 2  # Exemple de valeur pour a
b = 3  # Exemple de valeur pour b
integrand_with_params = partial(integrand, a=a, b=b)

# Calculer l'intégrale entre 0 et 5
I, _ = quad(integrand_with_params, 0, 5)

print("L'intégrale est:", I)
