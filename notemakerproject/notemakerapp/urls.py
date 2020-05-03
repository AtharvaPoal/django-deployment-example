from django.urls import path
from notemakerapp import views

app_name='notemakerapp'

urlpatterns=[
    path('register/',views.register_view,name="register"),
    path('index/',views.index,name="index"),
    path('login/',views.user_login,name="login"),
    path('logout/',views.user_logout,name="logout"),
    path('notes/',views.notes_view,name="notes"),
    path('note_add/',views.note_add_view,name="note_add"),
    path('about/',views.about,name="about"),
]
