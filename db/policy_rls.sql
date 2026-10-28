-- policy_rls.sql - RLS policy shoper. Source of truth = git ini.
-- Sudah di-run & sukses di SQL Editor Supabase (project zulfan-io).
-- Idempoten: DROP IF EXISTS + CREATE, boleh di-run ulang.
-- Aturan: publik = katalog/produk/kampanye/donasi-visible.
-- Self = data diri member. Sensitif (poin/reward/otp/order/konversi/audit) = TIDAK ada policy write = service/Edge Function only.
-- Klik = insert boleh siapa pun (funnel RCM), baca/ubah = service only.

CREATE OR REPLACE FUNCTION public.current_member_id()
RETURNS bigint LANGUAGE sql STABLE SECURITY DEFINER SET search_path = public AS $$
  SELECT id FROM shoper_members WHERE user_id = auth.uid()
$$;

-- PUBLIC READ
DROP POLICY IF EXISTS offers_pub_read ON shoper_offers;
CREATE POLICY offers_pub_read ON shoper_offers FOR SELECT USING (active);
DROP POLICY IF EXISTS products_pub_read ON shoper_products;
CREATE POLICY products_pub_read ON shoper_products FOR SELECT USING (active);
DROP POLICY IF EXISTS campaigns_pub_read ON shoper_campaigns;
CREATE POLICY campaigns_pub_read ON shoper_campaigns FOR SELECT USING (active);
DROP POLICY IF EXISTS donations_pub_read ON shoper_donations;
CREATE POLICY donations_pub_read ON shoper_donations FOR SELECT USING (visible);

-- CLICK: catat boleh siapa pun, baca/ubah = service only (no select policy)
DROP POLICY IF EXISTS clicks_pub_insert ON shoper_click_events;
CREATE POLICY clicks_pub_insert ON shoper_click_events FOR INSERT WITH CHECK (true);

-- SELF: member baca dirinya (tulis members = service only, biar nggak ubah points/role sendiri)
DROP POLICY IF EXISTS members_self_read ON shoper_members;
CREATE POLICY members_self_read ON shoper_members FOR SELECT USING (user_id = auth.uid());

-- SELF CRUD: kontak, preferensi, favorit
DROP POLICY IF EXISTS cc_self ON shoper_contact_channels;
CREATE POLICY cc_self_read ON shoper_contact_channels FOR SELECT USING (member_id = current_member_id());
CREATE POLICY cc_self_ins ON shoper_contact_channels FOR INSERT WITH CHECK (member_id = current_member_id());
CREATE POLICY cc_self_upd ON shoper_contact_channels FOR UPDATE USING (member_id = current_member_id()) WITH CHECK (member_id = current_member_id());
CREATE POLICY cc_self_del ON shoper_contact_channels FOR DELETE USING (member_id = current_member_id());

DROP POLICY IF EXISTS np_self ON shoper_notification_prefs;
CREATE POLICY np_self_read ON shoper_notification_prefs FOR SELECT USING (member_id = current_member_id());
CREATE POLICY np_self_ins ON shoper_notification_prefs FOR INSERT WITH CHECK (member_id = current_member_id());
CREATE POLICY np_self_upd ON shoper_notification_prefs FOR UPDATE USING (member_id = current_member_id()) WITH CHECK (member_id = current_member_id());
CREATE POLICY np_self_del ON shoper_notification_prefs FOR DELETE USING (member_id = current_member_id());

DROP POLICY IF EXISTS fav_self ON shoper_favorites;
CREATE POLICY fav_self_read ON shoper_favorites FOR SELECT USING (member_id = current_member_id());
CREATE POLICY fav_self_ins ON shoper_favorites FOR INSERT WITH CHECK (member_id = current_member_id());
CREATE POLICY fav_self_del ON shoper_favorites FOR DELETE USING (member_id = current_member_id());

-- NOTIF: baca/ubah-status/hapus diri sendiri; KIRIM (insert) = service only
DROP POLICY IF EXISTS notif_self ON shoper_notifications;
CREATE POLICY notif_self_read ON shoper_notifications FOR SELECT USING (member_id = current_member_id());
CREATE POLICY notif_self_upd ON shoper_notifications FOR UPDATE USING (member_id = current_member_id()) WITH CHECK (member_id = current_member_id());
CREATE POLICY notif_self_del ON shoper_notifications FOR DELETE USING (member_id = current_member_id());

-- VERIFIKASI (paste terpisah kalau mau audit):
-- SELECT tablename, policyname FROM pg_policies WHERE schemaname = 'public' ORDER BY tablename, policyname;

