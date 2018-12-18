


def and_(*predicates):
    def and_core(*args, **kwargs):
        return all(predicate(*args, **kwargs) for predicate in predicates)
    return and_core


def or_(*predicates):
    def or_core(*args, **kwargs):
        return any(predicate(*args, **kwargs) for predicate in predicates)
    return or_core
