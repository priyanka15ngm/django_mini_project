kritarthgram is an Instagram clone built using Django, Bootstrap, and jQuery. I recreated many of Instagrams features including: CRUD capabilties on posts, explore page, likes, comments, direct messaging, profiles, profiles pictures, bios, search bar, and followers/following categories. I used Bootstrap to recreate the UX of instagrams desktop page that changes for mobile use. jQuery is used to make real-time like/follower/following updates using AJAX calls.

Check out the website at (https://kritarthgram2.herokuapp.com/)
Getting Started

    Open up Terminal, and go into the directory where you want Kritarthgram to run

cd projects

    Download a copy

git clone https://github.com/priyanka15ngm/django_mini_project.git

    Install a virtual environment

pip install virtualenv

    Make a folder for your virtual environments e.g.

mkdir ~/venvs

    Make a new virtual environment for this project

    Start the virtual environment

    Generate a secret key for your django app using


    Go into the directory containing 'requirements.txt'

    Install the Python requirements

pip install -r requirements.txt

    Make migrations to set up the database

python manage.py makemigrations

Then run these migrations

python manage.py migrate

    Create a user profile to login with

python manage.py createsuperuser

    Once you have followed the instructions to create a user, run the server

python manage.py runserver

    Now go to http://localhost:8000/ in your browser to view kritarthgram


Deployment

kritarthgram is deployed on Heroku.
Built With

    Django - The web framework used
    Bootstrap - Frontend html/css classes
    jQuery - Used for AJAX calls
    Heroku - Used for deployment
