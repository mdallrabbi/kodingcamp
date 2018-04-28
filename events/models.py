import uuid
from django.db import models
from django.contrib.postgres.fields import JSONField
from django.core.files.storage import FileSystemStorage

# Create your models here.

FS = FileSystemStorage(location='')


class EventBasic(models.Model):
    uiqueidEVENTS = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    title = models.CharField(max_length=50)
    startDate = models.DateField(max_length=10)
    endDate = models.DateField(max_length=10)
    registrationDeadline = models.DateField(max_length=10)
    description = models.TextField(max_length=500)
    banner = models.ImageField(storage=FS)
    audienceType = JSONField()
    venue = JSONField()
    venueCoordinate = JSONField()
    region = JSONField()
    maxAudience = JSONField()
    cuurency = JSONField()
    regisTrationFee = models.FloatField(max_length=10)

    def __str__(self):
        return self.title


class EventDetail(models.Model):
    uniqueidEVENTS_EXTENDED = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    evntId = models.OneToOneField(EventBasic, on_delete=models.CASCADE)
    openForall = models.BooleanField(default=False)
    screeningProcess = models.URLField(max_length=50)
    registrationProcess = models.TextField(max_length=200)
    paymentProcess = models.URLField(max_length=50)
    additionalFees = models.FloatField(max_length=10)
    reviewEventHost = JSONField()

    def __str__(self):
        return self.title


class EventTrainer(models.Model):
    uniqueidTRAINER = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    allocatedEventID = models.ForeignKey(EventBasic, on_delete=models.CASCADE)
    #   trainerID = models.ForeignKey( {TRAINER_BUILD}, models.CASCADE)
    rating = JSONField()
    status = models.BooleanField(default=False)

    def __str__(self):
        #   return self.trainerID
        return self.title


class EventParticipant(models.Model):
    uniqueidPARTICIPANT = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    #   participantID = models.ForeignKey()
    eventID = models.ForeignKey(EventBasic, on_delete=models.CASCADE)
    isSelectionPass = models.BooleanField(default=False)
    paymentConfirmed = models.BooleanField(default=False)
    registrationComplete = models.BooleanField(default=False)
    statusParticipant = models.BooleanField(default=False)
    reviewParticipant = JSONField()
    ratingParticipant = JSONField()
    confirmationText = JSONField()

    def __str__(self):
        #   return self.participantID
        return self.title


import uuid
from django.db import models
from django.contrib.postgres.fields import JSONField
from django.core.files.storage import FileSystemStorage

# Create your models here.

FS = FileSystemStorage(location='')


class EventBasic(models.Model):
    uiqueidEVENTS = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    title = models.CharField(max_length=50)
    startDate = models.DateField(max_length=10)
    endDate = models.DateField(max_length=10)
    registrationDeadline = models.DateField(max_length=10)
    description = models.TextField(max_length=500)
    banner = models.ImageField(storage=FS)
    audienceType = JSONField()
    venue = JSONField()
    venueCoordinate = JSONField()
    region = JSONField()
    maxAudience = JSONField()
    cuurency = JSONField()
    regisTrationFee = models.FloatField(max_length=10)

    def __str__(self):
        return self.title


class EventDetail(models.Model):
    uniqueidEVENTS_EXTENDED = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    evntId = models.OneToOneField(EventBasic, on_delete=models.CASCADE)
    openForall = models.BooleanField(default=False)
    screeningProcess = models.URLField(max_length=50)
    registrationProcess = models.TextField(max_length=200)
    paymentProcess = models.URLField(max_length=50)
    additionalFees = models.FloatField(max_length=10)
    reviewEventHost = JSONField()

    def __str__(self):
        return self.title


class EventTrainer(models.Model):
    uniqueidTRAINER = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    allocatedEventID = models.ForeignKey(EventBasic, on_delete=models.CASCADE)
    #   trainerID = models.ForeignKey( {TRAINER_BUILD}, models.CASCADE)
    rating = JSONField()
    status = models.BooleanField(default=False)

    def __str__(self):
        #   return self.trainerID
        return self.title


class EventParticipant(models.Model):
    uniqueidPARTICIPANT = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    #   participantID = models.ForeignKey()
    eventID = models.ForeignKey(EventBasic, on_delete=models.CASCADE)
    isSelectionPass = models.BooleanField(default=False)
    paymentConfirmed = models.BooleanField(default=False)
    registrationComplete = models.BooleanField(default=False)
    statusParticipant = models.BooleanField(default=False)
    reviewParticipant = JSONField()
    ratingParticipant = JSONField()
    confirmationText = JSONField()

    def __str__(self):
        #   return self.participantID
        return self.title

