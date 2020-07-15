from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import piexif

class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics', blank='True')
    bio = models.TextField(default='', help_text='Enter your bio here', blank='True')


    def __str__(self):
        return f'{self.user.username} Profile'

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     img = Image.open(self.image.path)

    #     if img.height>300 or img.width>300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)

    #         # Prevent image from rotating itself
    #         if "exif" in img.info:
    #             exif_dict = piexif.load(img.info["exif"])

    #             if piexif.ImageIFD.Orientation in exif_dict["0th"]:
    #                 orientation = exif_dict["0th"].pop(piexif.ImageIFD.Orientation)
    #                 exif_bytes = piexif.dump(exif_dict)

    #                 if orientation == 2:
    #                     img = img.transpose(Image.FLIP_LEFT_RIGHT)
    #                 elif orientation == 3:
    #                     img = img.rotate(180)
    #                 elif orientation == 4:
    #                     img = img.rotate(180).transpose(Image.FLIP_LEFT_RIGHT)
    #                 elif orientation == 5:
    #                     img = img.rotate(-90, expand=True).transpose(Image.FLIP_LEFT_RIGHT)
    #                 elif orientation == 6:
    #                     img = img.rotate(-90, expand=True)
    #                 elif orientation == 7:
    #                     img = img.rotate(90, expand=True).transpose(Image.FLIP_LEFT_RIGHT)
    #                 elif orientation == 8:
    #                     img = img.rotate(90, expand=True)
    #         img.save(self.image.path)
