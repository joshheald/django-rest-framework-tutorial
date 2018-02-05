from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
	"""
	Custom permission to only allow owners of an object to edit it.
	"""

	def has_object_permission(self, request, view, obj):
		# Read permissions allowed for any request, so always allow GET, HEAD, Options.

		if request.method in permissions.SAFE_METHODS:
			return True

		# Otherwise allow access only to the owner
		return obj.owner == request.user