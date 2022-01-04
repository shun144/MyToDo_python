from django.db import models

class Status(models.Model):
  status = models.CharField('状態名称', max_length=5, blank=False, unique=True)
  
  def __str__(self):
    return self.status

class Todo(models.Model):
  disp_no = models.PositiveSmallIntegerField('表示順', blank=False)
  title = models.CharField('タイトル', max_length=50, blank=False)
  description = models.CharField('詳細', max_length=250, blank=True)
  user_name = models.CharField('担当者', max_length=20, blank=True)
  status = models.ForeignKey(Status, on_delete=models.CASCADE, blank=False, related_name='tasks')
  created_at = models.DateTimeField('作成日時', auto_now_add=True)
  updated_at = models.DateTimeField('更新日時', auto_now=True)

  def __str__(self):
    return self.title



