from baseinsight import BaseInsight
from abc import abstractmethod

# FUC***G abstract class!
class AbstractInsight(BaseInsight):
    @abstractmethod
    def check_api(self, api):
        pass

    @abstractmethod
    def get_attribute_by_name(self, name):
        pass

    @abstractmethod
    def metr_s(self, metrics):
        pass

    @abstractmethod
    def return_rep_ame(self, rep_name):
        pass
