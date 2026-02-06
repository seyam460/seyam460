from django.urls import path

from .views import (
    RegisterView,
    LoginView,
    MeView,
    RideRequestView,
    RideListView,
    AvailableDriversView,
    RideAssignView,
    RideCompleteView,
    TrackPointCreateView,
    TrackPointListView,
    PaymentCreateView,
)

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/me/', MeView.as_view(), name='me'),
    path('rides/request/', RideRequestView.as_view(), name='ride-request'),
    path('rides/', RideListView.as_view(), name='ride-list'),
    path('drivers/available/', AvailableDriversView.as_view(), name='drivers-available'),
    path('rides/<int:ride_id>/assign/', RideAssignView.as_view(), name='ride-assign'),
    path('rides/<int:ride_id>/complete/', RideCompleteView.as_view(), name='ride-complete'),
    path('rides/<int:ride_id>/track/', TrackPointCreateView.as_view(), name='track-create'),
    path('rides/<int:ride_id>/track/list/', TrackPointListView.as_view(), name='track-list'),
    path('rides/<int:ride_id>/payment/', PaymentCreateView.as_view(), name='payment-create'),
]
