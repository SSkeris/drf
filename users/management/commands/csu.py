from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email="admin@123.qwe",
            is_staff=True,
            is_superuser=True,
        )

        user.set_password("123qwe")
        user.save()
