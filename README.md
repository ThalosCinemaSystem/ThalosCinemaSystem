# ThalosCinemaSystem ([thalos.software](https://thalospublic.azurewebsites.net/))

# Start working on this project 
```bash
git clone https://github.com/ThalosCinemaSystem/ThalosCinemaSystem.git
cd ThalosCinemaSystem
```
### Windows
```bash
python -m venv env
source env/Scripts/activate
pip install -r requirements_windows.txt
```
### Linux
```bash
python3.9 -m venv env
source env/bin/activate
pip install -r requirements_linux.txt
```
## Next steps
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
## Go to browser
http://127.0.0.1:8000/


