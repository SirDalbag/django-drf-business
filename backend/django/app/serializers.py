from rest_framework import serializers
from app import models


class ProjectSerializer(serializers.ModelSerializer):
    """
    Serializer for the Project model.

        Fields:
            id (int): ID of the project.
            title (str): Title of the project.
            description (str): Description of the project.
            authors (list[str]): List of authors of the project.
            category (str): Category of the project.
            tags (list[str]): List of tags of the project.
            images (list[str]): List of image urls of the project.
            files (list[str]): List of file urls of the project.
            status (str): Status of the project.
            is_active (bool): Whether the project is active or not.
            created_at (datetime): Date and time when the project was created.
            updated_at (datetime): Date and time when the project was last updated.

        Methods:
            get_authors(): Returns a list of authors of the project.
            get_category(): Returns the category of the project.
            get_tags(): Returns a list of tags of the project.
            get_images(): Returns a list of image urls of the project.
            get_files(): Returns a list of file urls of the project.
            get_status(): Returns the status of the project.
    """

    authors = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()
    files = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()

    class Meta:
        model = models.Project
        fields = [
            "id",
            "title",
            "description",
            "authors",
            "category",
            "tags",
            "images",
            "files",
            "status",
            "is_active",
            "created_at",
            "updated_at",
        ]

    def get_authors(self, obj):
        """
        Returns a list of project author usernames.

            Parameters:
                obj (Project): The project object.

            Returns:
                (list[str] or None): List of user names of project authors or None if no authors.
        """

        return (
            [author.username for author in obj.authors.all()] if obj.authors else None
        )

    def get_category(self, obj):
        """
        Returns the category of the project.

            Parameters:
                obj (Project): The project object.

            Returns:
                (str or None): Category name of the project or None if no category.
        """

        return obj.category.name if obj.category else None

    def get_tags(self, obj):
        """
        Returns a list of tags of the project.

            Parameters:
                obj (Project): The project object.

            Returns:
                (list[str] or None): List of tag names of the project or None if no tags.
        """

        return [tag.name for tag in obj.tags.all()] if obj.tags else None

    def get_images(self, obj):
        """
        Returns a list of image urls of the project.

            Parameters:
                obj (Project): The project object.

            Returns:
                (list[str] or None): List of image urls of the project or None if no images.
        """

        return [str(image.url) for image in obj.images.all()] if obj.images else None

    def get_files(self, obj):
        """
        Returns a list of file urls of the project.

            Parameters:
                obj (Project): The project object.

            Returns:
                (list[str] or None): List of file urls of the project or None if no files.
        """

        return [str(file.url) for file in obj.files.all()] if obj.files else None

    def get_status(self, obj):
        """
        Returns the project status.

            Parameters:
                obj (Project): The project object.

            Returns:
                (str or None): Status name of the project or None if no status.
        """

        return obj.status.name if obj.status else None
