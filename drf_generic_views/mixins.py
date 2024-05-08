from rest_framework import status
from rest_framework.response import Response


class MultiDestroyModelMixin:
    def destroy(self, request, *args, **kwargs):
        for insance in self.get_queryset():
            self.perform_destroy(insance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()


class BulkDestroyModelMixin:
    def destroy(self, request, *args, **kwargs):
        self.perform_destroy(self.get_queryset())
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, queryset):
        queryset.delete()
