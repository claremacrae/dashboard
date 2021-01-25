def hyperlinked_image(link_label: str, image_url: str, target_url: str) -> str:
    return f'[![{link_label}]({image_url})]({target_url})'


def hyperlinked_text(link_label: str, target_url: str) -> str:
    return f'[{link_label}]({target_url})'


def encode_string(string: str) -> str:
    return string.replace(' ', '%20')
