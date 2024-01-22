from django.urls import path

from studies.apps import StudiesConfig
from rest_framework.routers import DefaultRouter

from studies.views.course import CourseViewSet
from studies.views.lesson import LessonCreateView, LessonRetrieveView, LessonListView, LessonUpdateView, \
    LessonDeleteView
from studies.views.payments import PaymentsViewSet

app_name = StudiesConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')
router.register(r'payments', PaymentsViewSet, basename='payments')

urlpatterns = [

    path('lesson/create/', LessonCreateView.as_view(), name='create-lesson'),
    path('lesson/retrieve/<int:pk>/', LessonRetrieveView.as_view(), name='retrieve-lesson'),
    path('lesson/list/', LessonListView.as_view(), name='list-lesson'),
    path('lesson/update/<int:pk>/', LessonUpdateView.as_view(), name='update-lesson'),
    path('lesson/delete/<int:pk>/', LessonDeleteView.as_view(), name='delete-lesson')

]+router.urls
