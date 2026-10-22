# MARKET_CASHIER_V1
import json, os, hashlib
from datetime import datetime
W14=["click_id","src_platform","src_caption","offer_id","promise_text","promise_source",
     "valid_until","landing_card_pos","partner_url_hash","converted","revenue","ts","thread_id","outcome"]
DEF={"converted":False,"revenue":0,"outcome":"seen","thread_id":""}
def _now(): return datetime.now().astimezone().isoformat(timespec="seconds")
def hurl(u): return "sha1:"+hashlib.sha1(str(u).encode()).hexdigest()[:12]
def record(path,row):
    r=dict(row)
    for k,v in DEF.items(): r.setdefault(k,v)
    if not r.get("ts"): r["ts"]=_now()
    miss=[k for k in W14 if k not in r]
    if miss: raise ValueError("struk kurang: "+",".join(miss))
    line=json.dumps({k:r[k] for k in W14},ensure_ascii=False,sort_keys=True)
    fd=os.open(path,os.O_APPEND|os.O_CREAT|os.O_WRONLY,0o600)
    try: os.write(fd,(line+"\n").encode()); os.fsync(fd)
    finally: os.close(fd)
    return r
def verify(path):
    good=[];bad=0
    if not os.path.exists(path): return good,bad
    with open(path,encoding="utf-8") as f:
        for ln in f:
            ln=ln.strip()
            if not ln: continue
            try: d=json.loads(ln); d["flushed"]=True; good.append(d)
            except Exception: bad+=1
    return good,bad
