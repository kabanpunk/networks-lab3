from dataclasses import dataclass, asdict


def dataclass_to_dict(dc):
    """
    :param dc: dataclass object
    :return: a dictionary created from a dataclass whose elements keys are None are not added
    """
    return {k: v for k, v in asdict(dc).items() if v}
