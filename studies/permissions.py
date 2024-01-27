from rest_framework.permissions import BasePermission

from studies.models import Lesson, Course


class IsModerator(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_staff


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if isinstance(obj, Course):
            return request.user == obj.course_author

        elif isinstance(obj, Lesson):
            return request.user == obj.lesson_author

