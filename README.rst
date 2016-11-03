1. Add "goodTravelRestApp" to your INSTALLED_APPS setting like this::

      INSTALLED_APPS = (
          ...
          'goodTravelRestApp',
      )

2. Include the polls URLconf in your project urls.py like this::
      url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
3. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).