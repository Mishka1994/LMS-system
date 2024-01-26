from rest_framework.permissions import BasePermission


class IsModerator(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_staff


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.course_author:
            return request.user == obj.course_author

        elif obj.lesson_author:
            return request.user == obj.lesson_author

