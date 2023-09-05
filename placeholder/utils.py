import math


__all__ = [
    'get_cosine_factor', 'num_params'
]


def get_cosine_factor(t, T, final=0.01):
    """ As `t` goes from `0` to `T`, return value goes from `1` to `final`
    """
    return final + 0.5 * (1 - final) * (1 + math.cos(t * math.pi / T))


def num_params(model):
    return sum(p.numel() for p in model.parameters() if p.requires_grad)
