import hashlib
import json
import requests
import time
import uuid
from django.core.management.base import BaseCommand, CommandError
from randomgroup.models import Group


def get_orgs(page=None):
    current_time = str(int(time.time()*1000))
    public_key = 'northwestern-07'
    random_string = str(uuid.uuid4())
    private_key = os.environ['WC_PRIVATE_KEY']
    hash_val = hashlib.md5(public_key + current_time +\
                           random_string + private_key).hexdigest()

    api_url = 'https://northwestern.collegiatelink.net/api/'
    resource = 'organizations'
    params = {
        'time': current_time,
        'apikey': public_key,
        'random': random_string,
        'hash': hash_val
    }
    if page:
        params['page'] = page

    response = requests.get(api_url + resource, params=params)
    return json.loads(response.text)

class Command(BaseCommand):
    """Scrape the groups from Wildcat Connection. 
    In the future, this should be changed to use the API."""

    def handle(self, *args, **options):
        first_page = get_orgs()
        orgs = first_page['items']
        num_pages = first_page['totalPages']
        for page in range(2, num_pages+1):
            orgs += get_orgs(page)['items']

        # Store organizations
        for org in orgs:
            group, created = Group.objects.get_or_create(name=org['name'],
                                defaults={'description': org['description']})
            if created:
                group.summary = org['summary']
                group.webpage = org['externalWebsite']
                group.fb_url = org['facebookUrl']
                group.twitter_url = org['facebookUrl']
                group.group_type = org['typeName']
                group.p_contact_name = org['primaryContactName']
                group.p_contact_email = org['primaryContactCampusEmail']
                group.save()

        print 'Total number of groups:', Group.objects.count()




