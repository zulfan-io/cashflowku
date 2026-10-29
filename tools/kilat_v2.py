import os,sys,subprocess,glob,shutil
SRC=os.path.expanduser('~/storage/downloads/ImageKilat')
DST='public/assets/kilat'
if not os.path.isdir(SRC): sys.exit('NGGAK ADA '+SRC)
files=[f for f in sorted(glob.glob(os.path.join(SRC,'*'))) if os.path.isfile(f)]
if not files: sys.exit('kosong')
os.makedirs(DST,exist_ok=True)
FF='ffmpeg'
def run(c):
    try:
        r=subprocess.run(c,capture_output=True,text=True); return r.returncode==0,(r.stderr[-120:] if r.returncode else '')
    except FileNotFoundError: return False,'no ffmpeg'
b=a=ok=cp=0; fail=[]
for f in files:
    base=os.path.basename(f); ext=base.lower().rsplit('.',1)[-1] if '.' in base else ''
    out=os.path.join(DST,base); asal=os.path.getsize(f); b+=asal
    cmd=None
    if ext in ('jpg','jpeg','webp'): cmd=[FF,'-y','-i',f,'-q:v','7',out]
    elif ext=='mp4': cmd=[FF,'-y','-i',f,'-c:v','libx264','-crf','30','-preset','veryfast','-pix_fmt','yuv420p','-vf','scale=-2:720','-c:a','aac','-b:a','96k','-ac','1','-movflags','+faststart',out]
    done=False
    if cmd:
        g,e=run(cmd)
        if g and os.path.isfile(out) and os.path.getsize(out)>0: done=True; ok+=1
        else: fail.append((base,e[:60]))
    if not done: shutil.copy2(f,out); cp+=1
    ns=os.path.getsize(out); a+=ns
    print('%-22s %8d -> %8d %s'%(base[:22],asal,ns,'OK' if done else 'MENTAH'))
print('---'); print('compress %d | mentah %d | byte %d -> %d | hemat %.0f%%'%(ok,cp,b,a,(1-a/b)*100 if b else 0))
if fail:
    print('gagal (tetep ke-backup):'); [print('  ',x,'|',y) for x,y in fail[:4]]
if ok==0 and cp==0: sys.exit('NOL proses')
