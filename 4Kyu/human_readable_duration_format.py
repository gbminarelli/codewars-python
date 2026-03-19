# https://www.codewars.com/kata/52742f58faf5485cae000b9a


def format_output_message(units):
    separators = [", ", ", ", ", ", " and ", ""]
    return (
        "".join(
            [
                f"{value} {key}{'s' if value > 1 else ''}{separators.pop()}"
                for key, value in reversed(units.items())
                if value > 0
            ][::-1]
        )
        or "now"
    )


def format_duration(seconds):
    seconds_left, units, units_multipliers = (
        seconds,
        {},
        (
            ("year", 31536000),
            ("day", 86400),
            ("hour", 3600),
            ("minute", 60),
            ("second", 1),
        ),
    )
    for name, multiplier in units_multipliers:
        units[name] = seconds_left // multiplier
        seconds_left %= multiplier
    return format_output_message(units)
