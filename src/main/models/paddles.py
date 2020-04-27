from src.main.models.abstract_extreme_sport_equip import AbstractExtremeSportEquip
from src.main.models.sport_type import SportType


class Paddles(AbstractExtremeSportEquip):

    def __init__(self, price_in_uah, weight, year_of_production, producer_name, sport_type=SportType.KAYAKING,
                 lenght=1):
        super().__init__(price_in_uah, weight, year_of_production, producer_name, sport_type)
        self.lenght = lenght

    def __str__(self):
        return super().__str__()

    def __repr__(self):
        return super().__repr__()
