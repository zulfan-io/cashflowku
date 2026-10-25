// tpoNormalize.js — adapter API tp-o.tk (produk+fitur+shopjson.json)
// Fakta KB: (1) SEMUA key punya TRAILING SPASI ("name ","price "), (2) numerik=STRING,
// (3) typo API: shop "average_raiting", produk "avg_rating", (4) 3 shape: product/list/shop.
// Parser GENERIK: strip spasi key rekursif + coerce numeric-string whitelist.
// Shape ke-4 otomatis nangkep begitu lo kasih byte. NOL ngarang.
const NUMKEYS=new Set(['price','weight','avg_rating','average_raiting','per_page','total','current_page','last_page','from','to','nonfulfilment_rate','product_count','all_product_count','min','max']);
const isNum=s=>typeof s==='string'&&/^-?\d+(?:\.\d+)?$/.test(s.trim());
function norm(v){
  if(Array.isArray(v))return v.map(norm);
  if(v&&typeof v==='object'){const o={};for(const k in v){const kk=k.replace(/\s+$/,'');o[kk]=(NUMKEYS.has(kk)&&isNum(v[k]))?Number(String(v[k]).trim()):norm(v[k]);}return o;}
  return v;
}
function prod(p){
  const models=Array.isArray(p.models)?p.models:[];
  const prices=models.map(m=>Number(m.price)).filter(n=>!isNaN(n));
  return{id:p.id,name:p.name,image:(p.images&&p.images[0])||null,sold:p.sold||0,rating:Number(p.avg_rating)||0,price:prices.length?Math.min.apply(null,prices):null,stock:models.reduce((a,m)=>a+(Number(m.stock)||0),0),variants:p.variations||[],models,wholesale:p.wholesale_prices||[]};
}
export function tpoParse(raw){
  const env=norm(raw);const d=(env&&env.data!==undefined)?env.data:env;
  if(d&&Array.isArray(d.data))return{kind:'list',list:d.data.map(prod),page:{current:d.current_page,last:d.last_page,total:d.total,per_page:d.per_page,next:d.next_page_url}};
  if(d&&typeof d.slug==='string')return{kind:'shop',shop:d};
  if(d&&Array.isArray(d.models))return{kind:'product',product:prod(d)};
  return{kind:'unknown',data:d};
}