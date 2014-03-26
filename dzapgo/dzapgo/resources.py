
from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.authentication import Authentication
from tastypie.authorization import Authorization

from django.contrib.auth import get_user_model

from rest_hooks.models import Hook


User = get_user_model()

class UserResource(ModelResource):
    class Meta:
        resource_name = 'user'
        queryset = User.objects.all()
        authentication = Authentication()
        authorization = Authorization()
        allowed_methods = ['get']


class HookResource(ModelResource):
    user = fields.ToOneField(UserResource, 'user', default=1)

    class Meta:
        resource_name = 'hooks'
        queryset = Hook.objects.all()
        authentication = Authentication()
        authorization = Authorization()
        allowed_methods = ['get', 'post', 'delete']
        fields = ['event', 'target']