from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import mixins
from .mixins import MultiDestroyModelMixin, BulkDestroyModelMixin


class MultiDestroyAPIView(MultiDestroyModelMixin, GenericAPIView):
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class BulkDestroyAPIView(BulkDestroyModelMixin, GenericAPIView):
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ListDestroyAPIView(
    mixins.ListModelMixin, MultiDestroyModelMixin, GenericAPIView
):
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ListBulkDestroyAPIView(
    mixins.ListModelMixin, BulkDestroyAPIView, GenericAPIView
):
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
