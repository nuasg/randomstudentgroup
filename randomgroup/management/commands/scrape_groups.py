from django.core.management.base import BaseCommand, CommandError
from randomgroup.models import Group

class Command(BaseCommand):
    """Scrape the groups from Wildcat Connection. 
    In the future, this should be changed to use the API."""
    print "Does nothing."
    pass
