import pytest
import time
from src.triangulateur import trianguler

# Tests unitaires: Mathématiques, binaires

# test logique n°1: Vérifier que ce sont bien des triangles qui se forment, l'algorithme doit fournir exactement 1 triangle unique composé de 3 points.
def test_trois_points_forment_triangle():
    # Arrange 
    points = [(0, 0), (1, 0), (0, 1)]
    # Act
    result = trianguler(points)
    # Assert
    assert len(result) == 1, "L'algorithme doit fournir exactement 1 triangle"
    assert all(len(triangle) == 3 for triangle in result), "Chaque triangle doit être composé de 3 points"

# test n°2: Eviter la triangulation pour 3 points colinéaires.
def test_trois_points_colineaires():
    points = [(0, 0), (1, 1), (2, 2)]  # Points colinéaires
    result = trianguler(points)
    assert len(result) == 0, "Aucun triangle ne doit être formé avec des points colinéaires"

# test n°3: Ne pas traiter, ignorer ou bien éliminer les points doublons.
def test_points_doublons():
    points = [(0, 0), (1, 0), (0, 1), (0, 0)]  # Point (0, 0) est un doublon
    result = trianguler(points)
    assert len(result) == 1, "L'algorithme doit ignorer les points doublons et former un triangle unique"
    assert all(len(triangle) == 3 for triangle in result), "Chaque triangle doit être composé de 3 points"

# test n°4: Une précision géométrique est nécessaire pour les float / double, car ce sont des coordonnées entières, on ne veut pas de points 'presques alignés'.
def test_points_presque_alignes():
    points = [(0, 0), (1, 1), (2, 2.0001)]  # Points presque alignés
    result = trianguler(points)
    assert len(result) == 0, "Aucun triangle ne doit être formé avec des points presque alignés"



# Tests d'intégration: HTTP, Mock


# Tests de robustesse: tout ce qui est value error
def test_points_invalides():
    points = [(0, 0), (1, 0)]  # Seulement 2 points, pas assez pour former un triangle
    with pytest.raises(ValueError):
        trianguler(points)


# Ne pas traiter la requête si l'algorithme reçoit moins de 3 points (0, 1 ou 2 points reçus exclus), j
# je peux le traiter avec un simple système d'exceptions, qui dans le cadre de pytest s'utilise avec le context manager 'with pytest.raises(Exception):'.
def test_points_insuffisants():
    points = [(0, 0), (1, 0)]  # Seulement 2 points, pas assez pour former un triangle
    with pytest.raises(ValueError):
        trianguler(points)

# Tests de performance
@pytest.mark.performance
def test_performance():
    # Simuler un test de performance
    start_time = time.time()
    
    # Exemple de code à tester (remplacez par votre code réel)
    result = sum(range(1000000))
    
    end_time = time.time()
    duration = end_time - start_time
    
    # Vérifier que le temps d'exécution est inférieur à un seuil (par exemple, 1 seconde)
    assert duration < 1, f"Performance test failed: took {duration} seconds"
