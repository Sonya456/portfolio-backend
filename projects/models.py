from django.db import models

class Project(models.Model):
    FONT_CHOICES = [
        ('Arial', 'Arial'),
        ('Times New Roman', 'Times New Roman'),
        ('Courier New', 'Courier New'),
        ('Georgia', 'Georgia'),
        ('Verdana', 'Verdana'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    default_image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    font = models.CharField(max_length=50, choices=FONT_CHOICES, default='Arial')

    def __str__(self):
        return self.title


class ProjectElement(models.Model):
    FONT_CHOICES = [
        ('Arial', 'Arial'),
        ('Times New Roman', 'Times New Roman'),
        ('Courier New', 'Courier New'),
        ('Georgia', 'Georgia'),
        ('Verdana', 'Verdana'),
    ]
    
    project = models.ForeignKey(Project, related_name='elements', on_delete=models.CASCADE)
    type = models.CharField(max_length=10)  # 'text' или 'image'
    content = models.TextField(blank=True, null=True)  # для текстового содержимого
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)  # для изображений
    order = models.PositiveIntegerField()
    font = models.CharField(max_length=50, choices=FONT_CHOICES, default='Arial')

    def __str__(self):
        return f"{self.project.title} - {self.type} - {self.order}"




class AboutElement(models.Model):
    FONT_CHOICES = [
        ('Arial', 'Arial'),
        ('Times New Roman', 'Times New Roman'),
        ('Courier New', 'Courier New'),
        ('Georgia', 'Georgia'),
        ('Verdana', 'Verdana'),
    ]



    type = models.CharField(max_length=10)  # 'text' или 'image'
    content = models.TextField(blank=True, null=True)  # для текстового содержимого
    image = models.ImageField(upload_to='about_images/', blank=True, null=True)  # для изображений
    order = models.PositiveIntegerField()
    font = models.CharField(max_length=50, choices=FONT_CHOICES, default='Arial')
    font_size = models.PositiveIntegerField(default=14)  # размер текста

    def __str__(self):
        return f"About Us - {self.type} - {self.order}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"



class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name