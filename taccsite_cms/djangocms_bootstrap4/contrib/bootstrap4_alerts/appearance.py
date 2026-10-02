ALERT_APPEARANCE_ATTR = 'data-cms-alert-appearance'
ALERT_APPEARANCE_ATTR_LEGACY = 'data-cms-alert-style'
ALERT_APPEARANCE_BOOTSTRAP = 'bootstrap'
ALERT_APPEARANCE_ADMONITION = 'admonition'


def get_alert_appearance(instance):
    attrs = instance.attributes or {}
    if ALERT_APPEARANCE_ATTR in attrs:
        return attrs[ALERT_APPEARANCE_ATTR]
    legacy = attrs.get(ALERT_APPEARANCE_ATTR_LEGACY)
    if legacy:
        return legacy
    return ALERT_APPEARANCE_BOOTSTRAP


def appearance_attributes(appearance):
    if appearance == ALERT_APPEARANCE_BOOTSTRAP:
        return {ALERT_APPEARANCE_ATTR: ALERT_APPEARANCE_BOOTSTRAP}
    return {ALERT_APPEARANCE_ATTR: appearance}
