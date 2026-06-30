#!/usr/bin/env python3
"""IndexNow 즉시 색인 통보 — 빙·네이버·얀덱스 등 IndexNow 참여 엔진에 알린다.

IndexNow 는 하나의 엔드포인트에 보내면 참여 검색엔진 전체에 공유된다.
네이버(Naver)·빙(Bing)·얀덱스(Yandex)·Seznam 이 참여한다. (구글은 미참여 →
구글은 scripts/google_index.py 또는 Search Console 사용)

사용법:
    # 전체(sitemap.xml 의 모든 색인 URL) 통보
    python3 scripts/indexnow.py

    # 특정 URL 만 통보 (글/페이지 새로 올렸을 때)
    python3 scripts/indexnow.py https://osan-massage.netlify.app/osan/won-dong-area-chuljangmassage/

키 파일은 빌드 시 루트에 "{KEY}.txt" 로 게시된다(build.py). 사이트가 배포되어
그 파일이 공개 접근 가능해야 통보가 검증된다.
"""
import json
import os
import re
import sys
import urllib.request
from urllib.parse import urlsplit

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from content.site import BASE_URL, INDEXNOW_KEY  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENDPOINT = "https://api.indexnow.org/IndexNow"
BASE = BASE_URL.rstrip("/")
HOST = urlsplit(BASE).netloc


def sitemap_urls():
    path = os.path.join(ROOT, "sitemap.xml")
    if not os.path.exists(path):
        sys.exit("sitemap.xml 이 없습니다. 먼저 `python3 build.py` 를 실행하세요.")
    with open(path, encoding="utf-8") as f:
        return re.findall(r"<loc>(.*?)</loc>", f.read())


def submit(urls):
    urls = [u for u in urls if u.startswith(BASE)]
    if not urls:
        sys.exit("통보할 URL 이 없습니다. (모든 URL 은 사이트 도메인과 같아야 함)")
    payload = {
        "host": HOST,
        "key": INDEXNOW_KEY,
        "keyLocation": f"{BASE}/{INDEXNOW_KEY}.txt",
        "urlList": urls,
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        ENDPOINT, data=data,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            code = resp.status
            body = resp.read().decode("utf-8", "ignore")
    except urllib.error.HTTPError as e:
        code = e.code
        body = e.read().decode("utf-8", "ignore")
    print(f"POST {ENDPOINT} → {code}")
    # 200/202 = 정상 접수. 키 검증 실패 시 403, 형식 오류 422.
    for u in urls:
        print("  •", u)
    if body.strip():
        print("응답:", body.strip())
    if code not in (200, 202):
        sys.exit(f"IndexNow 통보 실패(코드 {code}). 키 파일 공개 여부를 확인하세요.")
    print(f"\n{len(urls)}개 URL 을 IndexNow(빙·네이버·얀덱스 등)에 통보했습니다.")


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    submit(args if args else sitemap_urls())
