from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest
from rest_framework.decorators import api_view
from taskmanager.settings import DEBUG


def debug_only_view(view_method):
    if DEBUG:
        return view_method
    else:
        return lambda request: HttpResponseNotFound()


@debug_only_view
@api_view(['GET'])
def grant_admin(request):
    user = request.user
    if not user.is_authenticated:
        return HttpResponseBadRequest("you should log in")
    user.is_superuser = True
    user.is_staff = True
    user.save()
    return HttpResponse("admin granted")


@debug_only_view
@api_view(['GET'])
def revoke_admin(request):
    user = request.user
    if not user.is_authenticated:
        return HttpResponseBadRequest("you should log in")
    user.is_superuser = False
    user.is_staff = False
    user.save()
    return HttpResponse("admin revoked")
