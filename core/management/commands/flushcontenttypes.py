from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = (
        "Delete `ContentType` objects from database, including those related to it like `Permission`."
    )

    def handle(self, *app_labels, **options):
        content_types = ContentType.objects.all()
        messages = content_types.delete()
        print(messages)
