from django.db import models


class Pic(models.Model):
    """
    富文本编辑器
    """
    img = models.ImageField(upload_to='pic')
    datetime = models.CharField(max_length=25,blank=True, null=True)

    class Meta:
        db_table = 't_pic'