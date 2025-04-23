import data.creature as data
from model.creature import Creature


def get_all() -> list[Creature]:
    """모든 크리쳐 반환"""
    return data.get_all()


def get_one(name: str) -> Creature | None:
    """검색한 크리쳐 반환"""
    return data.get_one(name)


def create(creature: Creature) -> Creature:
    """크리쳐 생성"""
    return data.create(creature)


def replace(name: str, creature: Creature) -> Creature:
    """크리쳐 교체"""
    return data.replace(name, creature)


def modify(name: str, creature: Creature) -> Creature:
    """크리쳐 수정"""
    return data.modify(name, creature)


def delete(name: str) -> bool:
    """크리쳐 삭제"""
    return data.delete(name)
