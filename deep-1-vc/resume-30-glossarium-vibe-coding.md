# Resume: 30 Glossarium Penting pada Vibe Coding

**Sumber:** BuildWithAngga — oleh Angga Risky Setiawan (AI Product Engineer & Founder BuildWithAngga)
**Kategori:** Automation | Dipublikasikan: 28 Januari 2026

---

## Latar Belakang

Artikel ini lahir dari pengalaman penulis mengajar ribuan siswa vibe coding di BuildWithAngga. Kendala terbesar pemula ternyata bukan soal tools atau kode, melainkan **istilah/vocabulary** yang muncul di setiap tutorial — seperti *context window*, *few-shot prompting*, *hallucination*, atau *grounding*.

Vibe coding dianggap sebagai irisan dari tiga domain, masing-masing dengan bahasanya sendiri:
1. **AI Concepts** — token, context, prompt, hallucination
2. **Coding Practices** — refactor, scaffold, review, debug, test
3. **Tools & Workflow** — Cursor, Copilot, v0, Bolt, Windsurf

Tanpa memahami vocabulary ini, seseorang akan kesulitan mengikuti tutorial, berkomunikasi dengan AI secara efektif, berdiskusi dengan developer lain, dan melakukan troubleshooting.

Ke-30 istilah dikelompokkan ke dalam **5 kategori**, dan setiap istilah dijelaskan dengan definisi, analogi, contoh praktis, contoh prompt, tips, serta kesalahan umum yang perlu dihindari.

---

## Kategori 1: Fundamental Vibe Coding (8 istilah)

Istilah dasar yang muncul di hampir semua diskusi vibe coding.

| Istilah | Inti Penjelasan |
|---|---|
| **Vibe Coding** | Pendekatan pengembangan software di mana developer menulis kode lewat bahasa natural bersama AI sebagai partner kolaboratif — diibaratkan seperti pilot dan co-pilot pesawat. AI memperkuat kemampuan developer, bukan menggantikannya. |
| **AI Code Editor** | Editor kode yang sudah terintegrasi AI secara native (mis. Cursor), sehingga generate, refactor, dan chat dengan AI terjadi dalam satu tempat kerja, tanpa perlu berpindah ke tab browser lain. |
| **Code Generation** | Proses AI "menulis" kode dari instruksi bahasa natural, mulai dari level fungsi sederhana sampai sistem kompleks (autentikasi, dsb). |
| **Natural Language Programming** | Paradigma di mana developer cukup mendeskripsikan logika yang diinginkan dalam bahasa manusia, dan AI menerjemahkannya menjadi kode dengan sintaks yang benar. |
| **AI Pair Programming** | Adaptasi dari pair programming tradisional — manusia berperan sebagai navigator yang mengarahkan, AI berperan sebagai driver yang mengeksekusi dan memberi saran. |
| **Prompt-to-Code** | Alur kerja inti vibe coding: input berupa prompt teks diproses menjadi kode yang bisa langsung dijalankan. |
| **Context Window** | Batas "memori" AI — seberapa banyak kode dan riwayat percakapan yang bisa dipertimbangkan AI saat merespons. Diibaratkan seperti ukuran meja kerja: makin besar, makin banyak referensi yang bisa dilihat sekaligus. |
| **Token** | Satuan pengukuran teks yang diproses AI, menentukan kapasitas input/output serta biaya penggunaan API. |

---

## Kategori 2: Prompting & Communication (7 istilah)

Fokus pada cara berkomunikasi dengan AI agar hasilnya optimal.

| Istilah | Inti Penjelasan |
|---|---|
| **Prompt Engineering** | Skill merancang instruksi yang jelas dan spesifik agar AI menghasilkan output berkualitas — mencakup teknik seperti memberi konteks, menentukan format output, dan menetapkan batasan (constraint). |
| **System Prompt** | Instruksi permanen yang mengatur "mode operasi" AI sepanjang sesi — mirip employee handbook yang menetapkan tech stack, standar kode, dan gaya respons yang harus diikuti. |
| **Instruction Prompt** | Perintah spesifik per-task yang dijalankan dalam kerangka yang sudah ditetapkan system prompt — seperti penugasan kerja harian di bawah job description. |
| **Few-shot Prompting** | Teknik memberi beberapa contoh (2–5) sebelum meminta AI mengerjakan task baru, agar AI meniru pola/format dari contoh tersebut. |
| **Chain-of-thought (CoT) Prompting** | Meminta AI menjabarkan alasan/langkah berpikirnya sebelum memberi jawaban akhir — berguna untuk keputusan arsitektur atau debugging yang kompleks. |
| **Iterative Prompting** | Membangun hasil akhir secara bertahap lewat banyak putaran prompt, alih-alih mencoba mendapatkan hasil sempurna dalam satu permintaan besar. |
| **Context Injection** | Menyisipkan kode, dokumentasi, atau contoh yang relevan ke dalam prompt agar AI punya dasar yang cukup untuk memberi jawaban yang akurat dan konsisten. |

---

## Kategori 3: Tools & Environment (6 istilah)

Alat-alat populer yang digunakan dalam praktik vibe coding.

| Tool | Inti Penjelasan |
|---|---|
| **Cursor** | AI code editor berbasis VS Code, saat ini paling populer untuk vibe coding karena fitur Chat, Inline Edit, Composer, dan Tab completion yang terintegrasi mulus. |
| **GitHub Copilot** | Asisten coding AI dari GitHub/Microsoft, bekerja sebagai extension dengan fitur saran kode inline dan Copilot Chat untuk tanya-jawab maupun perintah slash (`/explain`, `/fix`, `/tests`). |
| **Claude Code** | Tool coding berbasis terminal dari Anthropic yang bersifat agentic — dapat membaca, menulis file, dan menjalankan perintah, bukan sekadar menyarankan. |
| **Windsurf** | Editor AI dari Codeium dengan asisten "Cascade" yang lebih otonom — bisa merencanakan dan mengeksekusi task multi-langkah dari satu tujuan besar. |
| **v0 (by Vercel)** | Tool generasi UI berbasis AI yang mengubah deskripsi teks atau gambar referensi menjadi komponen React/Next.js siap pakai dengan Tailwind CSS. |
| **Bolt.new** | Pembuat aplikasi full-stack berbasis browser — tanpa setup lokal, langsung membangun frontend, backend, dan database, lalu bisa di-deploy sekali klik. |

---

## Kategori 4: Workflow & Techniques (5 istilah)

Cara kerja dan teknik penggunaan AI dalam alur kerja sehari-hari.

| Istilah | Inti Penjelasan |
|---|---|
| **Scaffolding** | AI menghasilkan struktur dasar/boilerplate (kerangka project atau fitur) sebagai titik awal yang kemudian diisi manual dengan logika bisnis. |
| **Code Refactoring (AI-assisted)** | Proses menata ulang kode yang sudah ada dengan bantuan AI untuk meningkatkan keterbacaan, performa, atau kepatuhan pola — tanpa mengubah perilaku eksternalnya. |
| **Inline Completion** | Saran kode real-time berupa "ghost text" saat mengetik, mirip predictive text di ponsel tapi jauh lebih canggih. |
| **Chat-based Coding** | Interaksi dengan AI lewat antarmuka percakapan, mirip mengobrol dengan rekan senior yang selalu siap membantu. |
| **Agentic Coding** | Pendekatan di mana AI diberi tujuan besar (bukan langkah demi langkah) dan AI sendiri yang merencanakan serta mengeksekusi banyak langkah dengan intervensi manusia minimal. |

---

## Kategori 5: Quality & Best Practices (4 istilah)

Menjaga kualitas output AI agar tetap andal dan bisa dipercaya.

| Istilah | Inti Penjelasan |
|---|---|
| **Code Review (AI-assisted)** | Menggunakan AI sebagai reviewer tambahan untuk memeriksa bug, keamanan, performa, dan kepatuhan best practice sebelum kode di-merge. |
| **Hallucination** | Situasi ketika AI menghasilkan kode yang terlihat benar tapi sebenarnya memakai API, library, atau sintaks yang tidak ada/salah — disampaikan dengan nada percaya diri seolah benar. |
| **Grounding** | Teknik menjangkarkan respons AI pada informasi faktual, kode yang sudah ada, atau dokumentasi, untuk mengurangi risiko hallucination. |
| **Human-in-the-Loop (HITL)** | Prinsip bahwa manusia tetap memegang kendali pengawasan, persetujuan, dan pengambilan keputusan meski AI melakukan sebagian besar pekerjaan teknis — mirip mobil self-driving yang tetap diawasi pengemudi. |

---

## Rekomendasi Alur Belajar (dari Artikel)

1. **Minggu 1** — Kuasai istilah fundamental (#1–8), coba vibe coding dasar.
2. **Minggu 2** — Pelajari teknik prompting (#9–15), bangun template prompt pribadi.
3. **Minggu 3** — Pilih satu tool utama (disarankan **Cursor** untuk pemula), pelajari secara mendalam.
4. **Minggu 4** — Kembangkan workflow sendiri lewat proyek nyata (#22–26).
5. **Berkelanjutan** — Internalisasi prinsip kualitas (#27–30): selalu review output AI dan tetap human-in-the-loop.

---

## Kesimpulan

Glossary ini dimaksudkan sebagai **titik awal**, bukan tujuan akhir. Penguasaan sejati datang dari praktik langsung — membangun proyek, melakukan kesalahan, dan mengulanginya. Istilah-istilah teknis ini akan terasa lebih familiar seiring semakin sering digunakan dalam proyek nyata.

Artikel asli juga menyertakan promosi kelas-kelas gratis di BuildWithAngga (Web Development Fundamentals, JavaScript Modern, React Basics, Tailwind CSS, Git & GitHub) sebagai langkah lanjutan bagi pembaca yang ingin belajar terstruktur.

---

*Resume ini merangkum poin-poin utama dari artikel asli "30 Glossarium Penting Pada Vibe Coding yang Wajib Kamu Kuasai" karya Angga Risky Setiawan di BuildWithAngga. Untuk contoh kode lengkap, contoh prompt siap pakai, dan penjelasan detail tiap istilah, silakan baca artikel aslinya di [buildwithangga.com](https://buildwithangga.com/tips/30-glossarium-penting-pada-vibe-coding-yang-wajib-kamu-kuasai).*
