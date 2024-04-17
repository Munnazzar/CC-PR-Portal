from django.contrib.auth.models import AbstractUser

from mongoengine import Document, StringField, BooleanField, DateTimeField, IntField

class DevDayAttendance(Document):
    consumerNumber = StringField(required=True)
    Team_Name = StringField(required=True)
    Leader_name = StringField(required=True)
    Leader_email = StringField(required=True)
    mem1_name = StringField(default="")
    mem1_email = StringField(default="")
    mem2_name = StringField(default="")
    mem2_email = StringField(default="")
    mem3_name = StringField(default="")
    mem3_email = StringField(default="")
    mem4_name = StringField(default="")
    mem4_email = StringField(default="")
    att_code = StringField(required=True)
    Competition = StringField(required=True)


class Event(Document):
    competitionName = StringField(required=True)
    start_time = DateTimeField(required=True)
    end_time = DateTimeField(required=True)


class Attendance(Document):
    teamName = StringField(required=True)
    attendanceStatus = BooleanField(default=False)


class User(AbstractUser):
    pass
