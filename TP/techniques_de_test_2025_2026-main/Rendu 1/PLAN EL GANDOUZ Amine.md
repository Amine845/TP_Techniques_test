# Rendu n°1 - Plan de tests 

EL GANDOUZ Amine
M1 - IA 

## 1. Choix des catégories de tests (Pourquoi ?)

Ma stratégie de tests va reposer sur la démarche Test Driven Development qui va consiter à écrire les tests avant le code et ensuite mettre en place le cycle Red Green Refactor pour guider l'implémentation. Mon objectif principal reste d'éclaircir et de mettre en place les tests qui couvrent les cas pertinents tout en évitant les cas inutiles. 

Premièrement, je vais dresser des catégories de tests suivant les axes vu en cours qui sont: Axe 1 (boîtes noires, blanches et grises) selon l'accès au code, Axe 2 (granularité) niveau d'abstraction et Axe 3 selon la qualité.

1. Tests unitaires
Les tests unitaires vont me permettre de tester le bon fonctionnement d'une petite partie précise du code ce qui est idéal dans mon cas selon moi car l'algorithme final sera complexe. 

2. Tests d'intégrations
Ces tests vont me permettre de vérifier que les composants interagissent correctement entre eux car dans le cadre du triangulateur il faudra tester les interactions réseau.

3. Tests de robustesse 
Ils évaluent la capacité du système à fonctionner correctement en présence d'entrées invalides ou de conditions d'utilisation stressantes.   

4. Tests de performance 
Ces tests évaluent la capacité du composant à fonctionner sous contrainte de temps et de ressources, en mesurant les temps de réponse de l'algorithme. 

Détail de mes cas de base (Tests logiques / mathématiques):

- Vérifier que ce sont bien des triangles qui se forment, l'algorithme doit fournir exactement 1 triangle unique composé de 3 points.
- Eviter la triangulation pour 3 points colinéaires.
- Ne pas traiter, ignorer ou bien éliminer les points doublons. 
- Une précision géométrique est nécessaire pour les float / double, car ce sont des coordonnées entières, on ne veut pas de points 'presques alignés'. 
- Gestion de l'échelle précise. 
- Ne pas traiter la requête si l'algorithme reçoit moins de 3 points (0, 1 ou 2 points reçus exclus), je peux le traiter avec un simple système d'exceptions, qui dans le cadre de pytest s'utilise avec le context manager 'with pytest.raises(Exception):'.
- Ne pas supposer que les coordonnées doivent être strictement positives, elles peuvent être nulles ou négatives.
- Si 4 points sont soumis l'algorithme doit me rendre 2 triangles sans chevauchement. 
- Fournir le même triangle peut importe le sens des points données en arguments, exemple: triangulation(p1, p2, p3) donnera le même triangle que triangulation(p3, p2, p1). 

Principes de conception: 

- Découper les tests: unitaires, intégration système et performance.
- Eviter les tests inutiles qui sont déjà testés ailleurs, c'est à dire tester uniquement la partie de code en cours sans revérifier le travail d'une autre fonction ou d'un compostant externe. 

Détail des tests liés à l'architecture et aux données (issus du sujet) :

Le sujet précise que les échanges se font via une représentation binaire compacte. Il faudra tester que le code arrive bien à lire ce format (vérifier par exemple que les 4 premiers bytes donnent bien le nombre de points attendus, puis lire correctement les float X et Y).

Vérifier que la création du format binaire de sortie pour les Triangles est conforme à la structure demandée (points d'abord, puis nombre de triangles, puis indices des sommets).

Le workflow général indique que le composant est une API HTTP. Il faudra vérifier que le Triangulator gère bien la réception d'un PointSetID depuis le Client, fait correctement l'appel au PointSetManager, et renvoie une réponse HTTP valide.

Tester les cas limites sur la structure binaire pour garantir la robustesse du composant : soumettre un PointSet vide, un compteur (count) qui ne correspond pas au nombre de bytes réellement présents, ou encore des données tronquées.


## 2. Implémentation de la stratégie (Comment ?)

L'implémentation de mes tests va s'appuyer sur le framework pytest qui va me permettre de structurer chaque test pour préparer le contexte, exécuter le comportement puis comparer le résultat à l'attendu.   

Ensuite, d'après le cours, il est important de respecter le principe d'isolation pour ne pas dépendre de systèmes externes lors des tests unitaires. Plutôt que d'utiliser le véritable serveur PointSetManager, je compte m'appuyer sur le mécanisme des doublures (stubs ou mocks) vu en cours, ça me permettra de simuler une réponse fixe du serveur ou de provoquer artificiellement une erreur de réseau pour voir comment mon code réagit.   

Concernant les tests de performance, je compte les séparer du reste avec un marqueur spécifique (comme @pytest.mark.performance) pour ne pas ralentir l'exécution quotidienne des tests, ça s'intègre parfaitement avec la commande make perf_test demandée dans le sujet. Enfin, toujours d'après le cours, j'utiliserai l'outil coverage pour vérifier quelles lignes et quelles branches de mon code sont réellement traversées par mes scénarios de test.  