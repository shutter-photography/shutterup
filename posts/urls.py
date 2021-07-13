from django.conf.urls import url
from posts import views

app_name = 'posts'

urlpatterns = [

    url(r'^options/$',views.Options.as_view(),name='option'),
    url(r'^new-post/$',views.NewPost.as_view(),name='newpost'),
    url(r'^gallery/$',views.DisplayImages.as_view(),name='gallery'),
    url(r'^info/(?P<pk>\d+)/$',views.Detail_post.as_view(),name='info'),
    url(r'^delete/(?P<pk>\d+)/$',views.Delete_image.as_view(),name='delete'),
    url(r'^Updates/$',views.updates_create.as_view(),name='update'),
    url(r'^Updates_list/$',views.Updates_list.as_view(),name='update_list'),
    url(r'^update_info/(?P<pk>\d+)/$',views.Updates_detail.as_view(),name='update_detail'),
    url(r'^update_remove/(?P<pk>\d+)/$',views.Updates_delete.as_view(),name='update_delete'),
]
