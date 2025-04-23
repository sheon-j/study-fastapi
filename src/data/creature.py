from model.creature import Creature

from . import curs

curs.execute("""
  create table if not exists creature(
    name text primary key,
    description text,
    country text,
    area text,
    aka text
  )
""")


def row_to_model(row: tuple) -> Creature:
    """fetch 결과 튜플를 모델로 변환"""
    name, description, country, area, aka = row
    return Creature(name, description, country, area, aka)


def model_to_dict(creature: Creature) -> dict:
    """Pydantic 모델을 딕셔너리로 변환"""
    return creature.model_dump()


def get_one(name: str) -> Creature:
    """이름으로 하나의 데이터를 조회"""
    qry = "select * from creature where name=:name"
    params = {"name": name}
    curs.execute(qry, params)
    row = curs.fetchone()
    return row_to_model(row)


def get_all() -> list[Creature]:
    """모든 데이터를 조회"""
    qry = "select * from creature"
    curs.execute(qry)
    rows = curs.fetchall()
    return [row_to_model(row) for row in rows]


def create(creature: Creature) -> Creature:
    """데이터 생성"""
    qry = """
      insert into creature(name, description, country, area, aka)
      values(:name, :description, :country, :area, :aka)
    """
    params = model_to_dict(creature)
    curs.execute(qry, params)
    return creature


def modify(creature: Creature) -> Creature:
    """데이터 수정"""
    qry = """
      update creature set 
      country=:country,
      name=:name,
      description=:description, 
      area=:area, 
      aka=:aka 
      where name=:name_orig
    """
    params = model_to_dict(creature)
    params["name_orig"] = creature.name
    _ = curs.execute(qry, params)
    curs.execute(qry, params)
    return creature


def replace(creature: Creature) -> Creature:
    """데이터 교체"""
    return creature


def delete(creature: Creature) -> None:
    """데이터 삭제"""
    qry = "delete from creature where name=:name"
    params = {"name": creature.name}
    res = curs.execute(qry, params)
    return bool(res)
