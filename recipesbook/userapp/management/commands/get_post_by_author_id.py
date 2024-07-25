from django.core.management.base import BaseCommand
# 1 variant
# from userapp.models import Author, Post
from userapp.models import Post


class Command(BaseCommand):
    help = 'Get all posts by author.'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')

    # 1 variant
    # def handle(self, *args, **kwargs):
    #     pk = kwargs.get('pk')
    #     author = Author.objects.filter(pk=pk).first()
    #     if author is not None:
    #         posts = Post.objects.filter(author=author)
    #         intro = f'All posts of {author.name}\n'
    #         text = '\n'.join(post.content for post in posts)
    #         self.stdout.write(f'{intro}{text}')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        posts = Post.objects.filter(author__pk=pk)
        intro = f'All posts:\n'
        text = '\n'.join(post.get_summary() for post in posts)
        self.stdout.write(f'{intro}{text}')
