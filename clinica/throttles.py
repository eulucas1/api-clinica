from rest_framework.throttling import AnonRateThrottle

class ConsultaAnonRateThrottle(AnonRateThrottle):
    rate = '5/day'