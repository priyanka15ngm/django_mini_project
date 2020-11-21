# caseygram
caseygram is an Instagram clone built using Django, Bootstrap, and jQuery. I recreated many of Instagrams features including: CRUD capabilties on posts, explore page, likes, comments, direct messaging, profiles, profiles pictures, bios, search bar, and followers/following categories. I used Bootstrap to recreate the UX of instagrams desktop page that changes for mobile use. jQuery is used to make real-time like/follower/following updates using AJAX calls. 

Check out the website at (https://caseygram.herokuapp.com/)
## Getting Started

1. Open up Terminal, and go into the directory where you want Caseygram to run

```
cd projects
```
2. Download a copy
```
git clone https://github.com/cdelange/caseygram.git
```
3. Install a virtual environment
```
pip install virtualenv
```
4. Make a folder for your virtual environments e.g.
```
mkdir ~/venvs
```

5. Make a new virtual environment for this project
```
virtualenv --system-site-packages ~/venvs/caseygram
```

6. Start the virtual environment
```
source ~/venvs/caseygram/bin/activate
```

7. Generate a secret key for your django app using
```
python
```
  **then**
```
from django.utils.crypto import get_random_string
```
  **then**
```
chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
```
  **then**
```
get_random_string(50, chars)
```
  **and then**
```
quit()
```

8. Copy this result and in your caseygram/caseygram/settings.py file replace
```
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
```
  **with**
```
SECRET_KEY = 'generated key'
```

9. Go into the directory containing 'requirements.txt'
```
cd caseygram
```

10. Install the Python requirements
```
pip install -r requirements.txt
```

11. Make migrations to set up the database
```
python manage.py makemigrations
```

12. 
Then run these migrations
```
python manage.py migrate
```

13. Create a user profile to login with
```
python manage.py createsuperuser
```

14. Once you have followed the instructions to create a user, run the server
```
python manage.py runserver
```

15. Now go to http://localhost:8000/ in your browser to view caseygram



## Unit Tests

I have a handful of unit tests written for testing messages and posts.
```
class MessageTestCase(TestCase):

    def create_message(self, sender=User.objects.get(id=1), receiver=User.objects.get(id=2), content='test message'):
        return Message.objects.create(sender=sender, receiver=receiver, content=content, date_created=timezone.now())
    
    def test_message_creation(self):
        message = self.create_message()
        self.assertTrue(isinstance(message, Message))
        self.assertEqual(message.__str__(), message.content)
```

## Deployment

caseygram is deployed on Heroku.

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [Bootstrap](https://getbootstrap.com/) - Frontend html/css classes
* [jQuery](https://jquery.com/) - Used for AJAX calls
* [Heroku](https://www.heroku.com/) - Used for deployment

## Authors

* **Casey DeLange** - [cdelange](https://github.com/cdelange)


## Additional Plans
* Add more infinite scroll capabilities
* Use AWS Lambda to resize my current S3 bucket images to smaller formats
* Fix notification server error with comment deletion
* alternate new account image so there is not 100 of the same image.
* formatting the comment system to not spill over the container
* comment text field on image page. and use ajax to submit comment and update in real time
