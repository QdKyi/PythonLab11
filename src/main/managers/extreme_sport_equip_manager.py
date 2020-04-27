from src.main.models.ice_axe import IceAxe
from src.main.models.kayak import Kayak
from src.main.models.paddles import Paddles
from src.main.models.sport_type import SportType


class ExtremeSportEquipManager:

    def __init__(self, equip_list):
        self.equip_list = equip_list

    def add_one_equip(self, one_equip):
        self.equip_list.append(one_equip)

    def add_equip(self, equip_list):
        self.equip_list.extend(equip_list)

    def find_by_sport_type(self, sport_type):
        """
        >>> equip_manager.find_by_sport_type(SportType.KAYAKING)[0].sport_type
        <SportType.KAYAKING: 1>
        >>> equip_manager.find_by_sport_type(SportType.KAYAKING)[1].sport_type
        <SportType.KAYAKING: 1>
        >>> equip_manager.find_by_sport_type(SportType.KAYAKING)
        [(Sport type: SportType.KAYAKING), (Sport type: SportType.KAYAKING)]
        """
        found_equip = list(
            filter(lambda iterated_equip: sport_type == iterated_equip.sport_type, self.equip_list))
        return found_equip


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True, extraglobs={'equip_manager': ExtremeSportEquipManager(equip_list=[
        IceAxe(4, 4, 4, "dota"),
        Kayak(1, 1, 1, "maran"),
        Paddles(3, 3, 3, "osada"),
        IceAxe(2, 2, 2, "odasa")])})