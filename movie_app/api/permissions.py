from rest_framework import permissions
from movie_app.models import Collections


class IsCollectionOwnerLoggedIn(permissions.BasePermission):
    """
    Custom permission to only allow owners of a collection to view/update collections belongs to him.
    """
    def has_object_permission(self, request, view, obj):
        print(obj, ">>>>>", view)
        return obj.created_by == request.user
    
    def has_permission(self, request, view):
        try:
            print("=========")
            if view.kwargs.get("pk") : return Collections.objects.get(uuid=view.kwargs["pk"]).created_by == request.user
            else: return True
        except Exception as e:
            print(e)
            return False