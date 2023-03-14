import datetime

from django.db import models

# from NoteVault.authentication.models import CustomUser
# Create your models here.


class Notes(models.Model):
    created_at = models.DateTimeField(
        "Created at", editable=False, auto_now=datetime.datetime.now()
    )
    expire_time = models.DateTimeField("Expired at", editable=True)
    user = models.ForeignKey(
        "authentication.CustomUser", related_name="notes", on_delete=models.CASCADE
    )

    def get_by_user_id(self, id):
        return Notes.objects.user.filter(pk=id)
