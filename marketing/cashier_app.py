# MARKET_CASHIER_V1 app
import json,os
from flask import Flask,redirect,request,abort
from cashier import record,verify,hurl
APP=Flask(__name__)
STRUK=os.environ.get("MARKET_STRUK","struk.jsonl")
def offers():
    p="offers.local.json"
    if os.path.exists(p): return json.load(open(p))
    return json.loads(os.environ.get("MARKET_OFFERS_JSON","{}"))
@APP.route("/go")
def go():
    q=request.args; oid=q.get("o",""); mp=offers()
    if oid not in mp: abort(404)
    row={"click_id":q.get("c",""),"src_platform":q.get("p",""),"src_caption":q.get("cap",""),
         "offer_id":oid,"promise_text":q.get("pt",""),"promise_source":q.get("ps",""),
         "valid_until":q.get("vu",""),"landing_card_pos":int(q.get("pos",0) or 0),
         "partner_url_hash":hurl(mp[oid]),"thread_id":q.get("t","")}
    record(STRUK,row)
    sep="&" if "?" in mp[oid] else "?"
    return redirect(mp[oid]+sep+"c="+row["click_id"],code=302)
@APP.route("/verify")
def v():
    g,b=verify(STRUK); return {"aman":len(g),"rusak":b}
if __name__=="__main__": APP.run(host="0.0.0.0",port=int(os.environ.get("PORT","5001")))
