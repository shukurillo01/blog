from django.db import models
from datetime import datetime
class Blog(models.Model):
        sarlovha = models.CharField(max_length=250,help_text="Bu yerga maqola sarlovhasini kiriting:")
        tanasi = models.TextField(help_text="maqolani matni:")
        vaqt = models.DateTimeField(help_text="maqola matni", default=datetime.now())
        rasm = models.ImageField(upload_to="blog_rasimlar/",help_text="Maqola uchun rasm",blank=True,null=True)
        def __str__(self,):
                return self.sarlovha
        class Meta:
                verbose_name="Maqola"
                verbose_name_plural="Maqolalar"
                