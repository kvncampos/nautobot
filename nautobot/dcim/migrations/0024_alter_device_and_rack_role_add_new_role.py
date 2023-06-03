# Generated by Django 3.2.16 on 2022-11-25 11:45

from django.db import migrations, models
import django.db.models.deletion
import nautobot.extras.models.roles


class Migration(migrations.Migration):
    dependencies = [
        ("extras", "0062_collect_roles_from_related_apps_roles"),
        ("dcim", "0023_alter_interface_mac_address"),
    ]

    operations = [
        # ##########
        # Device
        # ##########
        # Setting device role to nullable because device role would be null when
        # conducting reverse migration, resulting in an error.
        migrations.AlterField(
            model_name="device",
            name="device_role",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="devices",
                to="dcim.devicerole",
                null=True,
            ),
        ),
        migrations.RenameField(
            model_name="device",
            old_name="device_role",
            new_name="legacy_role",
        ),
        migrations.AddField(
            model_name="device",
            name="new_role",
            field=nautobot.extras.models.roles.RoleField(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="dcim_device_related",
                to="extras.role",
            ),
        ),
        # ##########
        # Rack
        # ##########
        migrations.RenameField(
            model_name="rack",
            old_name="role",
            new_name="legacy_role",
        ),
        migrations.AddField(
            model_name="rack",
            name="new_role",
            field=nautobot.extras.models.roles.RoleField(
                null=True,
                blank=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="dcim_rack_related",
                to="extras.role",
            ),
        ),
    ]