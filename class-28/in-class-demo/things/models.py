from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


# 1. do models.py
# 2. python manage.py makemigrations
# 3. python manage.py migrate
# 4. register Thing with admin.py


class Thing(models.Model):
    name = models.CharField(max_length=256)
    rating = models.IntegerField(default=0)
    # use the first argument of ForeignKey() to link to other tables
    reviewer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        print("the url is:", reverse('thing_detail', args=[str(self.id)]))
        return reverse('thing_detail', args=[str(self.id)])
        # return reverse('thing_list')
