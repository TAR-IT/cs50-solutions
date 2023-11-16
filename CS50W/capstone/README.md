
# Lyfetree (by TAR-IT for CS50 Web)

## Distinctiveness and Complexity

### Distinctiveness
My web application "Lyfetree" differs from the other projects of the course in that it is a kind of personal diary app in which users can display their "life accomplishments" in a tree-like structure.

Furthermore, the priority in this project is not the user experience, i.e. the front-end, but rather I tried to implement a "workflow" with the help of GitHub Actions, since this topic was only briefly touched upon in the lectures. Among other things, automated testing of views during a push was implemented using GitHub Actions. I changed the django settings/base dirs to fit my needs in this project and worked with enviromental variables using "pipenv" which adds to the complexity of the project.

I deliberately neglected the functionality of the user experience, as I wanted to focus more on CI/CD and simulating these processes in this project. The GitHub action tests turned out positive several times, so after these many hours of reading I am satisfied with the state of the project and plan a further execution in the follow-up.

### Complexity
The project demonstrates complexity in several ways:

1. **Enviromental Variables/Dependencies**: Using pipenv, i managed to create this project inside a python enviroment, where security variables are stored inside of an .env file. All dependencies for this project can be installed using "pipenv install" to then run the enviromental shell using "pipenv run".

2. **Database Models**: I've defined multiple database models, including [list the models you've created, e.g., Users, Posts, Comments], each with various fields, relationships, and constraints, making the database design complex.

3. **User Authentication**: I've implemented customized user authentication and registration using the build in Django User models and expanding them (e.g. with a profile picture).

4. **Interactive Features**: The application includes interactive features such as diary entries and user login, which require dynamic data handling and real-time updates.

5. **JavaScript and AJAX**: I've utilized JavaScript and AJAX extensively to create a seamless user experience, for instance, allowing users to post a diary entry.

6. **CSS Styling**: The design and layout are based on Bootstrap and further customized with a .css-file.

## Files Included

- `lyfetree/` - Contains the main application files, including Django settings.
- `journey/` - Contains the "user journey" model with all diary entries.
- `account/` - Contains all user models and everything related to user authentication (views etc.)
- `static/` - Holds static files like CSS, JavaScript, and images.
- `templates/` - Contains HTML templates for the application (including all apps).
- `workflows/` - Contains the .yml file of GitHub Actions.
- `manage.py` - Django management script.
- `README.md` - The file you're reading right now.
- `requirements.txt` - Lists Python packages that need to be installed to run the application.
- `Pipfile/Pipfile.lock` - The files used by "pipenv" to install dependencies using "pipenv install".
- `.env` - Contains environment variables like the security key and the debug mode setting.
- `.gitattributes/.gitignore` - GitHub configuration files for workflow/security.

## Running the Application

### Install and run via requirements.txt

1. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
2. Install the enviroment using pipenv:
   ```bash
   pipenv install
   ```
3. Make migrations:
   ```bash
   pipenv run python manage.py makemigrations
   pipenv run python manage.py migrate
   ```
4. Run the application:
   ```bash
   pipenv run python manage.py runserver
   ```
### Install and run via pipenv

1. Install the pipenv package:
   ```bash
   pip install pipenv
   ```
1. Install the enviroment using pipenv:
   ```bash
   pipenv install
   ```
2. Make migrations:
   ```bash
   pipenv run python manage.py makemigrations
   pipenv run python manage.py migrate
   ```
3. Run the application inside the enviroment:
   ```bash
    pipenv run python manage.py runserver
   ```