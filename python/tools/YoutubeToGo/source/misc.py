def incomplete_function(func) -> function:
    """Decorator to mark a function as incomplete."""
    def wrapper(*args, **kwargs):
        raise NotImplementedError(f'{func.__name__} is not implemented')
    return wrapper