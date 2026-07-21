def extendBootstrap4LinkPlugin():
    import copy

    from django.utils.translation import gettext_lazy as _

    from cms.plugin_pool import plugin_pool

    from djangocms_bootstrap4.contrib.bootstrap4_link.cms_plugins import Bootstrap4LinkPlugin as OriginalBootstrap4LinkPlugin
    from djangocms_bootstrap4.contrib.bootstrap4_link.models import Bootstrap4Link as OriginalBootstrap4Link

    # IMPORTANT: Do not use a proxy model, or else GH-1099
    # https://github.com/TACC/Core-CMS/issues/1099

    LINK_SIZE_CHOICES = (
        ('btn-sm', _('Small')),
        ('', _('Regular')),
    )

    OriginalBootstrap4Link._meta.get_field('link_size').choices = LINK_SIZE_CHOICES
    OriginalBootstrap4Link._meta.get_field('link_context').verbose_name = _('Type')

    class Bootstrap4LinkPlugin(OriginalBootstrap4LinkPlugin):
        model = OriginalBootstrap4Link

        original_fields = OriginalBootstrap4LinkPlugin.fieldsets[0][1]['fields']
        filtered_fields = tuple(f for f in original_fields if f != ('link_outline', 'link_block'))

        fieldsets = list(copy.deepcopy(OriginalBootstrap4LinkPlugin.fieldsets))
        fieldsets[0] = (None, {'fields': filtered_fields})

    plugin_pool.unregister_plugin(OriginalBootstrap4LinkPlugin)
    plugin_pool.register_plugin(Bootstrap4LinkPlugin)
