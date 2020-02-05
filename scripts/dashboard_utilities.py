def hyperlinked_image(link_label, image_url, target_url):
    return f'[![{link_label}]({image_url})]({target_url})'


def hyperlinked_text(link_label, target_url):
    return f'[{link_label}]({target_url})'
