#!/usr/bin/env python3
""" comments """


def schools_by_topic(mongo_collection, topic):
    """_summary_

    Args:
        mongo_collection (_type_): _description_
        topic (_type_): _description_

    Returns:
        _type_: _description_
    """
    return mongo_collection.find({"topic": topic})
