

class AbstractExtremeSportEquip:

    def __init__(self, price_in_uah, weight, year_of_production, producer_name, sport_type):
        self.price_in_uah = price_in_uah
        self.weight = weight
        self.year_of_production = year_of_production
        self.producer_name = producer_name
        self.sport_type = sport_type

    def __str__(self):
        return "price = %s uah, weight = %s kilos, year of production = %s producer name = %s " % (
            self.price_in_uah, self.weight, self.year_of_production, self.producer_name)

    def __repr__(self):
        return "(Sport type: {})".format(self.sport_type)
