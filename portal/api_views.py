from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from bson import ObjectId
import json
from django.shortcuts import HttpResponse
from .models import DevDayAttendance, Event, competitions, get_competition_name
from datetime import datetime
from django.contrib.auth.decorators import login_required
from rest_framework.pagination import PageNumberPagination
from math import ceil


class CustomPaginator(PageNumberPagination):
    page_size = 10
    page_query_param = "page"


# Events Times & Search
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


# Candidate Data Retrieval & Search


@api_view(["GET"])
@login_required(login_url="portal:login-page")
def get_rec(request):
    paginator = CustomPaginator()
    query = DevDayAttendance.objects.all()
    paginated_query = paginator.paginate_queryset(query, request)
    data = []

    for record in paginated_query:
        record_dict = record.to_mongo().to_dict()

        # Convert ObjectId to string for serialization
        for key, value in record_dict.items():
            if isinstance(value, ObjectId):
                record_dict[key] = str(value)
        data.append(record_dict)

    # Return paginated response
    # Calculate total count and total pages
    total_count = query.count()
    page_size = paginator.get_page_size(request)
    total_pages = ceil(total_count / page_size)
    # Extract current page number from request query parameters
    current_page = int(request.query_params.get("page", 1))
    return Response(
        {
            "count": total_count,
            "next": paginator.get_next_link(),
            "current_page": current_page,
            "previous": paginator.get_previous_link(),
            "first_page": 1,
            "last_page": total_pages,
            "results": data,
        }
    )


@api_view(["GET"])
@login_required(login_url="portal:login-page")
def record_search(request, competitionName, searchValue):
    search_query = searchValue
    competition_query = get_competition_name(competitionName)
    if search_query != "all":
        if competition_query == "all_competitions":
            records = DevDayAttendance.objects.filter(Team_Name__icontains=search_query)
            if not records:
                records = DevDayAttendance.objects.filter(Leader_name__icontains=search_query)
        else:
            records = DevDayAttendance.objects.filter(
                Team_Name__icontains=search_query, Competition=competition_query
            )
            if not records:
                records = DevDayAttendance.objects.filter(Leader_name__icontains=search_query, Competition=competition_query)
    else:
        if competition_query == "all_competitions":
            records = DevDayAttendance.objects.all()
        else:
            records = DevDayAttendance.objects.filter(Competition=competition_query)

    paginator = CustomPaginator()
    paginated_query = paginator.paginate_queryset(records, request)
    data = []
    for record in paginated_query:
        record_dict = record.to_mongo().to_dict()

        # Convert ObjectId to string for serialization
        for key, value in record_dict.items():
            if isinstance(value, ObjectId):
                record_dict[key] = str(value)
        data.append(record_dict)

    total_count = records.count()
    page_size = paginator.get_page_size(request)
    total_pages = ceil(total_count / page_size)
    # Extract current page number from request query parameters
    current_page = int(request.query_params.get("page", 1))
    return Response(
        {
            "count": total_count,
            "next": paginator.get_next_link(),
            "current_page": current_page,
            "previous": paginator.get_previous_link(),
            "first_page": 1,
            "last_page": total_pages,
            "results": data,
        }
    )


@api_view(["POST"])
@login_required(login_url="portal:login-page")
def mark(request):
    received_data = request.data
    team_status = received_data["status"]
    team_id = received_data["teamID"]

    if not team_status or not team_id:
        return Response({"Status": "Failed"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        # Retrieve the DevDayAttendance object with the given team ID
        attendance_obj = DevDayAttendance.objects.get(id=team_id)

        # Update the attendance status based on the received data
        if team_status == "present":
            attendance_obj.attendance = True
        else:
            attendance_obj.attendance = False

        # Save the updated object
        attendance_obj.save()

        return Response({"Status": "Successfully updated"}, status=status.HTTP_200_OK)

    except DevDayAttendance.DoesNotExist:
        return Response({"Status": "Failed"}, status=status.HTTP_400_BAD_REQUEST)
