class params:
    pop_size = 25
    maxD = 500
    minD = -500
    Lambda = 1.5
    pd = 0.25
    dims = 10
    trial = 10
    step_size = 0.01
    iterations = 2000
    @classmethod
    def __init__(self):
        return None
    @classmethod 
    def get_pop(cls):
        return cls.pop_size
    @classmethod 
    def get_pad(cls):
        return cls.pd
    
    @classmethod    
    def get_trial(cls):
        return cls.trial
    @classmethod 
    def get_iterations(cls):
        return cls.iterations
    @classmethod 
    def get_maxD(cls):
        return cls.maxD
    @classmethod 
    def get_pd(cls):
        return cls.pd
    @classmethod 
    def get_minD(cls):
        return cls.minD
    @classmethod 
    def set_maxD(cls, maxDomain):
        cls.maxD = maxDomian
    @classmethod 
    def set_minD(cls, minDomain):
        cls.minD = minDomain
    @classmethod 
    def get_dims(cls):
        return cls.dims
    @classmethod 
    def get_Lambda(cls):
        return cls.Lambda
    @classmethod 
    def set_Lambda(cls, _Lambda):
        cls.Lambda = _lambda
    @classmethod 
    def get_stepsize(cls):
        return cls.step_size