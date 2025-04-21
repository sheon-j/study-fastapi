# uv 실습

## 1. uv 설치방법
1. 전역 설치 (추천)
```shell
# macOS, Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Window
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# mac brew
brew install uv
```

2. pip 종속 설치
```shell
pip install uv
```

## 2. 가상 환경
2-1. 파이썬 설치
```shell
uv python install 3.10 3.11 3.12
uv python list
```

2-2. 가상환경

```shell
uv venv --python 3.11
# 가상환경 실행
source .venv/bin/activate
```

## 3. 프로젝트

```shell
uv init    # 새로운 프로젝트 생성
uv add     # 프로젝트 종속성 추가
uv remove  # 프로젝트 종속성 삭제
uv sync    # 프로젝트 종속성을 환경과 동기화
uv lock    # 프로젝트의 종속성 잠금 파일 생성
uv run     # 프로젝트 환경에서 명령어를 실행함
uv tree    # 프로젝트 종속성 트리
uv build   # 프로젝트 배포 아카이브 빌드
uv publish # 프로젝트 패키지 인덱스 게시
```

## 4. 예제

```shell
# 프로젝트 시작
uv init --python 3.11

# fast api, ruff 설치
uv add fastapi --extra standard
uv add --dev ruff

touch main.py
```

```python
# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
  return {"message": "Hello World"}
```

``` shell
# 실행
uv run fastapi dev main.py
```

