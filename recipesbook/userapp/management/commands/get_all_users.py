from django.core.management.base import BaseCommand
from userapp.models import User


class Command(BaseCommand):
    help = 'Get all users from DB.'

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        self.stdout.write(f'{users}')
