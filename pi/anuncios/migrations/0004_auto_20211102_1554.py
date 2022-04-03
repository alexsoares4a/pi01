# Generated by Django 3.2.9 on 2021-11-02 18:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import users.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('anuncios', '0003_auto_20211102_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='avaliacao',
            name='anunciante',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='fk_avaliacao_user2', to='users.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='avaliacao',
            name='cliente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='fk_avaliacao_user1', to='users.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='residencia',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='fk_residencia_user1', to='users.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='produto',
            name='usuario',
            field=models.ForeignKey(default=users.models.User, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fk_produto_user1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='servico',
            name='usuario',
            field=models.ForeignKey(default=users.models.User, on_delete=django.db.models.deletion.CASCADE, related_name='fk_produto_user2', to=settings.AUTH_USER_MODEL),
        ),
    ]