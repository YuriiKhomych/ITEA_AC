class MetaInsight(type):
    # change period value

    def __new__(cls, name, bases, m_dict):
        temp = super().__new__(cls, name, bases, m_dict)
        temp.period = {
            'FacebookInsight': 3,
            'GoogleInsight': 7,
            'TwitterInsight': 10,
        }.get(name, 30)
        return temp

    # def get_api_name(self, name):
    #     try:
    #         return self.get_api_name(name)
    #     except Exception as error:
    #         return error
