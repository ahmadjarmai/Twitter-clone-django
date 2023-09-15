from django.contrib import admin
from .models import Activity

@admin.register(Activity)
class ActionAdmin(admin.ModelAdmin):
  list_display = ['user', 'verb', 'timestamp']
  list_filter = ['timestamp']
  search_fields = ['verb']
 