import hashlib, urllib.request, json, getpass, sys
CC = "ID"
EMAIL = input("email accesstrade (persis email login): ").strip()
PWD = getpass.getpass("password (KETIK manual, jgn paste, layar kosong = aman): ")
# countryCode LOCKED di query (bukti: 400 hilang cuma di channel ini)
path_raw = "https://gurkha.accesstrade.global/publishers/auth/" + EMAIL + "?countryCode=" + CC
md5hex = hashlib.md5(PWD.encode()).hexdigest()
md5byt = hashlib.md5(PWD.encode()).digest()
VAR = [
  ("V1 @-mentah + md5-HEX  [paling standar]",
     path_raw, hashlib.sha256((EMAIL + ":" + md5hex).encode()).hexdigest()),
  ("V2 @-mentah + md5-BYTE [kalau doc maksud raw digest]",
     path_raw, hashlib.sha256(EMAIL.encode() + b":" + md5byt).hexdigest()),
]
for nm, url, tok in VAR:
    req = urllib.request.Request(url, headers={"Authorization": tok})  # provisioning = hash MENTAH, TANPA 'Bearer'
    try:
        raw = urllib.request.urlopen(req, timeout=20).read().decode()
        d = json.loads(raw)
        print("\n=== 200 OK via %s ===" % nm)
        print("SALIN 2 INI KE SUPABASE -> Settings -> Edge Functions -> SECRETS (bukan SQL editor):")
        print("ACCESSTRADE_USER_UID=" + str(d.get("userUid")))
        print("ACCESSTRADE_SECRET_KEY=" + str(d.get("secretKey")))
        print("(accountId=%s -> catet buat admin, fn TIDAK butuh)" % d.get("accountId"))
        sys.exit(0)
    except urllib.error.HTTPError as e:
        b = ""
        try: b = e.read().decode()[:160]
        except Exception: pass
        print("%s -> %d | %s" % (nm, e.code, b))
    except Exception as e:
        print("%s -> BUKAN-HTTP %s" % (nm, type(e).__name__))
print("\n=== 2 varian @-mentah tetap 401 -> bukan script gue, itu CREDS lo. Liat checklist di bawah. ===")
