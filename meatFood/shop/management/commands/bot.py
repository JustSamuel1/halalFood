from django.core.management.base import BaseCommand
from shop.bot import bot


class Command(BaseCommand):
    help = 'Telegram bot command'

    def handle(self, *args, **kwargs):
        bot.main()
