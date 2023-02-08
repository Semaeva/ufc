from rest_framework import serializers
from.models import *


class NewsSerializer(serializers.ModelSerializer):
    news_images = serializers.StringRelatedField(many=True)

    class Meta:
        model = News
        fields = ["id", "title", "description", "news_images"]


class TurnirSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turnir
        fields = "__all__"


class SportsmenSerializer(serializers.ModelSerializer):
    title_pol = serializers.CharField(source="pol.title", read_only=True)
    weight_category = serializers.CharField(source="weight_category.title", read_only=True)

    class Meta:
        model = Sportsmen
        fields = ['name', 'title_pol','age','weight', 'image','fight', 'weight','rating_total','wins','weight_category']


class PolSerialiazer(serializers.ModelSerializer):

    class Meta:
        model = Pol
        fields = ['title']


class CategorySerialiazer(serializers.ModelSerializer):
    sportsmen_category = serializers.StringRelatedField(many=True)

    class Meta:
        model = WeightCategory
        fields = ['id', 'title', 'weight_sportsmen']


class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = "__all__"


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"


class AchieveEventsSerializer(serializers.ModelSerializer):
    achieve_images = serializers.StringRelatedField(many=True)

    class Meta:
        model = AchieveEvents
        fields = ['id', 'title', 'created_date', 'video', 'image', 'result', 'description', 'achieve_images']


class AchieveEventsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AchieveEventsImage
        fields = "__all__"


class NewsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsImage
        fields = "__all__"

