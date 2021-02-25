#to allow only a specific author to edit a post
"""
read-only for all requests 
for any write requests, such as edit or delete, the author must be the same as the current logged-in user.
"""

from rest_framework import permissions

class IsAuthor(permissions.BasePermission):

    #override has_object_permission

    def has_object_permission(self, request, view, obj):
        #read only for any request
        if request.method in permissions.SAFE_METHODS:
            return True
        #Write permissions are only allowed to the author of a post
        return obj.author == request.user