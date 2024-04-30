from django.db import models
from django.db.models.signals import post_save
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
    MinLengthValidator,
    MaxLengthValidator,
    FileExtensionValidator,
)


class Country(models.Model):
    """
    A model to represent a country.

        Fields:
            name (CharField): Country name.
            slug (SlugField): Unique country identifier in the URL.
        
        Methods:
            save(): Overridden object save method, automatically generates a slug from the country name.
    """

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
        """
        Overridden method for saving an object.

        Automatically generates a slug from the country name when saving an object.
        """

        self.slug = slugify(self.name)
        super(Country, self).save(*args, **kwargs)

    def __str__(self) -> str:
        """
        Returns a string representation of the country object.

            Returns:
                (str): A string in the format "Country Name - Slug".
        """

        return f"{self.name} - {self.slug}"

    class Meta:
        app_label = "app"
        ordering = ("name",)
        verbose_name = "Country"
        verbose_name_plural = "Countries"


class City(models.Model):
    """
    A model to represent a city.

        Fields:
            name (CharField): City name.
            slug (SlugField): Unique city identifier in the URL.
        
        Methods:
            save(): Overridden object save method, automatically generates a slug from the city name.
    """

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
        """
        Overridden method for saving an object.

        Automatically generates a slug from the city name when saving an object.
        """

        self.slug = slugify(self.name)
        super(City, self).save(*args, **kwargs)

    def __str__(self) -> str:
        """
        Returns a string representation of the city object.

            Returns:
                (str): A string in the format "City Name - Slug".
        """

        return f"{self.name} - {self.slug}"

    class Meta:
        app_label = "app"
        ordering = ("name",)
        verbose_name = "City"
        verbose_name_plural = "Cities"


class Department(models.Model):
    """
    A model to represent a department.

        Fields:
            name (CharField): Name of the department.
            slug (SlugField): Unique department identifier in the URL.
        
        Methods:
            save(): Overridden object save method, automatically generates a slug from the department name.
    """

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
        """
        Overridden method for saving an object.

        Automatically generates a slug from the department name when saving an object.
        """

        self.slug = slugify(self.name)
        super(Department, self).save(*args, **kwargs)

    def __str__(self) -> str:
        """
        Returns a string representation of the department object.

            Returns:
                (str): A string in the format "Department Name - Slug".
        """

        return f"{self.name} - {self.slug}"

    class Meta:
        app_label = "app"
        ordering = ("name",)
        verbose_name = "Department"
        verbose_name_plural = "Departments"


class Position(models.Model):
    """
    A model to represent a position.

        Fields:
            name (CharField): Name of the position.
            slug (SlugField): Unique position identifier in the URL.
        
        Methods:
            save(): Overridden object save method, automatically generates a slug from the position name.
    """

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
        """
        Overridden method for saving an object.
        
        Automatically generates a slug from the position name when saving an object.
        """

        self.slug = slugify(self.name)
        super(Position, self).save(*args, **kwargs)

    def __str__(self) -> str:
        """
        Returns a string representation of the position object.

            Returns:
                (str): A string in the format "Position Name - Slug".
        """
        return f"{self.name} - {self.slug}"

    class Meta:
        app_label = "app"
        ordering = ("name",)
        verbose_name = "Position"
        verbose_name_plural = "Positions"


class Profile(models.Model):
    """
    A model to represent a user profile.
    
        Fields:
            user (ForeignKey): Foreign key to the user model.
            birth_date (DateField): User's birth date.
            bio (TextField): User's biography.
            country (ForeignKey): Foreign key to the country model.
            city (ForeignKey): Foreign key to the city model.
            department (ForeignKey): Foreign key to the department model.
            position (ForeignKey): Foreign key to the position model.
            avatar (ImageField): User's avatar.
    """

    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name="User",
    )
    birth_date = models.DateField(null=True, blank=True, verbose_name="Birth Date")
    bio = models.TextField(null=True, blank=True, verbose_name="Bio")
    country = models.ForeignKey(
        to=Country,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Country",
    )
    city = models.ForeignKey(
        to=City,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="City",
    )
    department = models.ForeignKey(
        to=Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Department",
    )
    position = models.ForeignKey(
        to=Position,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
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
        """
        Returns a string representation of the profile object.

            Returns:
                (str): A string in the format "Username - Full Name".
        """

        return f"{self.user} - {self.user.get_full_name()}"

    class Meta:
        app_label = "app"
        ordering = ("user__first_name", "user__last_name")
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    Creates a profile for a new user.
    """

    Profile.objects.get_or_create(user=instance)


class Category(models.Model):
    """
    A model to represent a category.

        Fields:
            name (CharField): Name of the category.
            slug (SlugField): Unique category identifier in the URL.
        
        Methods:
            save(): Overridden object save method, automatically generates a slug from the category name.
    """

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
        """
        Overridden method for saving an object.

        Automatically generates a slug from the category name when saving an object.
        """

        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self) -> str:
        """
        Returns a string representation of the category object.

            Returns:
                (str): A string in the format "Category Name - Slug".
        """

        return f"{self.name} - {self.slug}"

    class Meta:
        app_label = "app"
        ordering = ("name",)
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Tag(models.Model):
    """
    A model to represent a tag.

        Fields:
            name (CharField): Name of the tag.
            slug (SlugField): Unique tag identifier in the URL.
        
        Methods:
            save(): Overridden object save method, automatically generates a slug from the tag name.
    """

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
        """
        Overridden method for saving an object.

        Automatically generates a slug from the tag name when saving an object.
        """

        self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)

    def __str__(self) -> str:
        """
        Returns a string representation of the tag object.

            Returns:
                (str): A string in the format "Tag Name - Slug".
        """

        return f"{self.name} - {self.slug}"

    class Meta:
        app_label = "app"
        ordering = ("name",)
        verbose_name = "Tag"
        verbose_name_plural = "Tags"


class Image(models.Model):
    """
    A model to represent an image.

        Fields:
            url (ImageField): URL of the image.
    """

    url = models.ImageField(
        upload_to="images/",
        validators=[FileExtensionValidator(["jpg", "png", "jpeg"])],
        null=False,
        blank=False,
        verbose_name="Image",
        help_text="Only .jpg, .png, .jpeg files!",
    )

    def __str__(self) -> str:
        """
        Returns a string representation of the image object.

            Returns:
                (str): A string in the format "Image URL".
        """

        return f"{self.url}"

    class Meta:
        app_label = "app"
        verbose_name = "Image"
        verbose_name_plural = "Images"


class File(models.Model):
    """
    A model to represent a file.

        Fields:
            url (FileField): URL of the file.
    """

    url = models.FileField(
        upload_to="files/",
        validators=[FileExtensionValidator(["pdf", "doc", "docx", "xls", "xlsx"])],
        null=False,
        blank=False,
        verbose_name="File",
        help_text="Only .pdf, .doc, .docx, .xls, .xlsx files!",
    )

    def __str__(self) -> str:
        """
        Returns a string representation of the file object.

            Returns:
                (str): A string in the format "File URL".
        """

        return f"{self.url}"
    
    class Meta:
        app_label = "app"
        verbose_name = "File"
        verbose_name_plural = "Files"


class Status(models.Model):
    """
    A model to represent a status.

        Fields:
            name (CharField): Name of the status.
            slug (SlugField): Unique status identifier in the URL.
        
        Methods:
            save(): Overridden object save method, automatically generates a slug from the category name.
    """

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
        """
        Overridden method for saving an object.

        Automatically generates a slug from the status name when saving an object.
        """

        self.slug = slugify(self.name)
        super(Status, self).save(*args, **kwargs)

    def __str__(self) -> str:
        """
        Returns a string representation of the status object.

            Returns:
                (str): A string in the format "Status Name - Slug".
        """

        return f"{self.name} - {self.slug}"

    class Meta:
        app_label = "app"
        ordering = ("name",)
        verbose_name = "Status"
        verbose_name_plural = "Statuses"


class Project(models.Model):
    """
    A model to represent a project.

        Fields:
            authors (ManyToManyField): Authors of the project.
            category (ForeignKey): Category of the project.
            tags (ManyToManyField): Tags of the project.
            title (CharField): Title of the project.
            description (TextField): Description of the project.
            images (ManyToManyField): Images of the project.
            files (ManyToManyField): Files of the project.
            status (ForeignKey): Status of the project.
            created_at (DateTimeField): Date and time when the project was created.
            updated_at (DateTimeField): Date and time when the project was updated.
            is_active (BooleanField): Whether the project is active or not.
            status (ForeignKey): Status of the project.
    """

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
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Status",
    )

    def __str__(self) -> str:
        """
        Returns a string representation of the project object.

            Returns:
                (str): A string in the format "[Project ID] Project Title - Created At".
        """

        return f"[{self.id}] {self.title} - {self.created_at}"

    class Meta:
        app_label = "app"
        ordering = ("-created_at",)
        verbose_name = "Project"
        verbose_name_plural = "Projects"

class Rating(models.Model):
    """
    A model to represent a rating.

        Fields:
            user (ForeignKey): User who rated the project.
            project (ForeignKey): Project that was rated.
            value (IntegerField): Value of the rating.
            created_at (DateTimeField): Date and time when the rating was created.
    """

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
        """
        Returns a string representation of the rating object.

            Returns:
                (str): A string in the format "Username - [Project ID] Project Title - Value".
        """

        return f"{self.user.username} - [{self.project.id}] {self.project.title} - {self.value}"

    class Meta:
        app_label = "app"
        ordering = ("-created_at",)
        verbose_name = "Rating"
        verbose_name_plural = "Ratings"


class Like(models.Model):
    """
    A model to represent a like.

        Fields:
            user (ForeignKey): User who liked the project.
            project (ForeignKey): Project that was liked.
            is_like (BooleanField): Whether the project was liked or not.
    """

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
        """
        Returns a string representation of the like object.

            Returns:
                (str): A string in the format "Username - [Project ID] Project Title - Like or Dislike".
        """

        return f"{self.user.username} - [{self.project.id}] {self.project.title} - {"Like" if self.is_like else "Dislike"}"

    class Meta:
        app_label = "app"
        verbose_name = "Like"
        verbose_name_plural = "Likes"


class Comment(models.Model):
    """
    A model to represent a comment.
    
        Fields:
            user (ForeignKey): User who commented the project.
            project (ForeignKey): Project that was commented.
            text (TextField): Text of the comment.
            images (ManyToManyField): Images of the comment.
            files (ManyToManyField): Files of the comment.
            created_at (DateTimeField): Date and time when the comment was created.
            updated_at (DateTimeField): Date and time when the comment was updated.
    """

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

    def __str__(self) -> str:
        """
        Returns a string representation of the comment object.

            Returns:
                (str): A string in the format "Username - [Project ID] Project Title - Text (trimmed to 30 characters)".
        """

        return f"{self.user.username} - [{self.project.id}] {self.project.title} - {self.text[:30]}"

    class Meta:
        app_label = "app"
        ordering = ("-created_at",)
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

class Action(models.Model):
    """
    A model to represent an action.

        Fields:
            name (CharField): Name of the action.
            description (TextField): Description of the action.
            slug (SlugField): Unique action identifier in the URL.
        
        Methods:
            save(): Overridden object save method, automatically generates a slug from the action name.
    """

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
        """
        Overridden method for saving an object.

        Automatically generates a slug from the action name when saving an object.
        """

        self.slug = slugify(self.name)
        super(Position, self).save(*args, **kwargs)

    def __str__(self) -> str:
        """
        Returns a string representation of the action object.

            Returns:
                (str): A string in the format "Action Name - Slug".
        """

        return f"{self.name} - {self.slug}"

    class Meta:
        app_label = "app"
        verbose_name = "Action"
        verbose_name_plural = "Actions"


class ExtendedGroup(models.Model):
    """
    A model to represent an extended group.

        Fields:
            name (CharField): Name of the group.
            description (TextField): Description of the group.
            users (ManyToManyField): Users of the group.
            actions (ManyToManyField): Actions of the group.
    """

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
        """
        Returns a string representation of the extended group object.

            Returns:
                (str): A string in the format "Group Name".
        """
        
        return f"{self.name}"

    class Meta:
        app_label = "app"
        verbose_name = "Extended Group"
        verbose_name_plural = "Extended Groups"

