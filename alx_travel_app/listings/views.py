from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Listing, Booking, Review
from .serializers import (
    ListingSerializer,
    BookingSerializer,
    ReviewSerializer
)


class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all().select_related('operator')
    serializer_class = ListingSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(operator=self.request.user)


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
