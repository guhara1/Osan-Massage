# 페이지별 검색 썸네일(og:image) 생성기. 다크 럭스 골드 테마, 1200x630.
import os
from PIL import Image, ImageDraw, ImageFont

OUT = "assets/og"
os.makedirs(OUT, exist_ok=True)
W, H = 1200, 630
NAVY=(7,11,20); GOLD=(200,162,94); GOLD_SOFT=(233,215,171); TEXT=(234,237,244); DIM=(151,161,184)
KO="/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc"
SE="/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
def ko(sz): return ImageFont.truetype(KO, sz)
def se(sz): return ImageFont.truetype(SE, sz)
PHONE="0508-202-4719"

# slug -> (tag, line1, line2)
PAGES = {
 # 대표 행정동
 "jungang-dong-chuljangmassage":     ("경기 · 오산", "중앙동 출장마사지", "오산역 · 오산시청 생활권"),
 "daewon-dong-chuljangmassage":      ("경기 · 오산", "대원동 출장마사지", "원동 · 갈곶동 생활권"),
 "namchon-dong-chuljangmassage":     ("경기 · 오산", "남촌동 출장마사지", "궐동 · 가장동 인근 홈타이"),
 "sinjang-dong-chuljangmassage":     ("경기 · 오산", "신장동 출장마사지", "오산대역 · 수청동 생활권"),
 "sema-dong-chuljangmassage":        ("경기 · 오산", "세마동 출장마사지", "세마역 · 세교지구 홈타이"),
 "chopyeong-dong-chuljangmassage":   ("경기 · 오산", "초평동 출장마사지", "누읍 · 두곡 · 탑동 생활권"),
 # 지하철역
 "osan-station-chuljangmassage":     ("경기 · 오산", "오산역 출장마사지", "환승센터 · 중앙동 홈타이"),
 "osandae-station-chuljangmassage":  ("경기 · 오산", "오산대역 출장마사지", "수청동 · 오산대 인근"),
 "sema-station-chuljangmassage":     ("경기 · 오산", "세마역 출장마사지", "세마동 · 세교지구 생활권"),
 # 생활권·주요 거점
 "segyeo-area-chuljangmassage":      ("경기 · 오산", "세교지구 출장마사지", "오산 세교신도시 홈타이"),
 "unam-area-chuljangmassage":        ("경기 · 오산", "운암지구 출장마사지", "오산 중심 주거권"),
 "gwol-dong-area-chuljangmassage":   ("경기 · 오산", "궐동 출장마사지", "남촌동 · 궐동 생활권"),
 "won-dong-area-chuljangmassage":    ("경기 · 오산", "원동 출장마사지", "오산역 남부 생활권"),
 "osan-transfer-center-chuljangmassage":("경기 · 오산", "오산역환승센터 출장마사지", "오산역 중심 교통거점"),
 "osan-cityhall-area-chuljangmassage":("경기 · 오산", "오산시청 인근 출장마사지", "중앙동 행정 · 상권"),
 "osan-univ-area-chuljangmassage":   ("경기 · 오산", "오산대학교 인근 출장마사지", "오산대역 주변 홈타이"),
 "mulhyanggi-arboretum-area-chuljangmassage":("경기 · 오산", "물향기수목원 인근 출장마사지", "수청동 · 신장동 생활권"),
 # 안내 페이지
 "reservation": ("간다GO · 오산", "예약 안내", "방문 절차 · 이동비 · 결제 기준"),
 "guide":       ("간다GO · 오산", "이용 전 확인사항", "준비물 · 위생 · 안전 기준"),
 "hometai":     ("간다GO · 오산", "홈타이 이용 가이드", "진행 방식 · 추천 대상 안내"),
 "support":     ("간다GO · 오산", "고객센터", "공지 · 자주 묻는 질문 · 문의"),
}

def fit(draw, text, font_factory, max_w, start, min_sz=44):
    sz=start
    while sz>min_sz:
        f=font_factory(sz); bb=draw.textbbox((0,0),text,font=f)
        if bb[2]-bb[0]<=max_w: return f
        sz-=4
    return font_factory(min_sz)

def ctext(d,cx,y,text,font,fill):
    bb=d.textbbox((0,0),text,font=font); w=bb[2]-bb[0]
    d.text((cx-w/2-bb[0], y), text, font=font, fill=fill)

def make(slug, tag, l1, l2):
    img=Image.new("RGB",(W,H),NAVY); d=ImageDraw.Draw(img,"RGBA")
    # top gold glow
    for i,r in enumerate(range(540,0,-44)):
        a=int(11*(1-i/13))
        if a>0: d.ellipse([600-r,-300-r//3,600+r,-300+r],fill=(200,162,94,a))
    # frame
    d.rectangle([24,24,W-25,H-25],outline=GOLD,width=3)
    d.rectangle([34,34,W-35,H-35],outline=(200,162,94,90),width=1)
    # tag pill (outline)
    tf=ko(30); bb=d.textbbox((0,0),tag,font=tf); tw=bb[2]-bb[0]
    px0=600-tw/2-26; px1=600+tw/2+26; py0=70; py1=70+54
    d.rounded_rectangle([px0,py0,px1,py1],radius=27,outline=GOLD,width=2)
    d.text((600-tw/2-bb[0], py0+(54-(bb[3]-bb[1]))/2-bb[1]), tag, font=tf, fill=GOLD_SOFT)
    # line1 (auto-fit), line2
    f1=fit(d,l1,ko,1000,96); ctext(d,600,196,l1,f1,GOLD_SOFT)
    f2=fit(d,l2,ko,1000,52); ctext(d,600,322,l2,f2,TEXT)
    # divider
    d.line([520,406,680,406],fill=GOLD,width=3)
    # brand row: G ring + 간다GO
    cx,cy,R=600,468,40
    # measure brand text to center the (mark + gap + text) group
    bf=ko(46); tb=d.textbbox((0,0),"간다GO",font=bf); btw=tb[2]-tb[0]
    gap=18; total=R*2+gap+btw; gx=600-total/2+R  # mark center x
    d.ellipse([gx-R,cy-R,gx+R,cy+R],fill=(10,17,32,255))
    d.ellipse([gx-R+3,cy-R+3,gx+R-3,cy+R-3],outline=GOLD,width=4)
    gf=se(50); gbb=d.textbbox((0,0),"G",font=gf)
    d.text((gx-(gbb[2]-gbb[0])/2-gbb[0], cy-(gbb[3]-gbb[1])/2-gbb[1]),"G",font=gf,fill=GOLD_SOFT)
    d.text((gx+R+gap, cy-(tb[3]-tb[1])/2-tb[1]),"간다GO",font=bf,fill=TEXT)
    # phone pill
    pt=f"예약전화  {PHONE}"; pf=ko(38); pb=d.textbbox((0,0),pt,font=pf); ptw=pb[2]-pb[0]
    qx0=600-ptw/2-34; qx1=600+ptw/2+34; qy0=536; qy1=536+62
    d.rounded_rectangle([qx0,qy0,qx1,qy1],radius=31,fill=GOLD)
    d.text((600-ptw/2-pb[0], qy0+(62-(pb[3]-pb[1]))/2-pb[1]), pt, font=pf, fill=(18,14,6))
    img.save(f"{OUT}/{slug}.png")
    return f"{OUT}/{slug}.png"

for slug,(tag,l1,l2) in PAGES.items():
    print("wrote", make(slug,tag,l1,l2))
print("done", len(PAGES))
