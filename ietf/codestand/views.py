from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from ietf.codestand.helpers.utils import (render_page, get_user)
from ietf.codestand import constants
from ietf.codestand.matches.models import DashboardConfig
from ietf.codestand.dashboard import (get_my_matches, get_my_requests, get_all_matches)
from django.conf import settings
from django.contrib.auth.decorators import login_required


def index(request):
    return render_page(request, constants.TEMPLATE_INDEX)


def about(request):
    return render_page(request, constants.TEMPLATE_ABOUT)


def back(request):
    template = "/codestand/"

    if "previous_template" in request.session:
        template = request.session["previous_template"]

    return HttpResponseRedirect(template)

def handler500(request):
    return render_page(request, constants.TEMPLATE_ERROR_500)


def handler404(request):
    return render_page(request, constants.TEMPLATE_ERROR_404)
