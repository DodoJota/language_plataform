from django.urls import path
from . import views
from .views import logout_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.portugues, name='portugues'),

    path('materiais/', views.materiais, name='materiais'),
    path('landing/', views.landing, name='landing'),
    path('praticar/', views.praticar, name='praticar'),
    path('gramatica/', views.gramatica, name='gramatica'),
    path('faces/', views.faces, name='faces'),
    path('flashcards/', views.flashcards, name='flashcards'),
    path('aulas/', views.aulas, name='aulas'),
    path('dicionario/', views.dicionario, name='dicionario'),
    path('contato/', views.contato, name='contato'),
    path("login/", views.login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path('create_user/', views.create_user, name='create_user'),
    path('teacher/', views.teacher, name='teacher'),
    path('enviar_materiais/', views.enviar_materiais, name='enviar_materiais'),
    path('deletar_material/<int:material_id>/', views.deletar_material, name='deletar_material'),
    path('enviar_videos/', views.enviar_videos, name='enviar_videos'),
    path('deletar_video/<int:video_id>/', views.deletar_video, name='deletar_video'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)