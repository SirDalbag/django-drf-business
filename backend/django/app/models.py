from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
    MinLengthValidator,
    MaxLengthValidator,
    FileExtensionValidator,
)


class Country(models.Model):
    name = models.CharField(
        unique=True,
        max_length=100,
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(100),
        ],
        null=False,
        blank=False,
        verbose_name="Country",
        help_text="From 1 to 100 characters!",
    )
    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
        verbose_name="Slug",
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Country, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.name} - {self.slug}"

    class Meta:
        app_label = "app"
        ordering = ("name",)
        verbose_name = "Country"
        verbose_name_plural = "Countries"


class City(models.Model):
    name = models.CharField(
        unique=True,
        max_length=100,
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(100),
        ],
        null=False,
        blank=False,
        verbose_name="City",
        help_text="From 1 to 100 characters!",
    )
    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
        verbose_name="Slug",
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(City, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.name} - {self.slug}"

    class Meta:
        app_label = "app"
        ordering = ("name",)
        verbose_name = "City"
        verbose_name_plural = "Cities"


class Department(models.Model):
    name = models.CharField(
        unique=True,
        max_length=255,
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(255),
        ],
        null=False,
        blank=False,
        verbose_name="Department",
        help_text="From 1 to 255 characters!",
    )
    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
        verbose_name="Slug",
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Department, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.name} - {self.slug}"

    class Meta:
        app_label = "app"
        ordering = ("name",)
        verbose_name = "Department"
        verbose_name_plural = "Departments"


class Position(models.Model):
    name = models.CharField(
        unique=True,
        max_length=255,
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(255),
        ],
        null=False,
        blank=False,
        verbose_name="Position",
        help_text="From 1 to 255 characters!",
    )
    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
        verbose_name="Slug",
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Position, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.name} - {self.slug}"

    class Meta:
        app_label = "app"
        ordering = ("name",)
        verbose_name = "Position"
        verbose_name_plural = "Positions"


class Profile(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name="User",
    )
    first_name = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(100),
        ],
        null=False,
        blank=False,
        verbose_name="First Name",
        help_text="From 1 to 100 characters!",
    )
    last_name = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(100),
        ],
        null=False,
        blank=False,
        verbose_name="Last Name",
        help_text="From 1 to 100 characters!",
    )
    birth_date = models.DateField(null=False, blank=False, verbose_name="Birth Date")
    bio = models.TextField(null=True, blank=True, verbose_name="Bio")
    country = models.ForeignKey(
        to=Country,
        on_delete=models.SET_DEFAULT,
        null=False,
        blank=True,
        default="Unknown",
        verbose_name="Country",
    )
    city = models.ForeignKey(
        to=City,
        on_delete=models.SET_DEFAULT,
        null=False,
        blank=True,
        default="Unknown",
        verbose_name="City",
    )
    department = models.ForeignKey(
        to=Department,
        on_delete=models.SET_DEFAULT,
        null=False,
        blank=True,
        default="Unknown",
        verbose_name="Department",
    )
    position = models.ForeignKey(
        to=Position,
        on_delete=models.SET_DEFAULT,
        null=False,
        blank=True,
        default="Unknown",
        verbose_name="Position",
    )
    avatar = models.ImageField(
        upload_to="images/",
        default="images/person.png",
        validators=[FileExtensionValidator(["jpg", "png", "jpeg"])],
        null=False,
        blank=True,
        verbose_name="Avatar",
        help_text="Only .jpg, .png, .jpeg files!",
    )

    def __str__(self) -> str:
        return f"{self.user} - {self.first_name} {self.last_name}"

    class Meta:
        app_label = "app"
        ordering = ("first_name", "last_name")
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"


class Category(models.Model):
    name = models.CharField(
        unique=True,
        max_length=100,
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(100),
        ],
        null=False,
        blank=False,
        verbose_name="Category",
        help_text="From 1 to 100 characters!",
    )
    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
        verbose_name="Slug",
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.name} - {self.slug}"

    class Meta:
        app_label = "app"
        ordering = ("name",)
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Tag(models.Model):
    name = models.CharField(
        unique=True,
        max_length=100,
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(100),
        ],
        null=False,
        blank=False,
        verbose_name="Tag",
        help_text="From 1 to 100 characters!",
    )
    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
        verbose_name="Slug",
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.name} - {self.slug}"

    class Meta:
        app_label = "app"
        ordering = ("name",)
        verbose_name = "Tag"
        verbose_name_plural = "Tags"


class Image(models.Model):
    image = models.ImageField(
        upload_to="images/",
        validators=[FileExtensionValidator(["jpg", "png", "jpeg"])],
        null=False,
        blank=False,
        verbose_name="Image",
        help_text="Only .jpg, .png, .jpeg files!",
    )


class File(models.Model):
    file = models.FileField(
        upload_to="files/",
        validators=[FileExtensionValidator(["pdf", "doc", "docx", "xls", "xlsx"])],
        null=False,
        blank=False,
        verbose_name="File",
        help_text="Only .pdf, .doc, .docx, .xls, .xlsx files!",
    )


class Status(models.Model):
    name = models.CharField(
        unique=True,
        max_length=50,
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(50),
        ],
        null=False,
        blank=False,
        verbose_name="Status",
        help_text="From 1 to 50 characters!",
    )
    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
        verbose_name="Slug",
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.name} - {self.slug}"

    class Meta:
        app_label = "app"
        ordering = ("name",)
        verbose_name = "Status"
        verbose_name_plural = "Statuses"


class Project(models.Model):
    authors = models.ManyToManyField(
        to=User,
        blank=True,
        related_name="authors",
        verbose_name="Authors",
    )
    category = models.ForeignKey(
        to=Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Category",
    )
    tags = models.ManyToManyField(
        to=Tag,
        blank=True,
        related_name="tags",
        verbose_name="Tags",
    )
    title = models.CharField(
        max_length=150,
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(150),
        ],
        null=False,
        blank=False,
        verbose_name="Title",
        help_text="From 1 to 150 characters!",
    )
    description = models.TextField(
        null=True,
        blank=True,
        default="No description",
        verbose_name="Description",
    )
    images = models.ManyToManyField(
        to=Image,
        blank=True,
        related_name="project_images",
        verbose_name="Images",
    )
    files = models.ManyToManyField(
        to=File,
        blank=True,
        related_name="project_files",
        verbose_name="Files",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        null=False,
        verbose_name="Created At",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        null=False,
        verbose_name="Updated At",
    )
    is_active = models.BooleanField(
        default=False,
        verbose_name="Is Active",
    )
    status = models.ForeignKey(
        to=Status,
        on_delete=models.SET_DEFAULT,
        null=False,
        blank=True,
        default="Unknown",
        verbose_name="Status",
    )

    def __str__(self) -> str:
        return f"[{self.id}] {self.title} - {self.created_at}"

    class Meta:
        app_label = "app"
        ordering = ("-created_at",)
        verbose_name = "Project"
        verbose_name_plural = "Projects"

class Rating(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name="User",
    )
    project = models.ForeignKey(
        to=Project,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name="Project",
    )
    value = models.IntegerField(
        validators=[
            MinValueValidator(1), 
            MaxValueValidator(5)
        ],
        null=False,
        blank=False,
        help_text='From 1 to 5!',
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        null=False, 
        verbose_name="Created At",
    )

    def __str__(self) -> str:
        return f"{self.user.username} - [{self.project.id}] {self.project.title} - {self.value}"

    class Meta:
        app_label = "app"
        ordering = ("-created_at",)
        verbose_name = "Rating"
        verbose_name_plural = "Ratings"


class Like(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name="User",
    )
    project = models.ForeignKey(
        to=Project,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name="Project",
    )
    is_like = models.BooleanField(null=False, blank=True, verbose_name="Is Like")

    def __str__(self) -> str:
        return f"{self.user.username} - [{self.project.id}] {self.project.title} - {"Like" if self.is_like else "Dislike"}"

    class Meta:
        app_label = "app"
        verbose_name = "Like"
        verbose_name_plural = "Likes"


class Comment(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name="User",
    )
    project = models.ForeignKey(
        to=Project,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name="Project",
    )
    text = models.TextField(
        null=False, 
        blank=False, 
        verbose_name="Text",
    )
    images = models.ManyToManyField(
        to=Image, 
        blank=True, 
        related_name="comment_images", 
        verbose_name="Images",
    )
    files = models.ManyToManyField(
        to=File, 
        blank=True, 
        related_name="comment_files", 
        verbose_name="Files",
    )
    created_at= models.DateTimeField(
        auto_now_add=True, 
        null=False, 
        verbose_name="Created At",
    )
    updated_at = models.DateTimeField(
        auto_now=True, 
        null=False, 
        verbose_name="Updated At",
    )

class Action(models.Model):
    name = models.CharField(
        unique=True,
        max_length=50,
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(50),
        ],
        null=False,
        blank=False,
        verbose_name="Action",
        help_text="From 1 to 50 characters!",
    )
    description = models.TextField(
        null=True,
        blank=True,
        default="No description",
        verbose_name="Description",
    )

    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
        verbose_name="Slug",
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Position, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.name} - {self.slug}"

    class Meta:
        app_label = "app"
        verbose_name = "Action"
        verbose_name_plural = "Actions"


class ExtendedGroup(models.Model):
    name = models.CharField(
        unique=True,
        max_length=50,
        validators=[
            MinLengthValidator(1),
            MaxLengthValidator(50),
        ],
        null=False,
        blank=False,
        verbose_name="Group",
        help_text="From 1 to 50 characters!",
    )
    description = models.TextField(
        null=True,
        blank=True,
        default="No description",
        verbose_name="Description",
    )
    users = models.ManyToManyField(
        to=User,
        blank=True,
        related_name="users",
        verbose_name="Users",
    )
    actions = models.ManyToManyField(
        to=Action,
        blank=True,
        related_name="actions",
        verbose_name="Actions",
    )

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        app_label = "app"
        verbose_name = "Extended Group"
        verbose_name_plural = "Extended Groups"

