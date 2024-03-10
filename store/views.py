from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Item, ItemImage
from .serializers import ItemSerializer, ItemDetailSerializer, ImageSerializer, ItemUpdateSerializer


class ItemViewSet(ListModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get_permissions(self):
        if self.request.method in ["PATCH", "PUT"]:
            return [IsAuthenticated()]
        return [AllowAny()]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ItemDetailSerializer
        elif self.action in ['update', 'partial_update']:  # Use update or partial_update
            return ItemUpdateSerializer
        return ItemSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context


class ItemImageViewSet(ModelViewSet):
    serializer_class = ImageSerializer

    def get_queryset(self):
        return ItemImage.objects.filter(item_id=self.kwargs["item_pk"])

    def get_serializer_context(self):
        return {"item_id": self.kwargs["item_pk"]}