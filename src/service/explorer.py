import data.explorer as data
from model.explorer import Explorer


def get_all() -> list[Explorer]:
    """모든 탐험가 반환"""
    return data.get_all()


def get_one(name: str) -> Explorer | None:
    """검색한 탐험가 반환"""
    return data.get_one(name)


def create(explorer: Explorer) -> Explorer:
    """탐험가 생성"""
    return data.create(explorer)


def replace(name: str, explorer: Explorer) -> Explorer:
    """탐험가 교체"""
    return data.replace(name, explorer)


def modify(name: str, explorer: Explorer) -> Explorer:
    """탐험가 수정"""
    return data.modify(name, explorer)


def delete(name: str) -> bool:
    """탐험가 삭제"""
    return data.delete(name)
