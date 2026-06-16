# 전체 페이지 목록 집계
# 구조: 메인 1 + 대표 행정동 6 + 지하철역 3 + 생활권·주요 거점 8 + 안내 페이지 5 = 23
from . import main, areas, stations, living, info

PAGES = (
    [main.PAGE]
    + areas.PAGES
    + stations.PAGES
    + living.PAGES
    + info.PAGES
)
