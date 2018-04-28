from datetime import datetime, date

from django.db import models
from django.contrib.auth.models import User


##### Managers Start ######
class UserQueryset(models.QuerySet):
    def regular_user(self):
        return self.filter(is_trainer=False)

    def trainer(self):
        return self.filter(is_trainer=True)


class UserManager(models.Manager):
    def get_queryset(self):
        return UserQueryset(self.model, using=self._db)

    def regular_user(self):
        return self.get_queryset().regular_user()

    def trainer(self):
        return self.get_queryset().trainer()
    
    def experience_of(self, months):
        return self.get_queryset().trainer().filter(experience=months)
##### Managers End ######


class BaseUserProfile(models.Model):
    auth = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, help_text="user's full name")
    email = models.EmailField()
    contact = models.CharField(max_length=11)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.id:
            self.updated_at = datetime.now()
        super(BaseUserProfile, self).save(*args, **kwargs)


class IndividualUser(BaseUserProfile):
    date_of_birth = models.DateField()
    is_trainer = models.BooleanField(default=False)
    experience = models.IntegerField(help_text='experience in months', default=0)
    objects = models.Manager()
    user = UserManager()

    @property
    def age(self):
        return (date.today() - self.date_of_birth).days

    def __str__(self):
        return self.auth.username


class OrganizationUser(BaseUserProfile):
    is_training_institute = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)
