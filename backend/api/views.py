from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import permissions, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Ride, TrackPoint, Payment, User
from .serializers import (
    RegisterSerializer,
    LoginSerializer,
    UserSerializer,
    RideSerializer,
    RideRequestSerializer,
    RideAssignSerializer,
    TrackPointSerializer,
    PaymentSerializer,
)


class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = Token.objects.get(user=user)
        return Response({'token': token.key, 'user': UserSerializer(user).data}, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user': UserSerializer(user).data})


class MeView(APIView):
    def get(self, request):
        return Response(UserSerializer(request.user).data)


class RideRequestView(APIView):
    def post(self, request):
        serializer = RideRequestSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        ride = serializer.save()
        return Response(RideSerializer(ride).data, status=status.HTTP_201_CREATED)


class RideListView(APIView):
    def get(self, request):
        if request.user.role == User.Role.DRIVER:
            rides = Ride.objects.filter(driver=request.user).order_by('-requested_at')
        else:
            rides = Ride.objects.filter(rider=request.user).order_by('-requested_at')
        return Response(RideSerializer(rides, many=True).data)


class AvailableDriversView(APIView):
    def get(self, request):
        drivers = User.objects.filter(role=User.Role.DRIVER)
        return Response(UserSerializer(drivers, many=True).data)


class RideAssignView(APIView):
    def post(self, request, ride_id):
        ride = get_object_or_404(Ride, id=ride_id)
        serializer = RideAssignSerializer(data=request.data, context={'ride': ride})
        serializer.is_valid(raise_exception=True)
        ride = serializer.save()
        return Response(RideSerializer(ride).data)


class RideCompleteView(APIView):
    def post(self, request, ride_id):
        ride = get_object_or_404(Ride, id=ride_id)
        if ride.status not in [Ride.Status.ACCEPTED, Ride.Status.IN_PROGRESS]:
            return Response({'detail': 'Ride not active.'}, status=status.HTTP_400_BAD_REQUEST)
        ride.status = Ride.Status.COMPLETED
        ride.completed_at = timezone.now()
        ride.actual_price = ride.actual_price or ride.price_estimate
        ride.save()
        return Response(RideSerializer(ride).data)


class TrackPointCreateView(APIView):
    def post(self, request, ride_id):
        ride = get_object_or_404(Ride, id=ride_id)
        serializer = TrackPointSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        track_point = TrackPoint.objects.create(
            ride=ride,
            latitude=serializer.validated_data['latitude'],
            longitude=serializer.validated_data['longitude'],
        )
        return Response(TrackPointSerializer(track_point).data, status=status.HTTP_201_CREATED)


class TrackPointListView(APIView):
    def get(self, request, ride_id):
        ride = get_object_or_404(Ride, id=ride_id)
        points = ride.track_points.order_by('recorded_at')
        return Response(TrackPointSerializer(points, many=True).data)


class PaymentCreateView(APIView):
    def post(self, request, ride_id):
        ride = get_object_or_404(Ride, id=ride_id)
        serializer = PaymentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        payment, _ = Payment.objects.update_or_create(
            ride=ride,
            defaults={
                'amount': serializer.validated_data['amount'],
                'provider': serializer.validated_data.get('provider', 'mock'),
                'status': serializer.validated_data.get('status', Payment.Status.PAID),
                'transaction_id': serializer.validated_data.get('transaction_id', ''),
            },
        )
        return Response(PaymentSerializer(payment).data, status=status.HTTP_201_CREATED)
