from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from .models import Activity
import datetime

def create_action(user, verb, target=None):
    now = timezone.now()
    last_minute = now - datetime.timedelta(seconds=60)
    similar_actions = Activity.objects.filter(user_id=user.id,
    verb= verb, timestamp__gte=last_minute)
    
    if target:
      content_type= ContentType.objects.get_for_model(target)
      similar_actions = similar_actions.filter(
      content_type=content_type, object_id=target.id)
 
      if not similar_actions:
         activity= Activity(user=user, verb=verb, content_object=target)
         activity.save()
         return True
      return False