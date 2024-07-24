from django.core.management.base import BaseCommand
from userapp.models import Author, Post


class Command(BaseCommand):
    help = 'Generate fake authors and posts'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Quantity fake users and x10 posts of them')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            author = Author(name=f'Name{i}', email=f'email{i}@mail.com')
            author.save()
            for j in range(1, count + 1):
                post = Post(
                    title=f'Text{j}',
                    content=f'Text from {author.name} #{j} is bla bla text',
                    author=author
                )
                post.save()
