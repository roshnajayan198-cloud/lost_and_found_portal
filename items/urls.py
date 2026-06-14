from django.urls import path
from .views import *

urlpatterns=[

path('',home),

path('add/',add_item),

path('claim/<int:id>/',claim),

path('signup/',signup),
path(
'login/',
UserLoginView.as_view(),
name='login'
),

]