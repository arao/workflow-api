# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django_filters import rest_framework as filters

from rest_framework import response, status
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from apps.common import constant as common_constant
from apps.company import permissions as company_permissions
from apps.company import serializers as company_serializer
from apps.company.models import UserCompany, Company
from apps.company.permissions import (
    IsActiveCompanyAdmin,
    IsActiveCompanyEmployee,
    IsInactiveEmployee,
    IsCompanyAdmin
)

User = get_user_model()


class CompanyBaseClassView(GenericViewSet):
    '''
    Base class for company views view 
    '''
    queryset = UserCompany.objects.all()


class UpdateCompanyView(UpdateModelMixin, GenericViewSet):
    '''
    Update Company details.
    '''
    queryset = Company.objects.all()
    permission_classes = [IsCompanyAdmin]
    serializer_class = company_serializer.CompanySerializer


class CreateCompanyUserView(CreateModelMixin, CompanyBaseClassView):
    '''
    create:
        Create User and Company.
    '''
    serializer_class = company_serializer.UserCompanySignupSerializer
    authentication_classes = []


class CreateCompanyView(CompanyBaseClassView):
    '''
    new_company:
        Create company for old user
    '''
    serializer_class = company_serializer.UserCompanySerializer
    permission_classes = [IsInactiveEmployee]

    @action(detail=False, methods=['post'], url_path='new-company',)
    def new_company(self, request):
        '''
        create company, only for old users.
        '''
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


class EmployeeCompanyView(UpdateModelMixin, CompanyBaseClassView):
    '''
    my_company:
        Return company of employee
    partial_update:
        update employee details
    '''
    serializer_class = company_serializer.EmployeeSerializer
    permission_classes = [IsActiveCompanyAdmin]

    @action(detail=False, url_path='my-company', permission_classes=[IsActiveCompanyEmployee])
    def my_company(self, request):
        '''
        employee's company detail
        '''
        instance = self.get_queryset().get(user=request.user, company=request.user.company)
        serializer = company_serializer.EmployeeCompanySerializer(
            instance=instance)
        return response.Response(serializer.data, status=status.HTTP_200_OK)


class EmployeesView(GenericViewSet):
    '''
    employees:
        return employees of company, can be filtered on the basis of status and admin is possible.
    '''

    serializer_class = company_serializer.EmployeeSerializer
    permission_classes = [company_permissions.IsActiveCompanyEmployee]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('status', 'is_admin')
    queryset = UserCompany.objects.all()

    def get_queryset(self):
        return self.queryset.filter(
            company=self.request.user.company,
            status__in=[
                common_constant.USER_STATUS.ACTIVE,
                common_constant.USER_STATUS.INVITED
            ]
        )

    @action(detail=False, methods=['get'], )
    def employees(self, request):
        '''
        list all employees of company.
        '''
        queryset = self.filter_queryset(self.get_queryset())
        serialzer = self.get_serializer(queryset, many=True)

        return response.Response(serialzer.data, status=status.HTTP_200_OK)


class InviteEmployeeView(GenericViewSet):
    '''
    Invite User to the company with this view.
    '''
    serializer_class = company_serializer.InviteEmployeeSerializer
    permission_classes = [company_permissions.IsActiveCompanyEmployee]
    queryset = UserCompany.objects.all()

    @action(detail=False, methods=['post'], url_path='invite-employee',)
    def invite_employee(self, request):
        '''
        invite employee
        '''
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data, status=status.HTTP_200_OK)