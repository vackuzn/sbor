#!/bin/bash

# Settings
BASE_FOLDER=~
HOST_FOLDER="$BASE_FOLDER/public_html"
VENV_FOLDER="$BASE_FOLDER/venvs/prod"
TEMP_REPO_FOLDER="/tmp/deploy"
PROJECT_FOLDER="internet_shop"
BRANCH_NAME=${1:-master}

# Functions
print () {
	echo
	echo $1
}

# Main code
print "Recreating virtual environment and activating it..."
rm -rf $VENV_FOLDER
python3 "$BASE_FOLDER/virtualenv/virtualenv.py" $VENV_FOLDER
source $VENV_FOLDER/bin/activate

print "Cloning repo, branch $BRANCH_NAME"
rm -rf $TEMP_REPO_FOLDER
git clone -b $BRANCH_NAME https://github.com/o-seer/sbormarket.git $TEMP_REPO_FOLDER

print "Installing dependencies"
pip install -r $TEMP_REPO_FOLDER/requirements.txt

print "Cleanup of existing installation"
cd $HOST_FOLDER
rm -rf $PROJECT_FOLDER

print "Copying new files"
mv $TEMP_REPO_FOLDER/$PROJECT_FOLDER .

cd internet_shop
print "Running collectstatic"
python manage.py collectstatic --noinput
print "Applying migrations"
python manage.py migrate

print "Cleanup"
cd ~
rm -rf $TEMP_REPO_FOLDER
deactivate
