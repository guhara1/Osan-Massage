# 간다GO — 오산 출장마사지·홈타이 안내 사이트

경기도 오산시 전지역 방문 관리(출장마사지·홈타이) 안내용 지역 SEO 정적 사이트입니다.
예약전화: **0508-202-4719**

## 구조

오산시는 행정구가 없으므로 **오산시 → 대표 행정동 → 지하철역 → 생활권·주요 거점** 순서로 구성합니다.

- 정적 HTML 사이트 — GitHub Pages / Netlify / 일반 웹서버 어디서나 서빙 가능
- `build.py` + `content/` 패키지에서 페이지를 생성하는 빌드 방식
- 생성물(각 디렉터리의 `index.html`, `sitemap.xml`, `robots.txt`)도 저장소에 포함

```
build.py            # 빌드 스크립트 (레이아웃·목차·글자수 검사·sitemap 생성)
content/
  site.py           # 상호(간다GO)·전화·BASE_URL·메뉴 구조
  main.py           # 메인 페이지 (+ WebPage/BreadcrumbList/Organization/FAQPage JSON-LD)
  areas.py          # 대표 행정동 6개 (중앙·대원·남촌·신장·세마·초평)
  stations.py       # 지하철역 3개 (오산·오산대·세마, 모두 1호선/경부선)
  living.py         # 생활권·주요 거점 8개 (세교지구·운암지구·궐동·원동 등)
  info.py           # 예약 안내·이용 전 확인사항·홈타이 가이드·고객센터·개인정보 처리방침
assets/             # CSS, 모바일 내비 JS, 파비콘, OG 이미지
```

## 페이지 구성 (총 23개)

| 구분 | 페이지 | URL |
|------|--------|-----|
| 메인 | 오산 출장마사지·홈타이 | `/` |
| 행정동 | 중앙동 | `/osan/jungang-dong-chuljangmassage/` |
| 행정동 | 대원동 (대원1·2동 통합) | `/osan/daewon-dong-chuljangmassage/` |
| 행정동 | 남촌동 | `/osan/namchon-dong-chuljangmassage/` |
| 행정동 | 신장동 (신장1·2동 통합) | `/osan/sinjang-dong-chuljangmassage/` |
| 행정동 | 세마동 | `/osan/sema-dong-chuljangmassage/` |
| 행정동 | 초평동 | `/osan/chopyeong-dong-chuljangmassage/` |
| 역 | 오산역 (1호선·환승센터) | `/osan/osan-station-chuljangmassage/` |
| 역 | 오산대역 (1호선) | `/osan/osandae-station-chuljangmassage/` |
| 역 | 세마역 (1호선) | `/osan/sema-station-chuljangmassage/` |
| 생활권 | 세교지구 | `/osan/segyeo-area-chuljangmassage/` |
| 생활권 | 운암지구 | `/osan/unam-area-chuljangmassage/` |
| 생활권 | 궐동 | `/osan/gwol-dong-area-chuljangmassage/` |
| 생활권 | 원동 | `/osan/won-dong-area-chuljangmassage/` |
| 거점 | 오산역환승센터 | `/osan/osan-transfer-center-chuljangmassage/` |
| 거점 | 오산시청 인근 | `/osan/osan-cityhall-area-chuljangmassage/` |
| 거점 | 오산대학교 인근 | `/osan/osan-univ-area-chuljangmassage/` |
| 거점 | 물향기수목원 인근 | `/osan/mulhyanggi-arboretum-area-chuljangmassage/` |
| 안내 | 예약 안내 | `/reservation/` |
| 안내 | 이용 전 확인사항 | `/guide/` |
| 안내 | 홈타이 이용 가이드 | `/hometai/` |
| 정책 | 개인정보 처리방침 (noindex) | `/privacy/` |
| 안내 | 고객센터 | `/support/` |

## 빌드

```bash
python3 build.py
```

빌드 시 페이지별 본문 글자수와 색인 여부가 출력됩니다.

## SEO 운영 원칙 (빌드에 강제됨)

- 본문 **2,000자 미만 페이지는 자동 `noindex`** 처리되고 sitemap에서 제외
- 모든 페이지 **메타 디스크립션 80자 이내**
- 행정동은 대표 동 단위만 — 번호 행정동(대원1동·신장2동 등) 개별 페이지 없음
- 역은 역 1개당 페이지 1개 — 오산역도 URL 하나, 출구별·예정노선별 페이지 없음
- 예정역·예정 노선(동탄트램·GTX 등)은 단독 페이지 금지, 본문 보조 설명으로만 처리
- 생활권 페이지는 실제 검색 의도가 있는 거점만 생성하고 본문은 거점마다 다르게 작성
- **지역+역+테마 조합 페이지 없음** (도어웨이 방지)
- 실제 오프라인 매장 주소가 없으므로 **LocalBusiness 대신 Organization Schema** 사용
- 모든 페이지 본문은 페이지별 고유 작성 (지역명만 바꾼 복붙 없음)

## 배포 전 해야 할 일

1. `content/site.py`의 `BASE_URL`을 실제 도메인으로 변경 (현재 `https://osan-massage.pages.dev`)
2. `python3 build.py` 재실행 (canonical·sitemap·rss·robots.txt에 반영됨)
3. Google Search Console / 네이버 서치어드바이저에 `sitemap.xml` 제출

## 빠른 색인(인덱싱) 설정

빌드 시 색인용 파일이 자동 생성됩니다.

| 파일 | 용도 |
|------|------|
| `/sitemap.xml` | 구글·네이버 사이트맵 (lastmod·priority 포함) |
| `/rss.xml` | RSS 피드 — 네이버·구글 발견 속도 향상 (head에 `alternate` 링크 자동 삽입) |
| `/robots.txt` | 전체 허용 + Googlebot·Yeti(네이버)·bingbot 명시 + 사이트맵 |
| `/{INDEXNOW_KEY}.txt` | IndexNow 소유확인 키 파일 (루트 공개) |

### 1) IndexNow — 빙·네이버·얀덱스 즉시 통보 (구글 미참여)

글/페이지를 새로 올리거나 수정하면:

```bash
python3 build.py                                   # 사이트 갱신
python3 scripts/indexnow.py                        # sitemap 전체 통보
python3 scripts/indexnow.py https://osan-massage.pages.dev/osan/won-dong-area-chuljangmassage/  # 특정 URL만
```

- IndexNow 키: `content/site.py`의 `INDEXNOW_KEY`. 키 파일 `/{KEY}.txt`가 **배포되어 공개 접근 가능**해야 통보가 검증됩니다.
- 하나의 엔드포인트(api.indexnow.org)로 보내면 참여 엔진(빙·네이버·얀덱스·Seznam) 전체에 공유됩니다.

### 2) 구글 Indexing API — 구글 즉시 통보 (선택)

구글은 IndexNow에 참여하지 않습니다. 즉시 통보가 필요하면:

```bash
pip install google-auth requests
export GOOGLE_APPLICATION_CREDENTIALS=/path/service-account.json
python3 scripts/google_index.py                    # sitemap 전체
python3 scripts/google_index.py https://osan-massage.pages.dev/...   # 특정 URL
```

준비: Google Cloud에서 Indexing API 활성화 → 서비스 계정 JSON 키 발급 → Search Console 속성에 서비스 계정 이메일을 **소유자**로 추가. (서비스 계정 JSON은 `.gitignore`로 커밋 차단됨)

> 참고: 구글·빙의 **sitemap ping 엔드포인트는 2023년에 폐지**되어 더 이상 동작하지 않습니다.
> 따라서 빠른 색인의 현실적 경로는 **IndexNow(빙·네이버) + 구글 Indexing API/Search Console + RSS**입니다.
> 구글 Indexing API는 공식적으로 JobPosting·BroadcastEvent를 위한 것이라 일반 페이지엔 best-effort이며,
> 정식 경로는 Search Console의 sitemap·RSS 제출입니다.

## OG 검색 썸네일 재생성

```bash
pip install Pillow
python3 scripts/gen_thumbs.py    # assets/og/*.png 재생성
```
