from model.creature import Creature

_creatures = [
    Creature(
        name="Yeti",
        country="NEP",
        area="Himalayas",
        description="Yeti is a creature",
        aka="Abominable Snowman",
    ),
    Creature(
        name="Bigfoot",
        country="USA",
        area="North America",
        description="Bigfoot is a creature",
        aka="Sasquatch",
    ),
]


def get_all() -> list[Creature]:
    """모든 크리쳐 반환"""
    return _creatures


def get_one(name: str) -> Creature | None:
    """검색한 크리쳐 반환"""
    for _creature in _creatures:
        if _creature.name == name:
            return _creature
    return None


def create(creature: Creature) -> Creature:
    """크리쳐 생성"""
    return creature


def modify(name: str, creature: Creature) -> Creature:
    """크리쳐 수정"""
    return creature


def replace(name: str, creature: Creature) -> Creature:
    """크리쳐 교체"""
    return creature


def delete(name: str) -> bool:
    """크리쳐 삭제"""
    for _creature in _creatures:
        if _creature.name == name:
            return True
    return False
