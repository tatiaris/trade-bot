from typing import List, Optional, Tuple


def sma(values: List[float], days: int) -> List[float]:
    """
    Simple Moving Average
    https://www.investopedia.com/terms/s/sma.asp
    :param values: list of values
    :param days: how many days should be considered in each average
    :return: list of simple moving averages
    """
    cur = sum(values[:days])
    out = [cur/days]
    for value_add, value_sub in zip(values[days:], values):
        cur += value_add - value_sub
        out.append(cur/days)
    return out


def ema(values: List[float], days: Optional[int] = None, smoothing_factor: float = 2) -> List[float]:
    """
    Exponential Moving Average
    https://www.investopedia.com/terms/e/ema.asp
    :param values: list of values
    :param days: how many days should be considered in each average
    :param smoothing_factor: higher smoothing factor weighs more recent observations higher
    :return: list of exponential moving average values
    """
    multiplier = smoothing_factor / (1 + days)
    prev_ema = sum(values[:days]) / days  # SMA of first n days
    out = []  # alternative: out = [prev_ema]
    for value in values[days:]:
        new_ema = value * multiplier + prev_ema * (1 - multiplier)  # EMA Equation
        out.append(new_ema)
        prev_ema = new_ema
    return out


def macd(values: List[float], smoothing_factor: float = 2) -> Tuple[List[float], List[float], List[float]]:
    """
    Moving Average Convergence Divergence
    https://www.investopedia.com/terms/m/macd.asp#:~:text=Moving%20Average%20Convergence%20Divergence%20(MACD)%20is%20a%20trend%2Dfollowing,from%20the%2012%2Dperiod%20EMA.
    :param values: list of values
    :param smoothing_factor: used in EMA, higher smoothing factor weighs more recent observations higher
    :return:
    """
    ema_12 = ema(values, 12, smoothing_factor)
    ema_26 = ema(values, 26, smoothing_factor)

    macd_values = [x - y for x, y in zip(ema_12, ema_26)]
    macd_signal = ema(macd_values, 9, smoothing_factor)
    macd_dif = [x - y for x, y in zip(macd_values, macd_signal)]

    return macd_values, macd_signal, macd_dif


def cum_sum(values: List[float]) -> List[float]:
    """ Cumulative Summation """
    out = []
    current_cum_sum = 0  # cumulative sum
    for value in enumerate(values):
        current_cum_sum += value
        out.append(current_cum_sum)

    # cum_avrg = [x/i for i, x in enumerate(out, 1)]

    return out
