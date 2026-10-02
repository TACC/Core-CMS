ALERT_PRESENTATION_ATTR = 'data-cms-alert-style'
ALERT_PRESENTATION_BOOTSTRAP = 'bootstrap'
ALERT_PRESENTATION_ADMONITION = 'admonition'


def get_alert_presentation(instance):
    attrs = instance.attributes or {}
    return attrs.get(ALERT_PRESENTATION_ATTR, ALERT_PRESENTATION_BOOTSTRAP)


def presentation_attributes(presentation):
    if presentation == ALERT_PRESENTATION_BOOTSTRAP:
        return {}
    return {ALERT_PRESENTATION_ATTR: presentation}
