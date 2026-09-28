# Rendu n°1 - Mise en application du plan

EL GANDOUZ Amine
M1 - IA 

## Objectif 

Pour chaque point de mon plan je doit écrire une fonction test, le but est de définir clairement les données:
- Entrée = Arrange (préparer le contexte)
- Appel de la fonction = Act (exécuter le comportement)
- Assertion (proposition que l'on soutient comme vraie) = Assert(comparer à l'attendu)

Bon test unitaire : Lisible, Déterministe (même context, même résultat), Rapide, Isolé

## Résumé des outils 

- coverage = mesure la couverture du code, la proportion du code couvert par pytest durant les tests
- ruff = effectue l'analyse statique du code (linting) pour repérer les problèmes sans avoir à exécuter, commande = ruff check
- Make = automatise la vérification en organisant les commandes, enregistrer les commandes dans un Makefile, commandes : make test, make lint, make coverage 
- Mock = créer des doublures de tests pour remplacer les dépendances externes  
