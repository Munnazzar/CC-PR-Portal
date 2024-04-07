from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from bson import ObjectId
import json
from django.shortcuts import HttpResponse
from .models import DevDayAttendance, Attendance, Event
from datetime import datetime
from django.contrib.auth.decorators import login_required


@api_view(["GET"])
@login_required(login_url="portal:login-page")
def get_time(request):
    query = Event.objects.all()
    data = []
    for record in query:
        record_dict = record.to_mongo().to_dict()
        for key, value in record_dict.items():
            if isinstance(value, datetime):
                record_dict[key] = str(value)[11:16]
            if isinstance(value, ObjectId):
                record_dict[key] = str(value)
        data.append(record_dict)
    return Response(data, status=status.HTTP_200_OK)


@api_view(["GET"])
@login_required(login_url="portal:login-page")
def search_schedule(request, competitionName):
    search_query = competitionName
    if search_query != "all_competitions":
        records = Event.objects.filter(competitionName__icontains=search_query)
    else:
        records = Event.objects.all()

    data = []
    for record in records:
        record_dict = record.to_mongo().to_dict()
        for key, value in record_dict.items():
            if isinstance(value, datetime):
                record_dict[key] = str(value)[11:16]
            if isinstance(value, ObjectId):
                record_dict[key] = str(value)
        data.append(record_dict)
    return Response(data, status=status.HTTP_200_OK)


@api_view(["POST"])
@login_required(login_url="portal:login-page")
def update_time(request):
    data = request.data
    competitionName = data["competition"]
    startTime = data["startTime"]
    endTime = data["endTime"]

    if startTime >= endTime:
        return Response(
            {"Status": "Start time must be less than end time."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        startTime = datetime.strptime(startTime, "%H:%M")
        endTime = datetime.strptime(endTime, "%H:%M")

        compObj = Event.objects.get(competitionName=competitionName)
        date = compObj.start_time.date()

        compObj.start_time = datetime.combine(date, startTime.time())
        compObj.end_time = datetime.combine(date, endTime.time())
        compObj.save()
        return Response(
            {"Status": "Successsfullyy updated"},
            status=status.HTTP_200_OK,
        )
    except:
        return Response(
            {"Status": "Error occurred changing time."},
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(["GET"])
@login_required(login_url="portal:login-page")
def get_rec(request):
    query = DevDayAttendance.objects.all()
    data = []
    for record in query:
        record_dict = record.to_mongo().to_dict()
        for key, value in record_dict.items():
            if isinstance(value, ObjectId):
                record_dict[key] = str(value)
        team_name = record_dict["Team_Name"]
        try:
            AttendanceObj = Attendance.objects.get(teamName=team_name)
            record_dict["attendance"] = AttendanceObj.attendanceStatus
        except:
            record_dict["attendance"] = False
        data.append(record_dict)
    return Response(data, status=status.HTTP_200_OK)


@api_view(["GET"])
@login_required(login_url="portal:login-page")
def record_search(request, competitionName, searchValue):
    search_query = searchValue
    competition_query = competitionName

    if search_query != "all":
        if competition_query == "all_competitions":
            records = DevDayAttendance.objects.filter(Team_Name__icontains=search_query)
        else:
            records = DevDayAttendance.objects.filter(
                Team_Name__icontains=search_query, Competition=competition_query
            )
    else:
        if competition_query == "all_competitions":
            records = DevDayAttendance.objects.all()
        else:
            records = DevDayAttendance.objects.filter(Competition=competition_query)
    data = []
    for record in records:
        record_dict = record.to_mongo().to_dict()
        for key, value in record_dict.items():
            if isinstance(value, ObjectId):
                record_dict[key] = str(value)
        team_name = record_dict["Team_Name"]
        try:
            AttendanceObj = Attendance.objects.get(teamName=team_name)
            record_dict["attendance"] = AttendanceObj.attendanceStatus
        except:
            record_dict["attendance"] = False
        data.append(record_dict)
    return Response(data, status=status.HTTP_200_OK)


@api_view(["POST"])
@login_required(login_url="portal:login-page")
def mark(request):
    received_data = request.data
    status = received_data["status"]
    team_name = received_data["team"]

    if status == "present":
        attendance = True
    else:
        attendance = False
    try:
        attendanceObj = Attendance.objects.get(teamName=team_name)
        attendanceObj.attendanceStatus = attendance
        attendanceObj.save()
    except Attendance.DoesNotExist:
        attendanceObj = Attendance(teamName=team_name, attendanceStatus=attendance)
        attendanceObj.save()
    return Response({"Status": "Successsfully updated"})
