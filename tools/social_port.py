import os,sys,json
P='src/data/ports.json'
if not os.path.isfile(P): sys.exit('NGGAK ADA '+P)
t=open(P,encoding='utf-8').read()
if '"id": "drama"' in t: sys.exit('udah ada drama, skip')
OLD='    }\n  ],\n  "campaigns": []'
NEW='''    },
    {
      "id": "drama",
      "kind": "drama",
      "enabled": false,
      "mount": "floating",
      "config": {
        "provider": "",
        "window": "scroll_down"
      }
    }
  ],
  "campaigns": []'''
c=t.count(OLD)
if c!=1: sys.exit('MELESET count=%d (harus 1)'%c)
for ch in NEW:
    if ord(ch)>127: sys.exit('MELESET non-ASCII NEW')
t=t.replace(OLD,NEW)
try: json.loads(t)
except Exception as e: sys.exit('MELESET json rusak: %s'%e)
if '"id": "drama"' not in t: sys.exit('MELESET marker drama')
open(P,'w',encoding='utf-8',newline='\n').write(t)
print('OK port drama',P)
