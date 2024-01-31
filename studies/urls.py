from django.urls import path

from studies.apps import StudiesConfig
from rest_framework.routers import DefaultRouter

from studies.views.course import CourseViewSet
from studies.views.lesson import LessonCreateView, LessonRetrieveView, LessonListView, LessonUpdateView, \
    LessonDeleteView
from studies.views.payments import PaymentsViewSet
from studies.views.subscription import SubscriptionCreateView, SubscriptionDeleteView

app_name = StudiesConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')
router.register(r'payments', PaymentsViewSet, basename='payments')

urlpatterns = [
    # Lesson
    path('lesson/create/', LessonCreateView.as_view(), name='lesson-create'),
    path('lesson/retrieve/<int:pk>/', LessonRetrieveView.as_view(), name='lesson-retrieve'),
    path('lesson/list/', LessonListView.as_view(), name='lesson-list'),
    path('lesson/update/<int:pk>/', LessonUpdateView.as_view(), name='lesson-update'),
    path('lesson/delete/<int:pk>/', LessonDeleteView.as_view(), name='lesson-delete'),

    # Subscription
    path('subscription/create/', SubscriptionCreateView.as_view(), name='subscription-create'),
    path('subscription/delete/<int:pk>/', SubscriptionDeleteView.as_view(), name='subscription-delete')

]+router.urls
