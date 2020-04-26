from src.main.models.ice_axe import IceAxe
from src.main.models.kayak import Kayak
from src.main.models.paddles import Paddles
from src.main.models.sort_type import SortType


class ExtremeSportEquipmentManagerUtils:

    @staticmethod
    def sort_by_price(list_of_objects, sort_type=SortType.ascending):
        """
        >>> list_of_objects = [IceAxe(4, 4, 4, "dota"), Kayak(2, 2, 2, "maran"), Paddles(3, 3, 3, "pavlusha")]
        >>> sort_type = SortType.ascending
        >>> ExtremeSportEquipmentManagerUtils.sort_by_price(list_of_objects,sort_type)
        >>> print(list_of_objects[0].price_in_uah)
        2
        >>> print(list_of_objects[1].price_in_uah)
        3
        >>> print(list_of_objects[2].price_in_uah)
        4
        """
        if sort_type == SortType.ascending:
            list_of_objects.sort(key=lambda equip: equip.price_in_uah)
        elif sort_type == SortType.descending:
            list_of_objects.sort(key=lambda equip: equip.price_in_uah, reverse=True)
        else:
            print("Can't sort 'cause of wrong sort_type")

    @staticmethod
    def sort_by_year_of_production(list_of_objects, sort_type=SortType.ascending):
        """
        >>> list_of_objects = [IceAxe(4, 4, 4, "dota"), Kayak(2, 2, 2, "maran"), Paddles(3, 3, 3, "pavlusha")]
        >>> sort_type = SortType.ascending
        >>> ExtremeSportEquipmentManagerUtils.sort_by_price(list_of_objects,sort_type)
        >>> print(list_of_objects[0].year_of_production)
        2
        >>> print(list_of_objects[1].year_of_production)
        3
        >>> print(list_of_objects[2].year_of_production)
        4
        """
        if sort_type == SortType.ascending:
            list_of_objects.sort(key=lambda equip: equip.year_of_production)
        elif sort_type == SortType.descending:
            list_of_objects.sort(key=lambda equip: equip.year_of_production, reverse=True)
        else:
            print("Can't sort 'cause of wrong sort_type")


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)