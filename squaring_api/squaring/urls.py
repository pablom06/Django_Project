from django.urls import path
from squaring.views import SquaringView, HelloWorldView

urlpatterns = [

    path('home', HelloWorldView.as_view()),
    path('<int:number>', view=SquaringView.as_view()),
    
]