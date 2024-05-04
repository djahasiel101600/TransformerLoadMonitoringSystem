from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('get_data/LoadCurve/', views.retrieve_loadCurve, name='get_loadCurve'),
    path('get_data/ThreePhaseCurrent/', views.retrieve_threePhaseCurrent, name='get_threePhaseCurrent'),
    path('loadCurveOnly/', views.loadCurveDashboard, name='loadCurveOnly'),
    path('threePhaseCurrentOnly/', views.threePhaseCurrentDashboard, name='threePhaseCurrentOnly'),
    path('retrieve_all/', views.retrieve_all, name='retrieve_all'),
    path('post-request-endpoint/', views.post_request)
]