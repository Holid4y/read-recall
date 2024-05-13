from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractUser

# Create your models here.
from apps.book.models import Book


# from django.core.mail import send_mail
# from users_app.managers import UserManager
def settings_default():
    data = {
        "dark_theme": False,
        "levels": [1, 3, 5, 7, 11]
    }
    return data


class User(AbstractUser):
    first_name = None
    last_name = None
    
    is_active = models.BooleanField("active", default=True)
    activated_email = models.BooleanField("activated_email", default=False)
    email = models.EmailField("email address", blank=False, unique=True)
    settings = models.JSONField(default=settings_default, null=False)

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = "email"
    # objects = UserManager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        unique_together = ('username', 'email',)
        
    # def email_user(self, subject, message, from_email=None, **kwargs):
    #     """Send an email to this user."""
    #     send_mail(subject, message, from_email, [self.email], **kwargs)

class UserBookRelation(models.Model):
    user = models.ForeignKey(User, related_name='book_related_with_user', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='users_related_with_book', on_delete=models.CASCADE)
    target_page = models.IntegerField('target page', blank=False)
    
    def __str__(self) -> str:
        return f"User: {self.user} left a bookmark {self.target_page}. Book: {self.book} "

