# jsafe v2: balance=INFO (regex naif bohong pada URL-dalam-string), verdict=ghoib/trailing/mix saja; INV perluas operator-unicode (escape ASCII, kebal ligatur/clipboard)
import sys,os,re
INV={'\ufeff':'BOM','\u00a0':'NBSP','\u200b':'ZWSP','\u200d':'ZWJ','\u200e':'LRM','\u200f':'RLM','\u2060':'WJ','\u202f':'NNBSP','\u00ad':'SHY','\u2260':'NEQ(!=)','\u2265':'GE(>=)','\u2264':'LE(<=)','\u2192':'ARR(->)','\u2190':'LARR(<-)','\u2194':'HARR(<->)','\u21d2':'RARROW(=>)','\u00ac':'NOT(!)','\u2227':'AND(&&)','\u2228':'OR(||)'}
def scan(s):
    bad=[]
    for i,l in enumerate(s.split('\n'),1):
        for j,ch in enumerate(l,1):
            if ch in INV: bad.append((i,j,INV[ch],hex(ord(ch))))
        if l!=l.rstrip(): bad.append((i,len(l)+1,'TRAILING_WS','-'))
    return bad
def strip(s):
    s=re.sub(r'/\*.*?\*/','',s,flags=re.S); s=re.sub(r'//[^\n]*','',s)
    s=re.sub(r'`[^`]*`','',s,flags=re.S); s=re.sub(r"'[^']*'",'',s); s=re.sub(r'"[^"]*"','',s)
    return re.sub(r'\{\{.*?\}\}','',s,flags=re.S)
def bal(s):
    c=strip(s); out=[]
    for a,b,n in [('{','}','brace'),('(',')','paren'),('[',']','bracket')]:
        d=c.count(a)-c.count(b)
        if d: out.append('%s %+d'%(n,d))
    if c.count("'")%2: out.append('squote_odd')
    if c.count('"')%2: out.append('dquote_odd')
    return out
def style(s):
    ls=s.split('\n'); ind=set(); semi=0; kw=0
    for l in ls:
        m=re.match(r'^( +)',l)
        if m: ind.add(len(m.group(1)))
        if re.search(r'\w;\s*$',l): semi+=1
        if re.match(r'^\s*(const|let|var|function|return|if)\b',l): kw+=1
    tabs=sum(1 for l in ls if '\t' in l); crlf=s.count('\r\n'); lf=s.count('\n')-crlf
    return {'indent_sp':sorted(ind),'tabs':tabs,'semi':semi,'kw':kw,'crlf':crlf,'lf':lf}
def report(name,s):
    bad=scan(s); bb=bal(s); st=style(s)
    print('=== %s ==='%name); print('  gaya:',st)
    if bad:
        print('  [GHOIB/WS] %d:'%len(bad))
        for i,j,nm,cp in bad[:20]: print('    baris %d kol %d: %s %s'%(i,j,nm,cp))
        if len(bad)>20: print('    ... +%d lagi'%(len(bad)-20))
    if bb: print('  [INFO-BALANCE-parsial]',bb,'<< regex naif, JANGAN dipercaya, pakai compiler')
    if st['tabs'] and st['indent_sp']: print('  [MIX-INDENT] tab+%d spasi'%st['tabs'])
    if st['crlf'] and st['lf']: print('  [MIX-EOL] crlf=%d lf=%d'%(st['crlf'],st['lf']))
    ok=not bad; print('  => %s'%('BERSIH' if ok else 'MELESET')); return ok
mode=sys.argv[1] if len(sys.argv)>1 else ''
if mode=='check':
    p=sys.argv[2]; s=open(p,encoding='utf-8',errors='replace').read(); sys.exit(0 if report(p,s) else 1)
elif mode=='write':
    p=sys.argv[2]; s=sys.stdin.read()
    if not report(p,s): print('>> NOL nulis, perbaiki dulu'); sys.exit(1)
    os.makedirs(os.path.dirname(p) or '.',exist_ok=True); open(p,'w',encoding='utf-8').write(s); print('>> TERTULIS',p)
else: print('pakai: jsafe.py check <file>  |  jsafe.py write <file> < konten'); sys.exit(2)