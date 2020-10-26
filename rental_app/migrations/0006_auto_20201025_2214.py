from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('rental_app', '0005_remove_customer_room_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='book',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='room_number',
        ),
    ]
