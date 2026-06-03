# 🗺️ Step-by-Step Roadmap — Build IIT Ropar FAQ Portal with MinMax 2.7

> **How to use this file:**
> - Follow steps 1 to 12 **in order** (don't skip steps)
> - Each step has a **prompt** inside a box — copy that prompt and paste it into MinMax 2.7
> - Wait for MinMax to finish each step before moving to the next
> - If MinMax gives an error, just tell it: "fix the error and try again"
> - Each step builds on top of the previous one

---

## 📌 Before You Start

Make sure you have these installed on your Mac:
- **Node.js** (version 18+) → check with: `node --version`
- **Python 3** → check with: `python3 --version`
- **npm** → comes with Node.js

If you don't have Node.js, go to https://nodejs.org and install the LTS version.

---

## STEP 1: Create the Project from Scratch

> Copy-paste this prompt into MinMax 2.7:

```
Create a new full-stack web project for an "IIT Ropar Internship FAQ Portal" from scratch.

TECH STACK:
- Frontend: React.js with Vite (use: npx create-vite@latest ./ --template react)
- Styling: Vanilla CSS (no Tailwind)
- Backend: Python Flask API
- Database: JSON file (database.json)
- Icons: lucide-react package

PROJECT STRUCTURE:
Create these folders and files:
- src/components/ (empty for now)
- src/hooks/useLocalStorage.js (custom hook to save state in browser localStorage)
- src/services/ (empty for now)
- src/mockData.js (seed data)
- src/index.css (design system)
- app.py (Flask backend)
- requirements.txt (flask, flask-cors)
- vite.config.js (proxy /api to Flask on port 5001)

MOCK DATA (in mockData.js):
Create sample data for:
- 8 FAQs about IIT Ropar internships (categories: NOC Upload, Stipend Details, Accommodation, General & Campus)
- 3 sample questions from students
- 4 sample users (3 students + 1 admin named "Coordinator")

FLASK BACKEND (app.py):
- Run on port 5001
- Store data in database.json
- Endpoints: GET/POST /api/faqs, GET/POST/PUT /api/questions, GET/POST/PUT /api/users, POST /api/upload (for NOC PDF)
- On first run, seed database.json with the initial data
- Enable CORS

Add comments on every important line explaining WHY it's written.

Install dependencies: npm install lucide-react

Run instructions:
- Terminal 1: npm run dev
- Terminal 2: python3 app.py
```

**What this does:** Creates the entire project skeleton with working backend + frontend.

---

## STEP 2: Build the Premium Design System (CSS)

> Copy-paste this prompt:

```
Now create a premium, modern design system in src/index.css for our IIT Ropar portal.

DESIGN REQUIREMENTS:
- Import Google Fonts: 'Outfit' (for headings) and 'Inter' (for body text)
- Use CSS custom properties (variables) for ALL colors, spacing, borders, shadows
- Support BOTH light mode and dark mode (use .dark-theme class)

COLOR PALETTE:
- Light background: #f0f2f5
- Dark background: #0f172a (deep navy)
- Primary accent: #d97706 (warm amber — IIT Ropar's color)
- Accent light: #f59e0b
- Success: #10b981 (green)
- Danger: #ef4444 (red)
- Cards: use glassmorphism (rgba backgrounds + backdrop-filter: blur)

COMPONENTS TO STYLE:
1. .navbar — sticky top navigation bar with glass effect
2. .glass-card — frosted glass card with subtle border and shadow
3. .btn, .btn-primary, .btn-secondary — button styles with hover effects
4. .form-control — input/textarea with focus glow effect
5. .avatar — circular user avatar with gradient background
6. .badge — small colored badges for categories and status
7. .tag-filters — horizontal scrollable filter buttons
8. .footer — simple footer

ANIMATIONS TO ADD:
- @keyframes gradientShift — slowly shifts background gradient colors (12 second loop)
- @keyframes float — gentle up/down floating motion for decorative elements
- @keyframes slideUp — content slides up on page load
- @keyframes scaleIn — content scales in on page load
- @keyframes pulse — gentle pulsing glow effect
- All hover transitions should be smooth (0.2s ease)
- Cards should lift up slightly on hover (translateY -3px)

RESPONSIVE:
- Mobile-friendly at 600px breakpoint
- Cards stack vertically on mobile
- Navigation wraps on small screens

Add a comment above every CSS section explaining what visual effect it creates.
Make this look like a premium SaaS product, NOT a basic student project.
```

**What this does:** Creates the entire visual design — colors, animations, glass effects, dark mode.

---

## STEP 3: Build the Login & Registration Page

> Copy-paste this prompt:

```
Create src/components/Login.jsx — the login and registration page for our portal.

VISUAL DESIGN:
- Full-screen animated gradient background (navy → indigo → dark blue, slowly shifting)
- 2-3 floating decorative blurred orbs that gently move up and down
- Centered frosted glass card with blur effect and scale-in animation
- Large "R" logo at top with amber gradient, glow shadow, and floating animation
- Title: "IIT Ropar Intern Portal"
- Subtitle: "Secure Internship Management & Peer Q&A Platform"
- Three small colored badges below: "● Secure" (green), "AI-Powered" (blue), "Gamified" (amber)

FUNCTIONALITY:

Step 1 — Role Selection:
- Two clickable cards: "🎓 Student Login" and "🔐 Coordinator Login"
- Each card lifts up on hover with amber border glow
- Back button to return to role selection

Step 2a — Student Login:
- Dropdown to select from registered students (fetched from /api/users)
- Shows NOC status next to name: Approved ✅, Pending ⏳, Rejected ❌
- If NOC not approved → block login with warning message
- "New here? Sign Up" link to switch to signup form

Step 2b — Student Sign Up:
- Form: Full Name, Roll Number, Branch (dropdown with CSE, ECE, ME, etc.), NOC PDF Upload
- File upload accepts only PDF, max 2MB, shows file name after selection
- On submit → POST to /api/users → shows success message
- "Already registered? Log In" link to switch back

Step 2c — Coordinator Login:
- Username + PIN fields (correct: admin / 1234)
- Wrong credentials → show error with shake animation

Props: { users, onLogin(role, user), onRefresh() }

Add comments explaining WHY each feature exists (not just what it does).
```

**What this does:** Creates the stunning login page — first thing anyone sees.

---

## STEP 4: Build the Main App Shell (Navigation + Routing)

> Copy-paste this prompt:

```
Create src/App.jsx — the main application shell with navigation and page routing.

FEATURES:
1. State management using useLocalStorage hook for: currentUser, activeTab, theme, isLoggedIn, userRole
2. Fetch data from Flask API on mount: /api/faqs, /api/questions, /api/users
3. If not logged in → show Login component
4. If logged in → show the full app with navbar

NAVBAR:
- Sticky top with glass effect
- Left: "R" logo + "IIT ROPAR" title + role badge (COORDINATOR PORTAL or INTERN PORTAL)
- Center: 4 navigation tabs:
  - 📖 FAQ Hub (default landing page)
  - ❓ Q&A Feed
  - 🏆 Solve & Earn
  - 👤 Dashboard (shows "Admin Board" for coordinators)
- Right: User avatar pill (initial + name + karma points), Dark/Light toggle button, Logout button

THEME:
- Toggle between light and dark mode
- Persists choice in localStorage

FOOTER:
- "© 2026 Indian Institute of Technology Ropar. Internship & Training Placement cell."

Show each tab's component based on activeTab state.
Add comments on important lines explaining the purpose.
```

**What this does:** Creates the app's navigation bar, theme toggle, and page routing.

---

## STEP 5: Build the FAQ Hub (Landing Page)

> Copy-paste this prompt:

```
Create src/components/FAQHub.jsx — the main FAQ landing page (first page users see after login).

SECTIONS (top to bottom):

1. HERO BANNER:
   - Dark gradient background (navy → indigo → dark blue)
   - Title: "📚 IIT Ropar Knowledge Base" (large white text)
   - Subtitle describing the portal
   - Radial glow effect in corner using CSS pseudo-element
   - Slide-up entrance animation

2. LIVE STATS ROW (inside hero banner):
   - 3 frosted glass stat cards in a row:
     - Total FAQ count (auto-calculated from data)
     - Category count (auto-calculated)
     - "24/7" AI Available (green color)
   - Each has: big bold number + small uppercase label
   - Hover: lifts up slightly

3. SEARCH BAR:
   - Full-width search input with magnifying glass icon
   - Real-time autocomplete dropdown as user types
   - Shows matching FAQ questions in dropdown
   - Clear button (✕) when search has text
   - Shows "Found X matching FAQs" count

4. CATEGORY CARDS GRID:
   - 5 visual cards in responsive grid:
     - 🔖 All (purple gradient)
     - 📄 NOC Upload (yellow gradient)
     - 💰 Stipend Details (green gradient)
     - 🏠 Accommodation (blue gradient)
     - 🏫 General & Campus (purple gradient)
   - Each shows: gradient icon, name, FAQ count
   - Click → filters FAQs to that category
   - Active card has amber border + glow

5. FAQ ACCORDION LIST:
   - Collapsible cards — click to expand/collapse
   - Shows: category badge (color-coded), question text, arrow icon
   - Expanded: full answer + tags as small pills
   - Smooth slide animation on expand/collapse

6. AI ANSWER SANDBOX (sidebar on right):
   - Text input where user types any question
   - Instantly searches FAQs using similarity matching
   - Shows best match with confidence percentage
   - Only visible on desktop (hidden on mobile)

7. ADMIN ONLY — "Add New FAQ" button that opens a form

Props: { faqs, setFaqs, isAdmin }
Add comments explaining WHY each section exists.
```

**What this does:** Creates the beautiful landing page with hero banner, live stats, and category cards.

---

## STEP 6: Build the Q&A Feed (Community Questions)

> Copy-paste this prompt:

```
Create src/components/AskFeed.jsx — the community Q&A feed where students ask and answer questions.

LAYOUT: Two-column (main feed on left, sidebar on right)

LEFT SIDE — MAIN FEED:

1. ASK A QUESTION FORM (collapsible):
   - Title input + description textarea
   - Category dropdown (NOC Upload, Stipend Details, Accommodation, General & Campus)
   - Tag selector
   - AI Duplicate Checker: before posting, check if similar FAQ exists using similarity matching, warn user with match %
   - AI Tag Recommender: auto-suggest tags based on question text
   - Submit button → POST to /api/questions

2. SORT & FILTER BAR:
   - Sort: Newest, Most Votes, Unanswered
   - Filter by category

3. QUESTION CARDS:
   - Each card shows: title, description preview, category badge, tags, author name, date
   - Vote buttons (upvote ▲ / downvote ▼) with count
   - Answer count badge
   - Status: "Open" (orange), "Answered" (green)
   - Amber left border appears on hover
   - Click → expands to show answer thread

4. ANSWER THREAD (inside expanded question):
   - All answers listed with: author, text, votes, approval badge
   - "Write Answer" textarea + submit button
   - ADMIN ONLY: "✅ Approve" button on each answer
   - When approved → answer author gets +10 karma points

RIGHT SIDEBAR:
- "Featured FAQs" widget showing top 3-5 FAQs
- Each FAQ expandable to read answer inline

Props: { questions, setQuestions, faqs, setFaqs, currentUser, setCurrentUser, users, setUsers, isAdmin }
Add comments on every important function explaining the logic.

Also create src/services/aiService.js with these functions:
- getSimilarityScore(str1, str2) — Jaccard similarity (word overlap)
- checkDuplicateFAQs(title, description, faqs) — returns similar FAQs above threshold
- recommendTags(title, description) — auto-suggest tags based on keywords
- getChatbotReply(message, faqs, questions) — find best matching answer for chatbot
Add detailed comments explaining the algorithm.
```

**What this does:** Creates the StackOverflow-like Q&A system with AI-powered duplicate detection.

---

## STEP 7: Build the AI Chatbot

> Copy-paste this prompt:

```
Create src/components/AIChatbot.jsx — a floating AI chatbot assistant visible on every page.

TRIGGER BUTTON:
- Round amber button in bottom-right corner of screen
- Sparkle icon (✨)
- Gentle pulsing glow animation
- Unread badge showing "1" initially (greeting message ready)
- Click → opens chat window above it

CHAT WINDOW:
- Fixed position popup (400px wide, 500px tall)
- Header: "🤖 IIT Ropar AI Assistant" + close button
- Message area with scrolling
- Input bar at bottom with text input + send button + image upload button (📎)

MESSAGE TYPES:
- User messages: right-aligned, amber background, rounded corners
- Bot messages: left-aligned, dark glass background, rounded corners
- Each message shows timestamp

AI LOGIC:
- On send → show typing indicator (3 bouncing dots animation)
- Wait 1 second (simulated thinking time)
- Use getChatbotReply() from aiService.js
- Match user's question against all FAQs + approved Q&A answers
- If match confidence > 50% → show the answer with "Match: X%"
- If confidence 30-50% → show answer but say "I'm not fully sure, here's what I found..."
- If confidence < 30% → say "I couldn't find a match. Try asking in the Q&A Feed!"

GREETING:
- On first open, show: "Hi! 👋 I'm the IIT Ropar AI Assistant. Ask me anything about your internship — NOC, stipend, hostel, or campus facilities!"

SPECIAL COMMANDS:
- If user types "help" → show list of things they can ask about
- If user types "faq" → show top 3 FAQs

Props: { faqs, questions }
Add comments explaining the chatbot flow and why each part exists.
```

**What this does:** Creates the floating AI chatbot — the biggest "wow factor" of the project.

---

## STEP 8: Build Image Analysis Feature

> Copy-paste this prompt:

```
Add image analysis capability to the project. This is a PREMIUM feature.

PART 1 — Create src/services/imageService.js:

Functions to build:
1. extractTextFromImage(imageFile):
   - Use Tesseract.js library (npm install tesseract.js) for OCR
   - Takes an uploaded image file
   - Returns extracted text from the image
   - Add progress callback for loading indicator
   - Comment: "OCR reads any text in uploaded photos — students can photograph problems"

2. analyzeImageContent(imageFile):
   - Get image dimensions and basic info using Canvas API
   - Run OCR to extract text
   - Run extracted text through FAQ similarity matcher
   - Return: { extractedText, matchingFaqs, imageInfo }
   - Comment: "Combines OCR + AI matching — upload a screenshot, get instant FAQ answers"

3. validateNOCDocument(imageFile):
   - Extract text using OCR
   - Check if text contains expected NOC keywords ("No Objection", "Dean", "signature", "seal")
   - Check image dimensions (should be A4 ratio roughly)
   - Return: { isValid, issues[], confidence }
   - Comment: "Auto-checks if NOC document looks correct before admin reviews it"

PART 2 — Create src/components/ImageAnalyzer.jsx:
- A reusable component with drag-and-drop image upload zone
- Accepts: JPG, PNG, WEBP (max 5MB)
- Shows image preview after upload
- Shows loading spinner during OCR processing
- Displays extracted text in a box
- Shows matching FAQs based on the text found
- If it's a NOC → shows validation results

PART 3 — Add image upload to AIChatbot:
- Add 📎 button next to chat input
- User can upload image in chat
- Bot shows: "Analyzing your image..." with spinner
- Then shows: extracted text + matching FAQs
- Comment: "Students can literally photograph their problem and get AI help"

PART 4 — Add image attachment to Q&A Feed:
- In the "Ask a Question" form, add image attachment option
- Attached images show as thumbnails in the question card
- Click thumbnail → opens full-size in a lightbox overlay

Install: npm install tesseract.js
Add comments explaining WHY image analysis is useful for students.
```

**What this does:** Adds cutting-edge image analysis — students can upload photos and get AI answers.

---

## STEP 9: Build the Dashboard & Admin Panel

> Copy-paste this prompt:

```
Create src/components/Dashboard.jsx — profile page for students, full admin panel for coordinators.

IF USER IS STUDENT — Show:

1. PROFILE CARD:
   - Large avatar with gradient (shows first letter of name)
   - Name, Roll Number, Branch
   - Karma points with star icon
   - NOC status badge (Approved/Pending/Rejected)
   - Member since date

2. ACTIVITY STATS ROW:
   - 4 stat cards: Questions Asked, Answers Given, Answers Approved, Karma Points
   - Each with icon and number

3. ACHIEVEMENT BADGES:
   - Show earned badges as colored circles with icons:
     - 🌟 "First Steps" — asked first question
     - 💡 "Helper" — first answer approved
     - 🔥 "On Fire" — 5 answers approved
     - 🏆 "Top Contributor" — highest karma
     - 📚 "Knowledge Seeker" — viewed 20+ FAQs
   - Unearned badges shown grayed out
   - Toast notification when new badge earned

4. MY QUESTIONS LIST — all questions this student asked
5. MY ANSWERS LIST — all answers with approval status

IF USER IS ADMIN/COORDINATOR — Show:

1. OVERVIEW STATS:
   - Total Students, Total Questions, Total Answers, Approval Rate %
   - Each as a colored card with trend icon

2. MODERATION QUEUE:
   - All unapproved answers listed
   - Each shows: question title, answer preview, student name
   - ✅ Approve button → marks answer approved + gives student +10 points
   - ❌ Reject button → marks answer rejected
   - Comment: "Quality control — only verified answers get rewarded"

3. STUDENT DIRECTORY:
   - Table with columns: Name, Roll, Branch, NOC Status, Karma Points
   - Admin can click to Approve/Reject NOC for each student
   - Search/filter students
   - Comment: "Coordinator controls who can access the portal"

4. FAQ MANAGER:
   - List of all FAQs with Edit/Delete buttons
   - Add New FAQ form

Props: { currentUser, setCurrentUser, users, setUsers, userRole, questions, setQuestions, faqs, setFaqs, refreshData }
Add comments on admin actions explaining the moderation workflow.
```

**What this does:** Creates the student profile and the powerful admin control panel.

---

## STEP 10: Build Solve & Earn (Gamification)

> Copy-paste this prompt:

```
Create src/components/SolvePortal.jsx — gamified page showing unanswered questions students can solve for karma points.

SECTIONS:

1. HEADER:
   - Title: "🏆 Solve & Earn Karma Points"
   - Subtitle: "Help fellow interns and earn recognition"
   - Your current karma points shown prominently

2. POINTS EXPLAINER CARD:
   - How points work: +10 for each approved answer
   - Show total submitted vs approved ratio

3. UNANSWERED QUESTIONS LIST:
   - Filter to show only questions with 0 approved answers
   - Each card shows: question title, category badge, time posted, "💡 Answer Now" button
   - Click "Answer Now" → expands textarea to write answer
   - Submit → sends answer for admin approval
   - After submit → show "Submitted for review! ⏳" message

4. MINI LEADERBOARD:
   - Top 5 students ranked by karma points
   - Shows: rank, avatar, name, points
   - Current user highlighted if in top 5
   - Gold/Silver/Bronze colors for top 3

Props: { questions, setQuestions, faqs, setFaqs, currentUser, setCurrentUser, users, setUsers, isAdmin }
Add comments explaining the gamification strategy.
```

**What this does:** Creates the gamified "solve questions for points" page with leaderboard.

---

## STEP 11: Add Notification System

> Copy-paste this prompt:

```
Create src/components/Notifications.jsx — a notification bell system in the navbar.

TRIGGER:
- Bell icon (🔔) in the navbar with red unread count badge
- Click → opens dropdown panel below the bell

NOTIFICATION PANEL:
- List of recent notifications (newest first)
- Each notification shows: icon, message text, timestamp, read/unread dot
- "Mark all as read" button at top
- "Clear all" button to dismiss everything

NOTIFICATION TYPES (generate these automatically):
- "✅ Your NOC has been approved!" — when admin approves NOC
- "🎉 Your answer was approved! +10 points" — when admin approves answer
- "💬 Someone answered your question" — when someone replies
- "📚 New FAQ added: [title]" — when admin adds FAQ
- "🏅 You earned a badge: [badge name]!" — when badge is earned

STORAGE:
- Store notifications in localStorage per user
- Keep max 20 most recent notifications
- Auto-generate sample notifications on first load for demo purposes

Add this component to the navbar in App.jsx (between the user pill and theme toggle).
Add comments explaining notification flow.
```

**What this does:** Adds professional notification system — makes the app feel production-ready.

---

## STEP 12: Add Analytics Charts (Admin Only)

> Copy-paste this prompt:

```
Add visual analytics charts to the Admin Dashboard using a chart library.

Install: npm install recharts (lightweight React charting library)

Add a new "📊 Analytics" section to the Admin Dashboard with these charts:

1. BAR CHART — Questions per Category:
   - X axis: NOC Upload, Stipend Details, Accommodation, General & Campus
   - Y axis: number of questions
   - Amber colored bars

2. DONUT/PIE CHART — NOC Status Distribution:
   - Green: Approved, Yellow: Pending, Red: Rejected
   - Shows percentage labels

3. BAR CHART — Top 5 Students by Karma Points:
   - Horizontal bars with student names
   - Gold/Silver/Bronze colors for top 3

4. SUMMARY CARDS ROW at the top:
   - Total Students (with 👥 icon)
   - Total Questions (with ❓ icon)
   - Total Answers (with 💬 icon)
   - Approval Rate % (with ✅ icon)
   - Each card has subtle gradient background

Make charts responsive (stack on mobile).
Use smooth animations when charts load.
Add comments explaining what each chart shows and why it's useful for the coordinator.
```

**What this does:** Adds enterprise-grade analytics — makes the admin panel look professional.

---

## 🎁 BONUS STEPS (If You Have Time)

### BONUS A: Document Vault
```
Add a "📋 Document Vault" tab with downloadable template files.
Show: NOC Template, Stipend Form, Hostel Form, Campus Map.
Each as a card with file icon, name, and download button.
Admin can upload new documents.
```

### BONUS B: PWA Support
```
Add Progressive Web App support:
- Create public/manifest.json with app name "IIT Ropar Portal", amber theme color, and icon
- Add meta name="theme-color" content="#0f172a" to index.html
- Register a basic service worker for offline caching
This lets students install the website as a phone app.
```

### BONUS C: Hindi/English Toggle
```
Add a language toggle (🇮🇳/🇬🇧) in the navbar.
Create src/translations.js with all UI text in Hindi and English.
All buttons, labels, and placeholders switch dynamically.
FAQ content stays in English.
```

---

## ✅ Final Testing Checklist

After all steps are done, test these things:

| # | Test | Expected Result |
|---|------|----------------|
| 1 | Open login page | Animated gradient background, floating orbs, glass card |
| 2 | Sign up as new student | Form works, appears in student list with "Pending" status |
| 3 | Try login with pending NOC | Should be BLOCKED with warning |
| 4 | Login as admin (admin/1234) | Goes to admin dashboard |
| 5 | Approve a student's NOC | Student can now log in |
| 6 | Login as student | Lands on FAQ Hub with hero banner |
| 7 | Search FAQs | Autocomplete dropdown works |
| 8 | Click category cards | Filters FAQs correctly |
| 9 | Ask a question in Q&A | AI warns if duplicate exists |
| 10 | Open AI chatbot | Greeting message appears |
| 11 | Ask chatbot a question | Gets relevant answer with confidence % |
| 12 | Upload image in chatbot | OCR extracts text, matches FAQs |
| 13 | Submit answer in Solve & Earn | Shows "pending approval" |
| 14 | Admin approves answer | Student gets +10 karma points |
| 15 | Check notifications | Shows approval notification |
| 16 | Toggle dark/light mode | Everything switches cleanly |
| 17 | Check on mobile size | Responsive layout works |

---

## 🏆 Tips to Get First Rank

1. **Visual polish matters most** — Judges see the design before reading code
2. **Image analysis is your secret weapon** — Very few students will have this
3. **AI chatbot is the wow factor** — Demo it live during presentation
4. **Comments show understanding** — Judges read code to check if YOU built it
5. **Admin panel shows depth** — It proves the project is production-ready
6. **Dark mode toggle** — Small feature, huge impression
7. **Gamification (badges + points)** — Shows you thought about user engagement

> **Good luck! 🚀 Follow these 12 steps in order and you'll have a project that looks like it was built by a professional team.**
