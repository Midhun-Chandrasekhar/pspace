from django.views import generic

from web.constants import PARTNER_FORM_FIELDS, INDEX_URL
from web.models import Partner


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'partners'
    model = Partner


class PartnerView(generic.CreateView):
    template_name = 'partner.html'
    model = Partner
    fields = PARTNER_FORM_FIELDS
    success_url = INDEX_URL


class PartnerUpdateView(generic.UpdateView):
    template_name = 'edit_partner.html'
    model = Partner
    fields = PARTNER_FORM_FIELDS
    success_url = INDEX_URL
