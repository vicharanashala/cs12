# 🏆 IIT Ropar Internship FAQ Portal — Full Project Prompt

> **IMPORTANT NOTE FOR AI MODEL**: Read this entire document carefully before starting. This is a full-stack web project for IIT Ropar that needs to look extremely premium, modern, and professional. Build every feature listed below. Do NOT skip any section. Use comments on every important line explaining WHY that code is written. The code should be production-quality and visually stunning.

---

## 📋 What This Project Is (Simple Explanation)

This project is a **web-based FAQ and Q&A portal** built specifically for **IIT Ropar's summer internship program**.

Think of it like a **mini StackOverflow + FAQ page + Admin Panel** combined into one beautiful website — designed only for IIT Ropar interns.

**Who uses it?**
- **Students/Interns** — They can ask questions, browse FAQs, answer other students' questions, and earn points
- **Admin/Coordinator** — They can approve or reject student answers, manage student access, add official FAQs, and moderate the whole portal

**Why is it needed?**
- Every year 100+ interns join IIT Ropar and they all have the same questions — "When will my stipend come?", "How do I upload NOC?", "Where is the hostel?", etc.
- Instead of asking the coordinator repeatedly, this portal answers everything automatically using AI + existing FAQ database

---

## 🔧 Tech Stack (What Technologies to Use)

Build the project using these exact technologies:

| Layer | Technology | Why We Use It |
|-------|-----------|---------------|
| **Frontend** | React.js (with Vite) | Fast, modern UI framework — gives instant page loads and smooth interactions |
| **Styling** | Vanilla CSS with CSS Variables | Full control over design — allows glassmorphism, dark mode, gradients, animations |
| **Backend API** | Python Flask | Lightweight and easy — perfect for a small REST API server |
| **Database** | JSON file (database.json) | Simple flat-file storage — no complex database setup needed, easy to demo |
| **AI Chatbot** | Client-side NLP using Jaccard Similarity | Works offline, no API key needed — matches user questions against FAQ database |
| **Icons** | Lucide React | Beautiful, lightweight SVG icon library — looks professional |
| **File Upload** | Multer/Flask file handler | Students upload NOC PDFs directly through the portal |
| **Image Analysis** | Browser Canvas API + AI Vision | Analyze screenshots, handwritten docs, and campus images for smart help |

---

## 🎨 Design System (How It Should Look)

The design must follow a **premium glassmorphism aesthetic**. Here are the exact design rules:

### Color Palette
```
-- Background (Light): #f0f2f5 (soft gray)
-- Background (Dark): #0f172a (deep navy blue)
-- Primary Accent: #d97706 (warm amber/gold — IIT Ropar's signature color)
-- Accent Light: #f59e0b (lighter amber for gradients)
-- Success: #10b981 (green — for approved items)
-- Danger: #ef4444 (red — for errors and rejections)
-- Info Blue: #3b82f6 (blue — for informational badges)
-- Card Background: rgba(255, 255, 255, 0.08) with backdrop-filter: blur(16px)
-- Borders: rgba(255, 255, 255, 0.06) (very subtle)
```

### Typography
```
-- Display Font: 'Outfit' from Google Fonts (for headings — bold and modern)
-- Body Font: 'Inter' from Google Fonts (for text — clean and readable)
-- Use letter-spacing: -0.02em on large headings for a premium feel
```

### Design Effects to Use Everywhere
1. **Glassmorphism** — Cards should have frosted glass effect (background blur + subtle border)
2. **Dark Mode** — Full dark/light theme toggle that remembers your choice
3. **Micro-animations** — Hover effects on cards (lift up slightly), smooth transitions on all interactions
4. **Gradient backgrounds** — Login page has animated gradient (navy → indigo → dark blue that slowly shifts)
5. **Floating elements** — Decorative blurred orbs on login screen that slowly float up and down
6. **Slide-up animations** — Content slides up smoothly when page loads
7. **Accent border on hover** — Cards get a gold left-border when you hover over them

---

## 📄 All Pages & Features (Build All of These)

---

### PAGE 1: Login & Registration Screen

**What it does:** This is the first page users see. They can either log in as a Student or as an Admin (Coordinator).

**Features to build:**

1. **Animated Gradient Background**
   - The entire background slowly shifts colors (navy → indigo → dark blue)
   - Use CSS `@keyframes gradientShift` with `background-size: 400% 400%` for smooth infinite animation
   - Why: Makes the first impression premium and memorable

2. **Floating Decorative Orbs**
   - 2-3 small glowing circles that float up and down in the background
   - Use `filter: blur(80px)` and `animation: float 8s ease-in-out infinite`
   - Why: Adds visual depth — the page feels alive, not static

3. **Frosted Glass Login Card**
   - The login form sits inside a glassmorphic card
   - Use `backdrop-filter: blur(24px)` and `background: rgba(15, 23, 42, 0.85)`
   - Card should have `animation: scaleIn 0.3s` so it pops in when page loads
   - Why: Glassmorphism is the #1 modern UI trend — judges will be impressed

4. **IIT Ropar Branding**
   - Large "R" logo with amber gradient and glow shadow (floating animation)
   - Title: "IIT Ropar Intern Portal"
   - Subtitle: "Secure Internship Management & Peer Q&A Platform"
   - Three small badges: "● Secure", "AI-Powered", "Gamified"
   - Why: Shows this is an institutional-grade product, not a toy project

5. **Role Selection (Student / Coordinator)**
   - Two big clickable cards: "🎓 Student Login" and "🔐 Coordinator Login"
   - Each card has hover effect (lifts up, border glows amber)
   - Why: Clean separation of roles from the very start

6. **Student Login Flow**
   - Dropdown to select your name from the list of registered students
   - Shows your NOC status (Approved ✅ / Pending ⏳ / Rejected ❌)
   - If NOC is not approved → login is BLOCKED with a clear message
   - "Switch to Sign Up" link to register as a new student
   - Why: Security — only approved students can access the portal

7. **Student Sign Up Flow**
   - Form fields: Full Name, Roll Number, Branch (dropdown), NOC PDF Upload
   - File upload shows progress bar and accepts only PDF ≤ 2MB
   - On submit → sends data to Flask backend → student appears with "Pending" status
   - Why: New interns can self-register and upload their NOC for approval

8. **Admin/Coordinator Login**
   - Username + PIN input (default: admin / 1234)
   - Error shake animation if wrong credentials
   - Why: Only the internship coordinator should access admin features

---

### PAGE 2: FAQ Hub (Landing Page — First Page After Login)

**What it does:** This is the MAIN landing page. It shows all official Frequently Asked Questions organized by category. This is the first thing users see after logging in.

**Features to build:**

1. **Hero Banner**
   - Dark gradient banner (navy → indigo → dark blue) at the very top
   - Title: "📚 IIT Ropar Knowledge Base" in big white text
   - Subtitle explaining what the page does
   - Radial glow effect in top-right corner using CSS `::before` pseudo-element
   - Why: Hero banners are what professional SaaS products use — sets the tone immediately

2. **Live Stats Counter Row (inside Hero Banner)**
   - Three frosted glass stat cards in a row:
     - "8" → Official FAQs (auto-counts from database)
     - "4" → Categories (auto-counts from database)
     - "24/7" → AI Available (green color)
   - Each stat card has: big bold number, small uppercase label below
   - Hover effect: card lifts up, border glows amber
   - Why: Shows the portal is data-rich and active — looks professional

3. **Smart Search Bar with Autocomplete**
   - Full-width search input with magnifying glass icon
   - As user types → show dropdown of matching FAQ questions (real-time filtering)
   - Clear button (✕) appears when search has text
   - Shows "Found X matching FAQs for 'query'" count below
   - Why: Users can instantly find answers without scrolling through everything

4. **Visual Category Cards Grid**
   - 5 colorful category cards in a responsive grid (2 columns on mobile, 5 on desktop):
     - 🔖 All (purple gradient icon)
     - 📄 NOC Upload (yellow/amber gradient icon)
     - 💰 Stipend Details (green gradient icon)
     - 🏠 Accommodation (blue gradient icon)
     - 🏫 General & Campus (purple gradient icon)
   - Each card shows: icon, category name, and count of FAQs in that category
   - Click a card → filters the FAQ list to that category
   - Active card has amber border and subtle glow
   - Why: Visual categories are much more engaging than plain text filters

5. **FAQ Accordion List**
   - Each FAQ is a collapsible card (click to expand/collapse)
   - Shows: category badge (color-coded), question text, expand arrow
   - When expanded: shows the full answer with smooth slide-down animation
   - Tags shown as small pills (e.g., "stipend", "payment", "dates")
   - Why: Accordion pattern keeps the page clean — users see only what they need

6. **Admin: Add New FAQ Button**
   - Only visible when admin is logged in
   - Opens a form to add new official FAQ (question, answer, category, tags)
   - Why: Admin can keep the knowledge base up to date

7. **AI-Powered Instant Answer Sandbox (Sidebar)**
   - A panel on the right side where you can type any question
   - AI instantly searches FAQs + approved Q&A answers and returns the best match
   - Shows match confidence percentage
   - Why: This is the "wow factor" — instant AI answers without leaving the FAQ page

---

### PAGE 3: Q&A Feed (Community Questions)

**What it does:** Students can ask new questions and other students can answer them. Like a mini StackOverflow for IIT Ropar interns.

**Features to build:**

1. **Ask a New Question Form**
   - Title input, detailed description textarea
   - Category dropdown (NOC, Stipend, Accommodation, General)
   - Tag selector (students can add relevant tags)
   - **AI Duplicate Checker** — Before posting, AI scans existing FAQs and warns if a similar question already exists with match confidence %
   - **AI Tag Recommender** — AI automatically suggests relevant tags based on the question text
   - Why: Prevents duplicate questions and keeps the feed organized

2. **Question Feed Cards**
   - Each question shows: title, description preview, category badge, tags, author name, date
   - Vote buttons (upvote/downvote) with live counter
   - Answer count badge
   - Status indicator: "Open" (orange), "Answered" (green), "Official FAQ" (gold)
   - Hover: amber left-border slides in
   - Why: Looks like a professional Q&A platform

3. **Answer Thread (Expandable)**
   - Click a question → expands to show all answers
   - Each answer shows: author name, answer text, vote count, admin approval status
   - **Admin-only "Approve" button** — Only admin can approve an answer
   - Once approved → the answer author gets karma points
   - Why: Quality control — only verified answers get rewarded

4. **Featured FAQs Sidebar Widget**
   - Right sidebar shows top 3-5 most relevant FAQs
   - Each FAQ is expandable (click to read the answer inline)
   - Why: Students might find their answer here without even asking

5. **Sort & Filter Controls**
   - Sort by: Newest, Most Votes, Unanswered
   - Filter by: Category, Status
   - Why: Easy navigation when there are many questions

---

### PAGE 4: Solve & Earn (Gamification Portal)

**What it does:** Shows unanswered questions that students can solve to earn karma points. This motivates peer-to-peer helping.

**Features to build:**

1. **Unanswered Question Cards**
   - Shows only questions that have 0 approved answers
   - Each card has: question text, category, time posted, "Answer Now" button
   - Why: Focused view for students who want to help and earn points

2. **Answer Submission**
   - Rich text area to write your answer
   - Submit button sends the answer for admin review
   - Why: Answers need to be verified before rewarding points

3. **Points System Display**
   - Shows your current karma points
   - Shows how many answers you've submitted
   - Shows how many were approved
   - Points breakdown: 10 points per approved answer
   - Why: Gamification motivates students to help each other

4. **Leaderboard Preview**
   - Top 3 students by karma points shown as a mini leaderboard
   - Why: Healthy competition drives engagement

---

### PAGE 5: Dashboard (Student Profile / Admin Panel)

**What it does:** Personal profile page for students. For admins, it's the full admin control panel.

#### Student Dashboard Features:
1. **Profile Card** — Name, roll number, branch, avatar with initials
2. **NOC Status Tracker** — Shows current NOC approval status with visual progress (Pending → Under Review → Approved)
3. **Activity Stats** — Questions asked, answers given, points earned
4. **My Questions History** — List of all questions the student has asked
5. **My Answers History** — List of all answers with approval status

#### Admin Dashboard Features:
1. **Moderation Queue** — All pending answers waiting for admin approval
   - Each item shows: question, answer preview, student name
   - Approve (✅) or Reject (❌) buttons
   - When approved → student earns karma points automatically
   - Why: Quality control by the coordinator

2. **Student Directory & Access Manager**
   - Table of all registered students
   - Columns: Name, Roll Number, Branch, NOC Status, Karma Points
   - Admin can Approve/Reject NOC → controls who can log in
   - Why: Coordinator has full control over student access

3. **FAQ Manager**
   - Add, edit, or delete official FAQs
   - Category assignment
   - Why: Keep the knowledge base current

4. **Platform Analytics (Charts)**
   - Total questions, total answers, approval rate
   - Questions per category (bar chart)
   - Activity timeline
   - Why: Admin can see how the portal is being used

---

### FLOATING COMPONENT: AI Chatbot Assistant

**What it does:** A floating chat bubble (bottom-right corner) that opens an AI-powered chat window. Students can ask any question and get instant answers from the FAQ database.

**Features to build:**

1. **Floating Trigger Button**
   - Round amber button with sparkle icon (✨) in bottom-right corner
   - Gentle pulsing animation to attract attention
   - Unread message badge (shows "1" when chatbot has a greeting ready)
   - Why: Always accessible from any page

2. **Chat Window (Popup)**
   - Opens above the trigger button
   - Header bar with "IIT Ropar AI Assistant" title and close button
   - Chat messages area with scrolling
   - Message input with send button
   - Why: Familiar chat interface everyone knows how to use

3. **AI Response Logic**
   - Takes user's question
   - Runs Jaccard similarity matching against all FAQs + approved Q&A answers
   - Returns the best matching answer with confidence percentage
   - If confidence < 30% → says "I'm not sure, try asking in the Q&A Feed"
   - Typing indicator animation (3 bouncing dots) while "thinking"
   - Why: Instant answers 24/7 without waiting for humans

4. **Message Styling**
   - User messages: right-aligned, amber background
   - Bot messages: left-aligned, dark glass background
   - Timestamps on each message
   - Smooth scroll to bottom on new messages
   - Why: Professional chat UI like real messaging apps

---

## 🆕 NEW FEATURES TO ADD (These Will Win You First Rank)

These are **extra features** that go beyond the basics and will impress the judges:

---

### FEATURE 1: 📸 Image Analysis (Smart Image Upload)

**What it does:** Students can upload screenshots or photos of handwritten problems, NOC documents, or campus-related images, and the AI analyzes them to provide help.

**How to build it:**

1. **Image Upload Button in Chat & Q&A**
   - Add a camera/image icon button (📎) next to the message input in the AI chatbot
   - Also add it in the "Ask a Question" form in Q&A Feed
   - Accept: JPG, PNG, WEBP (max 5MB)
   - Why: Students often have screenshots of errors or photos of documents

2. **Client-Side Image Analysis Using Canvas API**
   ```
   Step 1: User uploads image
   Step 2: Display image preview with thumbnail
   Step 3: Use Canvas API to extract basic color/dimension info
   Step 4: Use OCR (Tesseract.js — client-side library) to read any text in the image
   Step 5: Take the extracted text and run it through our existing FAQ similarity matcher
   Step 6: Return matching FAQs based on text found in the image
   ```
   - Why: This is a cutting-edge feature — most student portals don't have image understanding

3. **Smart Document Scanner for NOC**
   - When student uploads NOC PDF/image, auto-detect:
     - Is it signed? (look for ink marks/stamps)
     - Is it the correct template? (match expected text patterns)
     - Is it readable? (check image quality/resolution)
   - Show feedback: "✅ Document looks valid" or "⚠️ Signature area appears blank"
   - Why: Reduces back-and-forth between student and coordinator

4. **Screenshot Problem Solver**
   - Student uploads a screenshot of an error or a campus map
   - OCR extracts text from the screenshot
   - AI matches the extracted text against FAQs
   - Returns: "Based on your screenshot, this FAQ might help: [matching FAQ]"
   - Why: Students can literally photograph their problem and get answers

5. **Image Gallery in Questions**
   - Questions in Q&A Feed can include attached images
   - Images shown as clickable thumbnails that open in a lightbox (full-screen overlay)
   - Why: Some questions are easier to explain with images

---

### FEATURE 2: 🔔 Smart Notification System

**What it does:** Real-time notifications so students know when something important happens.

**How to build it:**
1. **Notification Bell Icon** in the navbar with unread count badge
2. **Notification Dropdown Panel** — click bell → see recent notifications
3. **Notification Types:**
   - "Your NOC has been approved ✅" (when admin approves)
   - "Your answer was approved! +10 points 🎉" (when admin approves answer)
   - "Someone answered your question 💬" (when you get a reply)
   - "New official FAQ added 📚" (when admin adds FAQ)
4. **Store in localStorage** — persist notifications across sessions
5. **Mark as Read** — click to mark individual notifications as read
6. **"Clear All" button** — dismiss all notifications at once
- Why: Users always know what's happening without constantly checking every page

---

### FEATURE 3: 📊 Analytics Dashboard with Charts

**What it does:** Visual charts and statistics for the admin to understand portal usage.

**How to build it:**
1. Use a lightweight chart library (Chart.js or Recharts)
2. **Charts to include:**
   - 📊 Bar chart: Questions per category
   - 🍩 Donut chart: NOC status distribution (Approved/Pending/Rejected)
   - 📈 Line chart: Questions posted over time (by week)
   - 🏆 Leaderboard bar chart: Top 5 students by karma points
3. **Summary Cards at Top:**
   - Total Students | Total Questions | Total Answers | Approval Rate %
   - Each card has an icon, number, and trend indicator (↑ or ↓)
- Why: Data visualization makes the admin panel look enterprise-grade

---

### FEATURE 4: 📱 Progressive Web App (PWA) Support

**What it does:** The website can be "installed" on phones like a native app.

**How to build it:**
1. Add a `manifest.json` file with app name, icons, and theme colors
2. Add a service worker for basic offline caching
3. Add a meta tag: `<meta name="theme-color" content="#0f172a">`
4. The browser will show "Add to Home Screen" prompt on mobile
- Why: Students can access the portal from their phone home screen without opening a browser — feels like a real app

---

### FEATURE 5: 🌐 Multi-language Support (Hindi + English)

**What it does:** Toggle between English and Hindi for the entire UI.

**How to build it:**
1. Create a `translations.js` file with all UI text in both languages
2. Add a language toggle button (🇮🇳 / 🇬🇧) in the navbar
3. All UI labels, buttons, and placeholder text switch dynamically
4. FAQs stay in English (official content)
- Why: Many IIT interns are more comfortable in Hindi — this shows inclusivity

---

### FEATURE 6: 🔍 Advanced Search with Filters & Highlights

**What it does:** Power-user search that highlights matching keywords and filters results in real-time.

**How to build it:**
1. **Keyword Highlighting** — When searching, the matching words in results are highlighted in amber/yellow
2. **Multi-filter Search** — Search across: FAQs, Q&A questions, Q&A answers simultaneously
3. **Search History** — Show recent searches as quick-access chips below the search bar
4. **Voice Search** (bonus) — Use Web Speech API for voice input on the search bar
- Why: Makes finding information incredibly fast and impressive

---

### FEATURE 7: 📋 Document Vault (Download Center)

**What it does:** A centralized place where students can download important templates and documents.

**How to build it:**
1. Add a new tab/section: "📋 Document Vault"
2. List of downloadable files:
   - NOC Template (PDF)
   - Stipend Application Form
   - Hostel Allotment Form
   - Internship Completion Certificate Template
   - Campus Map (Image)
3. Each file card shows: file name, file type icon, size, download button
4. Admin can upload new documents
- Why: Students always ask "where is the NOC form?" — this solves it permanently

---

### FEATURE 8: ⏱️ Real-Time Activity Feed

**What it does:** A live feed showing recent portal activity (like a social media timeline).

**How to build it:**
1. Show recent events in a timeline format:
   - "Priya asked a question about stipend — 2 min ago"
   - "Admin approved Rohit's answer — 5 min ago"
   - "New FAQ added: Hostel mess timings — 1 hour ago"
2. Auto-refresh every 30 seconds
3. Show as a sidebar widget or on the Dashboard
- Why: Makes the portal feel alive and active

---

### FEATURE 9: 🎯 Quick Actions Panel

**What it does:** A floating quick-action menu for common tasks.

**How to build it:**
1. A "+" floating action button (bottom-right, above the chatbot)
2. When clicked, expands to show:
   - 📝 Ask a Question
   - 📄 Upload NOC
   - 🔍 Search FAQs
   - 💬 Open Chatbot
3. Smooth radial animation on expand
- Why: One-click access to the most common actions from any page

---

### FEATURE 10: 🏅 Achievement Badges System

**What it does:** Students earn badges for milestones — displayed on their profile.

**Badge list:**
- 🌟 "First Steps" — Asked your first question
- 💡 "Helper" — Got your first answer approved
- 🔥 "On Fire" — 5 answers approved
- 🏆 "Top Contributor" — Most karma points in a week
- 📚 "Knowledge Seeker" — Viewed 20+ FAQs
- 🤖 "AI Explorer" — Used the AI chatbot 10+ times

**How to build:**
1. Track user actions in the user profile object
2. Check badge conditions on each action
3. Show earned badges on the Dashboard profile card
4. Show a toast notification when a new badge is earned: "🏅 You earned the 'Helper' badge!"
- Why: Gamification keeps students engaged and coming back

---

## 🗂️ Project File Structure

Build the project with this exact file structure:

```
IIT-ROPAR-FAQ-PORTAL/
├── public/
│   └── index.html              -- Main HTML file with meta tags and Google Fonts
├── src/
│   ├── main.jsx                -- React entry point — renders App into the DOM
│   ├── App.jsx                 -- Main app component — handles routing, auth, theme
│   ├── App.css                 -- Extra app-specific styles
│   ├── index.css               -- FULL design system — all CSS variables, animations, component styles
│   ├── mockData.js             -- Seed data for FAQs, questions, users (used as fallback)
│   ├── translations.js         -- Hindi/English translation strings [NEW]
│   ├── components/
│   │   ├── Login.jsx           -- Login & Registration screen with animated background
│   │   ├── FAQHub.jsx          -- FAQ landing page with hero banner, categories, accordion
│   │   ├── AskFeed.jsx         -- Q&A Feed — ask questions, view answers, vote
│   │   ├── SolvePortal.jsx     -- Solve & Earn — gamified answer portal
│   │   ├── Dashboard.jsx       -- Student profile + Admin panel
│   │   ├── AIChatbot.jsx       -- Floating AI chatbot assistant
│   │   ├── ImageAnalyzer.jsx   -- Image upload & OCR analysis component [NEW]
│   │   ├── DocumentVault.jsx   -- Download center for templates [NEW]
│   │   ├── Notifications.jsx   -- Notification bell & dropdown [NEW]
│   │   └── Achievements.jsx    -- Badge system component [NEW]
│   ├── hooks/
│   │   └── useLocalStorage.js  -- Custom React hook for persistent state in localStorage
│   └── services/
│       ├── aiService.js        -- AI similarity matching, tag recommendation, duplicate checking
│       └── imageService.js     -- Image analysis & OCR service [NEW]
├── app.py                      -- Python Flask backend API server
├── database.json               -- JSON flat-file database (auto-created by Flask)
├── uploads/                    -- Uploaded NOC PDFs stored here
├── package.json                -- Node.js dependencies
├── vite.config.js              -- Vite build configuration with Flask proxy
└── requirements.txt            -- Python dependencies (flask, flask-cors)
```

---

## 🔌 Backend API Endpoints (Flask)

The Python Flask backend should serve these REST API endpoints:

| Method | Endpoint | What It Does |
|--------|----------|-------------|
| GET | `/api/faqs` | Returns all FAQ entries from database |
| POST | `/api/faqs` | Adds a new FAQ (admin only) |
| PUT | `/api/faqs/<id>` | Updates an existing FAQ |
| DELETE | `/api/faqs/<id>` | Deletes a FAQ |
| GET | `/api/questions` | Returns all Q&A questions |
| POST | `/api/questions` | Creates a new question |
| PUT | `/api/questions/<id>` | Updates a question (add answer, vote, approve) |
| GET | `/api/users` | Returns all registered users |
| POST | `/api/users` | Registers a new student |
| PUT | `/api/users/<id>` | Updates user profile (NOC status, points) |
| POST | `/api/upload` | Handles NOC PDF file upload |
| GET | `/api/analytics` | Returns portal statistics for admin dashboard [NEW] |
| POST | `/api/analyze-image` | Accepts image, returns OCR text extraction [NEW] |
| GET | `/api/documents` | Returns list of downloadable documents [NEW] |
| POST | `/api/notifications` | Creates a new notification [NEW] |
| GET | `/api/notifications/<userId>` | Returns notifications for a user [NEW] |

---

## 💬 Code Comments Guide

**Add comments on every important line.** Here's how to write good comments:

```javascript
// ✅ GOOD COMMENT — explains WHY
const [theme, setTheme] = useLocalStorage('iitrpr_theme', 'light');
// We persist theme in localStorage so user's dark/light mode choice 
// survives page refreshes and browser restarts

// ❌ BAD COMMENT — just restates the code
const [theme, setTheme] = useLocalStorage('iitrpr_theme', 'light');
// set theme to light
```

**Comment style guide:**
- At the top of every file: explain what the file does and why it exists
- Before every function: explain what it does and when it's called
- Before complex logic: explain the approach and why this method was chosen
- Before CSS sections: explain what visual effect this creates
- Before API calls: explain what data is being fetched and why

---

## 🎯 Priority Order for Building

Build features in this order for maximum impact:

1. **Design System (CSS)** — Set up all CSS variables, animations, glassmorphism first
2. **Login Page** — First impression matters most
3. **FAQ Hub** — The main landing page with hero banner and categories
4. **AI Chatbot** — The "wow factor" feature
5. **Q&A Feed** — Core community feature
6. **Image Analysis** — Cutting-edge feature judges will love
7. **Dashboard + Admin Panel** — Full admin control
8. **Notification System** — Professional polish
9. **Achievement Badges** — Engagement boost
10. **Document Vault** — Practical utility
11. **Analytics Charts** — Enterprise-grade admin panel
12. **PWA Support** — Mobile installation
13. **Multi-language** — Bonus inclusivity feature

---

## ✅ Quality Checklist (Make Sure All of These Are Done)

- [ ] Dark mode + Light mode toggle that remembers choice
- [ ] All animations are smooth (no janky transitions)
- [ ] Mobile responsive (works on phone screens)
- [ ] Login is secured (only approved NOC students can enter)
- [ ] Admin can approve/reject answers and student access
- [ ] AI chatbot gives relevant answers with confidence %
- [ ] Image upload works in chatbot and Q&A feed
- [ ] OCR reads text from uploaded images
- [ ] All FAQ categories have gradient icons
- [ ] Hero banner has animated stats counters
- [ ] Search has autocomplete suggestions
- [ ] Notifications work for key actions
- [ ] Achievement badges display on profile
- [ ] Every important code line has a comment
- [ ] File structure matches the structure shown above
- [ ] Flask backend handles all API endpoints
- [ ] No console errors in the browser
- [ ] Code is clean and well-organized

---

## 🚀 How to Run the Project

### Frontend (React + Vite)
```bash
npm install          # Install all JavaScript dependencies
npm run dev          # Start the frontend development server on http://localhost:5173
```

### Backend (Python Flask)
```bash
pip install flask flask-cors    # Install Python dependencies
python3 app.py                  # Start the Flask API server on http://localhost:5001
```

### Both Together
Run both in separate terminal tabs. The Vite config proxies API calls from frontend to Flask backend automatically.

---

> **FINAL NOTE**: This project should look and feel like a REAL product that IIT Ropar would actually deploy. Not a simple homework submission — a production-quality portal. Every pixel matters. Every animation should be intentional. Every feature should solve a real student problem. Build it like your career depends on it. 🏆
