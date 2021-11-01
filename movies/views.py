from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Movie
from .serializers import MovieListSerializer, MovieDetailSerializer, ReviewCreateSerializer


class MovieListView(APIView):
    """Вывод списка фильмов"""

    def get(self, request):
        movies = Movie.objects.filter(draft=False)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)


class MovieDetailView(APIView):
    """Вывод фильма"""

    def get(self, request, pk):
        try:
            movie = Movie.objects.get(id=pk, draft=False)
            serializer = MovieDetailSerializer(movie)
            return Response(serializer.data)
        except:
            print('errr')


class ReviewCreateView(APIView):
    """Добавление отзыва к фильму"""
    def post(self, request):
        print("[INFO] request=", request)
        review = ReviewCreateSerializer(data=request.data)
        print("[INFO] review=", review)
        if review.is_valid():
            review.save()
        return Response(status=201)