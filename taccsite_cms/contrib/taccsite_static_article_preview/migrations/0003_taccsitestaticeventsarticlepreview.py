# Generated by Django 2.2.16 on 2021-06-30 15:19

from django.db import migrations, models
import django.db.models.deletion
import djangocms_attributes_field.fields
import djangocms_link.validators
import filer.fields.file


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0012_file_mime_type'),
        ('cms', '0022_auto_20180620_1551'),
        ('taccsite_static_article_preview', '0002_taccsitestaticdocsarticlepreview'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaccsiteStaticEventsArticlePreview',
            fields=[
                ('template', models.CharField(choices=[('default', 'Default')], default='default', max_length=255, verbose_name='Template')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Display name')),
                ('external_link', models.CharField(blank=True, help_text='Provide a link to an external source.', max_length=2040, validators=[djangocms_link.validators.IntranetURLValidator(intranet_host_re=None)], verbose_name='External link')),
                ('anchor', models.CharField(blank=True, help_text='Appends the value only after the internal or external link. Do <em>not</em> include a preceding "#" symbol.', max_length=255, verbose_name='Anchor')),
                ('mailto', models.EmailField(blank=True, max_length=255, verbose_name='Email address')),
                ('phone', models.CharField(blank=True, max_length=255, verbose_name='Phone')),
                ('target', models.CharField(blank=True, choices=[('_blank', 'Open in new window'), ('_self', 'Open in same window'), ('_parent', 'Delegate to parent'), ('_top', 'Delegate to top')], max_length=255, verbose_name='Target')),
                ('attributes', djangocms_attributes_field.fields.AttributesField(blank=True, default=dict, verbose_name='Attributes')),
                ('cmsplugin_ptr', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='taccsite_static_article_preview_taccsitestaticeventsarticlepreview', serialize=False, to='cms.CMSPlugin')),
                ('title_text', models.CharField(default='', help_text='The title for the article.', max_length=50, verbose_name='Title')),
                ('abstract_text', models.TextField(default='', help_text='A summary of the article', verbose_name='Abstract')),
                ('expiry_date', models.DateField(blank=True, help_text='The date upon which the event starts (manual entry). Format: YYYY-MM-DD', null=True, verbose_name='Event End Date')),
                ('publish_date', models.DateField(blank=True, help_text='The date after which the event ends (manual entry). Format: YYYY-MM-DD', null=True, verbose_name='Event Start Date')),
                ('file_link', filer.fields.file.FilerFileField(blank=True, help_text='If provided links a file from the filer app.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='filer.File', verbose_name='File link')),
                ('internal_link', models.ForeignKey(blank=True, help_text='If provided, overrides the external link.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms.Page', verbose_name='Internal link')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
