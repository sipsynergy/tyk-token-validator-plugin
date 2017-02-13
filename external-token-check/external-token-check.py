from tyk.decorators import *
from gateway import TykGateway as tyk

import json, requests

@Hook
def ExternalTokenValidatorMiddleware(request, session, spec):

    token = request.get_header('Authorization')

    if token is None:
        return request, session

    targetUrl = 'https:/auth.sipsynergy.co.uk/oauth/token'

    r = requests.post(targetUrl, headers={'Authorization': token})

    if r.status_code > 299
        request.object.return_overrides.response_code = 401
        request.object.return_overrides.response_error = 'Not authorized by Auth Server'

    return request, session
