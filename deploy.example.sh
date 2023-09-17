#!/bin/bash

rsync_rsa_keyname='rsa-keyname'
rsync_user='host-user'
rsync_host='host-ip'
rsync_port='host-port'
rsync_directory='deployments/adituu.dev/'

read -p "Are you sure you want to sync these files? (y/n) " sync_option
if [ $sync_option != "y" ]; then
    echo "Exiting.."
    exit
fi

echo " "
echo "~~ Syncing.. ~~"
echo " "

rsync -avz -e "ssh -p $rsync_port -o StrictHostKeyChecking=no -i ~/.ssh/$rsync_rsa_keyname" \
--progress --exclude '__pycache__/' --exclude 'deploy.sh' --exclude '.env' --exclude 'log/' --exclude '.vscode/' \
--exclude '.venv/' --exclude '.gitignore' --exclude '.git/' --exclude 'deploy.example.sh' --exclude 'README.md' \
--exclude '.env.example' ./ $rsync_user@$rsync_host:/home/$rsync_user/$rsync_directory
