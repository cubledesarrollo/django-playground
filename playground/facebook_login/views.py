import urlparse
import requests  # @UnresolvedImport
from django.http.response import HttpResponse, HttpResponseBadRequest, \
    HttpResponseServerError
from django.contrib.auth import get_user_model
from .templatetags.facebook_tags import facebook_i18n
from .models import Profile


def channel(request):
    return HttpResponse('<script src="//connect.facebook.net/%s/all.js"></script>' % facebook_i18n(request.LANGUAGE_CODE));


def callback(request):
    """ """
    if 'redirect_uri' not in request.GET or 'access_token' not in request.GET \
        or 'user_id' not in request.GET:
        return HttpResponseBadRequest()

    access_token = request.GET.get('access_token')
    user_id = request.GET.get('user_id')
    redirect_uri = request.GET.get('redirect_uri')

    user_model = get_user_model()

    try:
        profile = Profile.objects.get(facebook_id=user_id)

        # Actualizas el access token
        profile.access_token = access_token
        profile.save()

    except Profile.DoesNotExist:

        # Obtener email
        graph = 'https://graph.facebook.com'
        payload = {'access_token': access_token}
        response = requests.get(urlparse.urljoin(graph, '/me'), params=payload)
        try:
            response.raise_for_status()
        except:
            return HttpResponseServerError("Error connecting with Facebook")
        data = response.json()
        print data['email']

        # Crear el usuario.
        user = user_model.objects.create_user(email=data['email'])
        # profile = Profile.objects.create()


    return HttpResponse("")
