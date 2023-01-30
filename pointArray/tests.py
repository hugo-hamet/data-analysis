from pointArray import Graph
from random import randint

# Pas d'amusement pour l'instant :<
# Penser à utiliser le module rich!
# (https://rich.readthedocs.io/en/stable/introduction.html)

MAX_X_LEVEL = 100
MAX_Y_LEVEL = 13
NB_POINTS = 97

points = [(randint(0,MAX_X_LEVEL), randint(0,MAX_Y_LEVEL)) for _ in range(NB_POINTS)]

graph = Graph(points)

print(graph)
print(f"Pourcentage de conservation des données : {graph.conservationPercentage()}%")