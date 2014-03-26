
from tastypie.resources import ModelResource
from rest_hooks.models import Hook

class HookResource(ModelResource):
    class Meta:
        resource_name = 'hooks'
        queryset = Hook.objects.all()
        allowed_methods = ['get', 'post', 'delete']
        fields = ['event', 'target']