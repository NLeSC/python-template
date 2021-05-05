"""Documentation about the {{ cookiecutter.package_name }} module."""


# FIXME: put actual code here
def hello(name):
    """Say hello

    Example docstring using Google docstring style.

    Args:
        name (str): Name to say hello to

    Returns:
        str: Hello message

    Raises:
        ValueError: If `name` is equal to `nobody`

    """
    if name == 'nobody':
        raise ValueError('Can not say hello to nobody')
    return f'Hello {name}!'
