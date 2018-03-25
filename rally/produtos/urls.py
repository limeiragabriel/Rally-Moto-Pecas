from django.conf.urls import url
from . import views

app_name = 'produtos'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^(?P<produto_id>[0-9]+)/$', views.detail, name='detail'),
    #url(r'^(?P<song_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
    #url(r'^songs/(?P<filter_by>[a-zA_Z]+)/$', views.songs, name='songs'),
    url(r'^create_produto/$', views.create_produto, name='create_produto'),
    #url(r'^(?P<album_id>[0-9]+)/create_song/$', views.create_song, name='create_song'),
    #url(r'^(?P<album_id>[0-9]+)/delete_song/(?P<song_id>[0-9]+)/$', views.delete_song, name='delete_song'),
    #url(r'^(?P<album_id>[0-9]+)/favorite_album/$', views.favorite_album, name='favorite_album'),
    url(r'^(?P<produto_id>[0-9]+)/delete_produto/$', views.delete_produto, name='delete_produto'),

    # /produtos/produto/2/      editar
    url(r'(?P<pk>[0-9]+)/update_produto/$', views.ProdutoUpdate.as_view(), name='produto-update'),

    url(r'^(?P<pk>[0-9]+)$', views.vender_produto, name='vender'),
]
