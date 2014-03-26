
from tastypie.resources import ModelResource
from tastypie.authentication import Authentication
from tastypie.authorization import Authorization
from rest_hooks.models import Hook

class HookResource(ModelResource):
    class Meta:
        resource_name = 'hooks'
        queryset = Hook.objects.all()
        authentication = Authentication()
        authorization = Authorization()
        allowed_methods = ['get', 'post', 'delete']
        fields = ['event', 'target']