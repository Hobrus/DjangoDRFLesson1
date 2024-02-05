from rest_framework import serializers
from .models import Post, Shop


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'text', 'owner']
        read_only_fields = ('owner',)

    def create(self, validated_data):
        user = self.context['request'].user
        return Post.objects.create(owner=user, **validated_data)


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['id', 'item', 'quantity', 'price']
