from error import Duplicate, Missing
from model.explorer import Explorer

from . import IntegrityError, curs

curs.execute("""
    create table if not exists explorer(
    name text primary key,
    country text,
    description text)
""")


def row_to_model(row: tuple) -> Explorer:
    """튜플을 모델로 변환"""
    name, country, description = row
    return Explorer(name, country, description)


def model_to_dict(explorer: Explorer) -> dict:
    """모델을 딕셔너리로 변환"""
    return explorer.model_dump() if explorer else None


def get_one(name: str) -> Explorer:
    """이름으로 조회"""
    qry = """select * from explorer where name=:name"""
    params = {"name": name}
    res = curs.execute(qry, params)
    row = res.fetchone()
    if row:
        return row_to_model(row)
    else:
        raise Missing(f"Explorer {name} not found")


def get_all() -> list[Explorer]:
    """모든 탐험가 조회"""
    qry = """select * from explorer"""
    res = curs.execute(qry)
    return [row_to_model(row) for row in res.fetchall()]


def create(explorer: Explorer) -> bool:
    """탐험가 생성"""
    if not explorer:
        return None
    qry = """
        insert into explorer(name, country, description)
        values(:name, :country, :description)
    """
    params = model_to_dict(explorer)
    try:
        curs.execute(qry, params)
    except IntegrityError:
        raise Duplicate(f"Explorer {explorer.name} already exists")
    return explorer


def modify(name: str, explorer: Explorer) -> Explorer:
    """탐험가 수정"""
    if not (name and explorer):
        return None
    qry = """
        update explorer set country=:country, name=:name, description=:description
        where name=:name_orig
    """
    params = model_to_dict(explorer)
    params["name_orig"] = explorer.name
    curs.execute(qry, params)
    if curs.rowcount == 1:
        return get_one(explorer.name)
    else:
        raise Missing(f"Explorer {name} not found")


def delete(name: str) -> bool:
    """탐험가 삭제"""
    if not name:
        return False
    qry = """
        delete from explorer where name=:name
    """
    params = {"name": name}
    curs.execute(qry, params)
    if curs.rowcount != 1:
        raise Missing(f"Explorer {name} not found")
    return True
