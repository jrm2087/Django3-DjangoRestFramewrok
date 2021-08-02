from django.urls import path


def perApp(self):
    print('============ App Per ============')


urlpatterns = [
    path('persona/', perApp)
]
