from django.urls import path
from . import views

urlpatterns = [
    path('', views.first ,name='first'),
    path('home/', views.home ,name='home'),
    path('homes/', views.homes ,name='homes'),
    path('room_t/', views.room_t),
    path('room_s/', views.room_s),
    path('recommendations/', views.recommendation_s, name='recommendations'),
     path('recommendationins/', views.recommendation_ins, name='recommendationins'),
     path('recommendationtpositive/', views.recommendation_tpositive, name='recommendationtpositive'),
     path('recommendationspositive/', views.recommendation_spositive, name='recommendationspositive'),
    path('recommendationt/', views.recommendation_t, name='recommendationt'),
    path('get_token/', views.getToken),
    path('create_member/', views.createMember),
    path('get_member/', views.getMember),
    path('delete_member/', views.deleteMember),
    path('student/', views.student, name='student'),
    path('detect-emotion/', views.emotion_detection, name='detect_emotion'),
    path('dashboard_t/', views.dashboard_t, name='dashboard_t'),
    path('dashboard_s/', views.dashboard_s, name='dashboard_s'),
    path('calcul/', views.calcul, name='calcul'),
    path('lobby/', views.lobby, name='lobby'),
    path('dashboard_teacher/<str:student_name>/', views.dashboard_teacher, name='dashboard_teacher'),
  
    path('dashboard_student/<str:student_name>/', views.dashboard_student, name='dashboard_student'),
]