from django.urls import path
from .views import BookApiView, BookApiDetail, BookApiCreate, BookApiUpdate, BookApiDelete

urlpatterns = [
    path('', BookApiView.as_view(), name='home'),
    path('<int:pk>/', BookApiDetail.as_view()),
    path('create', BookApiCreate.as_view()),
    path('update/<int:pk>/', BookApiUpdate.as_view()),
    path('delete/<int:pk>/', BookApiDelete.as_view()),
]
