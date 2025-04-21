from model.creature import Creature
from service import creature as code

sample = Creature(
    name="Yeti",
    country="NEP",
    area="Himalayas",
    description="Yeti is a creature",
    aka="Abominable Snowman",
)


def test_create():
    """크리쳐 생성"""
    resp = code.create(sample)
    assert resp == sample


def test_get_exists():
    """존재하는 크리쳐 검색"""
    resp = code.get_one("Yeti")
    assert resp == sample


def test_get_missing():
    """존재하지 않는 크리쳐 검색"""
    resp = code.get_one("Boxturtle")
    assert resp is None
