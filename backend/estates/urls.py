from django.conf.urls import url

from .views import (
    EstateList,
    EstateDetail,
    EstateCreation,
    EstateUpdate,
    EstateDelete
)

urlpatterns = [
    url(r'^$', EstateList.as_view(), name='list'),
    url(r'^(?P<pk>\d+)$', EstateDetail.as_view(), name='detail'),
    url(r'^nuevo$', EstateCreation.as_view(), name='new'),
    url(r'^editar/(?P<pk>\d+)$', EstateUpdate.as_view(), name='edit'),
    url(r'^borrar/(?P<pk>\d+)$', EstateDelete.as_view(), name='delete'),
]
