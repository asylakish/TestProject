# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountsUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'accounts_user'


class AccountsUserGroups(models.Model):
    user = models.ForeignKey(AccountsUser, models.DO_NOTHING)
    group = models.ForeignKey('AuthGroup', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'accounts_user_groups'
        unique_together = (('user', 'group'),)


class AccountsUserUserPermissions(models.Model):
    user = models.ForeignKey(AccountsUser, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'accounts_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AccountsUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class MoviesCertification(models.Model):
    name = models.CharField(unique=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'movies_certification'


class MoviesDirector(models.Model):
    name = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'movies_director'


class MoviesGenre(models.Model):
    name = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'movies_genre'


class MoviesMovie(models.Model):
    name = models.CharField(max_length=250)
    year = models.IntegerField()
    time = models.IntegerField()
    imdb = models.FloatField()
    votes = models.IntegerField()
    meta_score = models.FloatField(blank=True, null=True)
    gross = models.FloatField(blank=True, null=True)
    description = models.TextField()
    certification = models.ForeignKey(MoviesCertification, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'movies_movie'
        ordering = ('name', "year")


class MoviesMoviedirector(models.Model):
    director = models.ForeignKey(MoviesDirector, models.DO_NOTHING)
    movie = models.ForeignKey(MoviesMovie, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'movies_moviedirector'
        unique_together = (('movie', 'director'),)


class MoviesMoviegenre(models.Model):
    genre = models.ForeignKey(MoviesGenre, models.DO_NOTHING)
    movie = models.ForeignKey(MoviesMovie, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'movies_moviegenre'
        unique_together = (('movie', 'genre'),)


class MoviesMoviestar(models.Model):
    movie = models.ForeignKey(MoviesMovie, models.DO_NOTHING)
    star = models.ForeignKey('MoviesStar', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'movies_moviestar'
        unique_together = (('movie', 'star'),)


class MoviesStar(models.Model):
    name = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'movies_star'
