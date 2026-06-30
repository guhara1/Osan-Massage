# 사이트 공통 설정
# 배포 도메인 (Netlify)
BASE_URL = "https://osan-massage.netlify.app"

BRAND = "간다GO"
PHONE = "0508-202-4719"
PHONE_DISPLAY = "0508-202-4719"

# 사이트 한 줄 소개 (RSS 채널 설명 등에 사용)
SITE_DESCRIPTION = "경기도 오산시 전지역 방문 출장마사지·홈타이 예약 안내"

# IndexNow 키 — 빙·네이버·얀덱스 등에 즉시 색인 통보용.
# 빌드 시 루트에 "{KEY}.txt" 파일로 게시되며, scripts/indexnow.py 가 이 값을 사용한다.
INDEXNOW_KEY = "0c5d79c6bdc0632c61e9cfaee09f26df"

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
