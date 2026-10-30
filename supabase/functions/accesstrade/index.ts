// Supabase Edge Function: Accesstrade link-minter. Secret HANYA di vault, HARAM di repo/.env.
const BASE = "https://gurkha.accesstrade.global";
const UID = Deno.env.get("ACCESSTRADE_USER_UID") ?? "";
const KEY = Deno.env.get("ACCESSTRADE_SECRET_KEY") ?? "";
function b64url(b: Uint8Array): string { let s = ""; b.forEach((x) => { s += String.fromCharCode(x); }); return btoa(s).replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, ""); }
function enc(s: string): Uint8Array { return new TextEncoder().encode(s); }
async function makeJwt(): Promise<string> {
  const h = b64url(enc(JSON.stringify({ alg: "HS256" })));
  const p = b64url(enc(JSON.stringify({ sub: UID, iat: Math.floor(Date.now() / 1000) })));
  const d = h + "." + p;
  const k = await crypto.subtle.importKey("raw", enc(KEY), { name: "HMAC", hash: "SHA-256" }, false, ["sign"]);
  const sg = new Uint8Array(await crypto.subtle.sign("HMAC", k, enc(d)));
  return d + "." + b64url(sg);
}
function cors(req: Request): Headers { const x = new Headers(); const o = req.headers.get("Origin"); x.set("Access-Control-Allow-Origin", o ?? "*"); x.set("Access-Control-Allow-Headers", "authorization, apikey, content-type, x-accesstrade-user-type"); x.set("Access-Control-Allow-Methods", "POST, OPTIONS"); return x; }
Deno.serve(async (req: Request) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: cors(req) });
  if (!UID || !KEY) return new Response(JSON.stringify({ error: "vault secret missing" }), { status: 500, headers: cors(req) });
  let body: any; try { body = await req.json(); } catch { return new Response(JSON.stringify({ error: "bad json" }), { status: 400, headers: cors(req) }); }
  const { siteId, campaignId, landingUrl, imageUrl, anchorText, subIds } = body;
  if (!siteId || !campaignId || !landingUrl) return new Response(JSON.stringify({ error: "siteId, campaignId, landingUrl required" }), { status: 400, headers: cors(req) });
  const jwt = await makeJwt();
  const url = BASE + "/v1/publishers/me/sites/" + siteId + "/campaigns/" + campaignId + "/creatives/custom";
  const pl: any = { landingUrl, name: "shoper-" + campaignId };
  if (imageUrl) pl.imageUrl = imageUrl; if (anchorText) pl.anchorText = anchorText; if (Array.isArray(subIds)) pl.subIds = subIds;
  const r = await fetch(url, { method: "POST", headers: { "Content-Type": "application/json", "Authorization": "Bearer " + jwt, "X-Accesstrade-User-Type": "publisher" }, body: JSON.stringify(pl) });
  const t = await r.text(); let j: any = null; try { j = JSON.parse(t); } catch {}
  const link = j && j.content && j.content[0] && j.content[0].affiliateLink;
  return new Response(JSON.stringify({ ok: r.ok, status: r.status, affiliateLink: link ?? null, raw: link ? undefined : t.slice(0, 400) }), { status: r.ok ? 200 : 502, headers: cors(req) });
});
