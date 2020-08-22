from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
from rest_framework import viewsets
from rest_framework.response import Response


class PostsList(viewsets.ViewSet):
                           
    def list(self, request):
        id_post = self.request.query_params.get('id')
        if id_post:
            queryset = Post.objects.filter(id=int(id_post))
            serializer = PostSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            queryset = Post.objects.all()
            serializer = PostSerializer(queryset, many=True)
            di = {}
            lista = []
            print(serializer.data)
            for i in serializer.data:
                di['id'] = i['id']
                di['titulo'] = i['titulo']
                lista.append(di)
                di = {}
            return Response(lista)
