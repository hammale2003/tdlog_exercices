# Commandes Git de Base avec Explications

## Configuration de base

bash
git config --global user.name "Ton Nom"

- Définit ton nom d'utilisateur pour toutes les actions Git. Cela sera associé à chaque commit que tu fais.

bash
git config --global user.email "ton_email@example.com"

- Définit ton email pour toutes les actions Git, utilisé pour identifier qui fait les modifications.

## Initialisation et gestion du dépôt

bash
git init

- Crée un dépôt Git dans le répertoire actuel. Utilisé pour démarrer un projet avec Git.

bash
git clone <url>

- Copie un dépôt Git existant à partir d'une URL (comme un projet sur GitHub) sur ta machine.

bash
git remote add origin <url>

- Connecte ton dépôt local à un dépôt distant (souvent un dépôt GitHub). Utile après git init.

bash
git remote -v

- Liste les dépôts distants associés à ton projet local (utile pour voir si un dépôt distant est bien connecté).

## Vérification du statut et des modifications

bash
git status

- Affiche le statut actuel des fichiers : quels fichiers ont été modifiés, ajoutés ou sont prêts à être commités.

bash
git diff

- Montre les différences entre les fichiers modifiés mais non encore ajoutés au commit (non "staged").

bash
git log

- Affiche l'historique des commits avec les messages, auteurs et horodatages.

## Gestion des fichiers

bash
git add <fichier>

- Ajoute un fichier spécifique à l'index (état "staged") pour qu'il soit inclus lors du prochain commit.

bash
git add .

- Ajoute tous les fichiers modifiés dans l'index pour qu'ils soient inclus lors du prochain commit.

bash
git rm <fichier>

- Supprime un fichier du répertoire local *et* du dépôt (prêt pour le commit).

bash
git mv <ancien_nom> <nouveau_nom>

- Renomme un fichier et prépare ce changement pour le commit.

## Validation des modifications (Commit)

bash
git commit -m "Message du commit"

- Crée un commit avec un message décrivant les modifications. Un commit est un "point de sauvegarde" dans ton projet.

bash
git commit --amend

- Modifie le dernier commit (par exemple, pour changer le message ou ajouter des fichiers oubliés).

## Gestion des branches

bash
git branch

- Liste toutes les branches locales. Les branches sont comme des "versions parallèles" de ton projet.

bash
git branch <nom_de_branche>

- Crée une nouvelle branche pour développer des fonctionnalités ou corriger des bugs sans affecter la branche principale.

bash
git checkout <nom_de_branche>

- Bascule vers une autre branche, pour travailler dessus.

bash
git checkout -b <nom_de_branche>

- Crée une nouvelle branche *et* bascule dessus en une seule commande.

bash
git branch -d <nom_de_branche>

- Supprime une branche locale après avoir terminé le travail dessus (assure-toi qu'elle est fusionnée avant).

## Fusion des branches

bash
git merge <branche>

- Fusionne les modifications d'une branche dans la branche actuelle. Cela combine le travail fait dans différentes branches.

bash
git rebase <branche>

- Ré-applique les commits d'une branche par-dessus une autre branche. C'est une alternative à la fusion, mais cela garde un historique plus linéaire.

## Gestion des dépôts distants

bash
git fetch

- Récupère les modifications du dépôt distant *sans* les fusionner dans la branche actuelle.

bash
git pull

- Récupère les modifications du dépôt distant et les fusionne dans la branche actuelle (c'est un fetch + merge).

bash
git push

- Envoie les commits locaux vers le dépôt distant (comme GitHub).

bash
git push origin <branche>

- Pousse une branche spécifique vers le dépôt distant.

## Rebaser et interagir avec les commits

bash
git rebase -i <commit>

- Lance une rebase interactive pour réorganiser les commits (utile pour nettoyer l'historique ou fusionner des commits).

bash
git cherry-pick <commit>

- Applique un commit spécifique à la branche actuelle. C'est comme "copier" un commit d'une branche à une autre.

bash
git reset <commit>

- Réinitialise la branche actuelle à un commit spécifique (annule les commits faits après ce commit).

## Annuler et restaurer

bash
git reset --soft <commit>

- Réinitialise à un commit spécifique mais garde les modifications prêtes à être commitées (staged).

bash
git reset --hard <commit>

- Réinitialise à un commit spécifique *et* annule toutes les modifications non commitées.

bash
git checkout <fichier>

- Annule les modifications d'un fichier local pour revenir à son état d'origine (avant modification).

## Stash (sauvegarder temporairement les modifications)

bash
git stash

- Sauvegarde temporairement les modifications non commitées pour y revenir plus tard.

bash
git stash apply

- Réapplique les modifications sauvegardées par la commande git stash.

bash
git stash pop

- Réapplique les modifications sauvegardées et supprime la dernière entrée du stash.