from django.db import models
from .utils import find_object_data
from PIL import Image
import numpy as np
from io import BytesIO
from django.core.files.base import ContentFile


class Images(models.Model):
    title = models.CharField(max_length=150)
    image = models.FileField(upload_to='users/obmer/')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # open image
        pil_img = Image.open(self.image)

        # convert the image to array and do some processing
        cv_img = np.array(pil_img)
        img = find_object_data(cv_img)

        # convert back to pil image
        im_pil = Image.fromarray(img)

        # save
        buffer = BytesIO()
        im_pil.save(buffer, format='jpeg')
        image_png = buffer.getvalue()

        self.image.save(str(self.image), ContentFile(image_png), save=False)
        super().save(*args, **kwargs)
