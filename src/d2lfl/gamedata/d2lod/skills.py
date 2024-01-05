"""
"""

from ...diablo2.data.normalize import Diablo2LookupNormalizer


def d2_lod_skill_lookup_normalizer() -> Diablo2LookupNormalizer:
    n = Diablo2LookupNormalizer()

    n.add_alias("Dopplezon", "Decoy")
    n.add_alias("Enchant Fire", "Enchant")
    n.add_alias("Amplify Damage", "AmpDmg")
    n.add_alias("Raise Skeleton Warrior", "Raise Skeleton")
    n.add_alias("Poison Strike", "Poison Dagger")
    n.add_alias("Blood Golem", "BloodGolem")
    n.add_alias("Iron Golem", "IronGolem")
    n.add_alias("Lower Resist", "LowRes")
    n.add_alias("Fire Golem", "FireGolem")

    return n
