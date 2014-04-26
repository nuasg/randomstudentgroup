import random
from django.db import models

class GroupManager(models.Manager):
    def random(self):
        count = self.aggregate(models.Max('id'))['id__max']
        if not count:
            return None
        return self.get(pk=random.randint(1, count))

class Group(models.Model):
    objects = GroupManager()
    name = models.CharField(max_length=100)
    summary = models.TextField(null=True)
    description = models.TextField(null=True)
    webpage = models.URLField(null=True, blank=True)
    fb_url = models.URLField(null=True, blank=True)
    twitter_url = models.URLField(null=True, blank=True)

    group_type = models.TextField(null=True)

    # Some student groups we scrape aren't too active
    # or we don't want to display them because they're dorms
    is_active = models.BooleanField(default=True)

    p_contact_name = models.CharField(max_length=100, null=True, blank=True)
    p_contact_email = models.EmailField(null=True, blank=True)

    def __unicode__(self):
        return self.name

