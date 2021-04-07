from django.db import models
from django.contrib.auth import get_user_model

user = get_user_model()


class Chat(models.Model):
    roomname = models.CharField(blank=True, max_length=150, verbose_name="اسم اتاق")
    members = models.ManyToManyField(user, null=True, blank=True, verbose_name="اعضای گروه ")

    class Meta:
        verbose_name = 'چت'
        verbose_name_plural = 'چت ها'

    def __str__(self):
        return self.roomname


class Message(models.Model):
    author = models.ForeignKey(user, on_delete=models.CASCADE)
    content = models.TextField()
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def last_message(self, roomname):
        return Message.objects.filter(chat__roomname=roomname).order_by("-timestamp").all()

    class Meta:
        verbose_name = 'پیام'
        verbose_name_plural = 'پیام ها'

    def __str__(self):
        return self.author.username
