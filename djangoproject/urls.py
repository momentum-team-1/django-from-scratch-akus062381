"""djangoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from snippet import views as snippet_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    path('snippets/new/', snippet_views.new_snippet, name='new_snippet'),
    path('snippets/', snippet_views.show_snippets, name='show_snippets'),
    path('', snippet_views.home, name='home'),
    path('snippets/<int:snippet_pk>/', snippet_views.snippet_detail, name='snippet_detail'),
    path('snippets/<int:snippet_pk>/edit/', snippet_views.edit_snippet, name='edit_snippet'),
    path('snippets/<int:snippet_pk>/delete/', snippet_views.delete_snippet, name='delete_snippet'),
    path('tags/<str:tag_name>/', snippet_views.view_tag, name='view_tag'),
    path('snippets/list_tags/', snippet_views.list_tags, name='list_tags'),
    path('snippets/search/', snippet_views.search_snippets, name='search_snippets'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns


