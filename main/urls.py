from django.urls import path
from .views import IndexView, IndexGerView, IndexUzView, test, CheckTestView, IndexTestView, LoginView, ListView, OfertaView
urlpatterns = [
    path('', IndexView.as_view(), name='english'),
    path('eng/', IndexView.as_view(), name='english'),
    path('ger/', IndexGerView.as_view(), name='german'),
    path('uz/', IndexUzView.as_view(), name='uzbek'),
    path('test/', IndexTestView.as_view(), name='test'),
    path('login/', LoginView.as_view(), name='login'),
    path('list/', ListView.as_view(), name='list'),
    path('test/<int:test_id>', test, name='question'),
    path('check/<int:check_test_id>', CheckTestView.as_view(), name='check'),
    path('oferta/', OfertaView.as_view(), name='oferta'),
]