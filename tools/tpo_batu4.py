import json,os
prod={"status ":True,"data ":{"id ":2,"shop_id":3,"name ":"SG PBT Keycap Set","description ":"cut","weight ":"500 ","avg_rating ":"0 ","sold ":0,"images ":["demo-x "],"variations ":[],"models":[{"id ":5,"sku ":" ","price ":"24.9 ","stock ":43,"variation_index ":[0],"is_default ":False,"product_id ":2}]}}
lst={"status ":True,"data ":{"current_page ":1,"data":[{"id ":12,"name ":"Blackdot V200 Smartwatch","weight ":"300 ","avg_rating ":"0 ","sold ":0,"images ":["demo-y "],"variations ":[],"models":[{"id ":29,"sku ":" ","price ":"69 ","stock ":50,"variation_index ":[],"is_default ":False,"product_id ":12}]}],"last_page ":3,"total ":33,"per_page ":"12 ","next_page_url ":"http://x "}}
shp={"status ":True,"data ":{"slug ":"shop-de ","name ":"Shop odede ","id ":1,"statistic":{"product_count ":100,"average_raiting ":"80 ","nonfulfilment_rate ":"12 "}}}
fx={"product":prod,"list":lst,"shop":shp}
os.makedirs('src/data',exist_ok=True)
p='src/data/tpo_fixture.json'
json.dump(fx,open(p,'w'),ensure_ascii=False,indent=1)
assert json.load(open(p)),'fixture JSON invalid'
run='''import {readFileSync} from 'fs'
import {tpoParse} from '../src/utils/tpoNormalize.js'
const j=JSON.parse(readFileSync(new URL('../src/data/tpo_fixture.json',import.meta.url)))
for(const k of ['product','list','shop']){const r=tpoParse(j[k]);let d=r.kind==='list'?(r.list.length+' item price='+r.list[0].price):r.kind==='product'?(r.product.name+' price='+r.product.price+' rating='+r.product.rating):r.kind==='shop'?r.shop.slug:'?';console.log(k,'->',r.kind,'|',d)}
'''
open('tools/tpo_run.mjs','w').write(run)
print('OK fixture 3 record (key-spaced+numeric-string) + runner .mjs, json valid')