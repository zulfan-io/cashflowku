import subprocess
mjs='''import {readFileSync} from 'fs'
import {tpoParse} from '../src/utils/tpoNormalize.js'
const j=JSON.parse(readFileSync(new URL('../src/data/tpo_fixture.json',import.meta.url)))
const r=tpoParse(j.product)
const c=r.product
console.log('kind       =',r.kind)
console.log('id         =',c.id,typeof c.id)
console.log('shop_id    =',c.shop_id,typeof c.shop_id)
console.log('name       =['+c.name+']',typeof c.name)
console.log('images[0]  =['+(c.images&&c.images[0])+'] len='+(c.images?c.images.length:0))
console.log('sold       =',c.sold,typeof c.sold)
console.log('models[0]  price=',c.models[0].price,typeof c.models[0].price)
console.log('models[0]  stock=',c.models[0].stock,typeof c.models[0].stock)
'''
open('tools/card_field_check.mjs','w').write(mjs)
r=subprocess.run(['node','tools/card_field_check.mjs'],capture_output=True,text=True)
print(r.stdout,end='')
if r.stderr: print('[stderr]',r.stderr.strip()[:160])