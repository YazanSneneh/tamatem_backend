from rest_framework import serializers
from .models import Item, ItemImage



class ImageSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return ItemImage.objects.create(item_id=self.context["item_id"], **validated_data)

    class  Meta(object):
        model = ItemImage
        fields = ["id", "image"]


class ItemSerializer(serializers.ModelSerializer):
    image = ImageSerializer(read_only=True)

    class Meta:
        model = Item
        fields = ["name", "price", "image"]

    def to_representation(self, item):
        data = super().to_representation(item)

        if self.context['view'].action == 'update':
            data.pop("image")
            data['description'] = item.description
        return data


class ItemDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ["description"]


class ItemUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ["name", "price", "description"]

