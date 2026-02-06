from django.contrib import admin
from .models import User, Ride, TrackPoint, Payment


admin.site.register(User)
admin.site.register(Ride)
admin.site.register(TrackPoint)
admin.site.register(Payment)
