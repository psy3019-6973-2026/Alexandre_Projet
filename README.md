# Alexandre_Projet

J'ai choisi ce projet à cause de mon intérêt pour la mémoire! 

## Description du projet
Le nom du projet choisi est « _Functional Brain Activation During a Memory Encoding and Retrieval Task: Discovering Tools and Techniques for Analysis_ » de Stella Ruddy. [Ce projet](https://school-brainhack.github.io/project/activation-tools/) a été publié le 14 juin 2024 et a été inspiré par l'article scientifique « _Dynamic changes in neural representations underlie the repetition effect on false memory_ » ([Xuhao Shao et al., 2022](https://doi.org/10.1016/j.neuroimage.2022.119442)). 

L'article scientifique présente une tâche qui étudie les faux souvenirs ainsi que les régions cérébrales qui y sont associées grâce au « [_Deese-Roediger-McDermott (DRM) Task_](https://pubmed.ncbi.nlm.nih.gov/28190038/) » et à l'imagerie par résonance magnétique fonctionnelle (IRMf). La tâche était séparée en deux phases : la phase d'encodage et la phase de récupération. Dans la phase d'encodage, les participants devaient se souvenir de 9 listes de mots qui étaient chacune présentée 3 fois. La phase de récupération avait lieu 24h plus tard et le participant se faisait présenter une série de mots. Il devait ensuite indiquer si ce mot était présent ou non dans les listes de la journée précédente. Certains participants effectuaient la phase d'encodage et de récupération dans un IRMf (Ruddy, 2024). La figure ci-dessous explique davantage la description de la tâche.

<img width="1419" height="631" alt="image" src="https://github.com/user-attachments/assets/f7988e98-a4fe-4324-8696-6acf62a1b108" />

Les données importantes pour ce projet sont les résultats d'IRMf lors de la phase d'encodage. Les analyses sont axées sur les différences d'activation neuronale entre la première présentation des listes et la troisième présentation. Toutes les données se retrouvent sur OpenNeuro ([ds003789](https://openneuro.org/datasets/ds003789/versions/2.1.0)), mais dans le cadre de ce projet, les données IRMf d'un seul participant ont été analysées. 

Le projet Brainhack applique un modèle linéaire général (GLM) pour estimer l'activité cérébrale associée aux différentes phases, estimer si les données concordent avec le modèle, voir les contrastes grâce à des tests statistiques et visualiser les cartes d'activation cérébrale observées, entre autres. 

## Description des tâches 


### Tâche 1 : Reproductibilité et infrastructure

Ma première tâche consiste à reproduire le notebook existant à partir d’un environnement vierge. 

Sous-tâches :
- [x] Créer un fichier environment.yml
- [x] Cloner les données OpenNeuro
- [ ] Corriger des problèmes de chemins de fichiers
- [ ] Comprendre le pipeline d'analyse
- [ ] Documenter tout le processus dans un fichier Markdown

Tâches supplémentaires (si nécessaire) :
- [ ] Créer un script d'automatisation (comme l'exercice 4, question 11) pour mettre toutes les informations importantes dans un fichier sans être obligé d'utiliser les cellules individuelles.


### Tâche 2 : Données et standards
Ma deuxième tâche consiste à adapter le notebook à un jeu de données ouvert différent. En utilisant les données OpenNeuro ([ds002731](https://openneuro.org/datasets/ds002731/versions/1.0.2)) de l'article « _Multiple interactive memory representations underlie the induction of false memory_ » ([Bi Zhu et al., 2019](https://doi.org/10.1073/pnas.1817925116)), je planifie modifier le notebook existant pour qu'il puisse fonctionner avec ces données. Le notebook actuel est seulement fonctionnel pour les données OpenNeuro de l'article scientifique original, ce qui va peut-être entraîner des problèmes de fichiers, des problèmes d'organisation BIDS, etc.

Présentement, le fichier est seulement applicable pour un participant. Je vais changer le script pour que ce soit facile à changer entre les différents participants, que ce soit dans le jeu de données actuel ou dans le nouveau.

Sous-tâches :
 - [x] Trouver un article avec un jeu de données ouvert similaire au projet
 - [ ] Adapter le notebook au deuxième jeu de données ouvert
 - [ ] Adapter le notebook pour permettre de changer entre les participants d'un jeu de données

Tâches supplémentaires (si nécessaire) :
- [ ] Créer un script de validation de la structure du jeu de données, vérifier l'existence des fichiers nécessaires à l'analyse.
- [ ] Coder un tableau récapitulatif de plusieurs sujets d'un seul jeu de données avec les informations importantes

### Tâche 3 : Analyse et modélisation
Ma dernière tâche consiste à comparer plusieurs modèles de manière systématique. Une section du notebook démontre les différentes façons de controler les comparaisons multiples pour diminuer les erreurs statistiques de type I (threshold, Bonferroni, False discovery rate, Discard small voxels). La section est structurée de façon sérielle avec des visualisations sans expliquer leurs différences (plus démonstrative qu'explicative). Je vais faire en sorte que ce soit davantage explicatif. Je vais créer une fonction pour réunir les techniques afin de faciliter les comparaisons.



<img width="407.6" height="167.6" alt="image" src="https://github.com/user-attachments/assets/09f4104b-3200-4c97-89e5-55e7006db6f6" />
<img width="407.6" height="167.6" alt="image" src="https://github.com/user-attachments/assets/8e9520b2-bd73-4841-b712-a58d778dd7d7" />
<img width="407.6" height="167.6" alt="image" src="https://github.com/user-attachments/assets/f1baa2c4-91d8-45c3-9f12-90269ba5a56d" />
<img width="407.6" height="167.6" alt="image" src="https://github.com/user-attachments/assets/89cf0f43-8c9b-4fad-b52a-31c1bf021096" />


Sous-tâches : 
 - [ ] Rechercher la méthodologie d'une bonne comparaison pour que les informations utilisées soient pertinentes
 - [ ] Réorganiser le code et créer une fonction pour faire toutes les analyses en même temps, ce qui permettra de standardiser les résultats et de rendre le tout plus clair
 - [ ] Trouver une façon de les comparer selon la méthodologie trouvée. Mettre ces informations en tableau, par exemple : 


|         | Threshold           | Bonferroni  | False discovery rate  | Discard small voxels  |
| ------------- |:-------------:| -----:| -----:| -----:|
| Info. 1      | ... |  ... | ... | ... |
| Info. 2      |  ... | ... | ... | ... |
| Info. 3 |  ... | ... | ... | ... |

Tâches supplémentaires (si nécessaire) :
- [ ] Ajouter la comparaison du test-t et du test F qui est décrite dans cette même section et l'ajouter à la comparaison;
- [ ] Créer un court notebook pédagogique expliquant cette partie du projet (différences méthodologiques et de visualisation);
- [ ] Ajouter au notebook une visualisation avec les quatre côte à côte avec la même échelle pour montrer l'impact du choix de visualisation.

---

<table><tr><td>
  <strong>Utilisation d'intelligence artificielle</strong> :<br>
  <ul>
  <li>Compréhension de l'article scientifique.<br>
  <li>Différences de visualisations des méthodes pour évaluer la possibilité des tâches supplémentaires.<br>
<img width="160" height="64" alt="image" src="https://github.com/user-attachments/assets/a0896670-e6a3-405a-a3ea-1e8db5f07dd8" /><br>
<br></td></tr></table>



<details>
  <summary>Liens utilisés</summary>

-  Projet de Stella Ruddy : https://school-brainhack.github.io/project/activation-tools/
-  Article scientifique d'inspiration (Xuhao Shao et al., 2022) : https://doi.org/10.1016/j.neuroimage.2022.119442
-  Données OpenNeuro article d'inspiration (Xuhao Shao et al., 2022): https://openneuro.org/datasets/ds003789/versions/2.1.0
-  DRM task : https://pubmed.ncbi.nlm.nih.gov/28190038/
-  Article scientifique jeu de donnée additionnel (Bi Zhu et al., 2019): https://doi.org/10.1073/pnas.1817925116
-  Données OpenNeuro article additionnel (Bi Zhu et al., 2019) : https://openneuro.org/datasets/ds002731/versions/1.0.2

</details>

Merci!
