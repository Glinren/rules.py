


class _FirstMatchingLoaded:
    def __init__(self, default, rules):
        self._default = default
        self._rules = rules

    def __call__(self, *args, **kwargs):
        for rule in self._rules:
            if rule.predicate(*args, **kwargs):
                return rule.action(*args, **kwargs)
        return self._default

    @property
    def predicate(self):
        return lambda *args, **kwargs: any(rule.predicate( *args,**kwargs) for rule in self._rules)

    @property
    def action(self):
        return self

        
class FirstMatching:
    def __init__(self, default=None):
        self._default = default

    def __call__(self, *rules):
        return _FirstMatchingLoaded(self._default, rules)



class  _DefaultWithExceptionsLoaded:
    def __init__(self, default, rules):
        self._default = default
        self._rules = rules

    def __call__(self, *args, **kwargs):
        for rule in reversed(self._rules):
            if rule.predicate(*args, **kwargs):
                return rule.action(*args, **kwargs)
        return self._default(*args, **kwargs)


    @property
    def pedicate(self):
        return lambda *args, **kwargs: any(rule.predicate( *args,**kwargs) for rule in self._rules)

    @property
    def action(self):
        return self

        
class DefaultWithExceptions:
    def __init__(self, default=lambda *args, **kwargs: None):
        self._default = default

    def __call__(self, *rules):
        return _DefaultWithExceptionsLoaded(self._default, rules)



class  _AccumulateLoaded:
    def __init__(self, accumulator, init, rules):
        self._accumulator = accumulator
        self._init = init
        self._rules = rules

    def __call__(self, *args, **kwargs):
        val = self._init
        for rule in self._rules:
            if rule.predicate(*args, **kwargs):
                val = self._accumulator(val, rule.action(*args, **kwargs))
        return val

    @property
    def predicate(self):
        return lambda *args, **kwargs: any(rule.predicate( *args,**kwargs) for rule in self._rules)

    @property
    def action(self):
        return self

class Accumulate:
    def __init__(self, accumulator, init):
        self._accumulator = accumulator
        self._init = init

    def __call__(self, *rules):
        return _AccumulateLoaded(self._accumulator, self._init, rules)
