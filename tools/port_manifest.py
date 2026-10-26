import os,json,sys
P='src/data/ports.json'
os.makedirs(os.path.dirname(P),exist_ok=True)
M={
 "version":1,
 "ui":{"dual":True,"feed_bottom":"affiliate_card","floating":"widget_grid","floating_max_slots":8},
 "reward":{"pulsa_on_points":True,"capture":["email","phone","otp"]},
 "ports":[
   {"id":"accesstrade","kind":"affiliate","enabled":True,"mount":"feed_bottom","config":{}},
   {"id":"member_otp","kind":"auth","enabled":True,"mount":"gate","config":{"fields":["email","phone"],"otp":True}},
   {"id":"games_free","kind":"game","enabled":False,"mount":"floating","config":{"provider":"","slots":[]}},
   {"id":"voucher_pulsa","kind":"widget","enabled":False,"mount":"floating","config":{}},
   {"id":"voucher_marketplace","kind":"widget","enabled":False,"mount":"floating","config":{"brands":["shopee","blibli","tiktok","lazada"]}}
 ],
 "campaigns":[]
}
old=open(P,encoding='utf-8').read() if os.path.isfile(P) else None
new=json.dumps(M,ensure_ascii=False,indent=2)+"\n"
if old==new: print('>> ports.json udah sama, skip'); sys.exit(0)
open(P,'w',encoding='utf-8').write(new)
print('OK tulis',P,'(%d port, %d campaign-hook)'%(len(M['ports']),len(M['campaigns'])))
print('>> campaign baru = tambah objek di campaigns, NOL kode = port lo')