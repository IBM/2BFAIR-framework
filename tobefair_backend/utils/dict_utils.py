from collections import defaultdict
from typing import Any, Callable, Dict, List, TypeVar


def access_multilevel_implicit_dict(d=Dict[Any, Any], **kwargs):
    """
    Retrieves value from a specific layer of an implicit nested dictionary.
    Use dict_name<n> to pass the method that allows access of the dictionary
    at the n-th level. Use key<n> to pass the key that should be used
    at the n-th level. An implicit dictionary is a dictionary in which
    values are of a type that contains at least one field which is a dictionary.
    """
    curr_dict = d
    i = 1
    while i <= len(kwargs.keys()) / 2:
        curr_obj = curr_dict[kwargs[f"key{i}"]]
        curr_dict = vars(curr_obj)[kwargs[f"dict_name{i}"]]
        i += 1
    return curr_dict


def remove_empty_list_values(dict: Dict[Any, Any]) -> Dict[Any, Any]:
    no_empty_list_value_dict: Dict[Any, Any] = {}
    for key in dict:
        if dict[key] and len(dict[key]) > 0:
            no_empty_list_value_dict[key] = dict[key]
    return no_empty_list_value_dict


def remove_empty_fields(dict: Dict) -> Dict:
    return {k: v for k, v in dict.items() if v}


Object = TypeVar("Object")
Property = TypeVar("Property")


def group(
    objects: List[Object], property: Callable[[Object], Property]
) -> Dict[Property, List[Object]]:
    d: Dict[Property, List[Object]] = defaultdict(List)
    for object in objects:
        d[property(object)] += [object]
    return d
