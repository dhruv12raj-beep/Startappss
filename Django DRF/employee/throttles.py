from rest_framework.throttling import UserRateThrottle

class EmpoloyeeRateThrottle(UserRateThrottle):
    scope = 'employee'