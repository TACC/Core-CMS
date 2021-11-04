# Generated by Django 2.2.16 on 2021-08-06 04:17

from django.db import migrations, models
import django.db.models.deletion
import djangocms_attributes_field.fields
import djangocms_link.validators
import filer.fields.file


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('filer', '0012_file_mime_type'),
        ('cms', '0022_auto_20180620_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaccsiteSystemSpecs',
            fields=[
                ('template', models.CharField(choices=[('default', 'Default')], default='default', max_length=255, verbose_name='Template')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Display name')),
                ('external_link', models.CharField(blank=True, help_text='Provide a link to an external source.', max_length=2040, validators=[djangocms_link.validators.IntranetURLValidator(intranet_host_re=None)], verbose_name='External link')),
                ('anchor', models.CharField(blank=True, help_text='Appends the value only after the internal or external link. Do <em>not</em> include a preceding "#" symbol.', max_length=255, verbose_name='Anchor')),
                ('mailto', models.EmailField(blank=True, max_length=255, verbose_name='Email address')),
                ('phone', models.CharField(blank=True, max_length=255, verbose_name='Phone')),
                ('target', models.CharField(blank=True, choices=[('_blank', 'Open in new window'), ('_self', 'Open in same window'), ('_parent', 'Delegate to parent'), ('_top', 'Delegate to top')], max_length=255, verbose_name='Target')),
                ('attributes', djangocms_attributes_field.fields.AttributesField(blank=True, default=dict, verbose_name='Attributes')),
                ('cmsplugin_ptr', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='taccsite_system_specs_taccsitesystemspecs', serialize=False, to='cms.CMSPlugin')),
                ('system_desc', models.TextField(default='', help_text='Description of the system machine and mission.', verbose_name='System Description')),
                ('system_processor_count', models.IntegerField(blank=True, help_text='The number of processors in the system', null=True, verbose_name='Processors')),
                ('system_processor_type', models.CharField(blank=True, help_text='The number of processors in the system', max_length=50, verbose_name='Processor Type')),
                ('system_node_ram', models.CharField(blank=True, help_text='The amount of RAM in each node of the system, including the unit. (Reminder: Type "GB" for Gigabyte, not "Gb".)', max_length=50, verbose_name='RAM per Node')),
                ('system_network', models.CharField(blank=True, help_text='The network hardware in the system. (Reminder: Type "Gb" for Gigabit, not GB.)', max_length=50, verbose_name='Network')),
                ('system_performance', models.CharField(blank=True, help_text='The peak performance of the system, including the unit. (Reminder: Type number, then space, then unit; example: "38.8 PetaFLOPS".)', max_length=50, verbose_name='Peak Performance')),
                ('system_memory', models.CharField(blank=True, help_text='The amount of memory for the system, including the unit. (Reminder: Type "PB" for Petabyte, not "Pb".)', max_length=50, verbose_name='Memory')),
                ('other_title', models.CharField(blank=True, help_text='An alternate title to replace "Subsystems and Associated Resources".', max_length=40, verbose_name='Alternate Resources Title')),
                ('other_desc', models.TextField(blank=True, default='', help_text='Description of "Subsystems and Associated Resources".', verbose_name='Resources Description')),
                ('file_link', filer.fields.file.FilerFileField(blank=True, help_text='If provided links a file from the filer app.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='filer.File', verbose_name='File link')),
                ('internal_link', models.ForeignKey(blank=True, help_text='If provided, overrides the external link.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms.Page', verbose_name='Internal link')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
