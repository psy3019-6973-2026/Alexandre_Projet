"""
tasks.py — Automatisation du pipeline d'analyse fMRI
Utilisation : 
 - Aller dans le dossier qui contient les fichiers
 - pip install invoke --> invoke setup --> conda activate false_memory --> invoke all
"""

from invoke import task
from pathlib import Path

# Paramètres — modifie ici pour changer de sujet ou dataset
dataset_id_1 = "ds003789"  # dataset original
dataset_id_2 = "ds002731"  # dataset comparaison
subj = "5404"              # sujet dataset original
subj1 = "5024"             # sujet 1 dataset comparaison
subj2 = "3724"             # sujet 2 dataset comparaison
notebook = "Alexandre_Final.ipynb"

# Chemins
dataset_dir1 = Path(f"./{dataset_id_1}").absolute()
dataset_dir2 = Path(f"./{dataset_id_2}").absolute()


@task
def setup(c):
    """Crée et active l'environnement conda"""
    print("Installation des dépendances...")
    c.run("conda env create -f environnement_false_memory.yml", warn=True)
    print("Environnement créé! Pour l'activer :")
    print("conda activate false_memory")

@task
def fetch(c):
    """Télécharge les données depuis OpenNeuro"""
    print("Téléchargement des données...")

    # Dataset 1
    c.run(f"datalad install https://github.com/OpenNeuroDatasets/{dataset_id_1}.git", warn=True)
    c.run(f"datalad get -d {dataset_dir1} {dataset_dir1}/sub-{subj}/func/*encoding*nii.gz", warn=True)
    c.run(f"datalad get -d {dataset_dir1} {dataset_dir1}/sub-{subj}/func/*encoding*tsv", warn=True)
    c.run(f"datalad get -d {dataset_dir1} {dataset_dir1}/sub-{subj}/anat/*T1w.nii.gz", warn=True)
    print(f"Dataset 1 ({dataset_id_1}) - sub-{subj} téléchargé!")

    # Dataset 2
    c.run(f"datalad install https://github.com/OpenNeuroDatasets/{dataset_id_2}.git", warn=True)
    for subj_ds2 in [subj1, subj2]:
        c.run(f"datalad get -d {dataset_dir2} {dataset_dir2}/sub-{subj_ds2}/func/*encoding*nii.gz", warn=True)
        c.run(f"datalad get -d {dataset_dir2} {dataset_dir2}/sub-{subj_ds2}/func/*encoding*tsv", warn=True)
        c.run(f"datalad get -d {dataset_dir2} {dataset_dir2}/sub-{subj_ds2}/anat/*T1w.nii.gz", warn=True)
        print(f"Dataset 2 ({dataset_id_2}) - sub-{subj_ds2} téléchargé!")


@task
def run(c):
    """Exécute le notebook au complet"""
    print(f"Exécution du notebook {notebook}...")
    c.run(
        f"jupyter nbconvert --to notebook --execute "
        f"--inplace "  
        f"--log-level=10 "
        f"--ExecutePreprocessor.timeout=3600 "
        #f"--output Alexandre_Final_execute.ipynb "
        f"{notebook}",
        warn=True #pour nous dire s'il y a une erreur
    )
    print("Notebook exécuté! Résultat : Alexandre_Final.ipynb ") #Alexandre_Final_executed.ipynb


@task
def clean(c): #seulement utiliser si crée un fichier
    """Supprime le notebook exécuté"""
    output = Path("Alexandre_Final_execute.ipynb")
    if output.exists():
        output.unlink()
        print("Alexandre_Final_execute.ipynb supprimé!")
    else:
        print("Rien à nettoyer.")


@task
def all(c):
    """Exécute le pipeline complet : fetch + run"""
    fetch(c)
    run(c)
