# data_pipeline_drug_mention

### Description
Un pipeline Data qui sert à importer et ensuite trouver les références entre les données de drugs, articles Pubmed et les essais clinique. 

### Composants
- data : fichiers csv ou json d'entrée par datatype : drugs/pubmed/clinical_trials (avec une template)
- results : repertoire pour stocker le résultat finale drugs_references.json
- src.data_processing : class DataProcessor qui importe des données csv ou json depuis un répertoire, avec une centralisation et une déduplication en dataframe
- src.mention_analysis : la fonction qui détecte si un drug est considéré comme mentionné dans un article PubMed ou un essai clinique
- src.json_generation : JSONGenerator qui applique la détection de mention sur les dataframes et reformaliser le résultat dans un json

### Installation
```
python pip install -r requirements.txt
```

### Lancement
```
python main.py
```

### Traitement ad-hoc
- Extraire depuis le json produit par la data pipeline le nom du journal qui mentionne le plus de
médicaments différents : focntionnement réalisé par main.maxJournal ; 
- Affichage du résultat directement sur l'écran avcec un fichiers de détails stocké dans results : drugs_by_journal.json

exemple :
```
le nom du journal qui mentionne le plus de médicaments différents :
- Psychopharmacology，en total 2 médicaments différents : ['TETRACYCLINE', 'ETHANOL']
- The journal of maternal-fetal & neonatal medicine，en total 2 médicaments différents : ['ATROPINE', 'BETAMETHASONE']
```
### Pour aller plus loin - le traitement de grands volumes de données 
Pour les grands volumes de données, ce qui nécessite plus d'attention et d'optimisation pour garantir la performance et l'efficacité du code. Voici quelques facteurs à prendre en compte et les modifications qui peuvent être nécessaires :
- La gestion de la mémoire est essentielle, veillez à ce que le code ne charge pas l'ensemble des données en mémoire en une seule fois, mais qu'il utilise plutôt une approche lot par lot pour traiter les données.
Utilisez des générateurs ou des itérateurs pour lire et traiter les fichiers volumineux plutôt que de charger l'ensemble du fichier en mémoire.
- Envisagez d'utiliser un système de base de données approprié tel que SQLite, MySQL, PostgreSQL, etc. (ou même les platforms en cloud comme GCP/AWS) pour stocker et récupérer les données plus efficacement.
Créez des index pour accélérer les opérations de recherche et d'extraction des données.
- Optimiser les algorithmes : la gestion des exceptions est encore plus importante lorsque l'on traite de grandes quantités de données. Veillez à ce que le code soit capable de gérer les exceptions telles que les problèmes de qualité des données, les fichiers manquants ou corrompus, etc.
- Scheduling et surveillance par un orchestrateur de jobs comme Airflow ou Cloud Composer si on est sur GCP
- Utiliser le format de fichier parquet pour extraire et load au lieu de csv/json 

