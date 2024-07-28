from django.core.management.base import BaseCommand
from tmpltapp.models import Author, Post
from random import choices

LOREM = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aliquam beatae cum debitis ' \
        'deserunt eius fuga hic numquam quis, quisquam soluta, sunt veritatis vero voluptatem. ' \
        'Aperiam atque eum exercitationem expedita illum itaque, maxime nesciunt nobis obcaecati ' \
        'odit pariatur provident quam quia quo quod, ratione repellat, repudiandae vel. ' \
        'Accusantium aliquid delectus dolorum, eaque eligendi error esse possimus quod sint ' \
        'temporibus. Aperiam cupiditate impedit laboriosam non optio quibusdam reiciendis ' \
        'repellendus reprehenderit veniam vero? Aliquid, amet blanditiis cum deserunt dicta ' \
        'dolorem exercitationem fuga fugit hic itaque libero maxime minima, nobis porro praesentium ' \
        'qui repudiandae, rerum saepe sequi sunt tempore temporibus totam ullam? Dolore, error?'


class Command(BaseCommand):
    help = 'Generate fake authors and posts.'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        text = LOREM.split()
        count = kwargs.get('count')
        for i in range(1, count + 1):
            author = Author(name=f'Author_{i}', email=f'mail{i}@mail.ru')
            author.save()
            for j in range(1, count + 1):
                post = Post(
                    title=f'Title-{j}',
                    content=' '.join(choices(text, k=64)),
                    author=author
                )
                post.save()
