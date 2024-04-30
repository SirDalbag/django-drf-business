import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Action",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="From 1 to 50 characters!",
                        max_length=50,
                        unique=True,
                        validators=[
                            django.core.validators.MinLengthValidator(1),
                            django.core.validators.MaxLengthValidator(50),
                        ],
                        verbose_name="Action",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        default="No description",
                        null=True,
                        verbose_name="Description",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(blank=True, unique=True, verbose_name="Slug"),
                ),
            ],
            options={
                "verbose_name": "Action",
                "verbose_name_plural": "Actions",
            },
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="From 1 to 100 characters!",
                        max_length=100,
                        unique=True,
                        validators=[
                            django.core.validators.MinLengthValidator(1),
                            django.core.validators.MaxLengthValidator(100),
                        ],
                        verbose_name="Category",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(blank=True, unique=True, verbose_name="Slug"),
                ),
            ],
            options={
                "verbose_name": "Category",
                "verbose_name_plural": "Categories",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="City",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="From 1 to 100 characters!",
                        max_length=100,
                        unique=True,
                        validators=[
                            django.core.validators.MinLengthValidator(1),
                            django.core.validators.MaxLengthValidator(100),
                        ],
                        verbose_name="City",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(blank=True, unique=True, verbose_name="Slug"),
                ),
            ],
            options={
                "verbose_name": "City",
                "verbose_name_plural": "Cities",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Country",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="From 1 to 100 characters!",
                        max_length=100,
                        unique=True,
                        validators=[
                            django.core.validators.MinLengthValidator(1),
                            django.core.validators.MaxLengthValidator(100),
                        ],
                        verbose_name="Country",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(blank=True, unique=True, verbose_name="Slug"),
                ),
            ],
            options={
                "verbose_name": "Country",
                "verbose_name_plural": "Countries",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Department",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="From 1 to 255 characters!",
                        max_length=255,
                        unique=True,
                        validators=[
                            django.core.validators.MinLengthValidator(1),
                            django.core.validators.MaxLengthValidator(255),
                        ],
                        verbose_name="Department",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(blank=True, unique=True, verbose_name="Slug"),
                ),
            ],
            options={
                "verbose_name": "Department",
                "verbose_name_plural": "Departments",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="File",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "url",
                    models.FileField(
                        help_text="Only .pdf, .doc, .docx, .xls, .xlsx files!",
                        upload_to="files/",
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                ["pdf", "doc", "docx", "xls", "xlsx"]
                            )
                        ],
                        verbose_name="File",
                    ),
                ),
            ],
            options={
                "verbose_name": "File",
                "verbose_name_plural": "Files",
            },
        ),
        migrations.CreateModel(
            name="Image",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "url",
                    models.ImageField(
                        help_text="Only .jpg, .png, .jpeg files!",
                        upload_to="images/",
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                ["jpg", "png", "jpeg"]
                            )
                        ],
                        verbose_name="Image",
                    ),
                ),
            ],
            options={
                "verbose_name": "Image",
                "verbose_name_plural": "Images",
            },
        ),
        migrations.CreateModel(
            name="Position",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="From 1 to 255 characters!",
                        max_length=255,
                        unique=True,
                        validators=[
                            django.core.validators.MinLengthValidator(1),
                            django.core.validators.MaxLengthValidator(255),
                        ],
                        verbose_name="Position",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(blank=True, unique=True, verbose_name="Slug"),
                ),
            ],
            options={
                "verbose_name": "Position",
                "verbose_name_plural": "Positions",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Status",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="From 1 to 50 characters!",
                        max_length=50,
                        unique=True,
                        validators=[
                            django.core.validators.MinLengthValidator(1),
                            django.core.validators.MaxLengthValidator(50),
                        ],
                        verbose_name="Status",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(blank=True, unique=True, verbose_name="Slug"),
                ),
            ],
            options={
                "verbose_name": "Status",
                "verbose_name_plural": "Statuses",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="From 1 to 100 characters!",
                        max_length=100,
                        unique=True,
                        validators=[
                            django.core.validators.MinLengthValidator(1),
                            django.core.validators.MaxLengthValidator(100),
                        ],
                        verbose_name="Tag",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(blank=True, unique=True, verbose_name="Slug"),
                ),
            ],
            options={
                "verbose_name": "Tag",
                "verbose_name_plural": "Tags",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="ExtendedGroup",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="From 1 to 50 characters!",
                        max_length=50,
                        unique=True,
                        validators=[
                            django.core.validators.MinLengthValidator(1),
                            django.core.validators.MaxLengthValidator(50),
                        ],
                        verbose_name="Group",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        default="No description",
                        null=True,
                        verbose_name="Description",
                    ),
                ),
                (
                    "actions",
                    models.ManyToManyField(
                        blank=True,
                        related_name="actions",
                        to="app.action",
                        verbose_name="Actions",
                    ),
                ),
                (
                    "users",
                    models.ManyToManyField(
                        blank=True,
                        related_name="users",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Users",
                    ),
                ),
            ],
            options={
                "verbose_name": "Extended Group",
                "verbose_name_plural": "Extended Groups",
            },
        ),
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "birth_date",
                    models.DateField(blank=True, null=True, verbose_name="Birth Date"),
                ),
                ("bio", models.TextField(blank=True, null=True, verbose_name="Bio")),
                (
                    "avatar",
                    models.ImageField(
                        blank=True,
                        default="images/person.png",
                        help_text="Only .jpg, .png, .jpeg files!",
                        upload_to="images/",
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                ["jpg", "png", "jpeg"]
                            )
                        ],
                        verbose_name="Avatar",
                    ),
                ),
                (
                    "city",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="app.city",
                        verbose_name="City",
                    ),
                ),
                (
                    "country",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="app.country",
                        verbose_name="Country",
                    ),
                ),
                (
                    "department",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="app.department",
                        verbose_name="Department",
                    ),
                ),
                (
                    "position",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="app.position",
                        verbose_name="Position",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User",
                    ),
                ),
            ],
            options={
                "verbose_name": "Profile",
                "verbose_name_plural": "Profiles",
                "ordering": ("user__first_name", "user__last_name"),
            },
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        help_text="From 1 to 150 characters!",
                        max_length=150,
                        validators=[
                            django.core.validators.MinLengthValidator(1),
                            django.core.validators.MaxLengthValidator(150),
                        ],
                        verbose_name="Title",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        default="No description",
                        null=True,
                        verbose_name="Description",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated At"),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="Is Active"),
                ),
                (
                    "authors",
                    models.ManyToManyField(
                        blank=True,
                        related_name="authors",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Authors",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="app.category",
                        verbose_name="Category",
                    ),
                ),
                (
                    "files",
                    models.ManyToManyField(
                        blank=True,
                        related_name="project_files",
                        to="app.file",
                        verbose_name="Files",
                    ),
                ),
                (
                    "images",
                    models.ManyToManyField(
                        blank=True,
                        related_name="project_images",
                        to="app.image",
                        verbose_name="Images",
                    ),
                ),
                (
                    "status",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="app.status",
                        verbose_name="Status",
                    ),
                ),
                (
                    "tags",
                    models.ManyToManyField(
                        blank=True,
                        related_name="tags",
                        to="app.tag",
                        verbose_name="Tags",
                    ),
                ),
            ],
            options={
                "verbose_name": "Project",
                "verbose_name_plural": "Projects",
                "ordering": ("-created_at",),
            },
        ),
        migrations.CreateModel(
            name="Like",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("is_like", models.BooleanField(blank=True, verbose_name="Is Like")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User",
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.project",
                        verbose_name="Project",
                    ),
                ),
            ],
            options={
                "verbose_name": "Like",
                "verbose_name_plural": "Likes",
            },
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.TextField(verbose_name="Text")),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated At"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User",
                    ),
                ),
                (
                    "files",
                    models.ManyToManyField(
                        blank=True,
                        related_name="comment_files",
                        to="app.file",
                        verbose_name="Files",
                    ),
                ),
                (
                    "images",
                    models.ManyToManyField(
                        blank=True,
                        related_name="comment_images",
                        to="app.image",
                        verbose_name="Images",
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.project",
                        verbose_name="Project",
                    ),
                ),
            ],
            options={
                "verbose_name": "Comment",
                "verbose_name_plural": "Comments",
                "ordering": ("-created_at",),
            },
        ),
        migrations.CreateModel(
            name="Rating",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "value",
                    models.IntegerField(
                        help_text="From 1 to 5!",
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(5),
                        ],
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.project",
                        verbose_name="Project",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User",
                    ),
                ),
            ],
            options={
                "verbose_name": "Rating",
                "verbose_name_plural": "Ratings",
                "ordering": ("-created_at",),
            },
        ),
    ]
