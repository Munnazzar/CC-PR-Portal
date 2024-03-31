from django.urls import path
from .views import adminPanel, loginPage, adminPanelSchedule, logout_view
from .api_views import *

app_name = "portal"

urlpatterns = [
    path("", loginPage, name="login-page"),
    path("adminPanel/", adminPanel, name="admin-panel"),
    path("adminPanelSchedule/", adminPanelSchedule, name="admin-panel-schedule"),
    path("api/get_record/", get_rec),
    path("api/get_time/", get_time),
    path("api/update_time/", update_time),
    path("api/post_record_dropdown/", post_rec_dropdown),
    path("api/post_record_search/", post_rec_search),
    path("api/post_search_schedule/", post_search_schedule),
    path("api/update_attendance/", mark),
    path("logout/", logout_view, name="logout"),
]
