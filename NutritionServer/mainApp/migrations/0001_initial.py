# Generated by Django 2.1 on 2020-07-14 08:21

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('sex', models.IntegerField(default=1)),
                ('age', models.IntegerField(default=0)),
                ('height', models.FloatField(default=0)),
                ('weight', models.FloatField(default=0)),
                ('bmi', models.IntegerField(default=-1)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='CookQuantity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.CharField(default='', max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calorie', models.FloatField(default=0)),
                ('carbohydrate', models.FloatField(default=0)),
                ('fat', models.FloatField(default=0)),
                ('protein', models.FloatField(default=0)),
                ('cellulose', models.FloatField(default=0)),
                ('vitaminA', models.FloatField(default=0)),
                ('vitaminB1', models.FloatField(default=0)),
                ('vitaminB2', models.FloatField(default=0)),
                ('vitaminB6', models.FloatField(default=0)),
                ('vitaminC', models.FloatField(default=0)),
                ('vitaminE', models.FloatField(default=0)),
                ('carotene', models.FloatField(default=0)),
                ('cholesterol', models.FloatField(default=0)),
                ('Mg', models.FloatField(default=0)),
                ('Ca', models.FloatField(default=0)),
                ('Fe', models.FloatField(default=0)),
                ('Zn', models.FloatField(default=0)),
                ('Cu', models.FloatField(default=0)),
                ('Mn', models.FloatField(default=0)),
                ('K', models.FloatField(default=0)),
                ('P', models.FloatField(default=0)),
                ('Na', models.FloatField(default=0)),
                ('Se', models.FloatField(default=0)),
                ('niacin', models.FloatField(default=0)),
                ('thiamine', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='FoodMaterial',
            fields=[
                ('material_name', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('elements', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainApp.Element')),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('name', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('calorie', models.IntegerField(default=-1)),
                ('minutes', models.CharField(max_length=128)),
                ('flavor', models.CharField(max_length=64)),
                ('technology', models.CharField(max_length=16)),
                ('image_url', models.URLField(blank=True, null=True)),
                ('practice', models.TextField(default='')),
                ('menuclassification_set', models.CharField(max_length=128, null=True)),
                ('materials', models.CharField(default='', max_length=200)),
                ('cook_quantity', models.ManyToManyField(through='mainApp.CookQuantity', to='mainApp.FoodMaterial')),
                ('elements', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainApp.Element')),
            ],
        ),
        migrations.CreateModel(
            name='MenuClassification',
            fields=[
                ('classification', models.CharField(max_length=16, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Occupation',
            fields=[
                ('occupation_name', models.CharField(max_length=16, primary_key=True, serialize=False, unique=True)),
                ('bmi_classification', models.IntegerField(default=-1)),
                ('elements', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainApp.Element')),
            ],
        ),
        migrations.CreateModel(
            name='Physique',
            fields=[
                ('physical_name', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('cure_material', models.ManyToManyField(blank=True, null=True, to='mainApp.FoodMaterial')),
                ('elements', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainApp.Element')),
            ],
        ),
        migrations.CreateModel(
            name='Trick',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UploadFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='mainApp/media')),
            ],
        ),
        migrations.CreateModel(
            name='Illness',
            fields=[
                ('menu_classification', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='mainApp.MenuClassification')),
                ('elements', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainApp.Element')),
                ('ill_occupation', models.ManyToManyField(blank=True, null=True, to='mainApp.Occupation')),
            ],
        ),
        migrations.AddField(
            model_name='menuclassification',
            name='cure_occupation',
            field=models.ManyToManyField(blank=True, null=True, to='mainApp.Occupation'),
        ),
        migrations.AddField(
            model_name='history',
            name='menu',
            field=models.ForeignKey(on_delete=True, to='mainApp.Menu'),
        ),
        migrations.AddField(
            model_name='history',
            name='user',
            field=models.ForeignKey(on_delete=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cookquantity',
            name='material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.FoodMaterial'),
        ),
        migrations.AddField(
            model_name='cookquantity',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.Menu'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='eaten_elements',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainApp.Element'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='menu_history',
            field=models.ManyToManyField(blank=True, null=True, through='mainApp.History', to='mainApp.Menu'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='occupation_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainApp.Occupation'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='physical_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainApp.Physique'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AlterUniqueTogether(
            name='cookquantity',
            unique_together={('menu', 'material')},
        ),
        migrations.AddField(
            model_name='myuser',
            name='illness',
            field=models.ManyToManyField(blank=True, null=True, to='mainApp.Illness'),
        ),
    ]
