from django.db import models

# Create your models here.
class Bkuser(models.Model):
    username = models.CharField(max_length=64, verbose_name='사용자명')
    password = models.CharField(max_length=64, verbose_name='비밀번호')
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')

    def __str__(self): #클래스를 문자열로 변환했을때 값인데 str함수는 문자열로 어떻게 변환할지  
        return self.username

    class Meta: # meta라는 클래스를 통해 table을 지정한 이유: 구분해서 테이블 만들기 위해서
        db_table = 'book_bkuser'
        verbose_name = '책방사용자'
        verbose_name_plural = '책방사용자' # 복수형