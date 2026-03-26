def solve(s):
    lower = sum(c.islower() for c in s)
    upper = sum(c.isupper() for c in s)

    if lower == upper or lower > upper:
        return s.lower()

    else:
        return s.upper()