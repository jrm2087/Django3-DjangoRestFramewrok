from django.urls import path


def depApp(self):
    print('============ App Dep ============')


urlpatterns = [
    path('departamento/', depApp)
]
