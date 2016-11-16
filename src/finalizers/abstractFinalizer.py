import abc


class AbstractFinalizer(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def final_action():
        pass
