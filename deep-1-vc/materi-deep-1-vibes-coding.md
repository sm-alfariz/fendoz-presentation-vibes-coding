# Glossarium Key Penting Pada Vibe Coding yang Wajib Kamu Kuasai

### 30 istilah



![30 Glossarium Penting Pada Vibe Coding yang Wajib Kamu Kuasai](https://bwaplatformbucket.sgp1.cdn.digitaloceanspaces.com/assets/thumbnail_tips/buildwithangga-thumbnail-tips-edxxb-30-glossarium-penting-pada-vibe-coding-yang-wajib-kamu-kuasai-30-glossarium-penting-pada-vibe-coding-yang-wajib-kamu-kuasai-buildwithangga-ZA5oJ6.png)

Kamus Lengkap Istilah Vibe Coding dari A-Z untuk Pemula hingga Advanced

## Opening: Ketika Istilah Baru Bikin Overwhelmed

### Cerita yang Mungkin Familiar

Kamu baru mulai tertarik dengan vibe coding. Buka YouTube, cari tutorial, excited banget mau belajar.

Video pertama dimulai:

_"Okay, jadi kita akan pakai Cursor sebagai AI code editor. Pastikan context window cukup untuk project kamu. Nanti kita akan inject context dari beberapa files, pakai few-shot prompting untuk consistency, dan leverage chain-of-thought untuk complex logic. Kalau hasilnya hallucination, kita grounding dengan existing codebase..."_

Kamu pause video.

_"Wait... apa tadi? Context window? Few-shot? Hallucination? Grounding? Ini bahasa planet mana?"_

Sound familiar?

Kalau iya, kamu gak sendirian. Ini adalah pengalaman yang **sangat umum** bagi siapa saja yang baru masuk ke dunia vibe coding.


_"Mas, prompt engineering itu apa sih?""Bedanya system prompt sama instruction prompt apa?""Agentic coding maksudnya gimana?"_

Saya realize: sebelum bisa master vibe coding, kamu perlu **paham bahasanya** dulu. Dan itulah kenapa saya tulis artikel ini.

### Kenapa Glossary Ini Penting

Vibe coding adalah intersection dari **tiga domain** yang masing-masing punya vocabulary sendiri:

```yaml
VIBE CODING VOCABULARY:

┌────────────────────────────────────────────────────────────┐
│                       VIBE CODING                          │
│                                                            │
│    ┌─────────────┐  ┌─────────────┐  ┌─────────────┐       │
│    │     AI      │  │   CODING    │  │   TOOLS     │       │
│    │  CONCEPTS   │  │  PRACTICES  │  │ & WORKFLOW  │       │
│    │             │  │             │  │             │       │
│    │ - Token     │  │ - Refactor  │  │ - Cursor    │       │
│    │ - Context   │  │ - Scaffold  │  │ - Copilot   │       │
│    │ - Prompt    │  │ - Review    │  │ - v0        │       │
│    │ - Halluci-  │  │ - Debug     │  │ - Bolt      │       │
│    │   nation    │  │ - Test      │  │ - Windsurf  │       │
│    └─────────────┘  └─────────────┘  └─────────────┘       │
│                                                            │
└────────────────────────────────────────────────────────────┘

Tanpa paham vocabulary dari ketiga domain ini,
kamu akan struggle untuk:
├── Follow tutorials dan dokumentasi
├── Communicate dengan AI effectively
├── Diskusi dengan sesama developer
└── Troubleshoot masalah yang muncul
```

### Cara Menggunakan Artikel Ini

Artikel ini bisa kamu gunakan dengan beberapa cara:

**📖 Sequential Reading** Baca dari awal sampai akhir untuk full understanding. Recommended untuk yang baru mulai.

**🔍 Reference / Lookup** Bookmark artikel ini. Kapanpun ketemu istilah yang gak familiar, kembali ke sini.

**📚 Category Deep Dive** Fokus ke satu kategori yang paling relevan dengan kebutuhan kamu saat ini.

**💬 Before Learning Session** Baca relevant terms sebelum mulai tutorial atau course baru.

### Format Setiap Istilah

Untuk setiap dari 30 istilah, saya sertakan:

| Component | Isi |
| --- | --- |
| 📖 **Definisi** | Penjelasan clear dan comprehensive |
| 💡 **Analogi** | Perbandingan dengan sesuatu familiar |
| 🔧 **Contoh Praktis** | Real-world usage |
| 💬 **Contoh Prompt** | Prompt yang bisa langsung dicopy |
| ⚡ **Tips & Tricks** | Pro tips untuk memaksimalkan |
| ⚠️ **Common Mistakes** | Kesalahan yang harus dihindari |

### Overview 5 Kategori

30 istilah ini dikelompokkan ke dalam 5 kategori:

| # | Kategori | Fokus | Jumlah |
| --- | --- | --- | --- |
| 1 | **Fundamental Vibe Coding** | Dasar-dasar yang harus semua orang tau | 8 istilah |
| 2 | **Prompting & Communication** | Cara berkomunikasi dengan AI | 7 istilah |
| 3 | **Tools & Environment** | Alat-alat yang dipakai | 6 istilah |
| 4 | **Workflow & Techniques** | Cara kerja dan teknik | 5 istilah |
| 5 | **Quality & Best Practices** | Menjaga kualitas output | 4 istilah |

Mari kita mulai dari kategori pertama — fundamental yang harus semua orang kuasai.

* * *

## Kategori 1: Fundamental Vibe Coding

Ini adalah istilah-istilah dasar yang akan kamu temui di **setiap** diskusi tentang vibe coding. Kalau kamu baru mulai, prioritaskan kategori ini.

* * *

### 1\. Vibe Coding

📖 **Definisi:** Vibe coding adalah pendekatan development di mana developer menggunakan AI sebagai collaborative partner untuk menulis code melalui natural language. Istilah "vibe" merujuk pada flow kolaboratif antara manusia dan AI — kamu describe "vibe" atau feel yang diinginkan, AI membantu wujudkan dalam bentuk code. Bukan AI yang menggantikan developer, tapi AI yang amplify kemampuan developer.

💡 **Analogi:** Seperti bekerja dengan **co-pilot pesawat**. Kamu sebagai pilot utama yang menentukan destination, membuat keputusan critical, dan bertanggung jawab atas keseluruhan flight. Co-pilot (AI) membantu dengan navigation, monitor instruments, handle routine tasks, dan suggest kalau ada yang perlu diperhatikan. Pesawat tetap butuh pilot — co-pilot ada untuk membuat pilot lebih effective.

🔧 **Contoh Praktis:**

```markdown
TRADITIONAL CODING WORKFLOW:
────────────────────────────
1. Buka dokumentasi framework
2. Search Stack Overflow untuk pattern
3. Tulis code line by line
4. Debug dengan console.log
5. Google setiap error message
6. Repeat untuk setiap feature

Time: 4 jam untuk satu form component

VIBE CODING WORKFLOW:
─────────────────────
1. "Buatkan form registration dengan email, password,
    confirm password, dan validation"
2. AI generate code
3. Review dan test
4. "Tambahkan phone number field dengan format Indonesia"
5. AI update code
6. "Add loading state dan error handling"
7. Done!

Time: 30 menit untuk form yang lebih complete
```

💬 **Contoh Prompt:**

```diff
Saya mau build landing page untuk startup SaaS.

CONTEXT:
- Tech: Next.js 14, TypeScript, Tailwind CSS
- Style: Modern, minimalist, professional
- Target: B2B software companies

TASK:
Mulai dengan Hero section yang include:
- Headline yang catchy tentang productivity
- Subheadline yang explain value proposition
- Primary CTA button "Start Free Trial"
- Secondary CTA "Watch Demo"
- Abstract illustration placeholder

Generate code-nya dan explain structure yang kamu pilih.
```

⚡ **Tips & Tricks:**

- Treat AI sebagai junior developer yang capable tapi perlu direction
- Clear instruction menghasilkan better output
- Iterate dan refine — jangan expect perfect di first attempt
- Tetap review dan understand code yang di-generate
- Build mental model dari patterns yang AI gunakan

⚠️ **Common Mistakes:**

- Expect AI melakukan semua tanpa guidance → AI butuh direction
- Copy-paste tanpa understand → Kamu harus own the code
- Skip planning, langsung coding → Still need architecture thinking
- Gak verify output sebelum lanjut → Bugs compound
- Think vibe coding = no skill needed → Skill tetap essential

* * *

### 2\. AI Code Editor

📖 **Definisi:** Code editor yang sudah terintegrasi dengan AI capabilities secara native, memungkinkan code generation, intelligent completion, refactoring, dan assistance langsung dalam editor. Berbeda dengan menggunakan ChatGPT di browser terpisah, AI code editor menyatukan coding dan AI assistance dalam satu environment yang seamless.

💡 **Analogi:** Kalau code editor biasa seperti **mesin ketik canggih** — powerful untuk mengetik tapi kamu kerja sendiri. AI code editor seperti mesin ketik yang punya **asisten duduk di sebelah kamu**, siap membantu kapan saja kamu butuh, tau apa yang sedang kamu kerjakan, dan bisa langsung action tanpa kamu harus keluar dari flow.

🔧 **Contoh Praktis:**

```diff
REGULAR VS CODE:
────────────────
- Ketik code manual
- Autocomplete dari snippets yang terbatas
- Extension untuk formatting
- Perlu buka browser untuk ChatGPT
- Copy-paste code bolak-balik

AI CODE EDITOR (Cursor):
────────────────────────
- Ketik sebagian → AI complete sisanya
- Select code → "Refactor this to be cleaner"
- Chat panel untuk complex questions
- AI understand SELURUH codebase kamu
- Context-aware suggestions
- Multi-file edits dalam satu command

POPULAR AI CODE EDITORS:
├── Cursor (paling populer untuk vibe coding)
├── GitHub Copilot + VS Code
├── Windsurf (Codeium)
├── Zed (dengan AI integration)
├── Void (open source)
└── Continue (open source extension)
```

💬 **Contoh Prompt (di Cursor Chat):**

```less
@src/components/Navbar.tsx
@src/components/Footer.tsx

Lihat pattern dan style dari kedua components ini.
Sekarang buatkan Sidebar component yang:
- Follow exact same coding patterns
- Use same styling approach
- Include navigation items: Dashboard, Projects, Settings
- Collapsible on mobile

Ensure consistency dengan existing components.
```

💬 **Contoh Prompt (Cursor Inline dengan Cmd+K):**

```sql
[Select sebuah function yang messy]

Refactor this function:
- Use early returns
- Add proper TypeScript types
- Improve variable naming
- Add error handling
```

⚡ **Tips & Tricks:**

- Learn keyboard shortcuts — Cmd+L (chat), Cmd+K (inline), Cmd+I (composer)
- Use @mentions untuk include specific files sebagai context
- Chat untuk planning dan complex questions, Inline untuk quick edits
- Setup .cursorrules file untuk project-specific instructions
- Combine features: plan di chat, execute dengan composer

⚠️ **Common Mistakes:**

- Cuma pakai Chat, ignore Inline dan Composer → Miss productivity gains
- Gak leverage @mentions untuk context → AI missing information
- Not customizing settings dan rules → Generic suggestions
- Ignore Tab completions → Free productivity left on table
- Expect one editor fits all → Different editors untuk different needs

* * *

### 3\. Code Generation

📖 **Definisi:** Proses di mana AI menghasilkan code berdasarkan instruksi dalam bahasa natural, partial code, atau specifications. AI "menulis" code berdasarkan understanding dari prompt, context yang diberikan, dan patterns yang dipelajari dari training data. Code generation bisa range dari single function sampai entire features.

💡 **Analogi:** Seperti memesan pakaian ke **tailor custom**. Kamu describe apa yang kamu mau: "Kemeja biru, lengan panjang, slim fit, kancing putih, pocket di dada kiri." Tailor (AI) yang punya skill dan knowledge untuk wujudkan description itu menjadi produk jadi. Semakin detail description-nya, semakin sesuai hasilnya.

🔧 **Contoh Praktis:**

```bash
CODE GENERATION LEVELS:

LEVEL 1 - SIMPLE (Single function):
─────────────────────────────────────
Prompt: "Buatkan function untuk validate Indonesian phone number"

Output:
function validatePhoneIndonesia(phone: string): boolean {
  const regex = /^(\\+62|62|0)8[1-9][0-9]{6,10}$/;
  return regex.test(phone.replace(/[\\s-]/g, ''));
}

LEVEL 2 - MEDIUM (Component):
─────────────────────────────
Prompt: "Buatkan ProductCard component dengan image,
        title, price, dan add to cart button"

Output: Complete React component dengan props,
        styling, dan event handlers

LEVEL 3 - COMPLEX (Feature):
────────────────────────────
Prompt: "Buatkan shopping cart feature dengan add,
        remove, update quantity, dan total calculation"

Output: Multiple functions, state management,
        persistence logic, UI components

LEVEL 4 - ADVANCED (System):
────────────────────────────
Prompt: "Buatkan authentication system dengan login,
        register, forgot password, dan email verification"

Output: Multiple files, API routes, database schema,
        email templates, UI components
```

💬 **Contoh Prompt (Well-structured):**

```vbnet
TASK: Create utility function for currency formatting

SPECIFICATIONS:
- Input: number (amount in cents/smallest unit)
- Output: formatted string
- Currency: Indonesian Rupiah (IDR)
- Format: "Rp 1.000.000" (dot as thousand separator)

REQUIREMENTS:
- Handle negative numbers (show with minus sign)
- Handle zero
- Handle undefined/null (return "Rp 0")
- TypeScript dengan proper types

EXAMPLE:
formatCurrency(1500000) → "Rp 1.500.000"
formatCurrency(-50000) → "-Rp 50.000"
formatCurrency(0) → "Rp 0"
```

⚡ **Tips & Tricks:**

- Start simple, build complexity incrementally
- Always specify tech stack dan language
- Include edge cases yang harus di-handle
- Request comments untuk complex logic
- Ask untuk multiple approaches kalau uncertain

⚠️ **Common Mistakes:**

- Prompt terlalu vague: "buatkan website" → Too broad
- Terlalu complex dalam satu prompt → Overwhelming
- Gak specify tech/language → AI guessing
- Gak review generated code → Bugs dan issues missed
- No examples untuk expected behavior → Ambiguous

* * *

### 4\. Natural Language Programming

📖 **Definisi:** Paradigma programming di mana developer menggunakan bahasa manusia (bukan programming language) untuk menginstruksikan komputer atau AI apa yang harus dilakukan. AI berperan sebagai "translator" yang mengubah natural language menjadi actual executable code. Ini memungkinkan orang dengan berbagai level technical skill untuk create software.

💡 **Analogi:** Bayangkan punya **translator yang fasih semua bahasa programming**. Kamu bisa bicara dalam Bahasa Indonesia: "Filter produk yang harganya di bawah 100 ribu dan masih ada stoknya." Translator akan convert itu ke Python, JavaScript, SQL, atau bahasa apapun yang dibutuhkan — dengan syntax yang benar.

🔧 **Contoh Praktis:**

```php
TRADITIONAL WAY:
────────────────
Kamu harus tau:
- Syntax .filter()
- Arrow function syntax
- Comparison operators
- Logical AND operator
- Object property access

Dan menulis:
const affordableInStock = products.filter(product =>
  product.price < 100000 &&
  product.stock > 0 &&
  product.isActive === true
);

NATURAL LANGUAGE WAY:
─────────────────────
Kamu describe:
"Filter products di mana:
- Harga di bawah 100.000
- Stock lebih dari 0
- Status active

Return sebagai array baru."

AI generates the code above.

ANOTHER EXAMPLE:

Natural: "Sort users by tanggal registrasi, yang terbaru duluan,
         tapi yang sudah verified tampil paling atas"

AI translates to:
const sortedUsers = users.sort((a, b) => {
  // Verified users first
  if (a.isVerified && !b.isVerified) return -1;
  if (!a.isVerified && b.isVerified) return 1;
  // Then by registration date (newest first)
  return new Date(b.registeredAt) - new Date(a.registeredAt);
});
```

💬 **Contoh Prompt:**

```css
Saya punya data structure seperti ini:

interface Order {
  id: string;
  customerId: string;
  items: OrderItem[];
  status: 'pending' | 'processing' | 'shipped' | 'delivered';
  createdAt: Date;
  total: number;
}

Saya butuh function yang:
1. Ambil semua orders dari customer tertentu
2. Filter hanya yang status 'delivered'
3. Hitung total spending (sum of all totals)
4. Return object dengan: orderCount, totalSpending, averageOrder

Bahasa: TypeScript dengan proper types
```

⚡ **Tips & Tricks:**

- Describe WHAT you want, bukan HOW to implement
- Be specific tentang input dan expected output
- Include example data kalau structure complex
- Specify edge cases dan error handling
- Iterate untuk refinement

⚠️ **Common Mistakes:**

- Mixing natural language dengan code syntax → Confusing
- Assume AI tau context yang gak di-mention → Missing info
- Gak clear tentang expected output format → Ambiguous
- Over-reliance tanpa understanding → Gak bisa debug
- Skip verification → Bugs in production

* * *

### 5\. AI Pair Programming

📖 **Definisi:** Collaborative coding practice di mana developer bekerja bersama AI sebagai "pair" — satu pihak think, plan, dan direct (human), satu pihak execute, suggest, dan assist (AI). Ini adalah adaptasi dari traditional pair programming (dua developer) ke format human-AI collaboration, dengan AI sebagai partner yang knowledgeable dan tireless.

💡 **Analogi:** Traditional pair programming: **Driver** (yang ketik) + **Navigator** (yang guide). Dalam AI pair programming, kamu sebagai Navigator yang menentukan direction dan membuat decisions, AI sebagai Driver yang sangat cepat mengetik, punya knowledge luas, dan gak pernah capek. Bedanya dengan regular driver: AI bisa juga suggest routes yang mungkin kamu gak consider.

🔧 **Contoh Praktis:**

```markdown
AI PAIR PROGRAMMING SESSION:

YOU: "Kita mulai build user authentication untuk app ini"

AI: "Baik! Untuk authentication, saya suggest struktur:
    1. Login page dengan email/password
    2. Register page dengan validation
    3. Auth context untuk state management
    4. Protected route wrapper
    5. API routes untuk auth endpoints

    Mau mulai dari mana? Atau ada approach lain yang kamu prefer?"

YOU: "Sounds good. Mulai dari auth context dulu."

AI: [Generate AuthContext dengan provider, hooks, types]

YOU: "Bagus. Tapi saya mau add 'remember me' functionality.
     Gimana best practice-nya?"

AI: "Untuk 'remember me', ada beberapa approaches:
    1. Longer session expiry (simple tapi less secure)
    2. Refresh token dengan extended validity
    3. Persistent session di localStorage (perlu careful)

    Untuk app ini, saya recommend option 2. Mau saya implement?"

YOU: "Yes, go with refresh token approach."

AI: [Update code dengan refresh token logic]

YOU: "Hmm, ada security consideration lain yang perlu dipikirkan?"

AI: "Good question! Beberapa hal yang perlu di-address:
    - CSRF protection untuk form submissions
    - Rate limiting untuk prevent brute force
    - Secure httpOnly cookies untuk tokens
    - Input sanitization untuk prevent XSS

    Mau saya add CSRF protection dulu?"

YOU: "Yes, let's do that."

[Session continues...]
```

💬 **Contoh Prompt (Starting a pair session):**

```diff
Kita akan pair programming untuk build REST API.

PROJECT CONTEXT:
- Tech: Node.js, Express, PostgreSQL, Prisma
- Purpose: E-commerce backend
- Current state: Fresh project, nothing built yet

HOW WE'LL WORK:
- Saya akan describe requirements dan make decisions
- Kamu implement dan suggest improvements
- Setelah setiap step, highlight kalau ada concerns atau
  better alternatives yang perlu saya pertimbangkan
- Ask clarifying questions kalau something ambiguous

Let's start dengan project setup dan folder structure.
What do you suggest?
```

⚡ **Tips & Tricks:**

- Treat AI sebagai pair yang knowledgeable, bukan just executor
- Ask untuk suggestions dan alternatives, bukan cuma instructions
- Review setiap step sebelum lanjut ke next
- Let AI challenge your decisions — sometimes AI punya better ideas
- Maintain dialogue, bukan monologue

⚠️ **Common Mistakes:**

- One-way communication (cuma kasih perintah) → Miss AI insights
- Gak minta feedback/suggestions dari AI → Suboptimal solutions
- Skip review process → Compounding issues
- Gak leverage AI's knowledge untuk improvement → Underutilized
- Treat AI sebagai tool, bukan partner → Less effective collaboration

* * *

### 6\. Prompt-to-Code

📖 **Definisi:** Pipeline atau flow di mana text prompt ditransformasi menjadi working code. Ini mencakup seluruh proses dari input natural language instruction hingga output executable code yang bisa langsung dijalankan. Prompt-to-code adalah core mechanism di balik vibe coding — kemampuan untuk convert ideas ke implementation melalui language.

💡 **Analogi:** Seperti **vending machine canggih**. Kamu masukkan "request" (prompt), mesin process di dalam, keluar "produk" (code). Tapi berbeda dengan vending machine biasa yang fixed, kamu bisa fine-tune request dan iterate sampai produk yang keluar exactly sesuai keinginan.

🔧 **Contoh Praktis:**

```php
PROMPT-TO-CODE PIPELINE:

INPUT (Prompt):
┌─────────────────────────────────────────────────────┐
│ "Buatkan React component untuk star rating          │
│  dengan 5 stars, clickable untuk set rating,        │
│  dan display current rating as number"              │
└─────────────────────────────────────────────────────┘
                         │
                         ▼
PROCESSING (AI):
┌─────────────────────────────────────────────────────┐
│ 1. Parse requirements:                              │
│    - React component                                │
│    - Star rating (5 stars)                          │
│    - Clickable/interactive                          │
│    - Display numeric rating                         │
│                                                     │
│ 2. Identify patterns:                               │
│    - Need useState for rating                       │
│    - Need onClick handlers                          │
│    - Need star icons (filled/empty)                 │
│                                                     │
│ 3. Generate structure:                              │
│    - Component function                             │
│    - Props interface                                │
│    - State management                               │
│    - Render logic                                   │
│                                                     │
│ 4. Apply styling:                                   │
│    - Star styling (color, size)                     │
│    - Hover effects                                  │
│    - Layout                                         │
└─────────────────────────────────────────────────────┘
                         │
                         ▼
OUTPUT (Code):
┌─────────────────────────────────────────────────────┐
│ interface StarRatingProps {                         │
│   initialRating?: number;                           │
│   onChange?: (rating: number) => void;              │
│ }                                                   │
│                                                     │
│ export function StarRating({                        │
│   initialRating = 0,                                │
│   onChange                                          │
│ }: StarRatingProps) {                               │
│   const [rating, setRating] = useState(initialRating)│
│   const [hover, setHover] = useState(0);            │
│                                                     │
│   const handleClick = (value: number) => {          │
│     setRating(value);                               │
│     onChange?.(value);                              │
│   };                                                │
│                                                     │
│   return (                                          │
│     <div className="flex items-center gap-1">       │
│       {[1, 2, 3, 4, 5].map((star) => (              │
│         <button                                     │
│           key={star}                                │
│           onClick={() => handleClick(star)}         │
│           onMouseEnter={() => setHover(star)}       │
│           onMouseLeave={() => setHover(0)}          │
│           className="text-2xl"                      │
│         >                                           │
│           {star <= (hover || rating) ? '★' : '☆'}   │
│         </button>                                   │
│       ))}                                           │
│       <span className="ml-2">{rating}/5</span>      │
│     </div>                                          │
│   );                                                │
│ }                                                   │
└─────────────────────────────────────────────────────┘
```

💬 **Contoh Prompt (Structured for better output):**

```vbnet
PROMPT-TO-CODE REQUEST

COMPONENT: Password Strength Indicator
FRAMEWORK: React with TypeScript
STYLING: Tailwind CSS

REQUIREMENTS:
- Input: password string
- Output: visual indicator (bar) + text label
- Strength levels: Weak (red), Medium (yellow), Strong (green)

STRENGTH CRITERIA:
- Weak: < 8 chars
- Medium: 8+ chars, has number OR special char
- Strong: 8+ chars, has number AND special char AND uppercase

VISUAL:
- Progress bar that fills based on strength
- Color changes with strength
- Text label showing "Weak", "Medium", or "Strong"

OUTPUT FORMAT:
- Single file component
- Include TypeScript types
- Include Tailwind classes
- No external dependencies
```

⚡ **Tips & Tricks:**

- Structure prompt seperti spec document untuk complex features
- Include ALL requirements upfront — surprises later = rework
- Specify output format yang diinginkan
- Iterate untuk refinement — first output rarely perfect
- Test generated code sebelum move on

⚠️ **Common Mistakes:**

- Expect prompt-to-code solve everything in one shot → Need iteration
- One prompt untuk entire application → Too ambitious
- No iteration, no refinement → Suboptimal output
- Gak test generated code → Runtime surprises
- Vague requirements → Vague output

* * *

### 7\. Context Window (Vibe Coding Context)

📖 **Definisi:** Dalam vibe coding, context window adalah "memory" atau batasan seberapa banyak information (code, conversation history, files) yang bisa AI "lihat" dan pertimbangkan saat generate response. Semua yang ada dalam context window akan influence AI's output. Yang di luar context window = AI gak tau exists.

💡 **Analogi:** Seperti **meja kerja dengan ukuran terbatas**. Semakin besar meja, semakin banyak dokumen, referensi, dan notes yang bisa kamu taro untuk dikerjakan bersamaan. Context window = ukuran meja AI. Meja kecil: cuma bisa lihat 1-2 files. Meja besar: bisa lihat puluhan files + conversation history panjang.

🔧 **Contoh Praktis:**

```yaml
CONTEXT WINDOW COMPARISON:

SMALL CONTEXT (8K-16K tokens):
──────────────────────────────
├── Bisa lihat ~1-3 file kecil
├── Conversation history terbatas
├── AI sering "lupa" yang dibahas sebelumnya
├── Perlu repeat information
├── Good for: Simple, isolated tasks
└── Example: GPT-3.5 (16K)

MEDIUM CONTEXT (32K-64K tokens):
────────────────────────────────
├── Bisa lihat ~5-10 files
├── Moderate conversation memory
├── Bisa maintain context across steps
├── Occasional "forgetting"
├── Good for: Most development tasks
└── Example: GPT-4 (32K)

LARGE CONTEXT (128K-200K tokens):
─────────────────────────────────
├── Bisa lihat 20+ files sekaligus
├── Remember entire long conversation
├── Understand project-wide patterns
├── Consistent suggestions
├── Good for: Large projects, complex refactoring
└── Example: Claude 3.5 (200K), GPT-4o (128K)

TOKEN ESTIMATION:
├── 1 token ≈ 4 characters (English)
├── 1 line of code ≈ 10-15 tokens
├── 1 typical file ≈ 500-2000 tokens
├── 128K tokens ≈ 300 pages text
└── 200K tokens ≈ 500 pages text
```

💬 **Contoh Prompt (Leveraging context):**

```less
@src/components/ui/Button.tsx
@src/components/ui/Card.tsx
@src/components/ui/Input.tsx
@src/styles/theme.ts

Saya mau kamu lihat pattern dan style dari components di atas.

Perhatikan:
- Naming conventions
- Props patterns
- TypeScript usage
- Tailwind patterns
- Theme colors dari theme.ts

Sekarang buatkan Modal component yang:
- Follow EXACT same patterns
- Use same styling approach
- Consistent dengan existing design system

Include: overlay, content, close button, title, children
```

⚡ **Tips & Tricks:**

- Provide relevant files sebagai context dengan @mentions
- Clear conversation kalau start topic yang completely baru
- Summarize panjang conversation kalau needed untuk maintain context
- Use context features di tools (Cursor @file, @folder, @codebase)
- Prioritize most relevant context — quality over quantity

⚠️ **Common Mistakes:**

- Assume AI "ingat" everything dari conversation lalu → Context has limits
- Include too much irrelevant context → Dilutes attention
- Not refreshing context untuk new topic → Old context confuses
- Gak leverage context features di tools → Missing capabilities
- Ignore context window limits → Unexpected behavior when exceeded

* * *

### 8\. Token (Vibe Coding Context)

📖 **Definisi:** Token adalah unit pengukuran untuk text yang diproses AI. Dalam vibe coding, token menentukan: (1) berapa banyak code/text yang bisa di-process dalam satu request, (2) berapa banyak yang bisa di-generate sebagai response, dan (3) berapa biaya API usage. Rata-rata 1 token ≈ 4 karakter atau ≈ 0.75 kata dalam English. Bahasa Indonesia typically membutuhkan lebih banyak tokens.

💡 **Analogi:** Token seperti **kredit di arcade game**. Setiap action yang kamu mau lakukan butuh sejumlah kredit. Prompt yang panjang = lebih banyak kredit. Response yang panjang = lebih banyak kredit. Generate code yang complex = banyak kredit. Kamu perlu manage tokens seperti manage budget — use efficiently untuk maximize value.

🔧 **Contoh Praktis:**

```yaml
TOKEN USAGE EXAMPLES:

SIMPLE PROMPT:
─────────────
Prompt: "Create hello world function in JavaScript"
├── Input tokens: ~8
├── Output tokens: ~30
├── Total: ~38 tokens
└── Cost: $0.0001 (negligible)

MEDIUM PROMPT:
──────────────
Prompt: "Create registration form with email, password,
        confirm password, phone, and validation"
├── Input tokens: ~40
├── Output tokens: ~400
├── Total: ~440 tokens
└── Cost: ~$0.001

COMPLEX PROMPT WITH CONTEXT:
────────────────────────────
Prompt: 3 files included as context + detailed requirements
        untuk multi-file feature implementation
├── Input tokens: ~3,000
├── Output tokens: ~2,000
├── Total: ~5,000 tokens
└── Cost: ~$0.02

PRICING REFERENCE (approximate):
────────────────────────────────
Model           │ Input (per 1M) │ Output (per 1M)
────────────────┼────────────────┼────────────────
GPT-4o          │ $2.50          │ $10.00
GPT-4o-mini     │ $0.15          │ $0.60
Claude Sonnet   │ $3.00          │ $15.00
Claude Haiku    │ $0.25          │ $1.25

ESTIMATION:
├── Typical coding session: 10K-50K tokens
├── Cost per session: $0.05-$0.50
├── Monthly heavy usage: $10-50
└── Much cheaper than you'd think!
```

💬 **Contoh Prompt (Token-efficient):**

```python
❌ INEFFICIENT (banyak filler words):
"""
Halo, saya ingin meminta bantuan kamu untuk membuat sebuah
function dalam bahasa pemrograman JavaScript yang memiliki
kemampuan untuk memvalidasi apakah sebuah alamat email yang
diinputkan oleh user sudah memiliki format yang benar dan
sesuai dengan standar format email pada umumnya. Tolong
buatkan function tersebut dengan lengkap ya. Terima kasih
banyak atas bantuannya.
"""
→ ~75 tokens input untuk simple request

✅ EFFICIENT (concise, same information):
"""
JS function: validate email format
- Input: string
- Output: boolean
- Handle common edge cases
"""
→ ~20 tokens input untuk same request

SAVINGS: 55 tokens × 1000 requests = 55K tokens saved
         At $2.50/1M = $0.14 saved per 1000 requests
```

⚡ **Tips & Tricks:**

- Concise prompts save tokens tanpa sacrifice clarity
- Reuse context dari previous messages, jangan repeat
- Chunk large tasks untuk control token usage per request
- Monitor usage di billing dashboard (OpenAI, Anthropic)
- Use cheaper models untuk simple tasks (GPT-4o-mini, Haiku)

⚠️ **Common Mistakes:**

- Verbose prompts unnecessarily → Wasting tokens
- Repeat same context terus-terus → Inefficient
- Generate then regenerate full code repeatedly → Expensive
- Gak monitor token usage → Surprise bills
- Always use most expensive model → Overkill for simple tasks

## Kategori 2: Prompting & Communication

Ini adalah istilah-istilah tentang **bagaimana berkomunikasi dengan AI** untuk mendapatkan hasil terbaik. Prompting adalah skill yang bisa dipelajari — dan kategori ini akan membantu kamu master vocabulary-nya.

* * *

### 9\. Prompt Engineering

📖 **Definisi:** Prompt engineering adalah skill dan practice dalam merancang prompts yang effective untuk mendapatkan hasil optimal dari AI. Dalam vibe coding, ini berarti menulis instruksi yang menghasilkan code berkualitas tinggi, sesuai requirements, dan consistent. Prompt engineering adalah core skill yang membedakan beginner dari advanced vibe coder.

💡 **Analogi:** Seperti belajar **"bahasa" untuk komunikasi dengan orang dari budaya berbeda**. Ada cara tertentu untuk menyampaikan maksud agar dipahami dengan tepat. "Tolong ambilkan itu" bisa bermakna banyak hal. "Tolong ambilkan buku merah di rak kedua dari kiri" akan dipahami dengan jelas. Prompt engineering adalah skill untuk communicate dengan clarity ke AI.

🔧 **Contoh Praktis:**

```sql
PROMPT ENGINEERING TECHNIQUES:

1. BE SPECIFIC
───────────────
❌ Bad: "Buatkan form"
✅ Good: "Buatkan login form dengan email dan password fields,
         client-side validation, loading state, dan error handling"

2. PROVIDE CONTEXT
──────────────────
❌ Bad: "Add dark mode"
✅ Good: "Add dark mode toggle ke existing navbar.
         Tech stack: Next.js 14, Tailwind CSS.
         Use next-themes library untuk theme management.
         Persist preference ke localStorage."

3. SPECIFY OUTPUT FORMAT
────────────────────────
❌ Bad: "Explain this code"
✅ Good: "Explain this code dengan format:
         1. What it does (1 sentence)
         2. Line-by-line breakdown
         3. Potential improvements
         4. Edge cases to consider"

4. USE ROLE/PERSONA
───────────────────
"Act as a senior React developer reviewing code dari junior.
 Be constructive tapi thorough. Point out issues AND suggest fixes."

5. INCLUDE EXAMPLES
───────────────────
"Format response seperti ini:
 { success: true, data: {...} } untuk success
 { success: false, error: 'message' } untuk failure"

6. SET CONSTRAINTS
──────────────────
"Maximum 50 lines of code"
"Don't use any external libraries"
"Must be compatible dengan Node 18+"
```

💬 **Contoh Prompt (Well-engineered):**

```markdown
TASK: Create API endpoint for user registration

ROLE: You are a senior backend developer focused on security.

CONTEXT:
- Framework: Express.js with TypeScript
- Database: PostgreSQL with Prisma ORM
- Auth strategy: JWT tokens
- Validation: Zod schema

REQUIREMENTS:
- POST /api/auth/register
- Required fields: email, password, name
- Validation:
  - Email: valid format, unique in database
  - Password: min 8 chars, 1 uppercase, 1 number
  - Name: 2-50 characters
- Password hashing: bcrypt with cost factor 12
- Response: user object (without password) + JWT token
- Error handling: proper HTTP codes and messages

OUTPUT FORMAT:
1. Type definitions
2. Zod validation schema
3. Controller function
4. Route registration

ADDITIONAL:
- Include JSDoc comments
- Follow RESTful conventions
- Handle duplicate email gracefully (409 Conflict)
```

⚡ **Tips & Tricks:**

- Build personal prompt library untuk common tasks
- Template structure membantu consistency
- Iterate dan refine berdasarkan results
- Learn dari bad outputs — why did it fail?
- Different tasks need different prompt styles

⚠️ **Common Mistakes:**

- Assume AI knows what you want → Be explicit
- No structure in prompts → Hard to parse for AI
- One-size-fits-all prompts → Different tasks need different approaches
- Not learning dari failed prompts → Same mistakes repeated
- Overthinking simple requests → Sometimes brief is better

* * *

### 10\. System Prompt

📖 **Definisi:** System prompt adalah instruksi permanen yang mengatur behavior, personality, knowledge boundaries, dan rules AI sepanjang conversation. Berbeda dengan regular prompts yang per-request, system prompt set the "operating mode" untuk keseluruhan session. Dalam vibe coding, system prompt define how AI should approach coding tasks untuk project tertentu.

💡 **Analogi:** Seperti **employee handbook dan job description untuk karyawan baru**. Sebelum mulai kerja, kamu jelaskan: "Ini role kamu, ini standard kita, ini tools yang kita pakai, ini yang boleh dan tidak boleh, ini cara kita communicate." Setelah itu, setiap task yang diberikan akan dikerjakan sesuai dengan guidelines tersebut.

🔧 **Contoh Praktis:**

```markdown
SYSTEM PROMPT UNTUK VIBE CODING PROJECT:

"""
You are an expert full-stack developer helping me build
a portfolio website. You have 10+ years of experience
with React ecosystem.

═══════════════════════════════════════════════════════
TECH STACK (always use these):
═══════════════════════════════════════════════════════
- Next.js 14 with App Router
- TypeScript in strict mode
- Tailwind CSS for styling
- Prisma ORM for database
- Zod for validation

═══════════════════════════════════════════════════════
CODING STANDARDS:
═══════════════════════════════════════════════════════
- Functional components with hooks only
- Named exports for all components
- Descriptive variable names (no single letters except loops)
- Comments for complex logic
- Error boundaries for critical components

═══════════════════════════════════════════════════════
STYLE PREFERENCES:
═══════════════════════════════════════════════════════
- Concise responses - code first, explanation if needed
- Mobile-first responsive design
- Accessibility: semantic HTML, ARIA when needed
- Performance: lazy loading, optimized images

═══════════════════════════════════════════════════════
CONSTRAINTS (never do these):
═══════════════════════════════════════════════════════
- No class components
- No inline styles (use Tailwind)
- No 'any' type in TypeScript
- No console.log in final code
- Always handle loading and error states

═══════════════════════════════════════════════════════
BEHAVIOR:
═══════════════════════════════════════════════════════
When I give you a task:
1. Generate code following these standards
2. If something is ambiguous, ask ONE clarifying question
3. If you see potential issues, mention them after the code
4. Suggest improvements only if significant
"""
```

💬 **Contoh Prompt (Setting system context di awal session):**

```diff
Untuk session ini, kamu adalah senior TypeScript developer.

PROJECT: E-commerce admin dashboard
TECH: React 18, TypeScript, TanStack Query, Tailwind
TESTING: Vitest, Testing Library

STYLE GUIDE:
- Prefer composition over inheritance
- Small, focused functions
- Explicit return types
- Named exports

RESPONSE STYLE:
- Code first, minimal explanation
- Only explain if I ask or if there's a gotcha
- Use comments in code for clarity
- Suggest alternatives only if significantly better

Confirm you understand, then let's start.
```

⚡ **Tips & Tricks:**

- Set system prompt di awal setiap project
- Save system prompts untuk reuse across similar projects
- Update system prompt kalau project needs evolve
- Include tech stack ALWAYS — prevents wrong assumptions
- Be specific about response style preferences

⚠️ **Common Mistakes:**

- Skip system prompt, langsung task → Inconsistent outputs
- Too generic system prompt → Doesn't help much
- Not updating untuk different projects → Wrong context
- Conflicting instructions → Confuses AI
- Over-complicated system prompt → Diminishing returns

* * *

### 11\. Instruction Prompt

📖 **Definisi:** Instruction prompt adalah prompt spesifik yang memberikan task atau perintah tertentu kepada AI. Berbeda dengan system prompt yang persistent dan set context, instruction prompt adalah per-request command untuk accomplish specific task. Instruction prompt bekerja di dalam framework yang sudah di-set oleh system prompt.

💡 **Analogi:** Kalau system prompt adalah **job description** (define role dan expectations), instruction prompt adalah **task assignment harian** (define specific work untuk dikerjakan sekarang). "Hari ini, kerjakan laporan Q3" adalah instruction. "Kamu adalah financial analyst, selalu double-check numbers" adalah system.

🔧 **Contoh Praktis:**

```sql
RELATIONSHIP BETWEEN SYSTEM & INSTRUCTION:

SYSTEM PROMPT (set once):
"Kamu adalah React developer. Tech: Next.js, TypeScript, Tailwind.
 Always use functional components dan proper TypeScript types."

INSTRUCTION PROMPTS (per task):
├── "Buatkan Button component dengan variants: primary, secondary, ghost"
├── "Refactor this function untuk better error handling"
├── "Add pagination ke existing ProductList component"
├── "Debug kenapa form tidak submit — here's the code: [...]"
└── "Write unit tests untuk utils/formatCurrency.ts"

Each instruction operates within system context.

INSTRUCTION PROMPT ANATOMY:

┌─────────────────────────────────────────┐
│           INSTRUCTION PROMPT            │
├─────────────────────────────────────────┤
│ TASK: What to do                        │
│ INPUT: What you're providing            │
│ OUTPUT: What you expect back            │
│ CONSTRAINTS: Limitations or requirements│
│ FORMAT: How to structure response       │
└─────────────────────────────────────────┘
```

💬 **Contoh Prompt (Well-structured instruction):**

```diff
INSTRUCTION: Create custom hook for form handling

INPUT:
- Initial values object
- Validation schema (Zod)
- onSubmit callback

OUTPUT:
- values state
- errors state
- touched state
- handleChange function
- handleBlur function
- handleSubmit function
- isSubmitting state
- reset function

CONSTRAINTS:
- TypeScript with generics for type safety
- No external form libraries
- Support async validation
- Handle nested objects

FORMAT:
- Single file dengan hook dan types
- Include usage example in comments
```

⚡ **Tips & Tricks:**

- One clear instruction per prompt (don't bundle unrelated tasks)
- Include input/output specs untuk clarity
- Reference similar patterns kalau ada
- Be explicit about expected behavior
- Keep instruction focused — big tasks should be broken down

⚠️ **Common Mistakes:**

- Multiple unrelated instructions in one prompt → Confusion
- Vague instructions → Vague results
- Missing context from system prompt → Repeat yourself
- Contradicting system prompt → Conflicting behavior
- Too many details for simple task → Over-engineering

* * *

### 12\. Few-shot Prompting

📖 **Definisi:** Few-shot prompting adalah teknik prompting di mana kamu memberikan beberapa contoh (typically 2-5) sebelum actual task untuk "mengajarkan" pattern, format, atau style yang diinginkan ke AI. AI learns dari examples dan applies pattern tersebut ke task baru. Ini sangat effective untuk tasks yang membutuhkan consistent formatting atau specific style.

💡 **Analogi:** Seperti **training karyawan baru dengan menunjukkan contoh pekerjaan**. "Lihat ini bagaimana kita format report-nya, ini satu lagi, dan ini yang ketiga. Sekarang, coba kamu buatkan yang serupa untuk data ini." Dengan melihat examples, karyawan (AI) understands the pattern dan bisa replicate.

🔧 **Contoh Praktis:**

```python
FEW-SHOT UNTUK CONSISTENT CODE STYLE:

"""
Saya mau semua API routes di project ini follow pattern yang sama.
Berikut examples yang sudah ada:

EXAMPLE 1:
// GET /api/users
export async function GET(request: Request) {
  try {
    const users = await prisma.user.findMany();
    return Response.json({ success: true, data: users });
  } catch (error) {
    return Response.json(
      { success: false, error: 'Failed to fetch users' },
      { status: 500 }
    );
  }
}

EXAMPLE 2:
// GET /api/products/:id
export async function GET(
  request: Request,
  { params }: { params: { id: string } }
) {
  try {
    const product = await prisma.product.findUnique({
      where: { id: params.id }
    });

    if (!product) {
      return Response.json(
        { success: false, error: 'Product not found' },
        { status: 404 }
      );
    }

    return Response.json({ success: true, data: product });
  } catch (error) {
    return Response.json(
      { success: false, error: 'Failed to fetch product' },
      { status: 500 }
    );
  }
}

NOW CREATE: GET /api/orders route yang fetch orders untuk specific user.
Follow EXACT same patterns dari examples di atas.
"""
```

💬 **Contoh Prompt (Few-shot untuk formatting):**

```yaml
Convert informal Indonesian ke formal Indonesian.

EXAMPLE 1:
Informal: "Gw gak bisa dateng besok, sorry bgt ya"
Formal: "Mohon maaf, saya tidak dapat hadir besok."

EXAMPLE 2:
Informal: "Bisa tolong kirimin file-nya? Butuh ASAP nih"
Formal: "Mohon kesediaannya untuk mengirimkan berkas tersebut.
        Kami membutuhkannya segera."

EXAMPLE 3:
Informal: "Makasih banyak udah bantu, lo emang the best!"
Formal: "Terima kasih banyak atas bantuannya. Sangat kami apresiasi."

NOW CONVERT:
"Eh project-nya udah kelar belom? Klien nanya mulu nih, pusing gw"
```

⚡ **Tips & Tricks:**

- 2-3 examples biasanya cukup (more isn't always better)
- Make examples clear, consistent, dan representative
- Examples should cover different variations/edge cases
- Place examples BEFORE actual task
- Examples quality > examples quantity

⚠️ **Common Mistakes:**

- Inconsistent examples → AI gets confused about pattern
- Too many examples → Takes up context window, diminishing returns
- Examples don't match task complexity → Wrong expectations
- Skipping few-shot when consistency matters → Inconsistent outputs
- Low-quality examples → AI learns bad patterns

* * *

### 13\. Chain-of-thought (CoT) Prompting

📖 **Definisi:** Chain-of-thought prompting adalah teknik yang meminta AI untuk menjelaskan reasoning step-by-step sebelum memberikan final answer atau output. Dalam vibe coding, CoT membantu untuk complex logic problems, debugging mysteries, architectural decisions, dan situations di mana understanding the "why" is important alongside the "what".

💡 **Analogi:** Seperti meminta siswa **menunjukkan "cara penyelesaian"** di ujian matematika, bukan hanya jawaban akhir. "Tunjukkan step-by-step bagaimana kamu sampai ke jawaban ini." Step-by-step reasoning membuat thinking visible dan often leads to better, more verifiable answers.

🔧 **Contoh Praktis:**

```markdown
WITHOUT CHAIN-OF-THOUGHT:
─────────────────────────
You: "Should I use Redux or Context for this app?"
AI: "Use Redux."

Problem: No reasoning, can't evaluate if advice is right.

WITH CHAIN-OF-THOUGHT:
──────────────────────
You: "Should I use Redux or Context for this app? Think through
     the considerations step by step before recommending."

AI: "Let me analyze this step by step:

     1. APP COMPLEXITY
        - You mentioned 5 pages, ~10 components
        - This is relatively small/medium sized
        → Doesn't require complex state management

     2. STATE REQUIREMENTS
        - User authentication state (global)
        - Shopping cart (shared across pages)
        - UI state (mostly local)
        → Mix of global and local, nothing deeply nested

     3. UPDATE PATTERNS
        - Cart updates on user actions
        - Auth changes on login/logout
        → Infrequent updates, no complex async flows

     4. TEAM FAMILIARITY
        - You mentioned team is new to React
        → Simpler solution = faster onboarding

     5. BUNDLE SIZE CONSIDERATION
        - Redux + toolkit adds ~15KB
        - Context is built-in
        → Context has no additional cost

     CONCLUSION: For this use case, Context API is sufficient.
     Use Context for auth and cart. Local state for UI.
     Consider Redux only if state logic becomes complex later."

Now you can: Verify reasoning, push back on specific points,
             make informed decision.
```

💬 **Contoh Prompt (CoT untuk debugging):**

````cpp
Bug: useEffect runs infinitely, causing performance issues.

Code:
```jsx
useEffect(() => {
const filtered = items.filter(item => item.active);
setActiveItems(filtered);
}, [items, activeItems]);
````

Before suggesting a fix, think through step by step:

1. What triggers useEffect to run?
2. What happens inside useEffect?
3. How could this create infinite loop?
4. What's the root cause?
5. What are possible fixes?
6. What's the best fix and why?

Show your reasoning, then provide the fix.

```java

💬 **Contoh Prompt (CoT untuk architecture):**
```

I need to design the database schema for a booking system.

Before generating SQL, analyze step by step:

1. ENTITIES: What are the main entities needed?
2. RELATIONSHIPS: How do they relate? (1:1, 1:many, many:many)
3. ATTRIBUTES: What attributes does each entity need?
4. CONSTRAINTS: What business rules translate to constraints?
5. EDGE CASES: What scenarios might complicate the design?
6. INDEXES: What queries will be common? What needs indexing?

Show your reasoning for each step, then generate the schema.

Requirements:

- Users can book services
- Services have different durations and prices
- Bookings have time slots
- Need to prevent double-booking

```markdown

⚡ **Tips & Tricks:**
- Use untuk complex problems, bukan simple tasks
- "Think step by step" adalah magic phrase yang works
- Read dan verify the reasoning, bukan cuma final answer
- Great untuk learning — understanding WHY is valuable
- Helps catch AI mistakes earlier in the chain

⚠️ **Common Mistakes:**
- Using CoT untuk very simple tasks → Overkill, wastes tokens
- Not reading the reasoning → Miss insights dan errors
- Accepting solution tanpa verify logic → Trusting blindly
- Skipping CoT untuk complex tasks → Suboptimal solutions
- Interrupting CoT early → Incomplete reasoning

---

### 14. Iterative Prompting

📖 **Definisi:**
Iterative prompting adalah pendekatan di mana kamu build output secara incremental melalui multiple rounds of prompts. Setiap round refine, extend, atau improve pada previous output. Instead of trying to get perfect result in one shot, kamu iterate menuju desired outcome step by step.

💡 **Analogi:**
Seperti **sculptor yang membentuk patung secara bertahap**. Mulai dari rough shape, kemudian refine outlines, add details, polish surface. Kamu tidak carve perfect statue dalam satu cut. Iterative prompting follows same principle — build, review, refine, repeat.

🔧 **Contoh Praktis:**
```

ITERATIVE PROMPTING WORKFLOW:

INSTEAD OF (One-shot): ┌────────────────────────────────────────────────────────────┐ │ "Create complete e-commerce checkout page with cart │ │ summary, shipping form, payment form, order review, │ │ promo code input, order total calculation, all with │ │ validation, error handling, loading states, and..." │ └────────────────────────────────────────────────────────────┘ │ ▼ 😵 Overwhelming, incomplete, hard to fix

DO THIS (Iterative): ┌───────────────┐ ┌───────────────┐ ┌───────────────┐ │ ITERATION 1 │ → │ ITERATION 2 │ → │ ITERATION 3 │ │ │ │ │ │ │ │ Cart summary │ │ Add shipping │ │ Add payment │ │ component │ │ form │ │ form │ │ │ │ │ │ │ │ ✓ Review │ │ ✓ Review │ │ ✓ Review │ │ ✓ Works │ │ ✓ Works │ │ ✓ Works │ └───────────────┘ └───────────────┘ └───────────────┘ │ │ │ ▼ ▼ ▼ ┌───────────────┐ ┌───────────────┐ ┌───────────────┐ │ ITERATION 4 │ → │ ITERATION 5 │ → │ ITERATION 6 │ │ │ │ │ │ │ │ Add promo │ │ Add validation│ │ Polish & │ │ code logic │ │ & error states│ │ final testing │ │ │ │ │ │ │ │ ✓ Review │ │ ✓ Review │ │ ✓ Complete! │ │ ✓ Works │ │ ✓ Works │ │ │ └───────────────┘ └───────────────┘ └───────────────┘

```java

💬 **Contoh Prompt (Iteration sequence):**
```

ITERATION 1/5: Basic Structure ──────────────────────────────── Buatkan DataTable component dengan:

- Props: columns, data
- Static display (no features yet)
- Basic Tailwind styling

Just the foundation — we'll add features iteratively.

* * *

\[After reviewing and confirming it works\]

ITERATION 2/5: Add Sorting ──────────────────────────── DataTable dasar sudah bagus. Now add:

- Clickable column headers
- Sort ascending/descending toggle
- Visual indicator untuk sort direction

Keep everything else sama.

* * *

\[After reviewing and confirming it works\]

ITERATION 3/5: Add Pagination ───────────────────────────── Sorting works great. Now add:

- Rows per page selector (10, 25, 50)
- Page navigation (prev, next, page numbers)
- "Showing X-Y of Z" text

* * *

\[After reviewing and confirming it works\]

ITERATION 4/5: Add Search ───────────────────────── Pagination complete. Now add:

- Search input di header
- Filter across all columns
- Debounced search (300ms)

* * *

ITERATION 5/5: Polish ───────────────────── All features working! Final polish:

- Loading skeleton state
- Empty state when no data
- Empty state when search returns nothing
- Smooth transitions

```markdown

⚡ **Tips & Tricks:**
- Plan iterations before starting (at least rough outline)
- Verify EACH iteration works before moving on
- Keep context across iterations — reference previous work
- It's okay to go back and revise earlier iterations
- Small iterations = easier debugging

⚠️ **Common Mistakes:**
- Trying to do everything in one prompt → Overwhelming
- Not verifying each iteration → Compound errors
- Losing context between iterations → Inconsistency
- Moving on too fast → Bugs in foundation
- Too many micro-iterations → Inefficient

---

### 15. Context Injection

📖 **Definisi:**
Context injection adalah teknik menyertakan relevant code, files, documentation, atau information ke dalam prompt agar AI memiliki context yang cukup untuk memberikan response yang accurate, consistent, dan appropriate. Tanpa context injection, AI hanya bisa rely on general knowledge dan assumptions.

💡 **Analogi:**
Seperti **memberikan brief lengkap ke designer sebelum project dimulai**. Bukan cuma bilang "bikin logo", tapi kasih: brand guidelines, color palette, existing brand assets, competitor examples, target audience info, dan inspiration references. More context = better, more aligned output.

🔧 **Contoh Praktis:**
```

CONTEXT INJECTION TYPES:

1. FILE CONTEXT ─────────────── @src/types/user.ts ← User type definitions @src/lib/api.ts ← API utility functions @src/hooks/useAuth.ts ← Auth hook implementation

"Based on these files, create UserProfile component"

1. CODE SNIPPET CONTEXT ─────────────────────── "Here's how we format API responses:

```go
{ success: boolean, data?: T, error?: string }
```

Follow this pattern for the new endpoint."

1. DOCUMENTATION CONTEXT ──────────────────────── "According to Next.js 14 docs, Server Components are default. Use 'use client' directive only when needed. Create this component following that pattern."
2. STYLE CONTEXT ──────────────── "Existing components use:

- Rounded corners: rounded-lg
- Shadow: shadow-sm
- Padding: p-4 atau p-6
- Colors: slate gray scale Match these styles."

1. REQUIREMENTS CONTEXT ─────────────────────── "From the PRD:

- Users can upload max 5 images
- Each image max 5MB
- Supported formats: jpg, png, webp Implement the upload component with these constraints."

```java

💬 **Contoh Prompt (Rich context injection):**
```

PROJECT CONTEXT: ════════════════ Tech Stack: Next.js 14, TypeScript, Tailwind, Prisma, tRPC

EXISTING CODE (untuk reference patterns): ═══════════════════════════════════════

@src/server/routers/user.ts:

```php
export const userRouter = router({
getById: publicProcedure
    .input(z.object({ id: z.string() }))
    .query(async ({ input }) => {
      return prisma.user.findUnique({ where: { id: input.id } });
    }),
});
```

@src/types/product.ts:

```typescript
export interface Product {
id: string;
name: string;
price: number;
category: string;
stock: number;
createdAt: Date;
}
```

@src/components/ui/Card.tsx:

```javascript
export function Card({ children, className }: CardProps) {
return (
    <div className={cn("bg-white rounded-lg shadow-sm p-6", className)}>
      {children}
    </div>
);
}
```

TASK: ═════ Create product router di tRPC dengan:

- getAll: list all products dengan pagination
- getById: single product by id
- create: add new product (protected)
- update: update product (protected)
- delete: delete product (protected)

Follow EXACT patterns dari userRouter. Use Product type for schemas. Include proper Zod validation.

```markdown

⚡ **Tips & Tricks:**
- Use @mentions di Cursor untuk automatic file inclusion
- Include only RELEVANT context — too much dilutes attention
- Update context saat project evolves
- Create "context snapshots" untuk frequently used contexts
- Quality of context > quantity of context

⚠️ **Common Mistakes:**
- No context injection → AI makes assumptions (often wrong)
- Too much irrelevant context → Dilutes focus
- Outdated context → Wrong assumptions based on old code
- Inconsistent context across prompts → Inconsistent outputs
- Forgetting to include type definitions → Type errors
```

## Kategori 3: Tools & Environment

Kategori ini membahas **tools yang digunakan** untuk vibe coding. Knowing tools adalah essential — sama seperti carpenter perlu tau berbagai jenis tools untuk berbagai jenis pekerjaan.

* * *

### 16\. Cursor

📖 **Definisi:** Cursor adalah AI-first code editor yang dibangun di atas VS Code, terintegrasi dengan AI capabilities untuk code generation, editing, refactoring, dan assistance. Saat ini Cursor adalah tool paling populer untuk vibe coding karena seamless integration antara coding workflow dan AI assistance. Cursor menggunakan berbagai AI models termasuk GPT-4, Claude, dan proprietary models.

💡 **Analogi:** Kalau VS Code adalah **mobil manual yang powerful**, Cursor adalah **mobil dengan advanced driver assistance system (ADAS)**. Masih kamu yang menyetir dan menentukan arah, tapi ada banyak fitur yang membantu: lane keeping, adaptive cruise control, automatic braking. Kamu tetap in control, tapi driving jadi lebih effortless.

🔧 **Contoh Praktis:**

```sql
CURSOR KEY FEATURES:

1. CHAT (Cmd+L / Ctrl+L)
═══════════════════════
- Conversation dengan AI di sidebar
- Context-aware — AI bisa "lihat" codebase kamu
- Great untuk: complex questions, explanations, planning

Example usage:
"@src/components Explain the component architecture
and suggest improvements for reusability"

2. INLINE EDIT (Cmd+K / Ctrl+K)
═══════════════════════════════
- Select code → give instruction → AI edits
- Quick modifications without full chat
- Great untuk: refactoring, small changes, fixes

Example usage:
[Select a function]
"Add proper error handling with try-catch"

3. COMPOSER (Cmd+I / Ctrl+I)
════════════════════════════
- Multi-file creation dan editing
- AI understands entire project structure
- Great untuk: new features, large refactoring

Example usage:
"Create a complete authentication feature with
login page, register page, and auth context"

4. TAB COMPLETION
═════════════════
- AI-powered autocomplete as you type
- Predicts next lines of code
- Accept dengan Tab, dismiss dengan Esc

Example: You type "const handle"
AI suggests: "handleSubmit = async (data: FormData) => {"

5. @ MENTIONS
═════════════
@file      → Include specific file as context
@folder    → Include folder contents
@codebase  → Search across entire codebase
@docs      → Reference documentation
@web       → Search web for information
```

💬 **Contoh Prompt (Cursor Chat dengan @mentions):**

```less
@src/components/ui/Button.tsx
@src/components/ui/Input.tsx
@src/components/ui/Card.tsx
@src/styles/theme.ts

Saya mau buat design system yang consistent.

Analyze patterns dari components di atas:
1. What patterns are consistent?
2. What patterns are inconsistent?
3. Suggest standardized patterns untuk semua UI components

Then create a Select component following the standardized patterns.
```

💬 **Contoh Prompt (Cursor Inline/Cmd+K):**

```markdown
[Select entire component]

Refactor this component:
1. Extract magic strings ke constants
2. Memoize expensive computations
3. Add PropTypes atau TypeScript types
4. Improve accessibility
```

⚡ **Tips & Tricks:**

- **Learn keyboard shortcuts** — significantly improves workflow
- **Use @mentions extensively** — more context = better output
- **Combine features**: Chat untuk planning, Inline untuk execution
- **Setup .cursorrules** file untuk project-specific instructions
- **Enable "Cursor Tab"** untuk enhanced autocomplete
- **Use "Apply" button** untuk directly apply chat suggestions

⚠️ **Common Mistakes:**

- Only using Chat, ignoring Inline dan Composer → Missing productivity
- Not leveraging @mentions → AI lacks context
- Not customizing .cursorrules → Generic suggestions
- Ignoring Tab completions → Free productivity wasted
- Not exploring settings → Missing powerful features

* * *

### 17\. GitHub Copilot

📖 **Definisi:** GitHub Copilot adalah AI coding assistant dari GitHub (Microsoft) yang menyediakan code suggestions dan completions berbasis AI. Copilot bekerja sebagai extension di VS Code, JetBrains IDEs, dan editors lain. Copilot learns dari context dalam file dan project untuk memberikan relevant suggestions. Copilot ada dalam dua versi: Copilot (completions) dan Copilot Chat (conversational).

💡 **Analogi:** Seperti **autocomplete di smartphone, tapi untuk code dan 100x lebih powerful**. Saat kamu mulai ketik message, phone suggests next words. Copilot does the same — saat kamu mulai ketik code, Copilot suggests next lines, functions, bahkan entire implementations berdasarkan context.

🔧 **Contoh Praktis:**

```markdown
GITHUB COPILOT FEATURES:

1. INLINE SUGGESTIONS (Ghost Text)
══════════════════════════════════
- Gray text muncul saat kamu ketik
- Shows predicted code completion
- Tab to accept, Esc to dismiss

Example:
You type: // Function to calculate discount
Copilot shows (in gray):
function calculateDiscount(price: number, percentage: number): number {
return price - (price * percentage / 100);
}

2. COMMENT-DRIVEN DEVELOPMENT
═════════════════════════════
Write comment → Copilot generates implementation

// Fetch user data from API and handle errors
// Return null if user not found
[Copilot generates full function]

3. COPILOT CHAT
═══════════════
Conversational interface untuk:
- Ask questions about code
- Get explanations
- Request specific changes

Slash commands:
/explain  → Explain selected code
/fix      → Fix issues in selected code
/tests    → Generate tests for selected code
/docs     → Generate documentation

4. CONTEXT AWARENESS
════════════════════
Copilot reads:
- Current file
- Open tabs
- Recent edits
- Project structure (partially)

More context = better suggestions.
```

💬 **Contoh Prompt (Copilot Chat):**

```bash
/explain

What does this function do? Are there any edge cases
that aren't handled? Suggest improvements.
```

```php
/tests

Generate unit tests for this function using Jest.
Include tests for:
- Normal input
- Edge cases (empty array, single element)
- Invalid input types
```

```bash
/fix

This function throws "Cannot read property of undefined"
sometimes. Find and fix the issue.
```

⚡ **Tips & Tricks:**

- **Write descriptive comments first** — guides Copilot better
- **Use descriptive function names** — Copilot uses them as context
- **Tab for accept, Ctrl+\] for next suggestion** — cycle through options
- **Write first line** of function body to guide direction
- **Open related files** in tabs untuk more context
- **Use Copilot Chat** untuk complex questions, not just completions

⚠️ **Common Mistakes:**

- Accepting suggestions without reading → Bugs dan issues
- Not using Chat features → Missing capabilities
- Fighting Copilot instead of guiding → Frustrating experience
- No comments = worse suggestions → Give Copilot hints
- Expecting Copilot to understand entire codebase → Limited context

* * *

### 18\. Claude Code

📖 **Definisi:** Claude Code adalah terminal-based AI coding tool dari Anthropic yang memungkinkan interaksi dengan Claude untuk coding tasks langsung dari command line. Claude Code bisa membaca files, menulis/edit files, run commands, dan understand entire project structure. Ini adalah agentic coding tool — Claude bisa take actions, bukan hanya suggest.

💡 **Analogi:** Seperti punya **senior developer yang bisa kamu panggil dari terminal kapan saja**. Dia bisa lihat semua file kamu, edit langsung, run commands untuk test, dan explain apa yang dia lakukan. Bedanya dengan chatbot biasa: Claude Code bisa actually DO things, not just TELL you what to do.

🔧 **Contoh Praktis:**

```makefile
CLAUDE CODE CAPABILITIES:

1. READ FILES
═════════════
Claude bisa baca any file di project kamu.

> claude
You: What does the auth middleware do?
Claude: [Reads src/middleware/auth.ts]
        "This middleware validates JWT tokens..."

2. WRITE/EDIT FILES
═══════════════════
Claude bisa create dan modify files langsung.

You: Add rate limiting to the login endpoint
Claude: [Modifies src/routes/auth.ts]
        [Creates src/middleware/rateLimit.ts]
        "Done! I've added rate limiting..."

3. RUN COMMANDS
═══════════════
Claude bisa execute terminal commands.

You: Run the tests and fix any failures
Claude: [Runs: npm test]
        [Analyzes failures]
        [Fixes code]
        [Runs: npm test again]
        "All tests passing now!"

4. PROJECT UNDERSTANDING
════════════════════════
Claude understands project structure.

You: Explain how data flows in this app
Claude: [Analyzes multiple files]
        "Here's the data flow:
         1. User action triggers...
         2. API route handles...
         3. Database query...
         4. Response formatted..."
```

💬 **Contoh Prompt:**

```markdown
You: Look at my project structure and identify any
     architectural issues or code smells. Then propose
     improvements and implement them if I approve.

[Claude reads files, analyzes patterns]

Claude: "I found several issues:
        1. Duplicate validation logic in 3 places
        2. No error boundary in React app
        3. API routes missing consistent error handling

        Want me to fix any of these?"

You: Fix the duplicate validation first

Claude: [Creates shared validation utility]
        [Updates 3 files to use it]
        [Shows diff]
        "Done! Consolidated validation logic..."
```

⚡ **Tips & Tricks:**

- **Great untuk larger refactors** — Claude can handle multi-file changes
- **Use untuk debugging** — Claude can read logs, check files, trace issues
- **Let Claude run tests** — iterative fix until tests pass
- **Review changes before accepting** — always verify
- **Give clear goals** — "make auth more secure" vs "add CSRF protection"

⚠️ **Common Mistakes:**

- Not reviewing Claude's changes → Unexpected modifications
- Giving vague instructions → Vague results
- Not using untuk appropriate tasks → Overkill for simple edits
- Forgetting it can run commands → Security consideration
- Over-relying without understanding → Lost ownership of code

* * *

### 19\. Windsurf

📖 **Definisi:** Windsurf adalah AI code editor dari Codeium yang menawarkan "Cascade" — sebuah AI assistant dengan kemampuan agentic yang bisa understand, plan, dan execute multi-step coding tasks. Windsurf positioning sebagai alternative ke Cursor dengan focus pada seamless AI integration dan "Flow State" untuk developers.

💡 **Analogi:** Kalau Cursor seperti **co-pilot yang kamu instruksikan step by step**, Windsurf dengan Cascade lebih seperti **partner yang bisa kamu kasih bigger goal dan dia figure out the steps**. Lebih autonomous, lebih proactive dalam suggesting dan executing.

🔧 **Contoh Praktis:**

```csharp
WINDSURF KEY FEATURES:

1. CASCADE (AI ASSISTANT)
═════════════════════════
- More autonomous than typical AI assistants
- Can plan multi-step tasks
- Creates and edits multiple files
- Understands project context deeply

Example:
"Add user authentication to my Express app"
Cascade: [Plans steps]
         [Creates auth routes]
         [Creates middleware]
         [Updates existing routes]
         [Adds environment variables]
         [Updates documentation]

2. FLOWS
════════
- Persistent AI context across sessions
- AI remembers previous conversations
- Better continuity untuk long projects

Example:
Day 1: "Let's build an e-commerce backend"
Day 2: "Continue with the shopping cart feature"
[AI remembers context dari Day 1]

3. SUPERCOMPLETE
════════════════
- Advanced autocomplete
- Understands intent beyond current line
- Multi-line predictions

You type: "const getUser"
Supercomplete suggests:
async function getUserById(id: string): Promise<User | null> {
try {
    const user = await prisma.user.findUnique({ where: { id } });
    return user;
} catch (error) {
    console.error('Failed to fetch user:', error);
    return null;
}
}

4. COMMAND EXECUTION
════════════════════
- AI can run terminal commands
- Test, build, deploy assistance
- Automated fix-and-retry loops
```

💬 **Contoh Prompt:**

```diff
I'm starting a new project: Blog platform dengan Next.js 14.

Features needed:
- User authentication
- Create/edit/delete posts
- Markdown support
- Comments
- Search functionality

Set up the project with:
- TypeScript
- Tailwind CSS
- Prisma with PostgreSQL
- Proper folder structure

Create all the necessary files and basic implementations.
```

⚡ **Tips & Tricks:**

- **Let Cascade do multi-step tasks** — it's designed for autonomy
- **Use untuk project scaffolding** — setup entire project structure
- **Good untuk refactoring** — can handle large-scale changes
- **Compare dengan Cursor** — different tools suit different workflows
- **Leverage Flows** untuk long-term projects

⚠️ **Common Mistakes:**

- Assuming it works exactly like Cursor → Different paradigm
- Not exploring unique features → Missing Cascade capabilities
- Micromanaging Cascade → Let it be autonomous
- Not reviewing generated code → Trust but verify
- Using untuk simple tasks → Overkill, use simpler tools

* * *

### 20\. v0 (by Vercel)

📖 **Definisi:** v0 adalah AI-powered UI generation tool dari Vercel yang bisa generate React/Next.js components dari text descriptions atau image references. v0 focuses specifically pada UI/frontend generation — you describe atau show what you want, v0 generates working code. Output adalah production-ready React components dengan Tailwind CSS.

💡 **Analogi:** Seperti **magic converter dari design ke code**. Kamu punya screenshot atau design di kepala, describe it atau upload it, v0 generates working React component. Seperti punya designer sekaligus frontend developer yang bisa instantly prototype any UI.

🔧 **Contoh Praktis:**

```markdown
V0 CAPABILITIES:

1. TEXT-TO-UI
═════════════
Describe UI dalam natural language → get component.

Prompt: "Create a pricing page with 3 tiers:
        Basic ($9), Pro ($29 - highlighted), Enterprise (custom).
        Each card has features list dan CTA button."

Output: Complete React component dengan:
        - Three pricing cards
        - Proper styling
        - Responsive layout
        - Hover effects

2. IMAGE-TO-UI
══════════════
Upload screenshot atau design → get matching component.

[Upload screenshot of Stripe's checkout page]
"Recreate this checkout flow with these products:
 - Product A: $29
 - Product B: $49
Add shipping form below."

Output: Component matching the visual design.

3. ITERATE & REFINE
═══════════════════
v0 supports conversational refinement.

Initial: "Create a dashboard sidebar"
Iteration 1: "Make it collapsible on smaller screens"
Iteration 2: "Add icons to each menu item"
Iteration 3: "Add user profile section at bottom"

4. COMPONENT LIBRARY
════════════════════
v0 uses shadcn/ui patterns and Tailwind CSS.
Output is consistent dan production-ready.
```

💬 **Contoh Prompt:**

```vbnet
Create a modern hero section for a productivity app:

LAYOUT:
- Split layout: content left, image right
- Content: badge, headline, subheadline, 2 CTAs, social proof

CONTENT:
- Badge: "New: AI-powered features"
- Headline: "Get more done in less time"
- Subheadline: "The all-in-one workspace for your team"
- Primary CTA: "Start Free Trial"
- Secondary CTA: "Watch Demo"
- Social proof: "Trusted by 10,000+ teams"

STYLE:
- Clean, modern, plenty of whitespace
- Gradient accent on headline
- Subtle animation on image
- Dark mode compatible

Generate as single React component dengan Tailwind.
```

```diff
[Upload image of Linear's command palette]

Recreate this command palette component:
- Same visual style
- Same layout
- Add keyboard shortcuts display
- Support dark mode
```

⚡ **Tips & Tricks:**

- **Start dengan text, refine dengan iterations** — easier than perfect prompt
- **Use untuk rapid prototyping** — validate ideas quickly
- **Export dan customize** — v0 output is starting point
- **Combine dengan Cursor** — generate di v0, customize di Cursor
- **Reference specific sites** — "like Stripe's..." gives clear direction

⚠️ **Common Mistakes:**

- Expecting production-ready code for complex apps → It's untuk components
- Not iterating enough → First output rarely perfect
- Not customizing after export → v0 output needs project adaptation
- Using untuk non-UI tasks → v0 is specifically for UI
- Over-relying untuk every component → Sometimes manual is faster

* * *

### 21\. Bolt.new

📖 **Definisi:** Bolt.new adalah AI-powered full-stack app builder yang bisa create, edit, dan deploy applications entirely dari browser. Tidak perlu local development setup — everything happens in-browser. Kamu describe app yang kamu mau, Bolt builds it (frontend, backend, database), dan kamu bisa deploy dengan satu click.

💡 **Analogi:** Seperti punya **developer + server + deployment pipeline dalam satu browser tab**. Describe app kamu, Bolt build everything, kamu dapat working app dengan shareable URL. Mirip dengan Google Docs untuk documents — everything in-browser, instantly accessible.

🔧 **Contoh Praktis:**

```markdown
BOLT.NEW CAPABILITIES:

1. FULL-STACK GENERATION
════════════════════════
- Frontend (React, Vue, Svelte, etc.)
- Backend (Node.js, API routes)
- Database integration
- Styling (Tailwind, CSS)

Prompt: "Build a task management app with:
        - Add, edit, delete tasks
        - Due dates
        - Priority levels
        - Filter by status"

Bolt creates: Complete full-stack app with all features.

2. IN-BROWSER DEVELOPMENT
═════════════════════════
- No local setup needed
- Edit code directly in browser
- See changes in real-time
- Full IDE-like experience

3. INSTANT PREVIEW
══════════════════
- Live preview di sebelah code
- Changes reflect immediately
- Test functionality langsung
- Mobile preview available

4. ONE-CLICK DEPLOY
═══════════════════
- Deploy to Bolt hosting
- Get shareable URL instantly
- No configuration needed
- Free tier available

5. ITERATE WITH AI
══════════════════
"Add a dark mode toggle"
"Make it mobile responsive"
"Add authentication"
[Bolt updates the entire app]
```

💬 **Contoh Prompt:**

```diff
Build a personal finance tracker:

FEATURES:
- Add income and expenses with categories
- Dashboard with monthly summary
- Charts showing spending by category
- Budget setting per category
- Alerts when approaching budget limit

TECH:
- React frontend
- Node.js backend
- SQLite database
- Tailwind for styling

PAGES:
- Dashboard (main view)
- Add Transaction
- Categories management
- Budget settings

Make it mobile-friendly dan deploy when ready.
```

```diff
Build a simple blog CMS:

- Create, edit, delete posts
- Markdown support for content
- Tags for categorization
- Public view of posts
- Simple admin panel (password protected)

Keep it minimal dan clean.
```

⚡ **Tips & Tricks:**

- **Great untuk MVPs dan prototypes** — validate ideas fast
- **Use untuk learning projects** — experiment without setup
- **Quick demos untuk clients** — instant shareable URL
- **Start simple, add complexity** — iterative approach works best
- **Export code if needed** — take it to proper development later

⚠️ **Common Mistakes:**

- Using untuk complex production apps → Better for prototypes
- Expecting advanced features → Keep scope realistic
- Not understanding generated code → Learn from what Bolt creates
- No version control → Changes are ephemeral unless exported
- Over-engineering prompts → Bolt works best with clear, simple goals

## Kategori 4: Workflow & Techniques

Kategori ini membahas **cara kerja dan teknik** dalam vibe coding. Bukan just tools, tapi how to use them effectively dalam daily workflow.

* * *

### 22\. Scaffolding

📖 **Definisi:** Scaffolding dalam vibe coding adalah proses di mana AI generate basic structure, boilerplate, atau template code sebagai starting point yang kemudian di-fill dan customize. Focus pada creating foundation dan skeleton — bukan complete implementation. Scaffolding mempercepat project setup dan ensures consistent structure.

💡 **Analogi:** Seperti **kerangka bangunan sebelum diisi**. Tukang membangun frame dulu — struktur, rangka, posisi ruangan — sebelum mengisi dengan dinding, pintu, finishing. AI bikin scaffold (kerangka), kamu isi dengan actual business logic, custom features, dan specific implementation details.

🔧 **Contoh Praktis:**

```swift
SCAFFOLDING LEVELS:

1. PROJECT SCAFFOLDING
══════════════════════
"Setup new Next.js project dengan:
 - TypeScript, Tailwind, Prisma
 - Folder structure untuk e-commerce
 - Base configurations"

Output:
├── src/
│   ├── app/
│   │   ├── (auth)/
│   │   ├── (dashboard)/
│   │   └── (shop)/
│   ├── components/
│   │   ├── ui/
│   │   └── features/
│   ├── lib/
│   └── types/
├── prisma/
├── public/
└── config files...

2. FEATURE SCAFFOLDING
══════════════════════
"Scaffold authentication feature:
 - Pages: login, register, forgot password
 - Components: forms, protected route
 - API: auth endpoints
 - Types: user, session"

Output: File structure dengan basic implementations
        dan TODO comments untuk business logic.

3. COMPONENT SCAFFOLDING
════════════════════════
"Scaffold data table component:
 - Props interface
 - Basic structure
 - Placeholder for: sorting, filtering, pagination"

Output:
interface DataTableProps<T> {
columns: Column<T>[];
data: T[];
// TODO: Add sorting props
// TODO: Add filtering props
// TODO: Add pagination props
}

export function DataTable<T>({ columns, data }: DataTableProps<T>) {
// TODO: Implement sorting logic
// TODO: Implement filtering logic
// TODO: Implement pagination logic

return (
    <table>
      {/* Basic table structure */}
    </table>
);
}
```

💬 **Contoh Prompt:**

```bash
Scaffold a Next.js 14 feature for "User Management":

CREATE FILE STRUCTURE:
├── app/(dashboard)/users/
│   ├── page.tsx (list users)
│   ├── [id]/page.tsx (user detail)
│   └── new/page.tsx (create user)
├── components/users/
│   ├── UserTable.tsx
│   ├── UserForm.tsx
│   └── UserCard.tsx
├── lib/users/
│   ├── actions.ts (server actions)
│   └── validations.ts
└── types/user.ts

For each file:
- Include basic structure and imports
- Add TODO comments for business logic
- Define TypeScript interfaces
- NO implementation details — just scaffolding

I will fill in the actual implementation.
```

⚡ **Tips & Tricks:**

- **Great untuk starting new features** — consistent structure
- **Define your standard scaffold template** — reuse across projects
- **Use TODO comments** — mark where implementation goes
- **Scaffold includes types** — prevent type errors later
- **Don't over-scaffold** — some things better written manually

⚠️ **Common Mistakes:**

- Expecting complete implementation → Scaffolding is skeleton only
- Not customizing to project standards → Adapt scaffold to your patterns
- Over-scaffolding → Sometimes simple features don't need it
- Ignoring scaffolded structure → Defeats the purpose
- Scaffold without types → Miss type-safety benefits

* * *

### 23\. Code Refactoring (AI-assisted)

📖 **Definisi:** AI-assisted code refactoring adalah proses restructuring existing code dengan bantuan AI untuk improve readability, performance, maintainability, atau adherence to patterns — without changing external behavior. AI helps identify what to refactor dan executes the refactoring, while human ensures correctness.

💡 **Analogi:** Seperti **renovasi rumah dengan kontraktor AI**. Rumah (code) sudah berfungsi, tapi layout bisa lebih baik, atau style sudah outdated. Kamu tunjukkan bagian yang mau di-renovate, explain goals, AI suggest approach dan execute renovation. Fungsi rumah tetap sama, tapi structure dan appearance improved.

🔧 **Contoh Praktis:**

```bash
TYPES OF AI-ASSISTED REFACTORING:

1. READABILITY REFACTOR
═══════════════════════
Before:
function p(d){let r=[];for(let i=0;i<d.length;i++){if(d[i].a)r.push(d[i])}return r}

Prompt: "Refactor for readability: meaningful names, modern syntax"

After:
function filterActiveItems(items: Item[]): Item[] {
return items.filter(item => item.isActive);
}

2. PERFORMANCE REFACTOR
═══════════════════════
Before:
function findUser(users, id) {
for (let i = 0; i < users.length; i++) {
    if (users[i].id === id) return users[i];
}
return null;
}

Prompt: "Optimize for frequent lookups dengan many users"

After:
// Create lookup map once
const userMap = new Map(users.map(user => [user.id, user]));

// O(1) lookup
function findUser(id: string): User | undefined {
return userMap.get(id);
}

3. PATTERN REFACTOR
═══════════════════
Before: API calls scattered across components

Prompt: "Refactor to use repository pattern"

After: Centralized repository class dengan
       consistent methods dan error handling

4. MODERNIZATION REFACTOR
═════════════════════════
Before: Class components dengan lifecycle methods

Prompt: "Convert to functional components dengan hooks"

After: Functional components dengan
       useState, useEffect, custom hooks

5. DRY REFACTOR (Don't Repeat Yourself)
═══════════════════════════════════════
Before: Duplicate validation logic di 5 files

Prompt: "Extract duplicate validation ke shared utility"

After: Single validation module used across files
```

💬 **Contoh Prompt:**

```bash
Refactor this code:

function processOrder(order) {
let total = 0;
for (let i = 0; i < order.items.length; i++) {
    let item = order.items[i];
    let price = item.price;
    let qty = item.quantity;
    if (item.discount) {
      price = price - (price * item.discount / 100);
    }
    total = total + (price * qty);
}
if (order.coupon) {
    if (order.coupon.type === 'percentage') {
      total = total - (total * order.coupon.value / 100);
    } else {
      total = total - order.coupon.value;
    }
}
return total;
}

REFACTORING GOALS:
1. Modern ES6+ syntax (arrow functions, destructuring)
2. Meaningful variable dan function names
3. Extract helpers untuk calculations
4. Add TypeScript types
5. Improve readability dengan smaller functions
6. Add JSDoc comments

EXPLAIN each change you make.
```

⚡ **Tips & Tricks:**

- **Specify refactoring goals clearly** — "more readable" is vague
- **Ask AI to explain changes** — understand the why
- **Test before and after** — ensure behavior unchanged
- **Incremental refactoring** — don't refactor entire codebase at once
- **Review carefully** — AI sometimes changes behavior accidentally

⚠️ **Common Mistakes:**

- Refactoring without clear goals → Random changes
- Not testing after refactor → Broken functionality
- Too many changes at once → Hard to debug issues
- Changing behavior accidentally → Refactor should preserve behavior
- Blindly accepting AI suggestions → Review each change

* * *

### 24\. Inline Completion

📖 **Definisi:** Inline completion adalah AI feature yang memberikan real-time code suggestions saat kamu mengetik, muncul sebagai "ghost text" (text abu-abu/transparan) yang bisa di-accept dengan Tab atau di-dismiss. Ini berbeda dengan chat-based interaction — inline completion is passive, always-on, dan integrates directly into typing flow.

💡 **Analogi:** Seperti **predictive text di smartphone**, tapi untuk code dan jauh lebih intelligent. Saat kamu ketik pesan, phone suggests next words. Inline completion does the same — saat kamu ketik code, AI predicts dan suggests kelanjutannya berdasarkan context. Accept dengan Tab, ignore dan terus ketik kalau tidak sesuai.

🔧 **Contoh Praktis:**

```typescript
INLINE COMPLETION SCENARIOS:

1. FUNCTION COMPLETION
══════════════════════
You type: function calculateTax(
Ghost text: amount: number, rate: number): number {
              return amount * (rate / 100);
            }

2. PATTERN COMPLETION
═════════════════════
You type: const [loading, setLoading] = useState(
Ghost text: false);

You type: useEffect(() => {
Ghost text: // Effect logic here
           }, []);

3. COMMENT-DRIVEN COMPLETION
════════════════════════════
You type: // Validate email format
Ghost text:
const isValidEmail = (email: string): boolean => {
const emailRegex = /^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/;
return emailRegex.test(email);
};

4. IMPORT COMPLETION
════════════════════
You type: import { useState,
Ghost text: useEffect, useCallback } from 'react';

5. REPETITIVE PATTERN
═════════════════════
After writing:
const firstName = formData.get('firstName');
const lastName = formData.get('lastName');

You type: const
Ghost text: email = formData.get('email');
```

💬 **Contoh (Guiding inline completion):**

Inline completion doesn't use explicit prompts — it reads context. But you can guide it:

```typescript
// GUIDE WITH COMMENTS:
// Function to format currency to Indonesian Rupiah
// Input: number (cents)
// Output: formatted string "Rp X.XXX.XXX"
// [AI akan suggest implementation]

// GUIDE WITH FUNCTION SIGNATURE:
function formatToRupiah(amount: number): string {
// [AI suggests based on name dan types]
}

// GUIDE WITH CONTEXT:
// Other functions in file use Intl.NumberFormat
function formatToRupiah(amount: number): string {
// [AI likely suggests Intl.NumberFormat approach]
}
```

⚡ **Tips & Tricks:**

- **Write descriptive comments** — guides completion direction
- **Use descriptive function/variable names** — AI uses them as hints
- **Tab to accept, Esc to dismiss** — learn the shortcuts
- **Ctrl+\] untuk next suggestion** — cycle through options
- **Open related files** — more context = better suggestions

⚠️ **Common Mistakes:**

- Accepting without reading → Introducing bugs
- Fighting AI instead of guiding → Frustrating experience
- No context = poor suggestions → Give AI hints
- Ignoring valuable suggestions → Miss productivity gains
- Expecting perfect completion every time → It's a tool, not magic

* * *

### 25\. Chat-based Coding

📖 **Definisi:** Chat-based coding adalah paradigma vibe coding di mana interaksi dengan AI dilakukan melalui conversational chat interface, mirip messaging dengan colleague atau mentor. Kamu bisa ask questions, request code, discuss approaches, get explanations — all dalam natural conversation flow.

💡 **Analogi:** Seperti **Slack conversation dengan senior developer yang selalu available dan super knowledgeable**. Kamu bisa tanya apa saja, minta tolong apa saja, diskusi approach, bahkan rubber duck debugging. Dia selalu responsive, tidak pernah sibuk, dan happy to help at any hour.

🔧 **Contoh Praktis:**

```vbnet
CHAT-BASED CODING SESSION:

YOU: Saya perlu implement infinite scroll untuk product list.
     Currently pakai pagination biasa.

AI: Good enhancement! Beberapa questions dulu:
    1. Framework yang dipakai?
    2. Data fetching: REST atau GraphQL?
    3. API support cursor-based pagination?
    4. Prefer intersection observer atau scroll event?

YOU: Next.js 14, REST API, ya support cursor pagination,
     prefer intersection observer.

AI: Perfect choice. Here's the approach:
    1. Create custom hook useInfiniteScroll
    2. Use Intersection Observer API
    3. Track cursor for next page
    4. Append new items to existing list

    Here's the implementation:
    [Provides code]

YOU: Looks good! Tapi gimana kalau user scroll super fast?

AI: Great catch! Kita perlu debounce dan loading state.
    Let me update:
    [Provides updated code]

YOU: Kalau mau add "Back to Top" button?

AI: Easy addition!
    [Provides BackToTop component dan integration]
```

💬 **Contoh Prompt:**

```vbnet
Let's work through building a search feature step by step.

CURRENT SETUP:
- Next.js 14 App Router
- Products in PostgreSQL via Prisma
- Currently showing all products

REQUIREMENTS:
- Search by product name
- Filter by category (multiple select)
- Filter by price range
- Sort options (price, newest, popular)

Rather than generating everything at once, let's discuss:
1. What state do we need?
2. Client vs server filtering?
3. How to handle URL state?

Start dengan explaining your recommended approach.
```

⚡ **Tips & Tricks:**

- **Conversational tone works well** — natural language is fine
- **Ask follow-up questions** — dig deeper into solutions
- **Let AI ask clarifying questions** — better context
- **Build incrementally through conversation** — step by step
- **Reference previous messages** — maintain continuity

⚠️ **Common Mistakes:**

- Monologue instead of dialogue → Miss AI's insights
- Not engaging with AI's questions → Suboptimal solutions
- Jumping to implementation tanpa discussion → Skip considerations
- Very long prompts instead of conversation → Break it up
- Expecting one message to solve everything → Iterate

* * *

### 26\. Agentic Coding

📖 **Definisi:** Agentic coding adalah pendekatan vibe coding di mana AI beroperasi lebih autonomously — bisa plan, execute multi-step tasks, read/write files, run commands, make decisions, dan iterate with minimal human intervention. Berbeda dengan assistant yang tunggu instruksi setiap step, agent bisa diberi goal dan figure out steps sendiri.

💡 **Analogi:** Perbedaan **assistant vs agent** seperti perbedaan giving turn-by-turn directions vs giving destination. Assistant: "Belok kiri... jalan lurus... belok kanan..." Agent: "Pergi ke kantor pos" — agent figures out the route dan handles obstacles along the way.

🔧 **Contoh Praktis:**

```makefile
ASSISTANT-STYLE (Step by step):
═══════════════════════════════
YOU: Create user model
AI: [Creates model]
YOU: Create user controller
AI: [Creates controller]
YOU: Create user routes
AI: [Creates routes]
YOU: Add validation
AI: [Adds validation]
...continues step by step...

AGENTIC-STYLE (Goal-oriented):
══════════════════════════════
YOU: Build complete user CRUD with validation and tests.
     Follow existing patterns in the codebase.

AI: [Plans the work]
    "I'll create:
    1. User model with Prisma schema
    2. Validation schemas with Zod
    3. CRUD API routes
    4. Controller logic
    5. Unit tests

    Let me start..."

    [Creates prisma/schema.prisma update]
    [Creates src/lib/validations/user.ts]
    [Creates src/app/api/users/route.ts]
    [Creates src/app/api/users/[id]/route.ts]
    [Creates tests/users.test.ts]
    [Runs tests to verify]

    "Done! Created 5 files:
    - Updated Prisma schema
    - Created validation schemas
    - Created API routes (list, create, get, update, delete)
    - Created unit tests (all passing)

    Want me to explain any part?"
```

💬 **Contoh Prompt:**

```markdown
GOAL: Add complete authentication to this project

YOU HAVE AUTONOMY TO:
- Read existing code structure
- Create necessary files
- Install required packages (dengan npm)
- Update existing files as needed
- Run tests to verify

REQUIREMENTS:
- JWT tokens with refresh token flow
- Login, register, logout, forgot password
- Password hashing with bcrypt
- Protected route middleware
- Follow existing code patterns

CONSTRAINTS:
- Don't modify unrelated files
- Create proper TypeScript types
- Include error handling
- Add to existing API structure

Execute this task. Report back dengan summary of:
1. Files created
2. Files modified
3. Packages installed
4. Any decisions you made
```

⚡ **Tips & Tricks:**

- **Clear goal dan constraints** — guide without micromanaging
- **Let AI plan before execute** — review the plan
- **Review hasil, bukan setiap step** — trust but verify at end
- **Use untuk repetitive multi-file tasks** — leverage autonomy
- **Set boundaries** — what it can and cannot modify

⚠️ **Common Mistakes:**

- Micromanaging agent → Defeats the purpose
- Vague goals tanpa constraints → Unexpected changes
- Not reviewing final output → Miss issues
- Using untuk simple single-file tasks → Overkill
- No constraints → Agent might change too much

## Kategori 5: Quality & Best Practices

Kategori terakhir ini membahas **menjaga kualitas** dalam vibe coding. AI powerful, tapi tanpa quality control, outputnya bisa problematic. Ini adalah istilah-istilah yang help you build reliable, trustworthy code.

* * *

###27. Code Review (AI-assisted)

📖 **Definisi:** AI-assisted code review adalah proses menggunakan AI untuk review code dan mendapatkan feedback tentang quality, potential bugs, improvements, security issues, dan adherence to best practices. AI acts sebagai additional reviewer — catching things human might miss, providing consistent review standards, dan available anytime.

💡 **Analogi:** Seperti punya **senior reviewer yang selalu available untuk second opinion**. Sebelum submit code, kamu minta dia review. Dia punya fresh eyes, tidak bias karena sudah lama lihat code yang sama, dan bisa catch things yang kamu miss karena familiarity blindness.

🔧 **Contoh Praktis:**

```markdown
AI CODE REVIEW ASPECTS:

1. BUGS & ERRORS
════════════════
"Check untuk potential bugs, edge cases yang gak di-handle,
dan runtime errors yang mungkin terjadi"

2. SECURITY REVIEW
══════════════════
"Review untuk security vulnerabilities:
 - SQL injection
 - XSS
 - CSRF
 - Sensitive data exposure
 - Auth/authz issues"

3. PERFORMANCE REVIEW
═════════════════════
"Identify performance issues:
 - Unnecessary re-renders
 - N+1 queries
 - Memory leaks
 - Large bundle impact"

4. BEST PRACTICES
═════════════════
"Review adherence to:
 - React best practices
 - TypeScript best practices
 - Accessibility standards
 - Clean code principles"

5. READABILITY & MAINTAINABILITY
════════════════════════════════
"Evaluate code quality:
 - Naming conventions
 - Code organization
 - Documentation
 - Complexity"
```

💬 **Contoh Prompt:**

````kotlin
Review this code as a senior developer.

```typescript
export async function createOrder(data: any) {
  const order = await prisma.order.create({
    data: {
      userId: data.userId,
      items: data.items,
      total: data.items.reduce((sum, item) => sum + item.price * item.qty, 0),
      status: 'pending'
    }
  })

  await sendEmail(data.email, 'Order Confirmation', `Order ${order.id} created`)

  return order
}
````

REVIEW FOR:

1. Type safety issues
2. Error handling gaps
3. Security concerns
4. Performance problems
5. Best practice violations

FORMAT: For each issue found:

- Severity: Critical / Major / Minor
- Location: Line number atau area
- Problem: What's wrong
- Fix: How to fix it
- Why: Why this matters

```markdown

⚡ **Tips & Tricks:**
- **Review AI-generated code too** — AI makes mistakes
- **Specify review criteria** — focused review is better
- **Ask for severity ranking** — prioritize fixes
- **Use before merging** — catch issues early
- **Learn from reviews** — improve your own coding

⚠️ **Common Mistakes:**
- Not reviewing AI's own generated code → Blind trust
- Generic "review this" without criteria → Shallow review
- Ignoring review feedback → Defeats the purpose
- Only reviewing for bugs, not style/patterns → Miss quality issues
- Accepting all suggestions blindly → Some may not fit context

---

### 28. Hallucination (Code Context)

📖 **Definisi:**
Dalam code context, hallucination adalah ketika AI generate code yang terlihat correct tapi sebenarnya menggunakan APIs, methods, libraries, atau syntax yang tidak exist atau incorrect. AI "confident" tentang code yang sebenarnya invented atau outdated. Ini adalah risiko significant dalam vibe coding.

💡 **Analogi:**
Seperti **orang yang sangat confident menjawab padahal mengarang**. AI tidak bilang "saya tidak tau" — dia generate something yang looks plausible. Seperti someone citing a book that doesn't exist, atau referencing API method yang never existed. Sounds authoritative, tapi fabricated.

🔧 **Contoh Praktis:**
```

CODE HALLUCINATION EXAMPLES:

1. NON-EXISTENT METHODS ═══════════════════════ AI generates: response.getData() Reality: Method doesn't exist. Should be response.data
2. WRONG PACKAGE IMPORTS ════════════════════════ AI generates: import { useRouter } from 'next/navigation' Reality: Correct for Next.js 14, but AI might suggest for project using Next.js 12 (should be 'next/router')
3. INVENTED LIBRARIES ═════════════════════ AI generates: npm install react-super-forms Reality: Package doesn't exist. AI made it up based on similar-sounding packages
4. DEPRECATED/REMOVED APIs ══════════════════════════ AI generates: componentWillMount() { } Reality: Deprecated in React 16.3, removed later
5. WRONG SYNTAX FOR VERSION ═══════════════════════════ AI generates: <Suspense fallback={...}> for data fetching Reality: Correct concept but wrong implementation for the specific React version
6. FICTIONAL CONFIGURATION ══════════════════════════ AI generates: next.config.js dengan option yang gak exist Reality: AI extrapolated from partial knowledge

```java

💬 **Contoh Prompt (Verification):**
```

Kamu baru generate code yang pakai ini:

import { useAsyncData } from '@tanstack/react-query'

VERIFY:

1. Apakah hook 'useAsyncData' benar-benar ada di react-query?
2. Kalau tidak, apa yang seharusnya dipakai?
3. Tunjukkan correct import dan usage

Saya mau pastikan ini bukan hallucination sebelum implementasi.

Sebelum saya implementasi, verify these assumptions:

1. Next.js 14 supports 'use server' directive di inline function
2. Prisma's findMany supports 'cursor' pagination
3. Tailwind CSS class 'animate-pulse' exists by default

Cite documentation atau confirm ini accurate.

```markdown

⚡ **Tips & Tricks:**
- **Always verify unfamiliar APIs** — Google atau check docs
- **Test generated code** — don't just read it
- **Check package existence** — npm search before install
- **Use TypeScript** — catches many hallucinations at compile time
- **When in doubt, ask AI to verify** — sometimes it catches itself

⚠️ **Common Mistakes:**
- Blindly trusting AI → Implementing hallucinated code
- Not testing before committing → Runtime surprises
- Ignoring TypeScript errors → Often indicates hallucination
- Not verifying package existence → npm install fails
- Assuming AI is always current → Might use outdated patterns

---

### 29. Grounding

📖 **Definisi:**
Grounding adalah teknik untuk "anchor" AI responses ke factual information, existing code, atau documentation — reducing hallucination dan ensuring responses based on reality, bukan AI's imagination. Grounded AI response references actual, verifiable information rather than generating from general knowledge alone.

💡 **Analogi:**
Seperti memastikan seseorang **bicara berdasarkan dokumen yang ada**, bukan mengarang. "Jawab berdasarkan manual ini" vs "Jawab berdasarkan apa yang kamu tau." Grounding means providing the "manual" so AI references actual facts.

🔧 **Contoh Praktis:**
```

GROUNDING TECHNIQUES:

1. CODE CONTEXT GROUNDING ═════════════════════════ "Based on the existing code in @src/lib/api.ts, create a new function that follows the same patterns"

AI is grounded to existing patterns, not inventing new ones.

1. DOCUMENTATION GROUNDING ══════════════════════════ "According to Next.js 14 documentation, server components are the default. Using this fact, implement..."

AI is anchored to specific doc reference.

1. TYPE GROUNDING ═════════════════ "Here's the User type. All user-related code must strictly follow this type definition."

interface User { id: string; email: string; name: string; createdAt: Date; }

AI is constrained by the type.

1. EXAMPLE GROUNDING ════════════════════ "Here are 3 existing API routes. Create a new one following EXACTLY the same patterns."

AI is grounded to concrete examples.

1. CONSTRAINT GROUNDING ═══════════════════════ "Use ONLY these approved packages: react, react-dom, next, tailwindcss, prisma. No other packages."

AI is constrained to specific resources.

```java

💬 **Contoh Prompt (Heavily grounded):**
```

GROUNDING CONTEXT: ══════════════════

SOURCE OF TRUTH - User type:

```typescript
// @/types/user.ts
export interface User {
  id: string;
  email: string;
  name: string;
  role: 'admin' | 'user';
  createdAt: Date;
}
```

SOURCE OF TRUTH - API pattern:

```typescript
// @/app/api/products/route.ts (existing)
export async function GET() {
  try {
    const products = await prisma.product.findMany();
    return Response.json({ success: true, data: products });
  } catch (error) {
    return Response.json(
      { success: false, error: 'Failed to fetch' },
      { status: 500 }
    );
  }
}
```

TASK: ═════ Create GET /api/users route.

CONSTRAINTS:

- Use ONLY the User type as defined above
- Follow EXACTLY the API pattern shown above
- Do NOT invent additional fields or patterns
- Do NOT use any methods not shown in the example

Ground your response entirely on the provided context.

```markdown

⚡ **Tips & Tricks:**
- **Always provide relevant context** — more grounding = less hallucination
- **Reference documentation explicitly** — "According to X docs..."
- **Use types as guardrails** — TypeScript types constrain AI
- **Ask AI to cite sources** — "Where did you get this from?"
- **Provide working examples** — AI follows patterns

⚠️ **Common Mistakes:**
- Prompting without context → AI hallucinates freely
- Assuming AI knows your codebase → It doesn't without context
- Not providing type information → Type errors
- Generic prompts tanpa grounding → Unreliable output
- Not validating against ground truth → Miss inconsistencies

---

### 30. Human-in-the-Loop

📖 **Definisi:**
Human-in-the-loop (HITL) adalah paradigma di mana human tetap terlibat dalam oversight, review, approval, dan decision-making meskipun AI melakukan heavy lifting. AI assist, suggest, dan execute, tapi human approve, verify, dan refine. Ini adalah quality control mechanism yang essential untuk reliable vibe coding.

💡 **Analogi:**
Seperti **self-driving car dengan human driver tetap di belakang kemudi**. Car bisa drive — navigate, accelerate, brake, handle most situations. Tapi human tetap watch, bisa takeover anytime, makes critical decisions, dan responsible for outcomes. Not fully autonomous — supervised autonomy.

🔧 **Contoh Praktis:**
```

HUMAN-IN-THE-LOOP PATTERNS:

1. REVIEW BEFORE COMMIT ═══════════════════════ AI generates code ↓ Human reviews every change ↓ Human approves/modifies ↓ Only then: commit
2. APPROVAL CHECKPOINTS ═══════════════════════ AI: "I plan to:
1. Create user model
2. Add auth routes
3. Update middlewareShould I proceed?"

Human: "Yes, proceed"

AI: "Step 1 complete. Here's what I created: \[...\] Continue to step 2?"

Human: "Looks good, continue"

1. CRITICAL DECISION ESCALATION ═══════════════════════════════ AI: "I can solve this dengan approach A atau B. A: Simpler but less scalable B: More complex but future-proof This is architectural decision. Which do you prefer?"

Human makes the call, AI executes.

1. OVERRIDE CAPABILITY ══════════════════════ At any point, human can:

- Modify AI's output
- Reject AI's suggestions
- Take over manually
- Change direction

AI suggests, human decides.

1. VERIFICATION LOOPS ═════════════════════ AI generates ↓ Human tests ↓ Human finds issue ↓ Human describes issue to AI ↓ AI fixes ↓ Human verifies fix ↓ Repeat until satisfied

```markdown

💬 **Contoh Prompt:**
```

Build the payment integration feature.

HUMAN-IN-THE-LOOP REQUIREMENTS:

1. PLANNING PHASE:
   - Show me your plan FIRST
   - Wait for my approval before starting
   - I may modify the plan
2. IMPLEMENTATION:
   - After each major step, summarize what you did
   - Wait for my OK before continuing
   - Show diffs of changed files
3. DECISIONS:
   - For any decision dengan tradeoffs, present options
   - I will choose, you execute
   - Don't make architectural decisions alone
4. CONCERNS:
   - Flag security concerns immediately
   - Flag performance concerns
   - If unsure about something, ask
5. COMPLETION:
   - At end, provide full summary
   - List all files created/modified
   - Highlight anything I should double-check

Start dengan your plan for this feature.

```markdown

⚡ **Tips & Tricks:**
- **Set explicit checkpoints** — define when AI should pause
- **Always review sebelum merge** — final human approval
- **Don't let AI decide critical things alone** — you own decisions
- **Maintain understanding** — you should understand the code
- **Document AI-assisted work** — know what was generated

⚠️ **Common Mistakes:**
- Full autopilot mode → Lose control and understanding
- Approving tanpa reading → Rubber stamping
- No checkpoints for complex tasks → Too much unsupervised work
- Losing understanding of own codebase → Can't debug or extend
- Over-trusting AI → AI makes mistakes

---

## Closing: Dari Vocabulary ke Mastery

### Perjalanan Kita

Selamat! Kamu baru saja mempelajari **30 istilah essential** dalam vibe coding:
```

KATEGORI 1: FUNDAMENTAL (8 istilah) ├── Vibe Coding ├── AI Code Editor ├── Code Generation ├── Natural Language Programming ├── AI Pair Programming ├── Prompt-to-Code ├── Context Window └── Token

KATEGORI 2: PROMPTING (7 istilah) ├── Prompt Engineering ├── System Prompt ├── Instruction Prompt ├── Few-shot Prompting ├── Chain-of-thought Prompting ├── Iterative Prompting └── Context Injection

KATEGORI 3: TOOLS (6 istilah) ├── Cursor ├── GitHub Copilot ├── Claude Code ├── Windsurf ├── v0 └── Bolt.new

KATEGORI 4: WORKFLOW (5 istilah) ├── Scaffolding ├── Code Refactoring (AI-assisted) ├── Inline Completion ├── Chat-based Coding └── Agentic Coding

KATEGORI 5: QUALITY (4 istilah) ├── Code Review (AI-assisted) ├── Hallucination ├── Grounding └── Human-in-the-Loop


### Quick Reference Table

| # | Istilah | One-liner |
|---|---|---|
| 1 | Vibe Coding | Coding dengan AI sebagai collaborative partner |
| 2 | AI Code Editor | Editor dengan AI terintegrasi (Cursor, etc.) |
| 3 | Code Generation | AI generate code dari natural language |
| 4 | Natural Language Programming | Programming pakai bahasa manusia |
| 5 | AI Pair Programming | Collaboration coding dengan AI sebagai pair |
| 6 | Prompt-to-Code | Pipeline dari text prompt ke working code |
| 7 | Context Window | "Memory" AI untuk lihat code dan history |
| 8 | Token | Unit pengukuran text yang diproses AI |
| 9 | Prompt Engineering | Skill menulis prompt yang effective |
| 10 | System Prompt | Instruksi permanent untuk AI behavior |
| 11 | Instruction Prompt | Task/command spesifik per request |
| 12 | Few-shot Prompting | Kasih contoh sebelum actual task |
| 13 | Chain-of-thought | Minta AI explain reasoning step-by-step |
| 14 | Iterative Prompting | Build output melalui multiple rounds |
| 15 | Context Injection | Sertakan relevant code/info ke prompt |
| 16 | Cursor | AI-first code editor paling populer |
| 17 | GitHub Copilot | AI coding assistant dari GitHub |
| 18 | Claude Code | Terminal-based AI coding dari Anthropic |
| 19 | Windsurf | AI code editor dengan Cascade/Flow |
| 20 | v0 | AI UI generator dari Vercel |
| 21 | Bolt.new | Browser-based full-stack app builder |
| 22 | Scaffolding | AI generate basic structure/template |
| 23 | Code Refactoring | AI-assisted code restructuring |
| 24 | Inline Completion | Real-time code suggestions saat mengetik |
| 25 | Chat-based Coding | Coding via conversational chat interface |
| 26 | Agentic Coding | AI dengan autonomy untuk multi-step tasks |
| 27 | Code Review | AI-assisted code quality review |
| 28 | Hallucination | AI generate code/API yang tidak exist |
| 29 | Grounding | Anchor AI ke factual information |
| 30 | Human-in-the-Loop | Human oversight dalam AI workflow |

### Learning Path Recommendation


STEP 1: MASTER FUNDAMENTALS (Week 1) ════════════════════════════════════ ├── Understand terms 1-8 ├── Try basic vibe coding ├── Get comfortable dengan AI interaction └── Build simple project

STEP 2: LEARN PROMPTING (Week 2) ════════════════════════════════ ├── Study terms 9-15 ├── Practice prompt engineering ├── Experiment dengan different techniques └── Develop personal prompt templates

STEP 3: PICK ONE TOOL (Week 3) ══════════════════════════════ ├── Review terms 16-21 ├── Choose: Cursor recommended untuk start ├── Learn tool deeply └── Explore features

STEP 4: DEVELOP WORKFLOW (Week 4) ═════════════════════════════════ ├── Study terms 22-26 ├── Build actual projects ├── Develop your own workflow └── Find your rhythm

STEP 5: FOCUS ON QUALITY (Ongoing) ══════════════════════════════════ ├── Internalize terms 27-30 ├── Always review AI output ├── Stay human-in-the-loop └── Continuous improvement



### Frequently Asked Questions

**"Harus hafal semua istilah?"**
Tidak. Bookmark artikel ini sebagai reference. Seiring waktu pakai, istilah-istilah ini akan jadi natural.

**"Tool mana yang terbaik untuk mulai?"**
**Cursor** adalah recommendation untuk beginners — paling populer, banyak tutorials, good balance of features.

**"Perlu bisa coding dulu sebelum vibe coding?"**
Basic programming understanding sangat membantu. Kamu perlu bisa review dan understand code yang AI generate. Vibe coding amplifies skill, bukan replaces it.

**"Berapa lama untuk jago vibe coding?"**
Basics: 1-2 minggu untuk comfortable. Proficiency: 1-2 bulan dengan consistent practice. Mastery: Ongoing — field terus evolve.

###Pesan Penutup

Glossary ini adalah **starting point** — foundation vocabulary untuk perjalanan vibe coding kamu.

Tapi vocabulary alone tidak cukup. Real mastery comes from **practice**. Build projects. Make mistakes. Learn from them. Iterate.

Istilah-istilah ini akan menjadi second nature seiring kamu practice. Yang awalnya terasa asing akan menjadi comfortable. Yang awalnya harus di-lookup akan menjadi intuitive.

**Bookmark artikel ini.** Kembali kapanpun butuh reference. Share ke teman yang juga belajar vibe coding.

Dan yang paling penting: **Start building.**

* * *

**See you di dunia vibe coding! 🚀**
