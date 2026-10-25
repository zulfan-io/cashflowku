import {readFileSync} from 'fs'
import {tpoParse} from '../src/utils/tpoNormalize.js'
const j=JSON.parse(readFileSync(new URL('../src/data/tpo_fixture.json',import.meta.url)))
const raw=j.product
console.log('keys      =',JSON.stringify(Object.keys(raw)))
console.log('dot .data =',raw.data)
console.log('brk [data ]=',typeof raw['data '])
const r=tpoParse(raw)
console.log('tpoParse  =',r.kind,r.kind==='product'?(r.product.name+' price='+r.product.price):(r.kind==='list'?r.list.length+' item':''))
