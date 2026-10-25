import os,sys,re
S=r'''// GUNUNG 1 — 1 offer = 1 kartu CGiftRow/CGiftCards. KLIK-OUT, bukan checkout.
// Sumber: doc ACCESSTRADE telanjang (gurkha.accesstrade.global). Generator: tools/schema_gen.py.
// affiliateLink HARAM di client: diisi Netlify function (secretKey di env var). Ini BENTUK data.
export type RewardType = 'CPC' | 'CPA_FIXED' | 'CPA_SALES' | 'CPA' | 'CPS' | 'CPL';
export type AffiliationStatus = 'NEW' | 'APPLYING' | 'APPROVED' | 'REJECTED';
export type ConversionStatus = 'APPROVED' | 'PENDING' | 'REJECTED';
export interface CategoryRef { name: string; value: number; }
export interface Reward { type: RewardType; name?: string; reward: number | string; }
export interface SubId { name: string; value: string; label?: string; }
export interface AffiliateOffer {
  campaignId: number;
  campaignName: string;
  campaignType?: RewardType;
  merchantUrl: string;
  imageUrl?: string;
  currency?: string;
  categories: CategoryRef[];
  affiliationStatus: AffiliationStatus;
  defaultRewards: Reward[];
  highestRewardSummaries?: Reward[];
  affiliateLink?: string;
  subIds?: SubId[];
  promoCode?: string;
  promoTitle?: string;
  remainDays?: number;
  periodDays?: number;
  reward?: number;
  transactionAmount?: number;
  conversionStatus?: ConversionStatus;
}'''
lines=S.rstrip('\n').split('\n')
nc=[l for l in lines if not l.strip().startswith('//')]
J=''.join(nc)
def bal(a,b): return J.count(a)-J.count(b)
errs=[]
if bal('{','}'): errs.append('brace {} miring (%+d)'%bal('{','}'))
if bal('(',')'): errs.append('paren () miring')
if bal('[',']'): errs.append('bracket [] miring')
if S.count("'")%2: errs.append("quote ' ganjil")
if S.count('"')%2: errs.append('quote " ganjil')
FL=re.compile(r'^  [A-Za-z_]\w*\?? ?: .+;$')
nf=0
for i,l in enumerate(lines,1):
    if l.startswith('  '):
        nf+=1
        if not FL.match(l): errs.append('field baris %d bukan sintak: %r'%(i,l))
if S.count('export interface')!=4: errs.append('interface !=4')
if S.count('export type')!=3: errs.append('type !=3')
if lines[-1]!='}': errs.append('baris terakhir bukan }')
if 'TODO' in S or 'FIXME' in S: errs.append('ada TODO/FIXME')
if errs:
    print('[MELESET] file TIDAK ditulis:'); [print('  -',e) for e in errs]; sys.exit(1)
os.makedirs('src/schema',exist_ok=True)
open('src/schema/affiliateOffer.ts','w').write(S+'\n')
print('OK wrote',len(lines),'baris,',nf,'field, semua assert lolos')