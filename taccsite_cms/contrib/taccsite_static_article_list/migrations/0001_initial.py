# Generated by Django 2.2.16 on 2021-06-29 19:41

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
            name='TaccsiteArticleList',
            fields=[
                ('template', models.CharField(choices=[('default', 'Default')], default='default', max_length=255, verbose_name='Template')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Display name')),
                ('external_link', models.CharField(blank=True, help_text='Provide a link to an external source.', max_length=2040, validators=[djangocms_link.validators.IntranetURLValidator(intranet_host_re=None)], verbose_name='External link')),
                ('anchor', models.CharField(blank=True, help_text='Appends the value only after the internal or external link. Do <em>not</em> include a preceding "#" symbol.', max_length=255, verbose_name='Anchor')),
                ('mailto', models.EmailField(blank=True, max_length=255, verbose_name='Email address')),
                ('phone', models.CharField(blank=True, max_length=255, verbose_name='Phone')),
                ('target', models.CharField(blank=True, choices=[('_blank', 'Open in new window'), ('_self', 'Open in same window'), ('_parent', 'Delegate to parent'), ('_top', 'Delegate to top')], max_length=255, verbose_name='Target')),
                ('attributes', djangocms_attributes_field.fields.AttributesField(blank=True, default=dict, verbose_name='Attributes')),
                ('cmsplugin_ptr', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='taccsite_static_article_list_taccsitearticlelist', serialize=False, to='cms.CMSPlugin')),
                ('title_text', models.CharField(blank=True, help_text='The title at the top of the list.', max_length=100, verbose_name='Title Text')),
                ('layout_type', models.CharField(choices=[('Row Layouts', (('rows-always-N-even', 'Multiple Rows'),)), ('Column Layouts', (('cols-widest-2-even', '2 Equal-Width Columns'), ('cols-widest-2-wide-narr', '2 Columns: 1 Wide, 1 Narrow'), ('cols-widest-2-narr-wide', '2 Columns: 1 Narrow, 1 Wide'), ('cols-widest-3-even', '3 Equal-Width Columns')))], default='Row Layouts', help_text='Layout of the articles within. Notice: All Column Layouts become multiple rows when screen width is narrow.', max_length=255, verbose_name='Layout Option')),
                ('style_type', models.CharField(blank=True, choices=[('Row Layouts', (('rows-divided', 'Dividers Between Articles'), ('rows-gapless', 'Remove Gaps Between Articles'))), ('Column Layouts', (('cols-gapless', 'Remove Gaps Between Articles'),))], help_text='Optional styles for the list itself.', max_length=255, verbose_name='Style Option')),
                ('file_link', filer.fields.file.FilerFileField(blank=True, help_text='If provided links a file from the filer app.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='filer.File', verbose_name='File link')),
                ('internal_link', models.ForeignKey(blank=True, help_text='If provided, overrides the external link.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms.Page', verbose_name='Internal link')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
