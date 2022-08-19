#!/bin/bash

# récupérer la branche courrante et push
current_branch=$(git branch | sed -n -e 's/^\* \(.*\)/\1/p')

# git pull
git pull origin "$current_branch"
#echo "> pull changé dans la branche '$current_branch'"

# récuperer le message passé en argument
message="$1"

# ajouter tous les changements
git add .
echo "> Tous les fichiers sont ajoutés."

# ajouter le commit avec le message
git commit -m "$message"
echo "> Commit ajouté avec le message: '$message'"

# git push
git push origin "$current_branch"
echo "> Changement poussé sur la branche '$current_branch'"
