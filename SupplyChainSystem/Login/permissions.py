from rest_framework import permissions

# 自定义安全操作
SAFE_METHODS = permissions.SAFE_METHODS  # ['GET', 'HEAD', 'OPTIONS']


class IsHRDepartment(permissions.BasePermission):
    """
    Allows access only to HR department staff.
    """

    def has_permission(self, request, view):
        if request.method in ['POST']:
            return request.user.groups.filter(name='hr').exists()
        return request.user.is_superuser


class IsTransDepartment(permissions.BasePermission):
    """
    Allows access only to Transportation department staff.
    """

    def has_permission(self, request, view):
        if request.method in ['POST', 'GET']:
            return request.user.groups.filter(name='trans').exists()
        return request.user.is_superuser


class IsFinDepartment(permissions.BasePermission):
    """
    Allows access only to Finance department staff.
    """

    def has_permission(self, request, view):
        if request.method in ['POST', 'GET']:
            return request.user.groups.filter(name='fin').exists()
        return request.user.is_superuser


class IsSaleDepartment(permissions.BasePermission):
    """
    Allows access only to Sale department staff.
    """

    def has_permission(self, request, view):
        if request.method in ['POST', 'GET']:
            return request.user.groups.filter(name='sale').exists()
        return request.user.is_superuser


class IsStoreDepartment(permissions.BasePermission):
    """
    Allows access only to Store department staff.
    """

    def has_permission(self, request, view):
        if request.method in ['POST', 'GET']:
            return request.user.groups.filter(name='store').exists()
        return request.user.is_superuser

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
