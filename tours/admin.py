from django.contrib import admin
from .models import Package, User, Booking

# Customize Package Admin
@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('package_name', 'package_destinations', 'package_days', 'package_price','is_active')
    search_fields = ('package_name', 'package_destinations')
    list_filter = ('package_days', 'package_price','is_active')
    actions = ['make_active', 'make_inactive']
    @admin.action(description="Mark selected packages as Active")
    def make_active(self, request, queryset):
        _= request  # Explicitly reference request to avoid dimming
        queryset.update(is_active=True)

    @admin.action(description="Mark selected packages as Inactive")
    def make_inactive(self, request, queryset):
        _ = request  # Explicitly reference request to avoid dimming
        queryset.update(is_active=False)


# Customize User Admin
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user_name', 'phno')
    search_fields = ('user_name', 'phno')
    list_filter = ('user_name',)

# Customize Booking Admin
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('booking_id', 'booking_date', 'package_name', 'user_name', 'status','phno','date','payment_method')
    search_fields = ('user__user_name', 'package__package_name')
    list_filter = ('status', 'booking_date')
    ordering = ('-booking_date',)
    actions = ['delete_selected']
    list_per_page=15

    def delete_selected(self, request, queryset):
        queryset.delete()
        self.message_user(request, "Selected bookings have been deleted successfully.")
    delete_selected.short_description = "Delete selected bookings"