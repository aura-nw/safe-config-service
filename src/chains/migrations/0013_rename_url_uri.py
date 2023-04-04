# Generated by Django 3.2.5 on 2021-07-15 15:07

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("chains", "0012_chain_gas_price_fixed_wei"),
    ]

    operations = [
        migrations.RenameField(
            model_name="chain",
            old_name="block_explorer_url",
            new_name="block_explorer_uri",
        ),
        migrations.RenameField(
            model_name="chain",
            old_name="currency_logo_url",
            new_name="currency_logo_uri",
        ),
        migrations.RenameField(
            model_name="chain",
            old_name="gas_price_oracle_url",
            new_name="gas_price_oracle_uri",
        ),
        migrations.RenameField(
            model_name="chain",
            old_name="rpc_url",
            new_name="rpc_uri",
        ),
        migrations.RenameField(
            model_name="chain",
            old_name="transaction_service_url",
            new_name="transaction_service_uri",
        ),
    ]
