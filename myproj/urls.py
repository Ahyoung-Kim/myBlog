"""myproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from myapp import views
from django.conf import settings  # media
from django.conf.urls.static import static  # media

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.base, name='base'),
    path('diary/', views.diary, name='diary'),

    path('', views.home, name='home'),

    path('postform/', views.post_form, name='post_form'),

    # 만약 post.id 가 1이라면 127.0.0.1:8000/detail/1 url에선
    # post.id가 1인 게시글을 보여주어야 함
    # 이때 views.py의 detail() 함수의 첫번째 인수는 request, 두번째 인수는 post_id
    path('detail/<int:post_id>', views.detail, name='detail'),

    # 댓글 객체를 보여줄 함수
    path('comment/<int:post_id>', views.comment, name='comment'),
]

# media 파일을 접근할 수 있는 url도 추가해야 함 (외우는 것이 좋음)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
