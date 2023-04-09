from rest_framework_simplejwt.settings import api_settings
from .models import User

def get_user_from_token(request):
  token = request.data.get("access")
  for AuthToken in api_settings.AUTH_TOKEN_CLASSES:
      valid_token =  AuthToken(token)
  user_id = valid_token[api_settings.USER_ID_CLAIM]
  user = User.objects.get(**{api_settings.USER_ID_FIELD: user_id})
  return user