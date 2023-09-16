class SingleToneClass(object):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = cls
        return cls.instance