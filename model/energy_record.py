
class EnergyRecord:

    def __init__(self):
        self.__CSDUID = None
        self.__CSD = None
        self.__Period = None
        self.__IndicatorSummaryDescription = None
        self.__UnitOfMeasure = None
        self.__OriginalValue = None

    def get_CSDUID(self):
        return self.__CSDUID

    def set_CSDUID(self, CSDUID):
        self.__CSDUID = CSDUID

    def get_CSD(self):
        return self.__CSD

    def set_CSD(self, CSD):
        self.__CSD = CSD

    def get_Period(self):
        return self.__Period

    def set_Period(self, Period):
        self.__Period = Period

    def get_IndicatorSummaryDescription(self):
        return self.__IndicatorSummaryDescription

    def set_IndicatorSummaryDescription(self, IndicatorSummaryDescription):
        self.__IndicatorSummaryDescription = IndicatorSummaryDescription

    def get_UnitOfMeasure(self):
        return self.__UnitOfMeasure

    def set_UnitOfMeasure(self, UnitOfMeasure):
        self.__UnitOfMeasure = UnitOfMeasure

    def get_OriginValue(self):
        return self.__OriginalValue

    def set_OriginValue(self, OriginValue):
        self.__OriginalValue = OriginValue


