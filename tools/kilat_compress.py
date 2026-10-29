import os,sys,subprocess,glob,shutil
SRC=os.path.expanduser('~/storage/downloads/ImageKilat')
DST='public/assets/kilat'
if not os.path.isdir(SRC): sys.exit('NGGAK ADA '+SRC)
files=[f for f in sorted(glob.glob(os.path.join(SRC,'*'))) if os.path.isfile(f)]
if not files: sys.exit('folder kosong')
os.makedirs(DST,exist_ok=True)
FF='ffmpeg'
def run(cmd):
    try:
        r=subprocess.run(cmd,capture_output=True,text=True)
        return (r.returncode==0), (r.stderr[-160:] if r.returncode else '')
    except FileNotFoundError:
        return False,'ffmpeg not in PATH'
before=after=ok=copied=skipped=0; failed=[]; pngs=[]
for f in files:
    base=os.path.basename(f); ext=base.lower().rsplit('.',1)[-1] if '.' in base else ''
    out=os.path.join(DST,base); sz=os.path.getsize(f); before+=sz
    if os.path.isfile(out) and os.path.getsize(out)>0:
        skipped+=1; after+=os.path.getsize(out); continue
    cmd=None
    if ext in ('jpg','jpeg','webp'): cmd=[FF,'-y','-i',f,'-q:v','4',out]
    elif ext=='mp4': cmd=[FF,'-y','-i',f,'-c:v','libx264','-crf','28','-preset','veryfast','-vf','scale=-2:min(720,ih)','-c:a','aac','-b:a','96k','-movflags','+faststart',out]
    elif ext=='png': pngs.append(base)
    done=False
    if cmd:
        good,err=run(cmd)
        if good and os.path.isfile(out) and os.path.getsize(out)>0: done=True; ok+=1
        else: failed.append((base,err[:70]))
    if not done: shutil.copy2(f,out); copied+=1
    nsz=os.path.getsize(out); after+=nsz
    print('%-24s %8d -> %8d  %s'%(base[:24],sz,nsz,'OK' if done else 'COPY-mentah'))
print('---')
print('proses %d | compress %d | copy-mentah %d | skip-udah %d'%(len(files),ok,copied,skipped))
if before: print('byte %d -> %d | hemat %.0f%%'%(before,after,(1-after/before)*100))
if pngs: print('PNG di-copy mentah (transparansi, NOL dijpg-kan):',len(pngs),'file')
if failed:
    print('compress gagal (tetep ke-backup mentah, aman):')
    for b,e in failed[:5]: print('  ',b,'|',e)
if ok==0 and copied==0: sys.exit('NOL file keproses')
