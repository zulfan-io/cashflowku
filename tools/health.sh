#!/usr/bin/env bash
set +e
R="$(cd "$(dirname "$0")/.." && pwd)"; CDN="$R/csttan.md"
LOG="/tmp/dev2.log"; [ -f "$LOG" ] || LOG="/tmp/dev.log"
hr(){ printf '\n───── %s ─────\n' "$1"; }
hr "🩺 HEALTH"
if curl -s -m 4 http://localhost:3333/ 2>/dev/null | grep -q 'id="app"'; then
  echo "🟢 vite :3333 LIVE · #app=1 (Vue mount)"
elif ss -ltn 2>/dev/null | grep -q ':3333' || netstat -ltn 2>/dev/null | grep -q ':3333'; then
  echo "🟡 port 3333 OPEN tapi #app=0 (error runtime)"
else echo "🔴 vite :3333 MATI (port kosong)"; fi
if [ -f "$LOG" ]; then
  echo "📄 log $(basename "$LOG") · ready=$(grep -c 'ready in' "$LOG")"
  E=$(grep -iE 'ERROR|Build failed|already in use|createRequire|existsSync|optimized info' "$LOG" 2>/dev/null | tail -3)
  [ -n "$E" ] && { echo "  error:"; printf '%s\n' "$E" | sed 's/^/    /'; } || echo "  error: (bersih)"
else echo "📄 log: belum ada sesi ini"; fi
hr "🧭 GIT · SYNC"
BR=$(git -C "$R" branch --show-current 2>/dev/null)
echo "📍 branch=$BR · uncommitted=$(git -C "$R" status --porcelain 2>/dev/null | wc -l) · HEAD=$(git -C "$R" log --oneline -1 2>/dev/null)"
hr "🗓️  HARI INI"
T=$(git -C "$R" log --oneline --since="today 00:00" 2>/dev/null)
[ -n "$T" ] && printf '%s\n' "$T" | sed 's/^/  /' || echo "  (belum ada)"
hr "✅ SELESAI (csttan.md)"
X=$(grep -E '^- \[x\]' "$CDN" 2>/dev/null)
[ -n "$X" ] && printf '%s\n' "$X" | sed 's/^- \[x\] /  ✅ /' || echo "  (kosong)"
hr "⤴️  NEXT (csttan.md)"
I=$(grep -E '^- \[i\]' "$CDN" 2>/dev/null); echo "  in-progress:"; [ -n "$I" ] && printf '%s\n' "$I" | sed 's/^- \[i\] /    🟡 /' || echo "    (kosong)"
N=$(grep -E '^- \[ \]' "$CDN" 2>/dev/null | head -12); echo "  backlog:"; [ -n "$N" ] && printf '%s\n' "$N" | sed 's/^- \[ \] /    ⬜ /' || echo "    (kosong)"
hr "🎨 POC (:3333/<path>)"
P=$(ls "$R"/public/*poc*.html 2>/dev/null)
[ -n "$P" ] && printf '%s\n' "$P" | sed "s|$R/public/|  → /|" || echo "  (belum ada)"
hr "🔚 $R"
