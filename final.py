import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad
import sympy as sp


canvas = None

# Fonction pour dessiner la courbe et calculer l'intégrale de con 
def plot_graph():
    global canvas  # Utiliser la variable globale pour réutiliser et supprimer le canvas précédent

    # Si un graphique est déjà affiché, on le supprime car azy
    if canvas:
        canvas.get_tk_widget().destroy()

    # Récupérer la fonction entrée par l'user
    function_input = entry_function.get()

    # Vérifier si l'entrée est vide
    if not function_input.strip():
        label_result.config(text="Veuillez entrer une fonction valide.")
        return

    # Récupérer les bornes A et B pour le graphique
    try:
        A = float(entry_A.get())
        B = float(entry_B.get())
    except ValueError:
        label_result.config(text="Veuillez entrer des bornes valides pour le graphique.")
        return
    
    
    if A >= B:
        label_result.config(text="La borne inférieure (A) doit être inférieure à la borne supérieure (B).")
        return

    # Définir un intervalle pour la fonction
    x = np.linspace(A, B, 400)

    
    try:
        
        y = eval(function_input)
    except Exception as e:
        label_result.config(text=f"Erreur dans la fonction : {str(e)}")
        return

   
    fig, ax = plt.subplots()

    
    ax.plot(x, y, label=function_input)

    # ADD des labels et un titre
    ax.set_title(f"Graphique de {function_input}")
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.legend()

    # Tracer les droites représentant les bornes C et D pour l'intégrale
    try:
        C = entry_C.get()
        D = entry_D.get()

        # Si C et D ne sont pas vides, les utiliser
        if C and D:
            C = float(C)
            D = float(D)
            ax.axvline(x=C, color='r', linestyle='--', label=f'c = {C}')
            ax.axvline(x=D, color='g', linestyle='--', label=f'd = {D}')
            # Calculer l'intégrale entre C et D
            integral_value, error = quad(integrand, C, D)
            label_result.config(text=f"Valeur de l'intégrale de {function_input} entre {C} et {D}: {integral_value:.4f}\nErreur estimée: {error:.4e}")
        else:
            # Si C et D sont vides, calculer l'intégrale entre A et B
            integral_value, error = quad(integrand, A, B)
            label_result.config(text=f"Valeur de l'intégrale de {function_input} entre {A} et {B}: {integral_value:.4f}\nErreur estimée: {error:.4e}")
    except ValueError:
        label_result.config(text="Veuillez entrer des valeurs valides pour C et D.")

    # Afficher la figure dans Tkinter
    canvas = FigureCanvasTkAgg(fig, master=frame_graph)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Définir l'intégrande pour scipy
def integrand(x):
    function_input = entry_function.get()
    return eval(function_input)


root = tk.Tk()
root.title("Graphique de Fonction")


frame_graph = tk.Frame(root)
frame_graph.pack()


label_function = tk.Label(root, text="Entrez une fonction (par exemple '2*x**2 + 3*x'):")
label_function.pack()

entry_function = tk.Entry(root)
entry_function.pack()


label_A = tk.Label(root, text="Valeur de la borne A (Début de la fonction):")
label_A.pack()

entry_A = tk.Entry(root)
entry_A.pack()


label_B = tk.Label(root, text="Valeur de la borne B (Fin de la fonction):")
label_B.pack()

entry_B = tk.Entry(root)
entry_B.pack()


label_C = tk.Label(root, text="Valeur de C (Borne inférieure de l'intégrale, facultatif):")
label_C.pack()

entry_C = tk.Entry(root)
entry_C.pack()

label_D = tk.Label(root, text="Valeur de D (Borne supérieure de l'intégrale, facultatif):")
label_D.pack()

entry_D = tk.Entry(root)
entry_D.pack()


button_plot = tk.Button(root, text="Dessiner la fonction", command=plot_graph)
button_plot.pack()

label_result = tk.Label(root, text="Graphique de la fonction et résultats de l'intégrale")
label_result.pack()

# Lancer le neuille de code
root.mainloop()
