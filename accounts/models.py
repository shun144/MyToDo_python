# AbstructBaseUserを継承した独自ユーザーモデルを作成
# ユーザー作成メソッドを保持するクラス



from django.db import models
from django.contrib.auth.models import PermissionsMixin, UserManager, AbstractUser
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.validators import UnicodeUsernameValidator, ASCIIUsernameValidator
from django.core.mail import send_mail
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class CustomUserManager(UserManager):
    use_in_migrations = True

    # create_user と create_superuser の共通処理
    def _create_user(self, email, username, password, **extra_fields):

        if not email:
            raise ValueError('email must be set')
        if not username:
            raise ValueError('username must be set')

        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


    # 一般ユーザー作成メソッド
    def create_user(self, username, email=None, password=None, **extra_fields):
        # 管理者を示すフラグ
        extra_fields.setdefault('is_staff', False)      
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(email, username, password, **extra_fields)


    # 管理者ユーザー作成メソッド
    def create_superuser(self, username, email=None, password=None, **extra_fields):

        # 管理者を示すフラグ
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, username, password, **extra_fields)


# カスタムユーザーモデルに対応するクラス
class CustomUser(AbstractUser):
    objects = CustomUserManager()

    def __str__(self):
        return self.email
