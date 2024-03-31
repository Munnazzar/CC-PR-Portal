from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(
        "admin/devday_pr_portal/f92jfF4SG6fsad4f5fv75ff59nb8o5w0652fpwehio23ui9c1wepmstyrobns12jk98y169r10i6453e72ty21x6r12z854e/",
        admin.site.urls,
    ),
    path("", include("portal.urls")),
]
