# Ringkasan: 30 Glossarium Penting pada Vibe Coding

**Sumber asli:** BuildWithAngga — oleh Angga Risky Setiawan (AI Product Engineer & Founder BuildWithAngga)
**Link:** https://buildwithangga.com/tips/30-glossarium-penting-pada-vibe-coding-yang-wajib-kamu-kuasai

> Catatan: Ini adalah ringkasan yang ditulis ulang dengan kata-kata sendiri, bukan salinan langsung dari artikel asli.

## Latar Belakang

Artikel ini lahir dari pengalaman penulis mengajar ribuan siswa vibe coding, di mana ia menyadari bahwa hambatan terbesar pemula bukan pada tools atau logika coding, melainkan pada **kosakata**. Istilah seperti "context window", "few-shot prompting", atau "hallucination" terasa asing padahal sering muncul di tutorial. Artikel ini disusun sebagai kamus referensi 30 istilah penting, dikelompokkan ke dalam 5 kategori besar, masing-masing dijelaskan dengan definisi, analogi, contoh praktis, contoh prompt, tips, dan kesalahan umum yang perlu dihindari.

## Lima Kategori Istilah

### 1. Fundamental Vibe Coding (8 istilah)
Dasar-dasar yang membentuk pemahaman inti vibe coding:
- **Vibe Coding** — pendekatan development di mana AI menjadi partner kolaboratif melalui bahasa natural, mirip kerja sama pilot dan co-pilot.
- **AI Code Editor** — editor kode yang mengintegrasikan AI secara native (misalnya Cursor), berbeda dari sekadar membuka ChatGPT di tab terpisah.
- **Code Generation** — proses AI menghasilkan kode dari instruksi bahasa natural, mulai dari level fungsi sederhana hingga sistem kompleks.
- **Natural Language Programming** — paradigma "memerintah" komputer memakai bahasa manusia, dengan AI bertindak sebagai penerjemah ke kode.
- **AI Pair Programming** — adaptasi pair programming tradisional, manusia berperan sebagai navigator/pengambil keputusan, AI sebagai driver yang mengeksekusi.
- **Prompt-to-Code** — alur transformasi dari teks prompt menjadi kode yang bisa dijalankan.
- **Context Window** — batas jumlah informasi (kode, riwayat percakapan) yang bisa "dilihat" AI dalam satu waktu, ibarat ukuran meja kerja.
- **Token** — satuan pengukuran teks yang diproses AI, memengaruhi kapasitas input/output serta biaya penggunaan.

### 2. Prompting & Communication (7 istilah)
Cara berkomunikasi efektif dengan AI:
- **Prompt Engineering** — keterampilan merancang instruksi yang jelas dan spesifik agar hasil AI optimal.
- **System Prompt** — instruksi permanen yang mengatur perilaku AI sepanjang sesi, seperti buku panduan karyawan baru.
- **Instruction Prompt** — perintah spesifik per tugas yang beroperasi dalam kerangka system prompt.
- **Few-shot Prompting** — memberi beberapa contoh sebelum tugas utama agar AI meniru pola yang diinginkan.
- **Chain-of-thought (CoT) Prompting** — meminta AI menjabarkan alur berpikirnya langkah demi langkah sebelum memberi jawaban akhir, berguna untuk logika kompleks dan debugging.
- **Iterative Prompting** — membangun hasil secara bertahap lewat beberapa putaran prompt, bukan mengharapkan hasil sempurna sekali jadi.
- **Context Injection** — menyertakan kode, dokumentasi, atau informasi relevan lain ke dalam prompt agar AI punya dasar yang cukup untuk merespons secara akurat.

### 3. Tools & Environment (6 istilah)
Perangkat populer dalam ekosistem vibe coding:
- **Cursor** — AI-first code editor berbasis VS Code, saat ini dianggap paling populer untuk vibe coding, dengan fitur Chat, Inline Edit, Composer, dan Tab Completion.
- **GitHub Copilot** — asisten coding dari GitHub/Microsoft yang menyediakan saran kode inline dan fitur chat dengan slash command (/explain, /fix, /tests).
- **Claude Code** — tool coding berbasis terminal dari Anthropic yang bersifat agentic: bisa membaca, menulis file, dan menjalankan perintah, bukan sekadar menyarankan.
- **Windsurf** — editor AI dari Codeium dengan fitur "Cascade" yang lebih otonom dalam merencanakan dan mengeksekusi tugas multi-langkah.
- **v0 (by Vercel)** — tool generasi UI dari deskripsi teks atau gambar menjadi komponen React/Tailwind siap pakai.
- **Bolt.new** — pembuat aplikasi full-stack berbasis browser, dari pembuatan hingga deployment tanpa setup lokal.

### 4. Workflow & Techniques (5 istilah)
Teknik kerja sehari-hari:
- **Scaffolding** — AI menghasilkan struktur dasar/boilerplate sebagai fondasi yang nanti diisi manual.
- **Code Refactoring (AI-assisted)** — merestrukturisasi kode dengan bantuan AI untuk keterbacaan, performa, atau pola desain tanpa mengubah perilaku eksternal.
- **Inline Completion** — saran kode real-time ("ghost text") yang muncul saat mengetik, mirip prediksi teks di ponsel.
- **Chat-based Coding** — interaksi coding melalui percakapan alami dengan AI, mirip diskusi dengan rekan kerja.
- **Agentic Coding** — AI diberi tujuan besar dan otonomi untuk merencanakan serta mengeksekusi banyak langkah sendiri, bukan dipandu langkah demi langkah.

### 5. Quality & Best Practices (4 istilah)
Menjaga kualitas hasil AI:
- **Code Review (AI-assisted)** — memakai AI sebagai reviewer tambahan untuk memeriksa bug, keamanan, performa, dan best practice.
- **Hallucination** — ketika AI menghasilkan kode yang terlihat benar tapi memakai API/library/metode yang sebenarnya tidak ada atau sudah usang.
- **Grounding** — teknik menambatkan respons AI pada informasi faktual (kode nyata, dokumentasi, tipe data) untuk mengurangi halusinasi.
- **Human-in-the-Loop** — prinsip bahwa manusia tetap mengawasi, meninjau, dan menyetujui hasil kerja AI, bukan membiarkannya berjalan otomatis penuh.

## Rekomendasi Alur Belajar
Artikel menyarankan jalur belajar 4 minggu: minggu 1 kuasai fundamental, minggu 2 pelajari teknik prompting, minggu 3 fokus mendalami satu tool (disarankan Cursor untuk pemula), minggu 4 kembangkan workflow sendiri, dan seterusnya terus menjaga kualitas lewat human-in-the-loop.

## Penutup
Penulis menekankan bahwa menghafal istilah bukan tujuan akhir — vocabulary hanyalah titik awal. Penguasaan sejati datang dari praktik langsung: membangun proyek, membuat kesalahan, dan mengulang proses belajar. Artikel ditutup dengan ajakan mencoba kelas-kelas gratis di platform BuildWithAngga sebagai kelanjutan pembelajaran.
