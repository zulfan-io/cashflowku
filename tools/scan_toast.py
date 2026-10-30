import re,subprocess
r=subprocess.run(['grep','-rlE',r'const useToast[ \t]*=[ \t]*toast\(\)','src','--include=*.ts','--include=*.vue'],capture_output=True,text=True)
files=sorted(f for f in r.stdout.split() if f)
print('TOTAL file dgn pola:',len(files)); print('='*50)
for P in files:
    s=open(P,encoding='utf-8').read()
    lines=s.split('\n')
    # posisi baris target
    tgt=[i for i,l in enumerate(lines) if re.search(r'const useToast[ \t]*=[ \t]*toast\(\)',l)]
    if not tgt: continue
    ti=tgt[0]
    if P.endswith('.ts'):
        verdict='PATCH (module-scope, .ts)'; reason='file TS, top-level = module scope'
    else:
        # cari block <script ...> ... </script>, cek baris ti di block mana
        blocks=[]
        for m in re.finditer(r'<script([^>]*)>(.*?)</script>', s, re.S):
            start=s[:m.start(2)].count('\n'); end=start+m.group(2).count('\n')
            blocks.append((start,end,'setup' in m.group(1)))
        inside=[b for b in blocks if b[0]<=ti<=b[1]]
        if inside and inside[0][2]:
            verdict='SKIP (AMAN, <script setup>)'; reason='call di dalam setup function = pinia aktif'
        elif inside:
            verdict='PATCH (<script> non-setup)'; reason='call di block script tanpa setup = module scope'
        else:
            verdict='PATCH (di luar script block)'; reason='nggak ketemu di block script mana pun'
    print('%-4s %-55s %s'%(verdict.split()[0], P, reason))
    print('     line %d: %s'%(ti+1, lines[ti].strip()))
print('='*50)
print('DRY-RUN: NOL file ditulis. Lo liat PATCH vs SKIP, baru gue kasih versi tulis.')
