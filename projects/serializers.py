from rest_framework import serializers
from .models import AboutElement, Project, ProjectElement, ContactMessage, Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class ProjectElementSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = ProjectElement
        fields = ['id', 'type', 'content', 'image', 'image_url', 'order', 'project', 'font']

    def get_image_url(self, obj):
        request = self.context.get('request')
        if request and obj.image and hasattr(obj.image, 'url'):
            return request.build_absolute_uri(obj.image.url)
        elif obj.image and hasattr(obj.image, 'url'):
            return obj.image.url
        return None

class ProjectSerializer(serializers.ModelSerializer):
    elements = ProjectElementSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'default_image', 'elements', 'font']


class AboutElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutElement
        fields = '__all__'


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = '__all__'