// GUNUNG 1 — 1 offer = 1 kartu CGiftRow/CGiftCards. KLIK-OUT, bukan checkout.
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
}
