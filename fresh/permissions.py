from rest_framework import permissions


class IsOwnerReadOnly(permissions.BasePermission):
    """
    自定义权限，只允许对象的所有者编辑
    """

    def has_object_permission(self, request, view, obj):
        """
        所有的request请求都有读权限，因此一律允许GET/HEAD/OPTIONS方法
        :param request:
        :param view:
        :param obj:
        :return: boolean
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        # 仅对象所有者拥有修改权限
        return request.user == obj.teacher
