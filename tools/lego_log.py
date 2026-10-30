import os,sys,datetime
P='LEGODONE.md'
if not os.path.isfile(P): sys.exit('NGGAK ADA '+P+' (jalanin dari root repo)')
args=sys.argv[1:]
if args: lines=[' '.join(args)]
else: lines=[l.strip() for l in sys.stdin.read().splitlines() if l.strip()]
if not lines: sys.exit('NOL ide (kosong) - abort, file utuh')
HEAD='## MASUKAN COI - log ide SEBELUM ngoding (rule Coi)\n> Aturan: tiap masukan positif soal projek -> kesini dulu, baru gue ngoding. Inbox mentah, bukan task bercentang.\n\n'
t=open(P,encoding='utf-8').read()
idx=t.find('RINGKAS')
if idx==-1:
    ipos=len(t)
    if ipos and t[ipos-1]!='\n': t+='\n'
else: ipos=t.rfind('\n',0,idx)+1
need='## MASUKAN COI' not in t
stamp=datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
block=('' if not need else HEAD)+''.join('- %s :: %s\n'%(stamp,l) for l in lines)
new=t[:ipos]+block+t[ipos:]
if '## MASUKAN COI' not in new: sys.exit('MELESET heading')
for l in lines:
    if (':: '+l) not in new: sys.exit('MELESET ide hilang: '+l[:24])
if t.count('RINGKAS')!=new.count('RINGKAS'): sys.exit('MELESET RINGKAS berubah')
open(P,'w',encoding='utf-8',newline='\n').write(new)
print('OK log',len(lines),'ide -> MASUKAN (stamp',stamp+')')
