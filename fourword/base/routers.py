from rest_framework import routers


class BaseCredyRouter(routers.SimpleRouter):
    """Base abstract Router class."""
    def extend(self, extended_router=None):
        """Method to extend routes of other Django app(s)."""
        if extended_router:
            self.registry.extend(extended_router.registry)
