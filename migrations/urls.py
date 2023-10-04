from django.urls import path
from issues import views


urlpatterns = [
    path("", views.IssueListView.as_view(), name="list"),
    path("new/", views.IssueCreateView.as_view(), name="new"),
    path("<int:pk>/", views.IssueDetailView,as_view(), name="detail"),
]