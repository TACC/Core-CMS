from menus.base import Modifier
from menus.menu_pool import menu_pool


class NewTabModifier(Modifier):
    """
    Stamp each CMS nav node with its page's menu target value so the menu
    template can render the correct target="..." attribute on the link.
    Nodes without an explicit target are left unmodified; the existing
    target_blank tag logic then decides (external URLs open in a new tab).

    SEE: https://docs.django-cms.org/en/release-3.11.x/how_to/menus.html#navigation-modifiers
    """

    # Run after built-in CMS modifiers (which use rating ~10)
    rating = 20

    def modify(self, request, nodes, namespace, root_id, post_cut, breadcrumb):
        if post_cut:
            from .models import PageMenuTarget
            node_ids = [n.id for n in nodes if n.id]
            if node_ids:
                targets = dict(
                    PageMenuTarget.objects
                    .filter(extended_object_id__in=node_ids)
                    .exclude(target='')
                    .values_list('extended_object_id', 'target')
                )
                for node in nodes:
                    if node.id in targets:
                        node.attr['target'] = targets[node.id]
        return nodes


menu_pool.register_modifier(NewTabModifier)
