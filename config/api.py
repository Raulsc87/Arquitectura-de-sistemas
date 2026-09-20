from rest_framework.viewsets import ModelViewSet


class SoftDeleteModelViewSet(ModelViewSet):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

    def perform_destroy(self, instance):
        instance.soft_delete()