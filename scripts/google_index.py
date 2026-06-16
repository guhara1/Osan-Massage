#!/usr/bin/env python3
"""구글 Indexing API 색인 통보 (URL_UPDATED).

구글은 IndexNow 에 참여하지 않으므로, 즉시 통보가 필요하면 이 스크립트를 쓴다.

⚠ 공식적으로 구글 Indexing API 는 JobPosting·BroadcastEvent 구조화 데이터 페이지를
   대상으로 지원한다. 일반 안내 페이지에 대한 통보는 "best-effort" 이며, 정식 경로는
   Search Console 의 sitemap.xml 제출 + RSS 수집이다. (sitemap ping 엔드포인트는
   구글·빙 모두 2023년에 폐지되어 더 이상 동작하지 않는다.)

준비:
  1) Google Cloud 프로젝트에서 "Indexing API" 활성화
  2) 서비스 계정 생성 → JSON 키 발급
  3) Search Console 속성(https://osan-massage.pages.dev/)에 그 서비스 계정 이메일을
     '소유자(Owner)' 로 추가
  4) pip install google-auth requests

사용법:
  export GOOGLE_APPLICATION_CREDENTIALS=/path/service-account.json
  python3 scripts/google_index.py                      # sitemap 전체
  python3 scripts/google_index.py https://.../osan/...  # 특정 URL
  python3 scripts/google_index.py --delete https://...  # 삭제 통보(URL_DELETED)
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from content.site import BASE_URL  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = BASE_URL.rstrip("/")
ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"
SCOPES = ["https://www.googleapis.com/auth/indexing"]


def sitemap_urls():
    path = os.path.join(ROOT, "sitemap.xml")
    if not os.path.exists(path):
        sys.exit("sitemap.xml 이 없습니다. 먼저 `python3 build.py` 를 실행하세요.")
    with open(path, encoding="utf-8") as f:
        return re.findall(r"<loc>(.*?)</loc>", f.read())


def session():
    cred_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    if not cred_path or not os.path.exists(cred_path):
        sys.exit("환경변수 GOOGLE_APPLICATION_CREDENTIALS 에 서비스 계정 JSON 경로를 지정하세요.")
    try:
        from google.oauth2 import service_account
        from google.auth.transport.requests import AuthorizedSession
    except ImportError:
        sys.exit("의존성이 없습니다. `pip install google-auth requests` 를 실행하세요.")
    creds = service_account.Credentials.from_service_account_file(
        cred_path, scopes=SCOPES)
    return AuthorizedSession(creds)


def publish(urls, notif_type):
    urls = [u for u in urls if u.startswith(BASE)]
    if not urls:
        sys.exit("통보할 URL 이 없습니다.")
    sess = session()
    ok = 0
    for u in urls:
        resp = sess.post(ENDPOINT, json={"url": u, "type": notif_type}, timeout=30)
        mark = "✓" if resp.status_code == 200 else "✗"
        print(f"  {mark} [{resp.status_code}] {notif_type}  {u}")
        if resp.status_code != 200:
            print("     ", resp.text.strip()[:300])
        else:
            ok += 1
    print(f"\n{ok}/{len(urls)} URL 통보 성공 (구글 Indexing API).")
    if ok != len(urls):
        sys.exit(1)


if __name__ == "__main__":
    args = sys.argv[1:]
    notif = "URL_DELETED" if "--delete" in args else "URL_UPDATED"
    targets = [a for a in args if not a.startswith("-")]
    publish(targets if targets else sitemap_urls(), notif)
