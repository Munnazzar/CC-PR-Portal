from django.contrib.auth.models import AbstractUser

from mongoengine import Document, StringField, BooleanField, DateTimeField


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
    attendance = BooleanField(default=False)


class Event(Document):
    competitionName = StringField(required=True)
    start_time = DateTimeField(required=True)
    end_time = DateTimeField(required=True)


class User(AbstractUser):
    pass


competitions = {
    "all_competitions": "all_competitions",
    "Capture The Flag": "CF",
    "Competitive Programming": "CP",
    "Query Quest": "QQ",
    "Code in Dark": "CD",
    "PsuedoWar": "PW",
    "Speed Debugging": "SD",
    "UI/UX Design": "UX",
    "Data Visualization": "DV",
    "Web Dev": "WD",
    "Data Science": "DS",
    "SyncOS Challenge": "SO",
    "Code Sprint": "CS",
    "Photography": "PH",
    "Reels competition": "RE",
    "Board games": "BG",
    "Scavenger hunt": "SH",
    "Fast Stock Exchange": "FS",
    "Line Following Robot (LFR) Competition": "LF",
    "Robo Soccer Competition": "RS",
    "Counter-Strike 2 (CS2)": "C2",
    "Sketching Competition": "SK",
    "Quiz competition": "QC",
    "Scrabble": "SC",
    "Chess": "CH",
    "Ludo": "LD",
}


def get_competition_name(competition_code):
    print(competition_code)
    for name, code in competitions.items():
        if code == competition_code:
            return name
    return None
