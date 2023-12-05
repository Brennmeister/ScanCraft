import uuid
from pathlib import Path

from django.db import models


def rename_uploaded_file(instance, filename):
    # Set the filename as the uid of the instance
    # set MEDIA_ROOT in settings.py
    return f'uploads/{instance.uid}{Path(filename).suffix}'


class InputFile(models.Model):
    uid = models.CharField(max_length=255, unique=True, editable=False)
    file_input = models.FileField(upload_to=rename_uploaded_file,
                                  verbose_name="Input File", help_text="The file to be processed")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Time created", help_text="Date and Time when the file was uploaded")

    updated_at = models.DateTimeField(auto_now=True)

    status_is_processing = models.BooleanField(
        default=False, verbose_name="Processing", help_text="Indicates weather the file is currently processing.")

    status_is_processed = models.BooleanField(default=False)

    callback_token_update = models.UUIDField(
        default=uuid.uuid4, editable=False)

    class Meta:
        verbose_name = 'Input File'
        verbose_name_plural = 'Input Files'

    def save(self, *args, **kwargs):
        # If file exists, it will be replaced
        if self.pk is not None:
            old_self = InputFile.objects.get(pk=self.pk)
            if self.file and old_self.file != self.file:
                old_self.file.delete()
        return super().save(*args, **kwargs)
