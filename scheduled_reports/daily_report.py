from django.core.management.base import BaseCommand, CommandError
from analytics.models import TrackingSourceDetailsDaily, TrackingSourceDetailsLog

class Command(BaseCommand):
    help = 'Create daily report taking the reports created today'


    # def add_arguments(self, parser):
    #     parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        # for poll_id in options['poll_id']:
        #     try:
        #         poll = Poll.objects.get(pk=poll_id)
        #     except Poll.DoesNotExist:
        #         raise CommandError('Poll "%s" does not exist' % poll_id)
        #
        #     poll.opened = False
        #     poll.save()

        self.stdout.write(self.style.SUCCESS('This command is for:  "%s"' % help))
