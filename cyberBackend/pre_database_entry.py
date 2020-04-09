import os
import django

if __name__ == '__main__' and __package__ is None:
    os.sys.path.append(
        os.path.dirname(
            os.path.dirname(
                os.path.abspath(__file__))))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cyberBackend.settings")
django.setup()

from users.models import UsersRole

def create_user_role():
    UsersRole.objects.get_or_create(name='Admin')
    UsersRole.objects.get_or_create(name='Professors')
    UsersRole.objects.get_or_create(name='Student')


create_user_role()
