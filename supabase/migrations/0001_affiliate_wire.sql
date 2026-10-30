-- shoper_offers: rumah buat kawat accesstrade (jalanin di SQL editor / supabase db push)
alter table public.shoper_offers add column if not exists affiliate_link text;
alter table public.shoper_offers add column if not exists marketplace text;
alter table public.shoper_offers add column if not exists campaign_id integer;
alter table public.shoper_offers add column if not exists creative_id integer;
alter table public.shoper_offers add column if not exists landing_url text;
alter table public.shoper_offers add column if not exists sub_ids jsonb;
alter table public.shoper_offers add column if not exists at_updated_at timestamptz default now();
comment on column public.shoper_offers.affiliate_link is 'tracked deep-link dimintain server-side (custom creative)';
comment on column public.shoper_offers.marketplace is 'shopee|tokopedia|tiktok|tiket|agoda... buat filter widget per pasar';
