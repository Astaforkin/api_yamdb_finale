from rest_framework import serializers

from reviews.models import Category, Comment, Genre, Review, Title
from users.models import User
from users.validators import username_validation


class UserSerializer(serializers.ModelSerializer):
    """Serializer for user model."""
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'role'
        )


class SignupSerializer(serializers.ModelSerializer):
    """Signup serializer for user model."""
    class Meta:
        model = User
        fields = (
            'username',
            'email'
        )

    def validate_username(self, value):
        """Validate username."""
        username_validation(value)
        return value


class TokenSerializer(serializers.ModelSerializer):
    """Serializer for token model."""
    username = serializers.CharField(required=True)
    confirmation_code = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'confirmation_code'
        )


class CategorySerializer(serializers.ModelSerializer):
    """Categories Serializer"""
    class Meta:
        model = Category
        exclude = ('id',)
        lookup_field = 'slug'


class GenreSerializer(serializers.ModelSerializer):
    """Genres Serializer"""
    class Meta:
        model = Genre
        exclude = ('id',)
        lookup_field = 'slug'


class TitleSerializer(serializers.ModelSerializer):
    """Serializer for title model."""
    category = serializers.SlugRelatedField(
        slug_field='slug', queryset=Category.objects.all()
    )
    genre = serializers.SlugRelatedField(
        slug_field='slug', many=True, queryset=Genre.objects.all()
    )
    rating = serializers.IntegerField(
        source='reviews__score__avg',
        read_only=True
    )

    class Meta:
        model = Title
        fields = (
            'id',
            'name',
            'year',
            'category',
            'genre',
            'description',
            'rating',
        )


class GetTitleSerializer(serializers.ModelSerializer):
    """Get title serializer."""
    category = CategorySerializer(read_only=True)
    genre = GenreSerializer(read_only=True, many=True)
    rating = serializers.IntegerField(
        source='reviews__score__avg',
        read_only=True
    )

    class Meta:
        model = Title
        fields = (
            'id',
            'name',
            'year',
            'category',
            'genre',
            'description',
            'rating',
        )


class ReviewSerializer(serializers.ModelSerializer):
    """Review model serializer."""

    author = serializers.StringRelatedField(read_only=True)
    title = serializers.SlugRelatedField(
        slug_field='id',
        many=False,
        read_only=True,
    )

    class Meta:
        model = Review
        fields = (
            'id',
            'text',
            'author',
            'score',
            'pub_date',
            'title',
        )

    def validate(self, data):
        """User can leave only one review for each title."""
        if not self.context.get('request').method == 'POST':
            return data
        author = self.context.get('request').user
        title_id = self.context.get('view').kwargs.get('title_id')
        if Review.objects.filter(author=author, title=title_id).exists():
            raise serializers.ValidationError(
                'You can leave only one review for each title',
            )
        return data

    @staticmethod
    def validate_score(value):
        """Checking that score is in range 1-10."""
        if not 1 <= value <= 10:
            raise serializers.ValidationError('Score must be in range 1-10')
        return value


class CommentSerializer(serializers.ModelSerializer):
    """Serializer for Comment model."""

    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username',
    )

    class Meta:
        fields = (
            'id',
            'text',
            'author',
            'pub_date',
        )
        model = Comment
