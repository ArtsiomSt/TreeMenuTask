from django import template
from ..models import SubMenu


register = template.Library()


@register.inclusion_tag('menuapp/menu.html', takes_context=True)
def draw_menu(context, name):
    menu_items = list(SubMenu.objects.raw(f"SELECT id, title, parent_id, menu_id, slug FROM menuapp_submenu WHERE menu_id = (SELECT id FROM menuapp_menu WHERE menu_name='{name}')"))
    first_layer = list(filter(lambda x: x.parent_id is None, menu_items))
    current_layer = 0
    template_context = {
        "menuname": name,
        "layer": first_layer,
        "current_layer": list(range(current_layer)),
        "menu_items": menu_items,
        "is_first_layer": True
    }
    for item in menu_items:
        if item.get_absolute_url() == context['request'].path:
            template_context['target'] = item.id
            target_root = item
            target_tree = [target_root]
            while True:
                if target_root.parent_id is None or target_root.parent_id == target_root.id:    # if parent_id == self.id then it is submenu of the first layer
                    break
                for item in menu_items:
                    if item.id == target_root.parent_id:
                        target_root = item
                        target_tree.append(target_root)
            template_context['target_tree'] = target_tree
            template_context['target_tree_ids'] = list(map(lambda x: x.id, target_tree))
            break
    else:
        template_context['only_one_layer'] = True
    return template_context


@register.inclusion_tag('menuapp/menu.html', takes_context=True)
def draw_submenu(context, submenu_element, menu_items, current_layer, target_tree, target, target_tree_ids):
    layer = list(filter(lambda x: x.parent_id == submenu_element.id, menu_items))
    current_layer = list(range(len(current_layer)+1))
    template_context = {
        "layer": layer,
        "menu_items": menu_items,
        "current_layer": current_layer,
        'target_tree': target_tree,
        'target': target,
        'target_tree_ids': target_tree_ids,
    }
    if len(current_layer) == len(target_tree) - 1:
        template_context['print_full_layer'] = True
    return template_context
