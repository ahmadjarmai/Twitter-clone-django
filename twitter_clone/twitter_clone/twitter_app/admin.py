from django.contrib import admin
from .models import Profile,Tweet,Comment,Follow

admin.site.register(Tweet)
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
  list_display = ['user', 'bio', 'location']
  raw_id_fields = ['user']
 
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
  list_display = ['tweet','created', 'active']
  list_filter = ['active', 'created', 'updated']
  search_fields = ['body']
 
admin.site.register(Follow)