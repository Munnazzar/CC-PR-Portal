from rest_framework.response import Response
from rest_framework.decorators import api_view
from bson import ObjectId 
import json
from django.shortcuts import HttpResponse
from .models import DevDayAttendence,Attendance,Event
from datetime import datetime
@api_view(['GET'])
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
    return HttpResponse(json.dumps(data), content_type="application/json")

@api_view(['POST'])
def post_search_schedule(request):
    search_query = request.data.get('search')
    if search_query is not None:
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
    return HttpResponse(json.dumps(data), content_type="application/json")

@api_view(['POST'])
def update_time(request):
    data = request.data
    competitionName = data['competition']  
    startTime= data['startTime']
    endTime= data['endTime']
    
    try:
        startTime= datetime.strptime(startTime, '%H:%M')
        endTime= datetime.strptime(endTime, '%H:%M')

        compObj = Event.objects.get(competitionName=competitionName)
        date= compObj.start_time.date()

        compObj.start_time= datetime.combine(date, startTime.time())
        compObj.end_time= datetime.combine(date, endTime.time())
        compObj.save()
        return Response({'Status':"Successsfullyy updated"})
    except:
        return Response({'Status':"Error occured changing time"})
    

@api_view(['GET'])
def get_rec(request):    
    query = DevDayAttendence.objects.all()
    data = []
    for record in query:
        record_dict = record.to_mongo().to_dict()
        for key, value in record_dict.items():
            if isinstance(value, ObjectId):
                record_dict[key] = str(value)
        team_name= record_dict["team_name"]
        try:
            AttendanceObj= Attendance.objects.get(teamName=team_name)
            record_dict["attendance"]= AttendanceObj.attendanceStatus
        except:
            record_dict["attendance"]= False
        data.append(record_dict)
    return HttpResponse(json.dumps(data), content_type="application/json")
    
@api_view(['POST'])
def post_rec_search(request):
    search_query = request.data.get('search')
    competition_query= request.data.get('competition')
    if search_query is not None:
        if competition_query=="All competitions": 
            records = DevDayAttendence.objects.filter(team_name__icontains=search_query)
        else:
            records = DevDayAttendence.objects.filter(team_name__icontains=search_query, comp_name= competition_query)
    else:
        if competition_query=="All competitions": 
            records = DevDayAttendence.objects.all()
        else:
            records = DevDayAttendence.objects.filter(comp_name= competition_query)
        
    # else:
    #     return Response({"message": "Only POST method is allowed"})
    data = []
    for record in records:
        record_dict = record.to_mongo().to_dict()
        for key, value in record_dict.items():
            if isinstance(value, ObjectId):
                record_dict[key] = str(value)
        team_name= record_dict["team_name"]
        try:
            AttendanceObj= Attendance.objects.get(teamName=team_name)
            record_dict["attendance"]= AttendanceObj.attendanceStatus
        except:
            record_dict["attendance"]= False
        data.append(record_dict)

    return HttpResponse(json.dumps(data), content_type="application/json")

@api_view(['POST'])
def post_rec_dropdown(request):
    competition = request.data.get("competition")  
    if competition == "All Competitions":
        records = DevDayAttendence.objects.all()
    elif competition is not None:
        records = DevDayAttendence.objects.filter(comp_name=competition)
    else:
        records = DevDayAttendence.objects.none()

    data = []
    for record in records:
        record_dict = record.to_mongo().to_dict()
        for key, value in record_dict.items():
            if isinstance(value, ObjectId):
                record_dict[key] = str(value)
        team_name= record_dict["team_name"]
        try:
            AttendanceObj= Attendance.objects.get(teamName=team_name)
            record_dict["attendance"]= AttendanceObj.attendanceStatus
        except:
            record_dict["attendance"]= False
        data.append(record_dict)

    return HttpResponse(json.dumps(data), content_type="application/json")
@api_view(['POST'])
def mark(request):
    received_data = request.data
    status = received_data["status"]
    team_name=received_data["team"]

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
    return Response({'Status':"Successsfullyy updated"})

    

