from django.urls import path
from myblog.views import PostListView, PostDetailView, PostDeleteView, PostCreateView, PostUpdateView
urlpatterns = [
    path('blog/', PostListView.as_view(), name='post_list'),
    path('blog/create', PostCreateView.as_view(), name='post_create'),
    path('blog/<pk>', PostDetailView.as_view(), name='post_detail'),
    path('blog/<pk>/delete', PostDeleteView.as_view(), name='post_delete'),
    path('blog/<pk>/update', PostUpdateView.as_view(), name='post_update'),
]
