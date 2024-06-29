# Generated by Django 5.0.2 on 2024-06-28 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company_Staff', '0006_project_company_project_login_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='projectcost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('billingmethod', models.CharField(max_length=255)),
                ('cost', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='grand_total',
            field=models.CharField(max_length=255, null=True),
        ),
    ]