// catalog.ts — skema TS KATALOG tp-o.tk, MIRROR output tpoNormalize.tpoParse().
// BUKAN input mentah (key ber-spasi "name ") — adapter udah strip+coerce, TS input = sampah.
// Yang lo import = BENTUK HASIL parse, siap ke komponen. Field kebukti byte: tpo_run.mjs. NOL ngarang.
export interface ProductModel { id: number; sku: string; price: number; stock: number; variation_index: number[]; is_default: boolean; product_id: number; }
export interface WholesaleTier { min: number; max: number; price: number; }
export interface VariationGroup { name: string; options: string[]; }
export interface Product { id: number; name: string; image: string | null; sold: number; rating: number; price: number | null; stock: number; variants: VariationGroup[]; models: ProductModel[]; wholesale: WholesaleTier[]; }
export interface PageMeta { current: number; last: number; total: number; per_page: number; next: string | null; }
export interface ShopStatistic { product_count: number; all_product_count: number; average_raiting: number; nonfulfilment_rate: number; } // typo API "raiting" DIPERTAHANKAN: adapter nggak benerin typo, TS harus cermin runtime
export interface Shop { slug: string; name: string; description?: string; avatar_image?: string; cover_image?: string; banners?: Array<{ type: string; id: string; hyper_link: string }>; created_at?: string; id: number; statistic: ShopStatistic; }
export type CatalogResult = { kind: 'product'; product: Product } | { kind: 'list'; list: Product[]; page: PageMeta } | { kind: 'shop'; shop: Shop } | { kind: 'unknown'; data: unknown };