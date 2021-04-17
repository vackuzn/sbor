import os


def is_hosted():
    return f'{os.path.expanduser("~")}/public_html/static/'


def is_dev(base_dir: str) -> str:
    prod_flag_file = os.path.join(base_dir, '..', 'prod')
    if os.path.exists(prod_flag_file):
        return False
    return True


def get_static_root(base_dir: str) -> str:
    if is_hosted():
        return os.path.join(base_dir, '..', 'static')
    return os.path.join(base_dir, 'static')



def get_media_root(base_dir: str) -> str:
    if is_hosted():
        return os.path.join(base_dir, '..', 'media')
    return os.path.join(base_dir, 'media')
