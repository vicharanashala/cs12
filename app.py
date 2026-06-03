import os
import json
import time
import random
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from werkzeug.utils import secure_filename

app = Flask(__name__)
# Enable CORS for development
CORS(app)

DB_FILE = 'database.json'
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024  # 2MB limits

# Ensure uploads directory exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Initial Mock Data to seed the database if it doesn't exist
INITIAL_FAQS = [
  {
    "id": "faq-1",
    "category": "Stipend Details",
    "question": "What is the monthly stipend amount for interns at IIT Ropar?",
    "answer": "The stipend amount varies depending on the internship scheme. For institute-funded summer internships, it is typically ₹5,000 per month. For sponsored research project interns, it can range from ₹8,000 to ₹15,000 per month as approved by the Principal Investigator (PI) and funding agency. Please refer to your official offer letter for the exact amount.",
    "tags": ["stipend", "funding", "amount"]
  },
  {
    "id": "faq-2",
    "category": "Stipend Details",
    "question": "When is the stipend credited each month?",
    "answer": "Stipends are usually processed during the last week of every month and credited by the 5th working day of the subsequent month. Delays can occur if your monthly attendance sheet/progress report is not submitted to the Accounts section by the 25th of the current month.",
    "tags": ["stipend", "dates", "payment"]
  },
  {
    "id": "faq-3",
    "category": "NOC Upload",
    "question": "How do I request a No Objection Certificate (NOC) from IIT Ropar?",
    "answer": "To request an NOC, download the standard NOC template from our Document Vault, fill in your academic details, get it signed by your Parent Institution's Head/Dean, and then submit it to the IIT Ropar Internship Coordinator via this portal or email.",
    "tags": ["noc", "request", "template"]
  },
  {
    "id": "faq-4",
    "category": "NOC Upload",
    "question": "Where do I upload the signed NOC in the portal, and what is the size limit?",
    "answer": "You can upload your signed NOC in the 'NOC Status Tracker' section of this portal. The document must be in PDF format and the file size must not exceed 2MB. Ensure the seal of your college and the signature are clearly visible.",
    "tags": ["noc", "upload", "pdf"]
  },
  {
    "id": "faq-5",
    "category": "NOC Upload",
    "question": "What is the typical approval time for an NOC request?",
    "answer": "Once submitted, it takes approximately 3 to 5 working days for the Internship Coordinator and Academic Section to verify and approve your NOC. You will receive an automated email notification once approved, or you can track it live in the NOC Status Tracker.",
    "tags": ["noc", "timeline", "verification"]
  },
  {
    "id": "faq-6",
    "category": "Accommodation",
    "question": "Is hostel accommodation provided for external interns at IIT Ropar?",
    "answer": "Yes, subject to availability. External interns can request hostel accommodation during the application process. Allocation is done on a shared basis in the Chenab, Satluj, or Beas hostels. You will need to present your approved NOC and internship offer letter at the hostel office during check-in.",
    "tags": ["hostel", "accommodation", "stay"]
  },
  {
    "id": "faq-7",
    "category": "Accommodation",
    "question": "What are the hostel charges and mess fees for interns?",
    "answer": "Hostel rent is approximately ₹1,500 per month (electricity & water included). Mess charges are separate and cost around ₹150 per day, payable directly to the mess contractor. A refundable security deposit of ₹3,000 is also required at the time of check-in.",
    "tags": ["hostel", "fees", "mess"]
  },
  {
    "id": "faq-8",
    "category": "General & Campus",
    "question": "How do I get a temporary IIT Ropar ID card?",
    "answer": "After your NOC is approved, visit the Academic Section (JC Bose Block) on your first day. Bring two passport-sized photographs, your offer letter, and a government ID. They will issue a temporary gate pass and ID card valid for the duration of your internship.",
    "tags": ["id-card", "campus-access", "registration"]
  }
]

INITIAL_QUESTIONS = [
  {
    "id": "q-1",
    "category": "NOC Upload",
    "title": "Can I upload a digitally signed NOC from my university registrar?",
    "description": "My university is currently closed for holidays and they are only issuing digitally signed NOCs with QR codes. Is this acceptable, or does it strictly need to be physical ink signature and stamp?",
    "author": "Arjun Verma",
    "authorPoints": 45,
    "date": "2026-05-20",
    "tags": ["noc", "signature", "digital"],
    "status": "resolved",
    "views": 42,
    "answers": [
      {
        "id": "ans-1-1",
        "author": "Priya Patel",
        "authorBadge": "NOC Veteran",
        "content": "Yes, digitally signed NOCs are accepted as long as the QR code verification link works. I uploaded my university's digitally signed NOC last week and it got approved in 2 days. Just make sure the PDF isn't password protected!",
        "date": "2026-05-21",
        "votes": 12,
        "isApproved": True
      }
    ]
  },
  {
    "id": "q-2",
    "category": "Stipend Details",
    "title": "Has anyone received the stipend for April 2026?",
    "description": "I submitted my progress sheet signed by my PI on April 24th, but I haven't received the stipend credit yet. Is there an admin delay this month, or should I go visit the accounts office directly?",
    "author": "Rohan Das",
    "authorPoints": 150,
    "date": "2026-05-22",
    "tags": ["stipend", "april", "delay"],
    "status": "unresolved",
    "views": 29,
    "answers": [
      {
        "id": "ans-2-1",
        "author": "Aarav Sharma",
        "authorBadge": "Stipend Guru",
        "content": "There's a minor delay in accounts due to the financial year closing clearances. I spoke to the clerk yesterday, they said all summer stipends will be released together by Monday (May 25th). No need to visit the office yet unless you don't get it by Tuesday.",
        "date": "2026-05-23",
        "votes": 8,
        "isApproved": False
      }
    ]
  },
  {
    "id": "q-3",
    "category": "General & Campus",
    "title": "Are interns allowed to access the central library after 8 PM?",
    "description": "I want to work on a research paper and the lab gets noisy in the evening. Can we sit in the central library? Do we need any special permissions, or does the temporary ID card suffice?",
    "author": "Siddharth Sen",
    "authorPoints": 20,
    "date": "2026-05-22",
    "tags": ["library", "timings", "access"],
    "status": "unresolved",
    "views": 14,
    "answers": []
  },
  {
    "id": "q-4",
    "category": "Accommodation",
    "title": "Is it possible to request a single room in the hostel due to medical reasons?",
    "description": "I have a sleep apnea condition and use a CPAP machine which makes noise, so I prefer not to disturb room partners. Can I request a single room, and who should I write to?",
    "author": "Meera Nair",
    "authorPoints": 10,
    "date": "2026-05-19",
    "tags": ["hostel", "medical", "single-room"],
    "status": "resolved",
    "views": 23,
    "answers": [
      {
        "id": "ans-4-1",
        "author": "Dr. Vikram (Coordinator)",
        "authorBadge": "Official Admin",
        "content": "Please email a medical certificate issued by a registered practitioner along with your hostel allotment application to the Chief Warden Office (warden@iitrpr.ac.in) and CC me. They usually accommodate such requests on genuine medical grounds.",
        "date": "2026-05-20",
        "votes": 18,
        "isApproved": True
      }
    ]
  }
]

INITIAL_USERS = [
  {
    "id": "u-1",
    "name": "Aarav Sharma",
    "rollNumber": "2024CSB1001",
    "password": "password123",
    "points": 380,
    "badge": "Stipend Guru",
    "resolvedCount": 14,
    "nocStatus": "Approved",
    "avatarColor": "from-blue-500 to-indigo-600"
  },
  {
    "id": "u-2",
    "name": "Priya Patel",
    "rollNumber": "2024CSB1002",
    "password": "password123",
    "points": 295,
    "badge": "NOC Veteran",
    "resolvedCount": 9,
    "nocStatus": "Approved",
    "avatarColor": "from-purple-500 to-pink-500"
  },
  {
    "id": "u-3",
    "name": "Rohan Das",
    "rollNumber": "2024CSB1003",
    "password": "password123",
    "points": 158,
    "badge": "IIT Ropar Scholar",
    "resolvedCount": 4,
    "nocStatus": "Under Review",
    "avatarColor": "from-emerald-400 to-teal-600"
  },
  {
    "id": "u-4",
    "name": "Meera Nair",
    "rollNumber": "2024CSB1004",
    "password": "password123",
    "points": 85,
    "badge": "Active Contributor",
    "resolvedCount": 2,
    "nocStatus": "Approved",
    "avatarColor": "from-amber-400 to-orange-500"
  }
]

# Database Helpers
def load_db():
    if not os.path.exists(DB_FILE):
        return {"faqs": INITIAL_FAQS, "questions": INITIAL_QUESTIONS, "users": INITIAL_USERS}
    try:
        with open(DB_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            # Make sure keys exist
            if "faqs" not in data: data["faqs"] = []
            if "questions" not in data: data["questions"] = []
            if "users" not in data: data["users"] = []
            return data
    except Exception as e:
        print(f"Error loading {DB_FILE}: {e}")
        return {"faqs": [], "questions": [], "users": []}

def save_db(data):
    try:
        with open(DB_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"Error saving {DB_FILE}: {e}")

# MongoDB Setup (Optional fallback)
use_mongo = False
db_mongo = None

try:
    from pymongo import MongoClient
    # Set short timeout to not block start-up if mongo isn't active
    client = MongoClient("mongodb://127.0.0.1:27017/", serverSelectionTimeoutMS=1500)
    db_mongo = client["iitrpr_faq"]
    client.server_info()  # triggers server check
    use_mongo = True
    print("Connected to MongoDB successfully!")
except Exception as e:
    use_mongo = False
    print("MongoDB connection refused. Falling back to local database.json storage format.")

# Seeding MongoDB with local DB if Mongo is empty
def seed_database():
    if not use_mongo:
        return
    try:
        local_data = load_db()
        
        # Sync FAQs
        faq_count = db_mongo.faqs.count_documents({})
        local_faqs_len = len(local_data.get("faqs", []))
        if local_faqs_len > 0 and faq_count != local_faqs_len:
            db_mongo.faqs.delete_many({})
            db_mongo.faqs.insert_many([dict(f) for f in local_data["faqs"]])
            print(f"[Seed] Synchronized {local_faqs_len} FAQs to MongoDB.")
            
        # Sync Users
        user_count = db_mongo.users.count_documents({})
        local_users_len = len(local_data.get("users", []))
        if user_count == 0 and local_users_len > 0:
            db_mongo.users.insert_many([dict(u) for u in local_data["users"]])
            print(f"[Seed] Imported {local_users_len} Users to MongoDB.")
            
        # Sync Questions
        question_count = db_mongo.questions.count_documents({})
        local_questions_len = len(local_data.get("questions", []))
        if question_count == 0 and local_questions_len > 0:
            db_mongo.questions.insert_many([dict(q) for q in local_data["questions"]])
            print(f"[Seed] Imported {local_questions_len} Questions to MongoDB.")
    except Exception as err:
        print(f"Database seeding failed: {err}")

seed_database()

# --- API ROUTES ---

# GET FAQs
@app.route('/api/faqs', methods=['GET'])
def get_faqs():
    if use_mongo:
        try:
            faqs = list(db_mongo.faqs.find({}, {"_id": 0}))
            return jsonify(faqs)
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        db = load_db()
        return jsonify(db.get("faqs", []))

# POST FAQ
@app.route('/api/faqs', methods=['POST'])
def add_faq():
    new_faq = request.json or {}
    if use_mongo:
        try:
            db_mongo.faqs.insert_one(dict(new_faq))
            new_faq.pop("_id", None)
            return jsonify(new_faq), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        db = load_db()
        db.setdefault("faqs", []).insert(0, new_faq)
        save_db(db)
        return jsonify(new_faq), 201

# DELETE FAQ
@app.route('/api/faqs/<id>', methods=['DELETE'])
def delete_faq(id):
    if use_mongo:
        try:
            db_mongo.faqs.delete_one({"id": id})
            return jsonify({"success": True, "message": "FAQ deleted"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        db = load_db()
        db["faqs"] = [f for f in db.get("faqs", []) if f.get("id") != id]
        save_db(db)
        return jsonify({"success": True, "message": "FAQ deleted"})

# GET Questions
@app.route('/api/questions', methods=['GET'])
def get_questions():
    if use_mongo:
        try:
            questions = list(db_mongo.questions.find({}, {"_id": 0}))
            return jsonify(questions)
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        db = load_db()
        return jsonify(db.get("questions", []))

# POST Question
@app.route('/api/questions', methods=['POST'])
def add_question():
    new_q = request.json or {}
    if use_mongo:
        try:
            db_mongo.questions.insert_one(dict(new_q))
            new_q.pop("_id", None)
            return jsonify(new_q), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        db = load_db()
        db.setdefault("questions", []).insert(0, new_q)
        save_db(db)
        return jsonify(new_q), 201

# POST Approve Question
@app.route('/api/questions/<id>/approve', methods=['POST'])
def approve_question(id):
    if use_mongo:
        try:
            db_mongo.questions.update_one({"id": id}, {"$set": {"isApproved": True}})
            return jsonify({"success": True})
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        db = load_db()
        for q in db.get("questions", []):
            if q.get("id") == id:
                q["isApproved"] = True
                break
        save_db(db)
        return jsonify({"success": True})

# POST Increment Question Views
@app.route('/api/questions/<id>/views', methods=['POST'])
def increment_question_views(id):
    if use_mongo:
        try:
            db_mongo.questions.update_one({"id": id}, {"$inc": {"views": 1}})
            return jsonify({"success": True})
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        db = load_db()
        for q in db.get("questions", []):
            if q.get("id") == id:
                q["views"] = q.get("views", 0) + 1
                break
        save_db(db)
        return jsonify({"success": True})

# POST Add Answer
@app.route('/api/questions/<qId>/answers', methods=['POST'])
def add_answer(qId):
    new_ans = request.json or {}
    if use_mongo:
        try:
            db_mongo.questions.update_one({"id": qId}, {"$push": {"answers": new_ans}})
            return jsonify(new_ans), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        db = load_db()
        for q in db.get("questions", []):
            if q.get("id") == qId:
                q.setdefault("answers", []).append(new_ans)
                break
        save_db(db)
        return jsonify(new_ans), 201

# POST Vote Answer
@app.route('/api/questions/<qId>/answers/<ansId>/vote', methods=['POST'])
def vote_answer(qId, ansId):
    req_data = request.json or {}
    user_id = req_data.get("userId")
    vote_type = req_data.get("voteType")
    
    if not user_id:
        return jsonify({"error": "Missing userId"}), 400
        
    new_vote = 1 if vote_type == 'up' else -1
    
    if use_mongo:
        try:
            q = db_mongo.questions.find_one({"id": qId})
            if not q:
                return jsonify({"error": "Question not found"}), 404
            
            answers = q.get("answers", [])
            ans = None
            ans_index = -1
            for idx, a in enumerate(answers):
                if a.get("id") == ansId:
                    ans = a
                    ans_index = idx
                    break
            
            if not ans:
                return jsonify({"error": "Answer not found"}), 404
                
            votes_map = ans.setdefault("votesMap", {})
            previous_vote = votes_map.get(user_id, 0)
            
            if previous_vote == new_vote:
                net_change = -new_vote
                votes_map[user_id] = 0
            else:
                net_change = new_vote - previous_vote
                votes_map[user_id] = new_vote
                
            ans["votes"] = ans.get("votes", 0) + net_change
            ans["votesMap"] = votes_map
            
            db_mongo.questions.update_one(
                {"id": qId},
                {"$set": {f"answers.{ans_index}": ans}}
            )
            return jsonify({"success": True})
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        db = load_db()
        found = False
        for q in db.get("questions", []):
            if q.get("id") == qId:
                for ans in q.get("answers", []):
                    if ans.get("id") == ansId:
                        votes_map = ans.setdefault("votesMap", {})
                        previous_vote = votes_map.get(user_id, 0)
                        
                        if previous_vote == new_vote:
                            net_change = -new_vote
                            votes_map[user_id] = 0
                        else:
                            net_change = new_vote - previous_vote
                            votes_map[user_id] = new_vote
                            
                        ans["votes"] = ans.get("votes", 0) + net_change
                        found = True
                        break
                if found:
                    break
        if found:
            save_db(db)
            return jsonify({"success": True})
        return jsonify({"error": "Question or Answer not found"}), 404

# POST Approve Answer (resolved status + awards 50 points to solver)
@app.route('/api/questions/<qId>/answers/<ansId>/approve', methods=['POST'])
def approve_answer(qId, ansId):
    if use_mongo:
        try:
            q = db_mongo.questions.find_one({"id": qId})
            if not q:
                return jsonify({"error": "Question not found"}), 404
            
            answers = q.get("answers", [])
            resolver_name = None
            ans_index = -1
            for idx, ans in enumerate(answers):
                if ans.get("id") == ansId:
                    ans["isApproved"] = True
                    resolver_name = ans.get("author")
                    ans_index = idx
                    break
            
            if ans_index == -1:
                return jsonify({"error": "Answer not found"}), 404
                
            db_mongo.questions.update_one(
                {"id": qId},
                {"$set": {"status": "resolved", f"answers.{ans_index}": answers[ans_index]}}
            )
            if resolver_name:
                db_mongo.users.update_one(
                    {"name": resolver_name},
                    {"$inc": {"points": 50, "resolvedCount": 1}}
                )
            return jsonify({"success": True, "resolver": resolver_name})
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        db = load_db()
        resolver_name = None
        q_found = False
        for q in db.get("questions", []):
            if q.get("id") == qId:
                q["status"] = 'resolved'
                for ans in q.get("answers", []):
                    if ans.get("id") == ansId:
                        ans["isApproved"] = True
                        resolver_name = ans.get("author")
                        q_found = True
                        break
                if q_found:
                    break
                    
        if q_found:
            if resolver_name:
                for u in db.get("users", []):
                    if u.get("name") == resolver_name:
                        u["points"] = u.get("points", 0) + 50
                        u["resolvedCount"] = u.get("resolvedCount", 0) + 1
                        break
            save_db(db)
            return jsonify({"success": True, "resolver": resolver_name})
        return jsonify({"error": "Question or Answer not found"}), 404

# GET Users
@app.route('/api/users', methods=['GET'])
def get_users():
    if use_mongo:
        try:
            users = list(db_mongo.users.find({}, {"_id": 0}))
            return jsonify(users)
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        db = load_db()
        return jsonify(db.get("users", []))

# POST User
@app.route('/api/users', methods=['POST'])
def add_user():
    new_user = request.json or {}
    if use_mongo:
        try:
            db_mongo.users.insert_one(dict(new_user))
            new_user.pop("_id", None)
            return jsonify(new_user), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        db = load_db()
        db.setdefault("users", []).append(new_user)
        save_db(db)
        return jsonify(new_user), 201

# PUT User
@app.route('/api/users/<id>', methods=['PUT'])
def update_user(id):
    update_data = request.json or {}
    if use_mongo:
        try:
            db_mongo.users.update_one({"id": id}, {"$set": update_data})
            updated_user = db_mongo.users.find_one({"id": id}, {"_id": 0})
            if not updated_user:
                return jsonify({"error": "User not found"}), 404
            return jsonify(updated_user)
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        db = load_db()
        updated_user = None
        for u in db.get("users", []):
            if u.get("id") == id:
                for key, val in update_data.items():
                    u[key] = val
                updated_user = u
                break
        if updated_user:
            save_db(db)
            return jsonify(updated_user)
        return jsonify({"error": "User not found"}), 404

# POST File Upload (NOC PDF)
@app.route('/api/noc/upload', methods=['POST'])
def upload_noc():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400
        
    if file:
        filename = secure_filename(file.filename)
        name, ext = os.path.splitext(filename)
        unique_filename = f"{int(time.time() * 1000)}-{random.randint(100000000, 999999999)}{ext}"
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], unique_filename))
        return jsonify({"success": True, "filename": unique_filename})

# Serve uploads folder
@app.route('/uploads/<filename>', methods=['GET'])
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# Start Flask Server
if __name__ == '__main__':
    print("===================================================")
    print("IIT Ropar FAQ Python Flask Backend running on port 5000")
    print(f"Serving uploads from: {os.path.abspath(UPLOAD_FOLDER)}")
    print("===================================================")
    app.run(port=5000, debug=True)
