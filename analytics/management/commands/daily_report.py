__author__ = 'chitrankdixit'
from django.core.management.base import BaseCommand, CommandError
# from analytics.models import TrackingSourceDetailsDaily, TrackingSourceDetailsLog
# from datetime import datetime


class Command(BaseCommand):
    help = 'Hahaha'

    def handle(self, *args, **options):

        # today_datetime = datetime.now()
        # tracking_log = TrackingSourceDetailsLog.objects.filter(event_date=today_datetime.strftime("%Y-%m-%d"))
        # import pdb; pdb.set_trace()


        self.stdout.write('THis is working fine now %s' % self.help)

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_id', nargs='+', type=int)
    #
    # def handle(self, *args, **options):
    #     for poll_id in options['poll_id']:
    #         try:
    #             daily_report = TrackingSourceDetailsLog.objects.get(pk=poll_id)
    #         except Poll.DoesNotExist:
    #             raise CommandError('Poll "%s" does not exist' % poll_id)
    #
    #         poll.opened = False
    #         poll.save()
    #
    #         self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))

