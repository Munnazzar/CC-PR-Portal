from django.urls import path
from .views import adminPanel, loginPage, adminPanelSchedule, logout_view
from .api_views import *

app_name = "portal"

urlpatterns = [
    # Primary Views
    path("adminPanel/", adminPanel, name="admin-panel"),
    path("adminPanelSchedule/", adminPanelSchedule, name="admin-panel-schedule"),
    # Account Views
    path("", loginPage, name="login-page"),
    path("logout/", logout_view, name="logout"),
    # APIs
    # Candidate APIs
    path("api/get_record/", get_rec),
    path("api/record_search/<str:competitionName>/<str:searchValue>/", record_search),
    path("api/update_attendance/", mark),
    # Event  APIs
    path("api/get_time/", get_time),
    path("api/update_time/", update_time),
    path("api/search_schedule/<str:competitionName>/", search_schedule),
]
