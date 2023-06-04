from rest_framework import permissions

# 安全操作
SAFE_METHODS = permissions.SAFE_METHODS  # ['GET', 'HEAD', 'OPTIONS'] can be accessed by all users


class StaffListPermission(permissions.BasePermission):
    """
    permissions of StaffList view:
    1. superusers have all permissions
    2. user in group hr have all permissions
    3. users in other groups can use SAFE_METHODS
    """

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        elif request.user.groups.filter(name='hr').exists():
            return True
        elif request.method in SAFE_METHODS:
            return True
        else:
            return False


class StaffDetailPermission(permissions.BasePermission):
    """
    permissions of StaffDetail view:
    1. superusers have all permissions
    2. user in group hr have all permissions
    3. users in other groups can use SAFE_METHODS
    """

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        elif request.user.groups.filter(name='hr').exists():
            return True
        elif request.method in SAFE_METHODS:
            return True
        else:
            return False


class KpiListPermission(permissions.BasePermission):
    """
    permissions of KpiList view:
    1. superusers have all permissions
    2. user in group hr have all permissions
    3. users in other groups can use SAFE_METHODS on their own objects
    """

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        elif request.user.groups.filter(name='hr').exists():
            return True
        elif request.method in SAFE_METHODS:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return obj.user == request.user
        return False


class KpiDetailPermission(permissions.BasePermission):
    """
    permissions of KpiDetail view:
    1. superusers have all permissions
    2. user in group hr have all permissions
    3. users in other groups can use SAFE_METHODS
    """

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        elif request.user.groups.filter(name='hr').exists():
            return True
        elif request.method in SAFE_METHODS:
            return True
        else:
            return False


class OnlySuperUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser


class OnlySafeMethod(permissions.BasePermission):
    """
    Allows access by safe methods
    """

    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class OnlyHRDepartment(permissions.BasePermission):
    """
    Allows access only to HR department staff.
    """

    def has_permission(self, request, view):
        return request.user.groups.filter(name='hr').exists()


class OnlyTransDepartment(permissions.BasePermission):
    """
    Allows access only to Transportation department staff.
    """

    def has_permission(self, request, view):
        return request.user.groups.filter(name='trans').exists()


class OnlyFinDepartment(permissions.BasePermission):
    """
    Allows access only to Finance department staff.
    """

    def has_permission(self, request, view):
        return request.user.groups.filter(name='fin').exists()


class OnlySaleDepartment(permissions.BasePermission):
    """
    Allows access only to Sale department staff.
    """

    def has_permission(self, request, view):
        return request.user.groups.filter(name='sale').exists()


class OnlyStoreDepartment(permissions.BasePermission):
    """
    Allows access only to Store department staff.
    """

    def has_permission(self, request, view):
        return request.user.groups.filter(name='store').exists()


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    自定义权限，只允许对象的所有者编辑
    """

    def has_object_permission(self, request, view, obj):
        """
        仅对象用户拥有修改权限
        :param request:
        :param view:
        :param obj:
        :return: boolean
        """
        return request.user == obj.user
