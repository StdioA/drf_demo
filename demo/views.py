from rest_framework.viewsets import ModelViewSet
from .models import Data
from .serializers import DataSerializer


class DataViewSet(ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer

    def update(self, request, *args, **kwargs):
        """
        Allow user update a instance partially.
        """
        kwargs["partial"] = True
        return super().update(request, *args, **kwargs)
