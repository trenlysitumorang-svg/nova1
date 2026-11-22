# Membuat dist/ (versi web + PWA) dari nova.html tanpa mengubah gameplay.
import os,shutil
src=next(p for p in ('nova.html','../battle-arena-3d.html') if os.path.exists(p))
h=open(src,encoding='utf-8').read()
tag=('<link rel="manifest" href="manifest.webmanifest"><meta name="theme-color" content="#0b0916">'
 '<meta name="mobile-web-app-capable" content="yes"><meta name="apple-mobile-web-app-capable" content="yes">'
 '<meta name="apple-mobile-web-app-title" content="NOVA"><link rel="apple-touch-icon" href="icons/icon-180.png">'
 '<link rel="icon" type="image/png" href="icons/icon-192.png">')
reg="<script>if('serviceWorker' in navigator&&(location.protocol==='https:'||location.hostname==='localhost'))addEventListener('load',()=>navigator.serviceWorker.register('sw.js').catch(()=>{}))</script>"
h=h.replace('</head>',tag+'</head>',1).replace('</body>',reg+'</body>',1)
shutil.rmtree('dist',ignore_errors=True);os.makedirs('dist/icons')
open('dist/index.html','w',encoding='utf-8').write(h)
for f in ('manifest.webmanifest','sw.js','icon.svg'):shutil.copy(f,'dist/'+f)
for f in os.listdir('icons'):shutil.copy('icons/'+f,'dist/icons/'+f)
print('dist/ siap dari',src)
