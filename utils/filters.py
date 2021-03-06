import rest_framework_filters as drf_filters

from apps.core.models import *


class UserFilterSet(drf_filters.FilterSet):
    class Meta:
        model = User


class PersonalAssistantFilterSet(drf_filters.FilterSet):
    class Meta:
        model = PersonalAssistant


class ServiceSubscriptionFilterSet(drf_filters.FilterSet):
    class Meta:
        model = ServiceSubscription


class RoleSubscriptionFilterSet(drf_filters.FilterSet):
    class Meta:
        model = RoleSubscription


class StoreSubscriptionFilterSet(drf_filters.FilterSet):
    class Meta:
        model = StoreSubscription


class StoreAdminFilterSet(drf_filters.FilterSet):
    class Meta:
        model = StoreAdmin


class StoreFilterSet(drf_filters.FilterSet):
    class Meta:
        model = Store


class ServiceFilterSet(drf_filters.FilterSet):
    class Meta:
        model = Service


class SkillFilterSet(drf_filters.FilterSet):
    class Meta:
        model = Skill


class RoleFilterSet(drf_filters.FilterSet):
    class Meta:
        model = Role


class SkillRoleRelationFilterSet(drf_filters.FilterSet):
    class Meta:
        model = SkillRoleRelation


class ShopperFilterSet(drf_filters.FilterSet):
    class Meta:
        model = Shopper


class RegistryFilterSet(drf_filters.FilterSet):
    class Meta:
        model = Registry


class AppointmentFilterSet(drf_filters.FilterSet):
    class Meta:
        model = Appointment


class AppointmentShipFilterSet(drf_filters.FilterSet):
    class Meta:
        model = AppointmentShip