# 탐험가 실습

## 파일 구조

```shell
.
├── data
│   ├── __init__.py
│   ├── creature.py
│   └── explorer.py
├── fake
│   ├── __init__.py
│   ├── creature.py
│   └── explorer.py
├── main.py
├── model
│   ├── __init__.py
│   ├── creature.py
│   └── explorer.py
├── service
│   ├── __init__.py
│   ├── creature.py
│   └── explorer.py
└── web
    ├── __init__.py
    ├── creature.py
    └── explorer.py
```

```mermaid
graph TD
w("web<br>(라우팅)")
s("service<br>(비즈니스 로직)")
m("model<br>(데이터 클래스)")
d("data<br>(실 데이터)")
f("fake<br>(가짜 데이터)")

w <--> s <--> m <--> d & f
```
