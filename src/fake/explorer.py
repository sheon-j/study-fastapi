from model.explorer import Explorer

# 데이터 생성
_explorers = [
    Explorer(name="John", country="FR", description="보름달 뜨면 못 만남"),
    Explorer(name="Jane", country="DE", description="벌목도를 들고 다니고 눈이 나쁨"),
]


def get_all() -> list[Explorer]:
    """탐험가 목록 반환"""
    return _explorers


def get_one(name: str) -> Explorer | None:
    """검색한 탐험가 반환"""
    for _explorer in _explorers:
        if _explorer.name == name:
            return _explorer
    return None


def create(explorer: Explorer) -> Explorer:
    """탐험가 생성"""
    return explorer


def modify(name: str, explorer: Explorer) -> Explorer:
    """탐험가 수정"""
    return explorer


def replace(name: str, explorer: Explorer) -> Explorer:
    """탐험가 교체"""
    return explorer


def delete(name: str) -> bool:
    """탐험가 삭제"""
    for _explorer in _explorers:
        if _explorer.name == name:
            return True
    return False
