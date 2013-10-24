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
    description = models.TextField()
    fb_url = models.URLField(null=True, blank=True)

    # Some student groups we scrape aren't too active
    is_active = models.BooleanField(default=True)

    p_contact_name = models.CharField(max_length=100, null=True, blank=True)
    p_contact_email = models.EmailField(null=True, blank=True)

    def __unicode__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=100)
    time = models.DateTimeField()
    location = models.CharField(max_length=100)
    group = models.ForeignKey(Group)

    def __unicode__(self):
        return 'Event %s held by %s' % (self.name, self.group.name)

