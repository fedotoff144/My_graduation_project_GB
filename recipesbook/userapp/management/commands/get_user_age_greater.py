from django.core.management.base import BaseCommand
from userapp.models import User


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('age', type=int, help='User age')

    def handle(self, *args, **kwargs):
        age = kwargs['age']
        user = User.objects.filter(age__gt=age)
        self.stdout.write(f'{user}')
