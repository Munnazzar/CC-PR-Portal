from django.contrib.auth.models import AbstractUser

from mongoengine import Document, StringField, BooleanField, DateTimeField


class DevDayAttendence(Document):
    comp_name = StringField(required=True)
    team_name = StringField(required=True)
    leader_name = StringField(required=True)
    leader_phone = StringField(required=True)
    leader_cnic = StringField(required=True)
    leader_email = StringField(required=True)
    p1_name = StringField(required=True)
    p1_phone = StringField(required=True)
    p1_cnic = StringField(required=True)
    p1_email = StringField(required=True)
    p2_name = StringField(required=True)
    p2_phone = StringField(required=True)
    p2_cnic = StringField(required=True)
    p2_email = StringField(required=True)
    reference_code = StringField(required=True)
    att_code = StringField(required=True)


class Event(Document):
    competitionName = StringField(required=True)
    start_time = DateTimeField(required=True)
    end_time = DateTimeField(required=True)


class Attendance(Document):
    teamName = StringField(required=True)
    attendanceStatus = BooleanField(default=False)


class User(AbstractUser):
    pass
