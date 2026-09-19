# 📋 Shenyang City University Platform - Complete Project Plan
freebuff --continue 2026-06-16T14-10-58.827Z
**Project Status:** Large-scale but phased approach  
**Timeline:** Phase 1 (MVP): 6-8 weeks | Full Platform: 4-6 months  
**Team Size:** 2-3 developers recommended  
**Tech Stack:** Next.js 14+, MongoDB, Vercel, TailwindCSS, TypeScript

---

## 🎯 PHASE BREAKDOWN & TIMELINE

### **PHASE 1: MVP (Weeks 1-8)** ⭐ START HERE
Build core functionality to launch with ~100 users

**Must-Have Features:**
- ✅ Authentication (Student/Teacher login)
- ✅ Student Dashboard (basic info + enrolled courses)
- ✅ Course Timetable Display
- ✅ Assets Upload/Download (simple file management)
- ✅ Bilingual UI (English + Chinese) - Arabic/French can wait
- ✅ Teacher Course Management
- ✅ Basic Notifications

**Estimated Effort:** 6-8 weeks (2 developers)

---

### **PHASE 2: Enhanced Features (Weeks 9-14)**
Add specialized tools once MVP is stable

**Add Features:**
- 📐 Math Tools (Calculator, 2D/3D graphers - simpler versions)
- 💻 Online IDE (Python, C++ - via Replit API or similar)
- 🎓 Course-Specific Asset Organization
- 📲 Mobile-responsive improvements
- 🔔 Advanced Notifications (email, in-app)

**Estimated Effort:** 4-5 weeks

---

### **PHASE 3: Advanced & Scalability (Weeks 15+)**
Polish and full feature release

**Add Features:**
- 🌐 Full Multilingual Support (French, Arabic)
- 📊 Analytics Dashboard (Teachers/Admins)
- 🎤 Student Progress Tracking
- 📚 Advanced Resource Library
- 🔒 Enhanced Security & Audit Logs

**Estimated Effort:** Ongoing

---

## 📄 PAGE STRUCTURE (HIERARCHICAL)

```
SHENYANG UNIVERSITY PLATFORM
│
├─ PUBLIC PAGES
│  ├─ Landing Page
│  ├─ Login Page
│  ├─ About University
│  └─ Contact
│
├─ STUDENT AREA (/student)
│  ├─ Dashboard ⭐ MAIN
│  │  ├─ Upcoming Classes
│  │  ├─ Current Courses
│  │  ├─ Notifications
│  │  └─ Quick Links
│  │
│  ├─ Profile & Settings
│  │  ├─ Personal Info
│  │  ├─ School/Major/Year Selection
│  │  ├─ Language Preferences
│  │  └─ Password & Security
│  │
│  ├─ Courses (/student/courses)
│  │  ├─ My Courses (List view)
│  │  └─ Course Detail Page
│  │     ├─ Course Info
│  │     ├─ Timetable
│  │     ├─ Instructor Info
│  │     └─ Materials/Assignments
│  │
│  ├─ Timetable (/student/timetable)
│  │  ├─ Weekly View
│  │  ├─ Monthly View
│  │  └─ Exam Schedule
│  │
│  ├─ Assets Library (/student/assets) ⭐ IMPORTANT
│  │  ├─ By Course
│  │  ├─ By Type (Notes, Assignments, etc)
│  │  ├─ Upload Files
│  │  └─ Download Center
│  │
│  ├─ Specialized Tools
│  │  ├─ Math Playground (/student/math-tools)
│  │  │  ├─ Scientific Calculator
│  │  │  ├─ Calculus Solver
│  │  │  ├─ 2D/3D Graphing Tool
│  │  │  └─ Formula Reference
│  │  │
│  │  ├─ Coding IDE (/student/ide)
│  │  │  ├─ Python Editor
│  │  │  ├─ C++ Editor
│  │  │  ├─ JavaScript Editor
│  │  │  ├─ Run & Debug
│  │  │  └─ Code Templates
│  │  │
│  │  ├─ Chinese Learning (/student/chinese-resources)
│  │  │  ├─ Learning Materials
│  │  │  ├─ Dictionary
│  │  │  ├─ Practice Tools
│  │  │  └─ External Resources
│  │  │
│  │  └─ General Subjects (/student/subjects)
│  │     ├─ Subject Pages (Physics, Chemistry, etc)
│  │     ├─ Resource Links
│  │     └─ Forum/Discussion (Optional Phase 3)
│  │
│  └─ Notifications (/student/notifications)
│     ├─ All Notifications
│     ├─ By Course
│     └─ Settings
│
├─ TEACHER AREA (/teacher)
│  ├─ Dashboard ⭐ MAIN
│  │  ├─ Assigned Courses
│  │  ├─ Student List (by course)
│  │  ├─ Quick Actions
│  │  └─ Recent Activity
│  │
│  ├─ Profile & Settings
│  │  ├─ Personal Info
│  │  ├─ Course Selection (multi-select)
│  │  ├─ Department/School
│  │  ├─ Office Hours
│  │  └─ Preferences
│  │
│  ├─ Courses Management (/teacher/courses)
│  │  ├─ My Courses (List)
│  │  └─ Course Details Page
│  │     ├─ Edit Course Info
│  │     ├─ Manage Timetable
│  │     ├─ Add/Edit Schedule
│  │     ├─ Student List (enrolled)
│  │     ├─ Attendance Tracking (Optional)
│  │     └─ Class Notes
│  │
│  ├─ Materials Management (/teacher/materials)
│  │  ├─ Upload Notes
│  │  ├─ Upload Assignments
│  │  ├─ Upload Exam Schedules
│  │  ├─ Organize by Course
│  │  └─ File History/Versions
│  │
│  ├─ Notifications (/teacher/notifications)
│  │  ├─ Send Announcement
│  │  ├─ Send to Class/Individual
│  │  ├─ Notification History
│  │  └─ Settings
│  │
│  ├─ Student Management (/teacher/students)
│  │  ├─ View Enrolled Students
│  │  ├─ Filter by Major/Year
│  │  ├─ Student Details
│  │  └─ Mark Attendance (Optional)
│  │
│  └─ Reports (/teacher/reports) [Phase 2]
│     ├─ Class Statistics
│     ├─ Attendance Reports
│     └─ Student Progress
│
├─ ADMIN AREA (/admin)
│  ├─ Dashboard ⭐ MAIN
│  │  ├─ System Overview
│  │  ├─ Active Users
│  │  ├─ Quick Stats
│  │  └─ System Health
│  │
│  ├─ User Management (/admin/users)
│  │  ├─ All Users (Students + Teachers)
│  │  ├─ Add/Edit/Delete Users
│  │  ├─ Assign Roles
│  │  ├─ Activate/Deactivate Accounts
│  │  └─ Bulk Import (CSV)
│  │
│  ├─ Schools & Majors (/admin/schools)
│  │  ├─ Manage Schools (list of all 11)
│  │  ├─ Manage Majors per School
│  │  └─ View Course Distribution
│  │
│  ├─ Courses & Classes (/admin/courses)
│  │  ├─ All Courses (University-wide)
│  │  ├─ Assign Teachers to Courses
│  │  ├─ Edit Course Details
│  │  └─ Archive Old Courses
│  │
│  ├─ Academic Calendar (/admin/calendar)
│  │  ├─ Semester Management
│  │  ├─ Exam Periods
│  │  ├─ Holidays
│  │  └─ Important Dates
│  │
│  ├─ System Settings (/admin/settings)
│  │  ├─ General Settings
│  │  ├─ Email Configuration
│  │  ├─ File Upload Limits
│  │  ├─ Notification Templates
│  │  └─ Maintenance Mode
│  │
│  ├─ Reports & Analytics (/admin/analytics)
│  │  ├─ User Statistics
│  │  ├─ Login History
│  │  ├─ File Upload Statistics
│  │  └─ System Performance
│  │
│  └─ Logs & Security (/admin/logs)
│     ├─ Activity Logs
│     ├─ Error Logs
│     ├─ Security Audit
│     └─ Backup Management
│
└─ SHARED PAGES
   ├─ 404 Not Found
   ├─ 500 Error
   └─ Maintenance
```

---

## 🏗️ DATABASE SCHEMA (MongoDB Collections)

```javascript
// USERS COLLECTION
users: {
  _id: ObjectId,
  email: String (unique),
  password: String (hashed),
  firstName: String,
  lastName: String,
  role: Enum ["STUDENT", "TEACHER", "ADMIN"],
  profilePicture: String (URL),
  
  // Student-specific
  studentID: String (if role === STUDENT),
  school: ObjectId (ref: schools),
  major: ObjectId (ref: majors),
  year: Number (1-4),
  enrolledCourses: [ObjectId] (ref: courses),
  
  // Teacher-specific
  department: String (if role === TEACHER),
  taughtCourses: [ObjectId] (ref: courses),
  officeHours: String,
  qualification: String,
  
  // Language preference
  language: Enum ["EN", "ZH", "FR", "AR"],
  
  // Timestamps
  createdAt: Date,
  updatedAt: Date,
  lastLogin: Date,
  isActive: Boolean,
}

// SCHOOLS COLLECTION
schools: {
  _id: ObjectId,
  name: String,
  nameZH: String,
  code: String,
  description: String,
  headOfSchool: ObjectId (ref: users),
  majors: [ObjectId] (ref: majors),
  createdAt: Date,
}

// MAJORS COLLECTION
majors: {
  _id: ObjectId,
  name: String,
  code: String,
  schoolID: ObjectId (ref: schools),
  courses: [ObjectId] (ref: courses),
  yearsOfStudy: Number,
  description: String,
}

// COURSES COLLECTION
courses: {
  _id: ObjectId,
  code: String (unique),
  name: String,
  nameZH: String,
  description: String,
  credits: Number,
  
  // Teaching info
  teacher: ObjectId (ref: users),
  // For multiple teachers in future
  assistants: [ObjectId] (ref: users),
  
  // Schedule
  classRoom: String,
  dayOfWeek: String (MON, TUE, etc),
  startTime: String (HH:MM),
  endTime: String (HH:MM),
  capacity: Number,
  
  // Course details
  major: ObjectId (ref: majors),
  semester: String (e.g., "2024-Fall"),
  enrolledStudents: [ObjectId] (ref: users),
  
  // Materials
  syllabus: String (URL),
  materials: [ObjectId] (ref: materials),
  assignments: [ObjectId] (ref: assignments),
  
  // Exams
  examDate: Date,
  examLocation: String,
  examDuration: Number (minutes),
  
  createdAt: Date,
  updatedAt: Date,
}

// MATERIALS COLLECTION
materials: {
  _id: ObjectId,
  courseID: ObjectId (ref: courses),
  type: Enum ["NOTE", "ASSIGNMENT", "EXAM_SCHEDULE", "LECTURE_SLIDE", "OTHER"],
  title: String,
  description: String,
  fileURL: String,
  fileName: String,
  fileSize: Number,
  uploadedBy: ObjectId (ref: users),
  uploadedAt: Date,
  
  // Access control
  visibleToStudents: Boolean,
  dueDate: Date (if type === ASSIGNMENT),
}

// NOTIFICATIONS COLLECTION
notifications: {
  _id: ObjectId,
  recipientID: ObjectId (ref: users),
  senderID: ObjectId (ref: users),
  courseID: ObjectId (ref: courses, optional),
  type: Enum ["ANNOUNCEMENT", "ASSIGNMENT", "EXAM", "GENERAL"],
  title: String,
  message: String,
  read: Boolean,
  createdAt: Date,
  expiresAt: Date,
}

// ATTENDANCE COLLECTION (Optional)
attendance: {
  _id: ObjectId,
  courseID: ObjectId (ref: courses),
  studentID: ObjectId (ref: users),
  date: Date,
  status: Enum ["PRESENT", "ABSENT", "LATE"],
  remarks: String,
}

// TIMETABLE COLLECTION (Alternative structure)
timetable: {
  _id: ObjectId,
  courseID: ObjectId (ref: courses),
  dayOfWeek: String,
  startTime: String,
  endTime: String,
  location: String,
  recurrance: Enum ["WEEKLY", "BIWEEKLY", "ONCE"],
  startDate: Date,
  endDate: Date,
}

// SESSIONS COLLECTION (for authentication)
sessions: {
  _id: ObjectId,
  userID: ObjectId (ref: users),
  token: String,
  expiresAt: Date,
  deviceInfo: String,
  ipAddress: String,
}
```

---

## 🔐 USER ROLES & PERMISSIONS

```
┌─────────────────┬──────────────┬──────────────┬───────────────┐
│ Feature         │ STUDENT      │ TEACHER      │ ADMIN         │
├─────────────────┼──────────────┼──────────────┼───────────────┤
│ View Dashboard  │ ✅ Own only  │ ✅ Own       │ ✅ All        │
│ View Timetable  │ ✅ Own       │ ✅ Own Class │ ✅ All        │
│ Download Files  │ ✅ Own Class │ ✅ Own Class │ ✅ All        │
│ Upload Files    │ ❌           │ ✅ Own Class │ ✅ All        │
│ View Students   │ ❌           │ ✅ Own Class │ ✅ All        │
│ Send Notif.     │ ❌           │ ✅ Own Class │ ✅ All        │
│ Manage Users    │ ❌           │ ❌           │ ✅            │
│ Manage Courses  │ ❌           │ ❌           │ ✅            │
│ View Analytics  │ ❌           │ ✅ Own Class │ ✅ All        │
│ System Settings │ ❌           │ ❌           │ ✅            │
└─────────────────┴──────────────┴──────────────┴───────────────┘
```

---

## 🗺️ NAVIGATION FLOW (User Journey)

### **STUDENT FLOW:**
```
Login → Select School/Major/Year → Dashboard
        ├─→ View Courses → Select Course → View Materials
        ├─→ Check Timetable
        ├─→ Browse Assets Library
        ├─→ Access Math Tools
        ├─→ Access Coding IDE
        └─→ Check Notifications
```

### **TEACHER FLOW:**
```
Login → Select Course(s) to Teach → Dashboard
        ├─→ Manage Course Materials (Upload Notes/Assignments)
        ├─→ View Enrolled Students
        ├─→ Create Announcements
        ├─→ Set Exam Schedule
        └─→ View Class Statistics
```

### **ADMIN FLOW:**
```
Login → Admin Dashboard
        ├─→ User Management (Add/Edit/Remove)
        ├─→ Course Management (Create/Assign)
        ├─→ School & Majors (Configure)
        ├─→ Academic Calendar (Set Semesters)
        ├─→ System Settings
        ├─→ Analytics & Reports
        └─→ Security & Logs
```

---

## 🛠️ TECHNICAL ARCHITECTURE

### **Frontend Structure**
```
app/
├─ layout.tsx                 (Root layout with language switcher)
├─ page.tsx                   (Landing)
├─ login/
│  └─ page.tsx
├─ student/
│  ├─ layout.tsx
│  ├─ dashboard/
│  ├─ courses/
│  ├─ timetable/
│  ├─ assets/
│  ├─ math-tools/
│  ├─ ide/
│  ├─ chinese-resources/
│  ├─ profile/
│  └─ notifications/
├─ teacher/
│  ├─ layout.tsx
│  ├─ dashboard/
│  ├─ courses/
│  ├─ materials/
│  ├─ students/
│  ├─ notifications/
│  └─ profile/
├─ admin/
│  ├─ layout.tsx
│  ├─ dashboard/
│  ├─ users/
│  ├─ schools/
│  ├─ courses/
│  ├─ calendar/
│  ├─ settings/
│  ├─ analytics/
│  └─ logs/
└─ api/
   ├─ auth/
   ├─ courses/
   ├─ materials/
   ├─ users/
   ├─ notifications/
   └─ admin/

components/
├─ Navigation/
├─ Sidebar/
├─ LanguageSwitcher/
├─ Dashboard/
├─ CourseCard/
├─ TimetableView/
├─ FileUpload/
└─ ...

lib/
├─ db.ts                      (MongoDB connection)
├─ auth.ts                    (Authentication logic)
├─ middleware.ts              (Role-based access)
├─ i18n.ts                    (Internationalization)
└─ validators.ts

public/
├─ i18n/
│  ├─ en.json
│  ├─ zh.json
│  ├─ fr.json
│  └─ ar.json
└─ images/
```

### **Key Technologies**
- **Frontend:** Next.js 14, React 18, TypeScript, TailwindCSS
- **Backend:** Next.js API Routes
- **Database:** MongoDB Atlas (free tier: 512MB, grows as needed)
- **File Storage:** Vercel Blob or AWS S3 (for PDFs, docs)
- **Auth:** NextAuth.js v5 or JWT
- **Math Tools:** Mathjs, Plotly.js, Three.js (3D)
- **IDE:** Embed Replit or Glitch API
- **Deployment:** Vercel (automatic from Git)

---

## 📦 EXTERNAL INTEGRATIONS (PHASE 2+)

| Feature             | Service       | Free Tier  | Use Case          |
| ------------------- | ------------- | ---------- | ----------------- |
| Math Graphing       | Plotly.js     | ✅ Yes      | 2D/3D plotting    |
| Calculus Solver     | Mathjs        | ✅ Yes      | Symbolic math     |
| Online IDE          | Replit API    | ⚠️ Limited | Python/C++/JS     |
| File Storage        | Vercel Blob   | ✅ 3GB free | PDFs, assignments |
| Email Notifications | SendGrid      | ✅ 100/day  | Announcements     |
| Database            | MongoDB Atlas | ✅ 512MB    | Main database     |
| Hosting             | Vercel        | ✅ Yes      | Deployment        |

---

## 🌍 INTERNATIONALIZATION (i18n)

**Phase 1:** English + Chinese (Simplified)  
**Phase 2:** French + Arabic

**Translation Files Example:**
```json
// en.json
{
  "dashboard.title": "Student Dashboard",
  "courses.enrolled": "Enrolled Courses",
  "common.logout": "Logout"
}

// zh.json
{
  "dashboard.title": "学生仪表板",
  "courses.enrolled": "已选课程",
  "common.logout": "登出"
}
```

**Implementation:** next-intl or i18next

---

## 🚀 MVP DELIVERY CHECKLIST (PHASE 1)

### **Week 1-2: Setup & Auth**
- [ ] Project init (Next.js, MongoDB connection)
- [ ] User schema & authentication (StudentID login)
- [ ] Basic role-based middleware
- [ ] Login/Logout pages

### **Week 3: Student Dashboard**
- [ ] Student profile form (School, Major, Year selection)
- [ ] Dashboard layout
- [ ] Enrolled courses display
- [ ] Notifications display

### **Week 4: Courses & Timetable**
- [ ] Course list page
- [ ] Course detail page
- [ ] Timetable view (weekly/monthly)
- [ ] Exam schedule display

### **Week 5: Assets Library**
- [ ] File upload (teacher)
- [ ] File download (student)
- [ ] File organization by course
- [ ] File preview (PDFs)

### **Week 6: Teacher Dashboard**
- [ ] Teacher login & course selection
- [ ] Teacher dashboard
- [ ] Course management page
- [ ] Student list per course

### **Week 7: Notifications & Polish**
- [ ] In-app notifications
- [ ] Teacher ability to send announcements
- [ ] Email notifications (basic)
- [ ] Responsive design fixes

### **Week 8: Testing & Deploy**
- [ ] User testing with 5-10 beta users
- [ ] Bug fixes & optimization
- [ ] Admin panel basics
- [ ] Deploy to Vercel

---

## 💾 IMPLEMENTATION STRATEGY

### **Database Initialization:**
1. Create MongoDB Atlas cluster (free tier)
2. Seed with 11 schools from your list
3. Add sample courses (5-10 per school)
4. Create sample users (3 students, 2 teachers, 1 admin)

### **Git Workflow:**
```
main (production) ← develop ← feature branches
- main: production-ready
- develop: integration branch
- features: individual-feature/*
```

### **Deployment:**
1. Connect GitHub repo to Vercel
2. Set environment variables (MongoDB URI, JWT secret, etc.)
3. Auto-deploy on push to main
4. Staging on develop branch

---

## 📊 ESTIMATED RESOURCE REQUIREMENTS

| Resource | Phase 1 | Phase 2 | Total |
|----------|---------|---------|-------|
| Developer Hours | 240-320 | 160-200 | 400-520 |
| MongoDB Storage | ~100MB | ~500MB | ~1GB |
| Vercel Bandwidth | Free tier | Paid (~20$/mo) | - |
| External APIs | Free | ~$30-50/mo | - |
| **Total Cost** | ~$0 | ~$300-600 (semester) | - |

---

## ⚠️ CRITICAL SUCCESS FACTORS

1. **Database Design First** - Spend time on schema, saves refactoring later
2. **Role-based Access** - Build middleware early, not as afterthought
3. **File Handling** - Plan storage strategy (Vercel Blob vs S3) before Phase 1
4. **Internationalization** - Implement i18n structure now, translations easy to add
5. **Authentication** - Use NextAuth.js, don't roll custom auth
6. **Testing** - Write tests for API routes (use Jest)
7. **Monitoring** - Set up error tracking (Sentry) early

---

## 🎓 PAGES TO ADD (That You Might Miss)

| Page                      | Category | When    | Why                       |
| ------------------------- | -------- | ------- | ------------------------- |
| **FAQ**                   | Public   | Phase 1 | For new user onboarding   |
| **Help/Support**          | Shared   | Phase 2 | Reduce support load       |
| **Announcements Feed**    | Shared   | Phase 2 | University-wide news      |
| **Student Directory**     | Student  | Phase 2 | Find classmates           |
| **Grade Tracker**         | Student  | Phase 3 | Track performance         |
| **Course Feedback**       | Student  | Phase 3 | Rate courses/teachers     |
| **Attendance Portal**     | Teacher  | Phase 2 | Track class attendance    |
| **Grade Management**      | Teacher  | Phase 3 | Upload grades             |
| **Bulk User Import**      | Admin    | Phase 1 | CSV upload for enrollment |
| **System Logs**           | Admin    | Phase 2 | Audit trail               |
| **File Quota Management** | Admin    | Phase 2 | Prevent abuse             |

---

## 📝 NEXT STEPS

1. **Review this plan** with your team
2. **Set up GitHub repo** with proper branching strategy
3. **Create MongoDB Atlas** free cluster
4. **Set up Vercel project** (connect GitHub)
5. **Build database schema** (start with users, courses, schools)
6. **Begin Phase 1** with authentication module
7. **Weekly sprints** with 2-3 features per week

---

## 📚 USEFUL RESOURCES

- **Next.js Docs:** https://nextjs.org/docs
- **MongoDB Guide:** https://docs.mongodb.com/
- **NextAuth.js:** https://next-auth.js.org/
- **TailwindCSS:** https://tailwindcss.com/
- **i18n Setup:** https://next-intl-docs.vercel.app/
- **Vercel Docs:** https://vercel.com/docs

---

**Questions to Ask Before Starting:**
1. Do you already have a student database (CSV/Excel)?
2. Is there an existing student ID format to follow?
3. What file types will be uploaded most (PDF, Word, Images)?
4. Do teachers need to grade assignments through the platform?
5. Should students be able to communicate with each other?

Good luck with the project (to me)! 🚀
