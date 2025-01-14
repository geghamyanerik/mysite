# accounts/models.py
from django.db import models # type: ignore
from django.contrib.auth.models import User # type: ignore

class UserInformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_images/', null=True, blank=True, default='default.jpg')
    def __str__(self):
        return f"{self.user.username}'s Info"
    
# accounts/models.py
from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blogs")
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
