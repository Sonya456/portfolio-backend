from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.core.mail import send_mail

import json
from .models import AboutElement, ContactMessage, Project, ProjectElement
from .serializers import AboutElementSerializer, ContactMessageSerializer, ProjectSerializer, ProjectElementSerializer


from .models import Contact
from .serializers import ContactSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]



class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Отправка email
            name = serializer.validated_data['name']
            email = serializer.validated_data['email']
            subject = serializer.validated_data['subject']
            message = serializer.validated_data['message']
            full_message = f"From: {name}\nEmail: {email}\n\nMessage:\n{message}"

            try:
                send_mail(
                    subject,
                    full_message,
                    'lizka8456@gmail.com',  # Используйте действительный домен
                    ['sonahatiko@gmail.com'],  # Кому (исполнитель)
                    fail_silently=False,
                )
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticatedOrReadOnly])
    def add_elements(self, request, pk=None):
        project = self.get_object()
        elements_data = request.data.get('elements', [])

        if isinstance(elements_data, str):
            elements_data = json.loads(elements_data)

        print('Elements data received:', elements_data)
        print('Request files:', request.FILES)

        elements = []
        for index, element_data in enumerate(elements_data):
            element_data['project'] = project.id
            element_data['order'] = index
            serializer = ProjectElementSerializer(data=element_data)
            if serializer.is_valid():
                element = serializer.save()
                if element_data['type'] == 'image' and f'elements[{index}][image]' in request.FILES:
                    element.image = request.FILES[f'elements[{index}][image]']
                    element.save()
                    print(f'Saved image element: {element.image}')
                elements.append(element)
                print(f'Saved element: {element}')
            else:
                print('Error in element data:', serializer.errors)
                return Response(serializer.errors, status=400)

        elements_serializer = ProjectElementSerializer(elements, many=True)
        return Response(elements_serializer.data, status=201)

    @action(detail=True, methods=['get'], permission_classes=[IsAuthenticatedOrReadOnly])
    def get_elements(self, request, pk=None):
        project = self.get_object()
        elements = ProjectElement.objects.filter(project=project).order_by('order')
        serializer = ProjectElementSerializer(elements, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['put'], url_path='update_element/(?P<element_id>[^/.]+)', permission_classes=[IsAuthenticatedOrReadOnly])
    def update_element(self, request, pk=None, element_id=None):
        project = self.get_object()
        try:
            element = ProjectElement.objects.get(pk=element_id, project=project)
        except ProjectElement.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProjectElementSerializer(element, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            if 'image' in request.FILES:
                element.image = request.FILES['image']
                element.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    @action(detail=True, methods=['delete'], url_path='delete_element/(?P<element_id>[^/.]+)', permission_classes=[IsAuthenticatedOrReadOnly])
    def delete_element(self, request, pk=None, element_id=None):
        project = self.get_object()
        try:
            element = ProjectElement.objects.get(pk=element_id, project=project)
        except ProjectElement.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)

        element.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AboutUsViewSet(viewsets.ModelViewSet):
    queryset = AboutElement.objects.all().order_by('order')
    serializer_class = AboutElementSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(detail=False, methods=['post'], permission_classes=[IsAuthenticatedOrReadOnly])
    def add_elements(self, request):
        elements_data = request.data.get('elements', [])

        if isinstance(elements_data, str):
            elements_data = json.loads(elements_data)

        elements = []
        for index, element_data in enumerate(elements_data):
            element_data['order'] = index
            serializer = AboutElementSerializer(data=element_data)
            if serializer.is_valid():
                element = serializer.save()
                if element_data['type'] == 'image' and f'elements[{index}][image]' in request.FILES:
                    element.image = request.FILES[f'elements[{index}][image]']
                    element.save()
                elements.append(element)
            else:
                return Response(serializer.errors, status=400)

        elements_serializer = AboutElementSerializer(elements, many=True)
        return Response(elements_serializer.data, status=201)

    @action(detail=True, methods=['put'], url_path='update_element', permission_classes=[IsAuthenticatedOrReadOnly])
    def update_element(self, request, pk=None):
        try:
            element = AboutElement.objects.get(pk=pk)
        except AboutElement.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = AboutElementSerializer(element, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        
        updated_element = serializer.save()
        if 'image' in request.FILES:
            updated_element.image = request.FILES['image']
            updated_element.save()
        
        return Response(serializer.data)

    @action(detail=True, methods=['delete'], url_path='delete_element', permission_classes=[IsAuthenticatedOrReadOnly])
    def delete_element(self, request, pk=None):
        try:
            element = AboutElement.objects.get(pk=pk)
        except AboutElement.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)

        element.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)







