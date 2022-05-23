from distutils.command.upload import upload
from django.db import models  # django의 models improt!!


class Post(models.Model):
    # 데이터마다 타입 명시
    title = models.CharField(max_length=50)  # post의 제목
    body = models.TextField()
    # 첨부한 사진 media/post_photo에 업로드
    photo = models.ImageField(blank=True, null=True, upload_to='post_photo')
    # auto_now_add=True: 자동으로 현재 시간을 추가
    date = models.DateTimeField(auto_now_add=True)
    # admin 사이트에서 Post 객체를 title로 표시

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # Comment 객체는 Post 객체를 참조하기 때문에 외래키 설정
    # on_delete=models.CASCASE : 참조중인 Post 객체가 삭제된다면 해당 댓글도 삭제
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment
