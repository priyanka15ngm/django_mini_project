kritarthgram is an Instagram clone built using Django, Bootstrap, and jQuery. I recreated many of Instagrams features including: CRUD capabilties on posts, explore page, likes, comments, direct messaging, profiles, profiles pictures, bios, search bar, and followers/following categories. I used Bootstrap to recreate the UX of instagrams desktop page that changes for mobile use. jQuery is used to make real-time like/follower/following updates using AJAX calls.

Check out the website at (https://kritarthgram.herokuapp.com/)
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

python

then

from django.utils.crypto import get_random_string

then

chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'

then

get_random_string(50, chars)

and then

quit()

    Copy this result and in your settings.py file replace

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

with

SECRET_KEY = 'generated key'

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

Unit Tests

I have a handful of unit tests written for testing messages and posts.

class MessageTestCase(TestCase):

    def create_message(self, sender=User.objects.get(id=1), receiver=User.objects.get(id=2), content='test message'):
        return Message.objects.create(sender=sender, receiver=receiver, content=content, date_created=timezone.now())
    
    def test_message_creation(self):
        message = self.create_message()
        self.assertTrue(isinstance(message, Message))
        self.assertEqual(message.__str__(), message.content)

Deployment

kritarthgram is deployed on Heroku.
Built With

    Django - The web framework used
    Bootstrap - Frontend html/css classes
    jQuery - Used for AJAX calls
    Heroku - Used for deployment
