from django.core.management.base import BaseCommand
from userapp.models import User


class Command(BaseCommand):
    help = 'Create new user.'

    def handle(self, *args, **kwargs):
        user = User(name='John', email='john@example.com', password='secret', age=20)
        user.save()
        self.stdout.write(f'{user}')
