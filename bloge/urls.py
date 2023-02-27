from django.contrib import admin
from django.urls import path
from blog.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('register/', RegisterView.as_view()),
    path('blog/', BlogView.as_view()),
    path('maqola/<int:id>/', MaqolaView.as_view()),
    path('maqola_add/', MaqolaAddView.as_view()),
]
