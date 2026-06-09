# Project Report: IIT Ropar Crowdsourced FAQ & Internship Portal
**A Production-Grade MERN Stack Web Application with AI-Powered OCR and Gamified Peer Q&A**

---

## 1. Executive Summary & Objective
The **IIT Ropar Internship Portal & Crowdsourced FAQ Hub** is designed to streamline administrative clearances and peer-to-peer query resolution for internship cohorts. When handling thousands of concurrent student interns, traditional helpdesks face overwhelming administrative pressure. 

This project solves that bottleneck by implementing a **self-sustaining crowdsourced model** combined with **AI automation**:
- **Students help students** by answering questions and earning Karma points (Gamification).
- **AI-powered tools** (Chatbot & OCR Scanner) resolve standard queries before they reach the admin.
- **Admin Coordinators** manage system-wide clearances (NOCs) and promote high-quality crowdsourced answers to the official database.

---

## 2. Technology Stack Architecture (MERN)
The portal is built on a pure **MERN Stack** architecture designed for scalability, high performance, and robustness:

```
┌────────────────────────────────────────────────────────┐
│                   React + Vite (UI)                    │
│   (Vibrant glassmorphism, responsive charts, components)│
└───────────────┬────────────────────────┬───────────────┘
                │                        ▲
                │ API Requests (Fetch)   │ JSON Responses
                ▼                        │
┌────────────────────────────────────────────────────────┐
│               Node.js + Express (API)                  │
│   (RESTful endpoints, Multer upload, AI pipelines)     │
└───────────────┬────────────────────────┬───────────────┘
                │                        ▲
                │ Mongoose Queries       │ DB Results
                ▼                        │
┌────────────────────────────────────────────────────────┐
│                   MongoDB Database                     │
│    (Schemas: Users, FAQs, Threads, Answers, NOCs)      │
│   * Fail-safe fallback: Local JSON DB (database.json)   │
└────────────────────────────────────────────────────────┘
```

- **Frontend (React + Vite)**: Renders a modern single-page application (SPA) with full responsive support, custom HSL color systems, live analytics charts (using Recharts), and dynamic light/dark theme toggles.
- **Backend (Express + Node.js)**: Runs on port `5001`, exposing RESTful APIs with CORS validation, token-free secure session persistence, and file upload endpoints.
- **Database (MongoDB + Mongoose)**: Configured with schema definitions and validations for users, threads, answers, and FAQs.
- **Fail-Safe Integrity**: If MongoDB is offline, the backend server gracefully falls back to local file storage (`database.json`), keeping the application 100% operational in any environment.

---

## 3. Core Features Implemented

### 👥 A. Crowdsourced Q&A Engine (Peer-to-Peer)
- **Q&A Discussion Feed**: A threaded forum where students post custom internship queries.
- **Instant Publication**: Questions and answers go live immediately, bypassing administrative approval queues to prevent communication bottlenecks.
- **Community Upvoting**: Students upvote or downvote answers. High-quality community answers float to the top, allowing the community to self-regulate.
- **Verified FAQ Promotion**: Admins can approve exceptional peer answers and promote them directly to the official FAQ Hub with a single click.

### 🎮 B. Gamification & Ranks (Karma System)
- **Karma Points**: Students earn points for contributing approved answers and solving peer problems.
- **Milestone Badges**: Unlockable profile badges based on user contribution:
  - 🥇 *Helpful Peer* (First solved query)
  - 🥈 *Knowledge Seeker* (100+ points)
  - 🥉 *IIT Ropar Scholar* (250+ points)
  - 🏆 *Intern Sage* (500+ points)
- **Ranks & Leaderboard**: Visual stats bar showing points progression, tier limits, and a horizontal bar chart on the admin board showcasing the top 5 students.

### 🤖 C. Artificial Intelligence Integrations
- **AI Chatbot Assistant**: A floating drawer widget available on main tabs that queries the FAQ database via fast text-matching to answer generic queries instantly.
- **AI-Powered OCR Scanner**: A dedicated page where students upload screenshots of guidelines, email notifications, or portal notices. The system extracts the text (via Tesseract.js) and automatically matches it against relevant database FAQs.
- **Automated AI NOC Auditor**: Inside the Coordinator panel, the admin can run an **AI Verify scan** on a student's uploaded PDF. The AI checks compliance criteria (signature presence, institutional stamp, roll number matching) and lists verification issues.

### 📂 D. Dedicated Document Vault
- **Centralized Download Center**: A clean, categorized file vault housing standard documents (NOC templates, Stipend Claim Forms, Hostel Allotments, Campus Maps).
- **Dynamic File Generation**: Students download dynamically constructed template blobs as PDF/Word formats, deflecting repetitive requests from coordinators.

### 🛡️ E. Admin Coordinator Command Center
- **Analytics Dashboard**: Real-time cards displaying total students, query counts, and overall answer approval rates.
- **Interactive Recharts**: Bar charts plotting questions per category (NOC, Stipend, Hostel, Campus) and student leaderboards.
- **Bulk NOC Approval**: Access manager with checkboxes allowing coordinators to select multiple students and approve or reset/revoke clearance status in a single click.
- **Export Analytics as PDF**: Generates a clean, print-friendly administrative analytics summary report sheet and automatically launches the OS print/PDF save dialog.
- **Student Portal Feedback Reviews**: Live review feedback feed displaying rating emojis (😍, 🙂, 😐, 🙁, 😡) and comments left by students.
- **Global Announcement Banner**: An editor card allowing coordinators to broadcast alerts globally to all student screens, with a live editor preview.

---

## 4. UI/UX Refinements & Legibility
- **Pre-Login Theme Switcher**: A floating theme toggle on the login page allowing students to choose light or dark modes before authentication.
- **Dynamic Glassmorphism**: Glass-styled login cards adjust their opacity and background color dynamically (slate gray in dark mode, clean white with deep-slate text in light mode) for high readability.
- **Keyboard Shortcuts**: Power-user bindings (`Ctrl + K` or `Cmd + K` to focus any active search input; `Esc` to close modals or blur input fields).

---

## 5. MongoDB Database Schemas
The database holds three primary Mongoose collections:

```javascript
// User Schema
const userSchema = new mongoose.Schema({
  name: { type: String, required: true },
  rollNumber: { type: String, required: true },
  password: { type: String, required: true },
  points: { type: Number, default: 0 },
  badge: { type: String, default: 'New Scholar' },
  resolvedCount: { type: Number, default: 0 },
  nocStatus: { type: String, default: 'Pending Upload' },
  nocFile: { type: String, default: null }
});

// FAQ Schema
const faqSchema = new mongoose.Schema({
  category: { type: String, required: true },
  question: { type: String, required: true },
  answer: { type: String, required: true },
  tags: [String]
});

// Question & Threads Schema
const questionSchema = new mongoose.Schema({
  category: { type: String, required: true },
  title: { type: String, required: true },
  description: { type: String, required: true },
  author: { type: String, required: true },
  views: { type: Number, default: 0 },
  answers: [{
    author: String,
    content: String,
    votes: { type: Number, default: 0 },
    isApproved: { type: Boolean, default: false }
  }]
});
```

---

## 6. How to Run & Verify
Both servers run concurrently via Node.js runtime:

1. **Start Local MongoDB** (or use the built-in JSON Database fallback):
   ```bash
   brew services start mongodb-community
   ```
2. **Launch Node.js Backend Server** (Port `5001`):
   ```bash
   npm run backend
   ```
3. **Launch Vite React Frontend Dev Server** (Port `5173`):
   ```bash
   npm run dev
   ```
4. **Log in as Admin Coordinator**:
   - Username: `admin` | Verification PIN: `1234`
5. **Log in as pre-cleared Student**:
   - Roll Number: `2024CSB1001` (Aarav) | Password: `password123
