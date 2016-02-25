__author__ = 'chitrankdixit'
from rest_framework.pagination import PageNumberPagination


class TenItemsSetPagination(PageNumberPagination):
    page_size = 2
