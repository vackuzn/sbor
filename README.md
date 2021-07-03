# Configure dev environment


### Init git project
1. Clone project
2. Copy and rename `config.json.example` to `config.json` in the project root
3. `cd` to internet_shop subfolder
4. Init and activate virtual environment `virtualenv venv` `source venv/Scripts/activate`
5. Install requirements `pip install -r ../requirements.txt`
6. Make migrations and migrate `python manage.py makemigrations` `python manage.py migrate`
7. Optionally enable superuser account `python manage.py createsuperuser` see more here https://docs.djangoproject.com/en/1.8/intro/tutorial02/
8. Open internet_shop subfolder with PyCharm and configure Django project
