def round_to_decimals(decimals: int = 5):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            rounded_result = round(result, decimals)
            number = float(f"{rounded_result:.{decimals}f}")
            if number < (10**-3): number = result
            return number
        return wrapper
    return decorator