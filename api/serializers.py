from rest_framework import serializers

from web.constants import PARTNER_FORM_FIELDS
from web.models import Partner


class PartnerSerializer(serializers.ModelSerializer):
    """
        sample_data = {
            "name": "abc",
            "gst_no": "123123",
            "phone_number": "+911111111111",
            "website": "www.opo.com",
            "email": "abc@opo.com"
        }
    """
    class Meta:
        model = Partner
        fields = PARTNER_FORM_FIELDS

