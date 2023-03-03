from django.urls import path
from . import views
app_name = 'bbsnote'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:board_id>/', views.detail, name='detail'),
    path('comment/create/<int:board_id>/', views.comment_create, name='comment_create'),
    path('board/create/', views.board_create, name='board_create'),
]

# path('posts/', views.post_list),
# path('posts/new',views.post_create),
# path('posts/<int:post_id>/edit',views.post_update),
# path('posts/<int:post_id>/delete',views.post_delete),