# NOVA — Nexus of Valor and Ascension · paket platform (v2.25)
Orientasi dikunci landscape (manifest + Android). Satu inti game: `nova.html` (HTML + CSS + JS + Three.js, satu file). Nama lama: Battle Arena Absurd.

## Status jujur
| Target | Status |
|---|---|
| Browser (Chrome/Edge/Firefox/Safari) | ✅ jalan (diuji Chromium) |
| PWA / pasang dari browser | ✅ diuji di Chromium lokal: manifest, ikon, service worker, main offline. Belum diuji di HP/Safari asli |
| APK / AAB Android | ⚠️ BELUM dibangun. Workflow siap (`.github/workflows/android.yml`) tapi belum pernah dijalankan; lingkungan saya tidak punya Android SDK/jaringan |
| Windows / macOS / Linux (Tauri) | ⚠️ workflow siap (`desktop.yml`), belum dijalankan/diuji |
| iOS | ⚠️ hanya `npm run ios` (butuh Mac + Xcode + akun Apple Developer); belum diterbitkan |
| Multiplayer / cloud save | ❌ belum ada (sengaja) |

## 1. Main di browser / pasang sebagai aplikasi (PWA)
1. `python3 build_web.py` → folder `dist/`.
2. Upload `dist/` ke hosting HTTPS (GitHub Pages: pakai `web.yml`, Netlify, Cloudflare Pages, dll.).
3. Buka alamatnya di Chrome Android → menu ⋮ → **Pasang aplikasi**. PC Chrome/Edge: ikon pasang di address bar. iPhone Safari: Bagikan → Tambahkan ke Layar Utama.
Tes lokal: `cd dist && python3 -m http.server 8080` lalu buka http://localhost:8080.

## 2. APK + AAB Android (tanpa install Android Studio)
1. Buat repo GitHub baru, upload ISI folder ini (termasuk `.github/`).
2. Tab **Actions** → *Build NOVA Android* → **Run workflow**.
3. Selesai (±10 mnt) → unduh artefak **NOVA-android** (APK debug bisa langsung dipasang di HP; izinkan "pasang dari sumber tidak dikenal").
4. Untuk Google Play, AAB harus ditandatangani dengan keystore milikmu (belum disiapkan di sini).
5. Setelah punya link unduh APK, isi `NOVA_APK_URL` di `nova.html` supaya tombol *Unduh APK* muncul di menu game.
Manual (Android Studio): `npm install && npm run android && npx cap open android`.

## 3. Desktop
Actions → *Build NOVA Desktop* → unduh installer (.msi/.exe, .dmg, .deb/.AppImage). Manual: butuh Rust + Node, `npm install && npm run desktop`.

## 4. iOS
Mac + Xcode: `npm install && npm run ios && npx cap open ios`, lalu Signing di Xcode, uji di perangkat, distribusi via TestFlight/App Store.
