from __future__ import (unicode_literals)
import os

from leap import __branding
from leap.base import config as baseconfig

PROVIDER_CA_CERT = __branding.get(
    'provider_ca_file',
    'testprovider-ca-cert.pem')

provider_ca_path = lambda: unicode(os.path.join(
    baseconfig.get_default_provider_path(),
    'keys', 'ca',
    PROVIDER_CA_CERT
))

PROVIDER_DOMAIN = __branding.get('provider_domain', 'testprovider.example.org')


client_cert_path = lambda: unicode(os.path.join(
    baseconfig.get_default_provider_path(),
    'keys', 'client',
    'openvpn.pem'
))

eipconfig_spec = {
    'provider': {
        'type': unicode,
        'default': u"%s" % PROVIDER_DOMAIN,
        'required': True,
    },
    'transport': {
        'type': unicode,
        'default': u"openvpn",
    },
    'openvpn_protocol': {
        'type': unicode,
        'default': u"tcp"
    },
    'openvpn_port': {
        'type': int,
        'default': 80
    },
    'openvpn_ca_certificate': {
        'type': unicode,  # path
        'default': provider_ca_path
    },
    'openvpn_client_certificate': {
        'type': unicode,  # path
        'default': client_cert_path
    },
    'connect_on_login': {
        'type': bool,
        'default': True
    },
    'block_cleartext_traffic': {
        'type': bool,
        'default': True
    },
    'primary_gateway': {
        'type': unicode,
        'default': u"usa_west",
        'required': True
    },
    'secondary_gateway': {
        'type': unicode,
        'default': u"france"
    },
    'management_password': {
        'type': unicode
    }
}

eipservice_config_spec = {
    'serial': {
        'type': int,
        'required': True,
        'default': 1
    },
    'version': {
        'type': unicode,
        'required': True,
        'default': "0.1.0"
    },
    'capabilities': {
        'type': dict,
        'default': {
            "transport": ["openvpn"],
            "ports": ["80", "53"],
            "protocols": ["udp", "tcp"],
            "static_ips": True,
            "adblock": True}
    },
    'gateways': {
        'type': list,
        'default': [{"country_code": "us",
                    "label": {"en":"west"},
                    "capabilities": {},
                    "hosts": ["1.2.3.4", "1.2.3.5"]}]
    }
}