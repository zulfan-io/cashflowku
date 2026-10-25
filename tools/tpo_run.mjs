import {readFileSync} from 'fs'
import {tpoParse} from '../src/utils/tpoNormalize.js'
const j=JSON.parse(readFileSync(new URL('../src/data/tpo_fixture.json',import.meta.url)))
for(const k of ['product','list','shop']){const r=tpoParse(j[k]);let d=r.kind==='list'?(r.list.length+' item price='+r.list[0].price):r.kind==='product'?(r.product.name+' price='+r.product.price+' rating='+r.product.rating):r.kind==='shop'?r.shop.slug:'?';console.log(k,'->',r.kind,'|',d)}
