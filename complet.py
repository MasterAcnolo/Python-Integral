from scipy.integrate import quad
import sympy as sp

# Demander à l'utilisateur d'entrer la fonction
function_input = input("Entrez la fonction à intégrer (en termes de x, par exemple '2*x**2 + 3*x'): ")

# Demander les valeurs de a et b (comme bornes)
a = float(input("Valeur de petit A (borne inférieure): "))
b = float(input("Valeur de petit B (borne supérieure): "))

# Convertir la chaîne en fonction sympy parce que sinon il comprend pas le con
x = sp.symbols('x')
f = sp.sympify(function_input)


def integrand(x):
    return f.subs({'x': x}).evalf() ## FONCTION MAGIQUE POUR QUE LA LIB ELLE COMPRENNE LA FONCTION DE CON

# Intégrer la fonction avec les bornes a et b
I, error = quad(integrand, a, b)

print("L'intégrale est: ", I)
print("L'erreur estimée est: ", error)

