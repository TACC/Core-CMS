from django import template

register = template.Library()

@register.filter
def index(indexable, i):
    """
    Custom Template Tag `index`

    Use: Access Setting List Values by Index Number in Templates.

    Load custom tag into template:
        {% load custom_portal_settings %}

    Example settings.py configuration:
        settings_values = [['a','b','c'], ['d','e','f']]

    Template inline usage:
        {{ settings_values|index:x|index:y }}

    Example:
        <div>{{ settings_values|index:0 }}</div>
            # <div>['a','b','c']</div>
        <div>{{ settings_values|index:0|index:2 }}</div>
            # <div>c</div>

    - Also works with for loops:
        {% with settings.BRANDING as branding %}
        <p><ul>
            <li>{{ branding }}</li><br />
            <li>{{ branding|index:0 }}</li><br />
            <li>{{ branding|index:0|index:0 }}</li><br/>
            {% for brand in branding %}
                <li>{{ brand|index:forloop.counter0 }}</li>
                <li>{{ brand|index:forloop.counter }}</li>
                <!--### OR ###-->
                <li>{{ brand|index:0 }}</li>
                <li>{{ brand|index:1 }}</li>
                <li>{{ brand|index:2 }}</li>
                <li>{{ brand|index:3 }}</li>
                <li>{{ brand|index:4 }}</li>
                <li>{{ brand|index:5 }}</li>
            {% endfor %}
        </ul></p>
        {% endwith %}
    """
    return indexable[i]
