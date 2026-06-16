# 사이트 공통 설정
# 배포 도메인 (Cloudflare Pages)
BASE_URL = "https://osan-massage.pages.dev"

BRAND = "간다GO"
PHONE = "0508-202-4719"
PHONE_DISPLAY = "0508-202-4719"

# 상단 메뉴 — 하위 메뉴에는 키워드를 반복하지 않고 지역명·역명만 표시한다.
# 구조: 오산시 → 대표 행정동 → 지하철역 → 생활권·주요 거점.
# 행정동/역/생활권 허브 페이지는 따로 두지 않고 메인 페이지의 해당 섹션 앵커로 묶는다(얇은 페이지 방지).
NAV = [
    ("홈", "/", []),
    ("대표 행정동별 안내", "/#areas", [
        ("중앙동", "/osan/jungang-dong-chuljangmassage/"),
        ("대원동", "/osan/daewon-dong-chuljangmassage/"),
        ("남촌동", "/osan/namchon-dong-chuljangmassage/"),
        ("신장동", "/osan/sinjang-dong-chuljangmassage/"),
        ("세마동", "/osan/sema-dong-chuljangmassage/"),
        ("초평동", "/osan/chopyeong-dong-chuljangmassage/"),
    ]),
    ("지하철역별 안내", "/#stations", [
        ("오산역", "/osan/osan-station-chuljangmassage/"),
        ("오산대역", "/osan/osandae-station-chuljangmassage/"),
        ("세마역", "/osan/sema-station-chuljangmassage/"),
    ]),
    ("생활권·주요 거점별 안내", "/#living", [
        ("세교지구", "/osan/segyeo-area-chuljangmassage/"),
        ("운암지구", "/osan/unam-area-chuljangmassage/"),
        ("궐동", "/osan/gwol-dong-area-chuljangmassage/"),
        ("원동", "/osan/won-dong-area-chuljangmassage/"),
        ("오산역환승센터", "/osan/osan-transfer-center-chuljangmassage/"),
        ("오산시청 인근", "/osan/osan-cityhall-area-chuljangmassage/"),
        ("오산대학교 인근", "/osan/osan-univ-area-chuljangmassage/"),
        ("물향기수목원 인근", "/osan/mulhyanggi-arboretum-area-chuljangmassage/"),
    ]),
    ("예약 안내", "/reservation/", []),
    ("이용 전 확인사항", "/guide/", []),
    ("홈타이 이용 가이드", "/hometai/", []),
    ("고객센터", "/support/", []),
]
