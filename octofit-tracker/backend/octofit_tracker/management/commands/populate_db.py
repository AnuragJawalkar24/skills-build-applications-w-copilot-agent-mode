from django.core.management.base import BaseCommand
from octofit_tracker.models import Team, User, Activity, Workout, Leaderboard
from django.utils import timezone
from djongo import connection

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Deleting old data...'))
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Creating teams...'))
        marvel = Team.objects.create(name='Marvel', universe='Marvel')
        dc = Team.objects.create(name='DC', universe='DC')

        self.stdout.write(self.style.SUCCESS('Creating users...'))
        users = [
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc),
        ]

        self.stdout.write(self.style.SUCCESS('Creating activities...'))
        for user in users:
            Activity.objects.create(user=user, type='Running', duration=30, date=timezone.now().date())
            Activity.objects.create(user=user, type='Cycling', duration=45, date=timezone.now().date())

        self.stdout.write(self.style.SUCCESS('Creating workouts...'))
        Workout.objects.create(name='Strength Training', description='Full body workout', suggested_for='strength')
        Workout.objects.create(name='Cardio Blast', description='High intensity cardio', suggested_for='cardio')

        self.stdout.write(self.style.SUCCESS('Creating leaderboard...'))
        Leaderboard.objects.create(team=marvel, points=100, week='2025-W49')
        Leaderboard.objects.create(team=dc, points=90, week='2025-W49')

        self.stdout.write(self.style.SUCCESS('Ensuring unique index on email field...'))
        with connection.cursor() as cursor:
            cursor.db_conn['user'].create_index('email', unique=True)

        self.stdout.write(self.style.SUCCESS('Database populated with test data!'))
