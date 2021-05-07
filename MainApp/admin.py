from PIL import Image

from django.contrib import admin
from django.forms import ModelChoiceField, ModelForm, ValidationError

from .models import *


class LaptopAdminForm(ModelForm):

    MIN_RESOLUTION = (400, 400)
    MAX_IMAGE_SIZE = 3145728

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].help_text = 'Upload a photo with the minimum size: {}x{}, Maximum file size: 3MB'.format(*self.MIN_RESOLUTION)

    def clean_image(self):
        image = self.cleaned_data['image']
        img = Image.open(image)
        print(img.width, img.height)
        min_height, min_weidth = self.MIN_RESOLUTION
        if image.size > self.MAX_IMAGE_SIZE:
            raise ValidationError('file size should not exceed 3MB')             
        if img.height < min_height or img.width < min_weidth:
            raise ValidationError('Resolution is less than minimum') 
        return image


class LaptopAdmin(admin.ModelAdmin):

    form = LaptopAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='laptops'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)



class PhoneAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='phones'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Category)
admin.site.register(Laptop, LaptopAdmin)
admin.site.register(Phone, PhoneAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(Order)
