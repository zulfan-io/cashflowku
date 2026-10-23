import sys,os,shutil,subprocess
SPEC="1|swipe-hero|webm|m;2|avatar-shop|png|s;3|avatar-store|png|s;4|avatar-customer|png|s;5|notif-1|jpg|s;6|notif-2|jpg|s;7|notif-3|jpg|s;8|notif-4|jpg|s;9|notif-5|jpg|s;10|preview-1|jpg|s;11|preview-2|jpg|s;12|preview-3|jpg|s;13|preview-4|jpg|s;14|preview-5|jpg|s;15|insurance|png|s;16|hero-loop-bg|webm|m;17|category-orbit|webm|m;18|gift-bounce|json|j;19|flash-badge-pulse|json|j;20|cart-add-pop|json|j;21|success-check-draw|json|j;22|empty-cart-wave|json|j;23|coin-stack|json|j;24|mascot-kilat|png|s;25|badge-flash|png|s;26|badge-xpress|png|s;27|sticker-discount|png|s;28|gift-box-open|png|s;29|voucher-ticket|png|s;30|wallet-topup|png|s;31|qr-frame|png|s;32|trophy|png|s;33|sparkle|png|s;34|arrow-tap|png|s;35|divider-wave|svg|s;36|empty-illustration|png|s;37|bell-new|png|s;38|location-pin|png|s;39|star-rating-fill|svg|s;40|star-rating-empty|svg|s"
M={}
for t in SPEC.split(';'):
    if not t: continue
    a,b,c,d=t.split('|'); M[int(a)]=(b,c,d)
SRC=os.path.expanduser('~/storage/downloads/ImageKilat')
DST='public/img/gen'
if not os.path.isdir('src'): print('[ERR] bukan root repo -> cd ~/cashflowku'); sys.exit(1)
if not os.path.isdir(SRC): print('[ERR] kotak ImageKilat belum ada'); sys.exit(1)
if not shutil.which('ffmpeg'): print('[ERR] ffmpeg belum -> pkg install -y ffmpeg'); sys.exit(1)
os.makedirs(DST,exist_ok=True)
VID=('mp4','mov','mkv','avi','webm','gif')
STL=('png','jpg','jpeg','webp')
def conv(src,dst,tg):
    if tg=='gif':
        cmd=['ffmpeg','-y','-i',src,'-vf','fps=10,scale=480:-1:flags=lanczos,split[a][b];[a]palettegen[p];[b][p]paletteuse',dst]
    elif tg=='webm':
        cmd=['ffmpeg','-y','-i',src,'-c:v','libvpx-vp9','-crf','32','-b:v','0','-vf','scale=1280:-2:flags=lanczos','-row-mt','1','-an',dst]
    elif tg=='mp4':
        cmd=['ffmpeg','-y','-i',src,'-c:v','libx264','-crf','28','-preset','veryfast','-vf','scale=1280:-2:flags=lanczos','-movflags','+faststart','-an',dst]
    else:
        return False
    r=subprocess.run(cmd,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
    if r.returncode!=0:
        print('[FFERR]',os.path.basename(src),r.stderr.decode('utf-8','ignore')[-180:]); return False
    return True
found={}
for f in sorted(os.listdir(SRC)):
    base,_,ext=f.partition('.'); ext=ext.lower()
    if not base.isdigit(): continue
    n=int(base)
    if n not in M: print('[SKIP]',f,'(nomor di luar 1-40)'); continue
    if n in found: print('[SKIP]',f,'(dobel, pakai',found[n],')'); continue
    found[n]=f
    name,tg,kd=M[n]; pipe=name+'.'+tg; sp=os.path.join(SRC,f); dp=os.path.join(DST,pipe)
    if kd=='m':
        if ext in VID:
            if ext==tg: shutil.copy2(sp,dp); print('[OK-copy]',f,'->',pipe)
            elif conv(sp,dp,tg): print('[OK-conv]',f,'->',pipe,'(convert+compress)')
        elif ext in STL:
            shutil.copy2(sp,dp); print('[WARN]',f,'->',pipe,'(still di slot gerak: DIEM, ganti Canva/Runway)')
        else: print('[SKIP]',f,'(ekstensi',ext,'bukan video)')
    elif kd=='j':
        if ext=='json': shutil.copy2(sp,dp); print('[OK]',f,'->',pipe)
        else: print('[SKIP-strict]',f,'-> kursi',n,'butuh .json LottieFiles, bukan .'+ext)
    else:
        if tg=='svg':
            if ext=='svg': shutil.copy2(sp,dp); print('[OK]',f,'->',pipe)
            else: print('[SKIP-strict]',f,'-> kursi',n,'butuh .svg vector, bukan .'+ext)
        elif ext in VID:
            print('[SKIP]',f,'-> video di slot still, pindahin ke slot gerak (1/16/17)')
        elif ext in STL:
            shutil.copy2(sp,dp)
            if ext!=tg: print('[WARN-ext]',f,'->',pipe,'(ekstensi beda, tetep salin)')
            else: print('[OK]',f,'->',pipe)
        else: print('[SKIP]',f,'(ekstensi',ext,'bukan gambar)')
miss=[n for n in sorted(M) if n not in found]
if miss:
    print('--- WAIT (antrean, bukan kuota) ---')
    for n in miss:
        nm,pe,_=M[n]; print('  kursi',n,'=',nm+'.'+pe)
print('=== RINGKAS terisi',len(found),'/',len(M),'wait',len(miss),'===')
