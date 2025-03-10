import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

# Variable globale pour stocker le canvas afin de pouvoir le supprimer
canvas = None

# Fonction pour dessiner la courbe
def plot_graph():
    global canvas  # Utiliser la variable globale pour réutiliser et supprimer le canvas précédent

    # Si un graphique est déjà affiché, on le supprime
    if canvas:
        canvas.get_tk_widget().destroy()

    # Récupérer la fonction entrée par l'utilisateur
    function_input = entry_function.get()

    # Vérifier si l'entrée est vide
    if not function_input.strip():
        label_result.config(text="Veuillez entrer une fonction valide.")
        return

    # Récupérer les bornes a et b
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
    except ValueError:
        label_result.config(text="Veuillez entrer des bornes valides.")
        return
    
    # Vérifier si a est inférieur à b
    if a >= b:
        label_result.config(text="La borne inférieure (a) doit être inférieure à la borne supérieure (b).")
        return

    # Définir un intervalle pour la fonction
    x = np.linspace(a, b, 400)

    # Remplacer l'expression de la fonction par de l'évaluation dynamique
    try:
        # Cette méthode évalue la fonction en remplaçant 'x' dans l'expression entrée par l'utilisateur
        y = eval(function_input)
    except Exception as e:
        label_result.config(text=f"Erreur dans la fonction : {str(e)}")
        return

    # Créer une figure et un axe
    fig, ax = plt.subplots()

    # Tracer la courbe de la fonction
    ax.plot(x, y, label=function_input)

    # Ajouter des labels et un titre
    ax.set_title(f"Graphique de {function_input}")
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.legend()

    # Ajuster la plage de l'axe y
    ax.set_ylim(min(y) - 1, max(y) + 1)  # Ajuster l'intervalle de y autour des valeurs minimales et maximales

    # Afficher la figure dans Tkinter
    canvas = FigureCanvasTkAgg(fig, master=frame_graph)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Créer la fenêtre principale
root = tk.Tk()
root.title("Graphique de Fonction")

# Créer un cadre pour la fonction d'affichage graphique
frame_graph = tk.Frame(root)
frame_graph.pack()

# Créer un champ de texte pour entrer la fonction
label_function = tk.Label(root, text="Entrez une fonction (par exemple '2*x**2 + 3*x'):")
label_function.pack()

entry_function = tk.Entry(root)
entry_function.pack()

# Créer un champ pour la borne inférieure a
label_a = tk.Label(root, text="Valeur de la borne inférieure (a):")
label_a.pack()

entry_a = tk.Entry(root)
entry_a.pack()

# Créer un champ pour la borne supérieure b
label_b = tk.Label(root, text="Valeur de la borne supérieure (b):")
label_b.pack()

entry_b = tk.Entry(root)
entry_b.pack()

# Créer un bouton pour dessiner la courbe
button_plot = tk.Button(root, text="Dessiner la fonction", command=plot_graph)
button_plot.pack()

# Créer un label pour afficher le résultat
label_result = tk.Label(root, text="Graphique de la fonction")
label_result.pack()

# Lancer l'application
root.mainloop()
