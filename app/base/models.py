from django.db import models


class BaseFourWordModel(models.Model):
    """Abstract Base model class for all FourWord models.
    Attr:
        created_at (object): Represents timestamp when object was created.
        modified_at (object): Represents timestamp when object was last modified.
    """
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True
