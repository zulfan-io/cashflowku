#!/usr/bin/env bash
# legodone renderer — warna psikologis dari emoji penanda di LEGODONE.md. Plain di file, warna di layar.
f=""; for c in /workspaces/cashflowku "$HOME/cashflowku"; do [ -f "$c/LEGODONE.md" ] && f="$c/LEGODONE.md" && break; done
[ -z "$f" ] && { echo "legodone: LEGODONE.md nggak ketemu"; exit 1; }
if [ -t 1 ]; then
  ESC=$'\033'; B="$ESC[1;34m"; C="$ESC[36m"; R="$ESC[31m"; Y="$ESC[33m"; G="$ESC[32m"; Z="$ESC[0m"
  while IFS= read -r line; do
    case "$line" in
      "### "*) printf '%s%s%s\n' "$C" "$line" "$Z";;
      "## "*)  printf '%s%s%s\n' "$B" "$line" "$Z";;
      *"🔴"*)  printf '%s%s%s\n' "$R" "$line" "$Z";;
      *"🟡"*)  printf '%s%s%s\n' "$Y" "$line" "$Z";;
      *"🟢"*)  printf '%s%s%s\n' "$G" "$line" "$Z";;
      *)       printf '%s\n' "$line";;
    esac
  done < "$f"
else
  cat "$f"
fi
echo ""
echo "── RINGKAS ──"
echo "  sudah(☑): $(grep -c '☑' "$f") · belum(☐): $(grep -c '☐' "$f") · 🟢 siap: $(grep -c '🟢' "$f") · 🔴 bahaya: $(grep -c '🔴' "$f") · 🟡 keputusan: $(grep -c '🟡' "$f")"
