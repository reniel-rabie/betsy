def kelly_criterion(odds: float, probability_of_winning: float) -> float:
    b: float = odds - 1  # Convert decimal odds to profit odds
    p: float = probability_of_winning
    q: float = 1 - p

    f_star: float = (b * p - q) / b

    return f_star
