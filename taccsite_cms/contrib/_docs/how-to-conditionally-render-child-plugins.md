# How to Conditionally Render Child Plugins

```handlebars
    {% for plugin_instance in instance.child_plugin_instances %}
      {% if plugin_instance.plugin_type == 'LinkPlugin' %}
        <a href="{{ link }}" <!-- ... -->>
          <!-- ... -->
        </a>
      {% endif %}
    {% endfor %}
```
