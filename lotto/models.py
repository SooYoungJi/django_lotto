from django.db import models
from django.utils import timezone
import random

# Create your models here.
class GuessNumbers(models.Model):
    name = models.CharField(max_length=24) # 로또 번호 리스트의 이름
    text = models.CharField(max_length=255) # 로또 번호 리스트에 대한 설명
    lottos = models.CharField(max_length=255, default='[1, 2, 3, 4, 5, 6]') # 로또 번호들이 담길 str
    num_lotto = models.IntegerField(default=5) # 6개 번호 set의 갯수
    update_date = models.DateTimeField()

    """
    def str(self): # Admin page에서 display되는 텍스트에 대한 변경
        return "안녕하세요!!!" # pk는 자동생성됨


    row_1 = GuessNumbers()
    row_1.generate()
    print(row_1.num_lotto) # 5
    print(row_1.name) # 
    print(row_1.lottos) # '[1, 2, 3, 4, 5, 6]'

    print(row_1) # <Object GuessNumbers ~~~>
    print(row_1) # "안녕하세요!!!"

    model = linear_model.LinearRegression()
    print(model) # LinearRegression()
    """

    def generate(self): # 로또 번호를 자동으로 생성
        self.lottos = ""
        origin = list(range(1,46)) # 1~46의 숫자 리스트
        # 6개 번호 set 갯수만큼 1~46 뒤섞은 후 앞의 6개 골라내어 sorting
        for _ in range(0, self.num_lotto):
            random.shuffle(origin) # origin속 수를 랜덤하게 섞어
            guess = origin[:6]
            guess.sort() # [1, 2, 10, 14, 20, 32]
            self.lottos += str(guess) +'\n' # 로또 번호 str에 6개 번호 set 추가
        self.update_date = timezone.now()
        self.save() # GuessNumbers object를 DB에 저장

    def __str__(self): # Admin page에서 display되는 텍스트에 대한 변경
        return "pk {} : {} - {}".format(self.pk, self.name, self.text) # pk는 자동생성됨 / pk == id 같은거
