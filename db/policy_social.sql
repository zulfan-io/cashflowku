-- policy_social.sql :: social commerce shoper. Source of truth = git.
-- Nyambung pola policy_rls.sql: idempoten (DROP IF EXISTS + CREATE).
-- Prinsip: love/comment/status = INTEGRITAS (write butuh login).
--          share = FUNNEL sebar (insert boleh anonim, kayak clicks).
--          SELECT semua = PUBLIK (biar love kesebar bisa diliat semua orang).
-- target_id pakai TEXT biar nyambung ke id apa pun tanpa nebak tipe lo.

CREATE TABLE IF NOT EXISTS shoper_status (
  id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  member_id bigint NOT NULL REFERENCES shoper_members(id) ON DELETE CASCADE,
  body text NOT NULL,
  media_url text, media_kind text,
  expires_at timestamptz NOT NULL DEFAULT now() + interval '1 day',
  love_count int NOT NULL DEFAULT 0, comment_count int NOT NULL DEFAULT 0,
  created_at timestamptz NOT NULL DEFAULT now() );
CREATE TABLE IF NOT EXISTS shoper_loves (
  id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  member_id bigint NOT NULL REFERENCES shoper_members(id) ON DELETE CASCADE,
  target_type text NOT NULL, target_id text NOT NULL,
  created_at timestamptz NOT NULL DEFAULT now(),
  UNIQUE (member_id, target_type, target_id) );
CREATE TABLE IF NOT EXISTS shoper_shares (
  id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  member_id bigint REFERENCES shoper_members(id) ON DELETE SET NULL,
  target_type text NOT NULL, target_id text NOT NULL, channel text,
  love_count int NOT NULL DEFAULT 0,
  created_at timestamptz NOT NULL DEFAULT now() );
CREATE TABLE IF NOT EXISTS shoper_comments (
  id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  member_id bigint NOT NULL REFERENCES shoper_members(id) ON DELETE CASCADE,
  target_type text NOT NULL, target_id text NOT NULL, body text NOT NULL,
  parent_id bigint REFERENCES shoper_comments(id) ON DELETE CASCADE,
  created_at timestamptz NOT NULL DEFAULT now() );
CREATE INDEX IF NOT EXISTS idx_status_feed ON shoper_status (expires_at DESC, created_at DESC);
CREATE INDEX IF NOT EXISTS idx_loves_t ON shoper_loves (target_type, target_id);
CREATE INDEX IF NOT EXISTS idx_shares_t ON shoper_shares (target_type, target_id);
CREATE INDEX IF NOT EXISTS idx_comments_t ON shoper_comments (target_type, target_id, created_at);
ALTER TABLE shoper_status ENABLE ROW LEVEL SECURITY;
ALTER TABLE shoper_loves ENABLE ROW LEVEL SECURITY;
ALTER TABLE shoper_shares ENABLE ROW LEVEL SECURITY;
ALTER TABLE shoper_comments ENABLE ROW LEVEL SECURITY;

DROP POLICY IF EXISTS status_pub_read ON shoper_status;
CREATE POLICY status_pub_read ON shoper_status FOR SELECT USING (expires_at > now());
DROP POLICY IF EXISTS loves_pub_read ON shoper_loves;
CREATE POLICY loves_pub_read ON shoper_loves FOR SELECT USING (true);
DROP POLICY IF EXISTS shares_pub_read ON shoper_shares;
CREATE POLICY shares_pub_read ON shoper_shares FOR SELECT USING (true);
DROP POLICY IF EXISTS comments_pub_read ON shoper_comments;
CREATE POLICY comments_pub_read ON shoper_comments FOR SELECT USING (true);

DROP POLICY IF EXISTS status_self_ins ON shoper_status;
CREATE POLICY status_self_ins ON shoper_status FOR INSERT WITH CHECK (member_id = current_member_id());
DROP POLICY IF EXISTS status_self_del ON shoper_status;
CREATE POLICY status_self_del ON shoper_status FOR DELETE USING (member_id = current_member_id());
DROP POLICY IF EXISTS loves_self_ins ON shoper_loves;
CREATE POLICY loves_self_ins ON shoper_loves FOR INSERT WITH CHECK (member_id = current_member_id());
DROP POLICY IF EXISTS loves_self_del ON shoper_loves;
CREATE POLICY loves_self_del ON shoper_loves FOR DELETE USING (member_id = current_member_id());
DROP POLICY IF EXISTS shares_any_ins ON shoper_shares;
CREATE POLICY shares_any_ins ON shoper_shares FOR INSERT WITH CHECK (true);
DROP POLICY IF EXISTS comments_self_ins ON shoper_comments;
CREATE POLICY comments_self_ins ON shoper_comments FOR INSERT WITH CHECK (member_id = current_member_id());
DROP POLICY IF EXISTS comments_self_del ON shoper_comments;
CREATE POLICY comments_self_del ON shoper_comments FOR DELETE USING (member_id = current_member_id());

CREATE OR REPLACE FUNCTION public.shoper_recount()
RETURNS trigger LANGUAGE plpgsql SECURITY DEFINER SET search_path = public AS $$
BEGIN
  IF TG_TABLE_NAME = 'shoper_loves' THEN
    IF TG_OP = 'INSERT' THEN
      IF NEW.target_type='status' THEN UPDATE shoper_status SET love_count=love_count+1 WHERE id::text=NEW.target_id;
      ELSIF NEW.target_type='share' THEN UPDATE shoper_shares SET love_count=love_count+1 WHERE id::text=NEW.target_id; END IF;
    ELSE
      IF OLD.target_type='status' THEN UPDATE shoper_status SET love_count=GREATEST(love_count-1,0) WHERE id::text=OLD.target_id;
      ELSIF OLD.target_type='share' THEN UPDATE shoper_shares SET love_count=GREATEST(love_count-1,0) WHERE id::text=OLD.target_id; END IF;
    END IF;
  ELSIF TG_TABLE_NAME = 'shoper_comments' THEN
    IF TG_OP='INSERT' AND NEW.target_type='status' THEN UPDATE shoper_status SET comment_count=comment_count+1 WHERE id::text=NEW.target_id;
    ELSIF TG_OP='DELETE' AND OLD.target_type='status' THEN UPDATE shoper_status SET comment_count=GREATEST(comment_count-1,0) WHERE id::text=OLD.target_id; END IF;
  END IF;
  RETURN NULL;
END $$;
DROP TRIGGER IF EXISTS trg_loves_count ON shoper_loves;
CREATE TRIGGER trg_loves_count AFTER INSERT OR DELETE ON shoper_loves FOR EACH ROW EXECUTE FUNCTION public.shoper_recount();
DROP TRIGGER IF EXISTS trg_comments_count ON shoper_comments;
CREATE TRIGGER trg_comments_count AFTER INSERT OR DELETE ON shoper_comments FOR EACH ROW EXECUTE FUNCTION public.shoper_recount();

CREATE OR REPLACE FUNCTION public.shoper_purge_expired()
RETURNS int LANGUAGE plpgsql SECURITY DEFINER SET search_path = public AS $$
DECLARE n int; BEGIN
  DELETE FROM shoper_status WHERE expires_at <= now();
  GET DIAGNOSTICS n = ROW_COUNT; RETURN n; END $$;
SELECT public.shoper_purge_expired();
-- Schedule (uncomment 2 baris ini KALAU pg_cron udah lo aktifin di dashboard Supabase):
-- CREATE EXTENSION IF NOT EXISTS pg_cron;
-- SELECT cron.schedule('shoper-purge','0 */6 * * *',$$SELECT public.shoper_purge_expired()$$);
