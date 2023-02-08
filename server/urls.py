from django.urls import path

from .views import *

urlpatterns = [
    path('news/list/', NewsListView.as_view()),
    path('news/detail/<int:pk>', NewsDetailListView.as_view()),
    path('turnir/list/', TurnirListView.as_view()),
    path('turnir/detail/<int:pk>', TurnirDetailListView.as_view()),
    path('achievements/list/', AchieveEventsListView.as_view()),
    path('achievements/detail/<int:pk>', AchieveEventsDetailListView.as_view()),

    path('coaches/list/', CoachListView.as_view()),
    path('coaches/detail/<int:pk>', CoachDetailListView.as_view()),
    path('sportsmen/list/', SportsmenListView.as_view()),
    path('pol/list/', PolListView.as_view()),
    path('sportsmen/detail/<int:pk>', SportsmenDetailListView.as_view()),

    # path('news_image/list/', NewsImageListView.as_view()),
    # path('achievements_image/list/', AchieveImageListView.as_view()),
]