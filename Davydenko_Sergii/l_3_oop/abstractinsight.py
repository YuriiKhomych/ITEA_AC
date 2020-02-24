from abc import abstractmethod, ABCMeta
# from meta_insight import MetaInsight


class AbstractInsight(metaclass=ABCMeta):

    @abstractmethod
    def sums_of_metrics(self):
        pass

    @abstractmethod
    def method_report_name(self):
        pass

    @abstractmethod
    def get_attribute_value(self, name):
        pass

    @abstractmethod
    def get_attribute(self, name):
        pass
