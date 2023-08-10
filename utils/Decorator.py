def round_to_decimals(decimals):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            rounded_result = round(result, decimals)
            return float(f"{rounded_result:.{decimals}f}")
        return wrapper
    return decorator