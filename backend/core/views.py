from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response

from backend.core.models import Cliente, Endereco
from backend.core.serializers import ClienteSerializer, EnderecoSerializer


class ClienteViewSet(viewsets.ViewSet):

    def get_serializer_class(self):
        return ClienteSerializer

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        return serializer_class(*args, **kwargs)

    def get_queryset(self):
        queryset = Cliente.objects.all()
        return queryset

    def get_object(self):
        queryset = self.get_queryset()
        pk = self.kwargs.get('pk')
        obj = get_object_or_404(queryset, pk=pk)
        return obj

    def list(self, request):
        # queryset = Student.objects.all()
        # serializer = StudentSerializer(queryset, many=True)
        # return Response(serializer.data)
        serializer = self.get_serializer(self.get_queryset(), many=True)
        # Sem paginação
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        queryset = Cliente.objects.all()
        student = get_object_or_404(queryset, pk=pk)
        serializer = ClienteSerializer(student)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def destroy(self, request, pk=None):
        item = self.get_object()
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EnderecoViewSet(viewsets.ViewSet):

    def get_serializer_class(self):
        return EnderecoSerializer

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        return serializer_class(*args, **kwargs)

    def get_queryset(self):
        queryset = Endereco.objects.all()
        return queryset

    def get_object(self):
        queryset = self.get_queryset()
        pk = self.kwargs.get('pk')
        obj = get_object_or_404(queryset, pk=pk)
        return obj

    def list(self, request):
        # queryset = Student.objects.all()
        # serializer = StudentSerializer(queryset, many=True)
        # return Response(serializer.data)
        serializer = self.get_serializer(self.get_queryset(), many=True)
        # Sem paginação
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        queryset = Endereco.objects.all()
        student = get_object_or_404(queryset, pk=pk)
        serializer = ClienteSerializer(student)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def destroy(self, request, pk=None):
        item = self.get_object()
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
