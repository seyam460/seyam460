from django.contrib.auth import authenticate
from django.utils import timezone
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from .models import User, Ride, TrackPoint, Payment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'phone_number']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'role', 'phone_number']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        Token.objects.create(user=user)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        user = authenticate(username=attrs['username'], password=attrs['password'])
        if not user:
            raise serializers.ValidationError('Invalid credentials')
        attrs['user'] = user
        return attrs


class RideSerializer(serializers.ModelSerializer):
    rider = UserSerializer(read_only=True)
    driver = UserSerializer(read_only=True)

    class Meta:
        model = Ride
        fields = '__all__'


class RideRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = [
            'pickup_address', 'dropoff_address', 'pickup_lat', 'pickup_lng',
            'dropoff_lat', 'dropoff_lng', 'distance_km', 'price_estimate'
        ]

    def create(self, validated_data):
        user = self.context['request'].user
        ride = Ride.objects.create(rider=user, **validated_data)
        return ride


class RideAssignSerializer(serializers.Serializer):
    driver_id = serializers.IntegerField()

    def validate(self, attrs):
        ride = self.context['ride']
        if ride.status != Ride.Status.REQUESTED:
            raise serializers.ValidationError('Ride cannot be assigned.')
        return attrs

    def save(self, **kwargs):
        ride = self.context['ride']
        driver = User.objects.get(id=self.validated_data['driver_id'])
        ride.driver = driver
        ride.status = Ride.Status.ACCEPTED
        ride.accepted_at = timezone.now()
        ride.save()
        return ride


class TrackPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackPoint
        fields = ['id', 'ride', 'latitude', 'longitude', 'recorded_at']
        read_only_fields = ['id', 'ride', 'recorded_at']


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'ride', 'amount', 'provider', 'status', 'transaction_id', 'created_at']
        read_only_fields = ['id', 'ride', 'created_at']
