from django.contrib.auth.models import AbstractUser

from mongoengine import Document, StringField, BooleanField, DateTimeField, IntField

class DevDayAttendance(Document):
    consumerNumber = StringField(required=True)
    Team_Name = StringField(required=True)
    Leader_name = StringField(required=True)
    Leader_email = StringField(required=True)
    Leader_whatsapp_number = StringField(required=True)
    Leader_cnic = StringField(required=True)
    mem1_name = StringField(required=True)
    mem1_email = StringField(required=True)
    mem1_whatsapp_number = StringField(required=True)
    mem1_cnic = StringField(required=True)
    mem2_name = StringField(required=True)
    mem2_email = StringField(required=True)
    mem2_whatsapp_number = StringField(required=True)
    mem2_cnic = StringField(required=True)
    mem3_name = StringField()
    mem3_email = StringField()
    mem3_whatsapp_number = StringField()
    mem3_cnic = StringField()
    mem4_name = StringField()
    mem4_email = StringField()
    mem4_whatsapp_number = StringField()
    mem4_cnic = StringField()
    fees_amount = IntField(required=True)
    paid = BooleanField(required=True, default=False)  # Assigning a default value as per your document
    reference_code = StringField(required=True)
    Competition = StringField(required=True)
    Competition_id = StringField(required=True)
    Competition_type = StringField(required=True)


class Event(Document):
    competitionName = StringField(required=True)
    start_time = DateTimeField(required=True)
    end_time = DateTimeField(required=True)


class Attendance(Document):
    teamName = StringField(required=True)
    attendanceStatus = BooleanField(default=False)


class User(AbstractUser):
    pass
