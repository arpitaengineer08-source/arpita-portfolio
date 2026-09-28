# Arpita Sharma — Professional Portfolio Website

A sleek, modern, high-performance, and responsive portfolio website designed for **Arpita Sharma** — Computer Science & Engineering (Data Science & AI) student at SRM University, SIH 2025 National Finalist, and AI Developer.

---

## 🌟 Key Features

- **Modern Glassmorphic Dark & Light Theme**: Built-in toggle with automatic system theme detection and persistent `localStorage` preference.
- **Hero & Profile Showcase**:
  - Live availability badge (`Open to Opportunities & Collaborations`).
  - Sleek tech avatar monogram `AS` (ready to be swapped with a headshot).
  - Quick metric counters (Projects, SIH '25 Finalist, Languages).
- **Interactive Project Showcase**:
  - Category filters: *All Projects*, *AI & NLP*, *Computer Vision*, *Full-Stack Web*, *Hardware & IoT*.
  - Detailed case study modals with architectural highlights and technology tags.
  - Sourced directly from `js/projects-data.js` for effortless updates.
- **Career & Leadership Timeline**:
  - Highlights experience and leadership with *AI Lytics Coding Society* and *SPNF-HP*.
- **National Recognition Feature**:
  - Dedicated spotlight for *Smart India Hackathon (SIH) 2025 Hardware Edition Finalist* with *Team Vajraa* at *GIET University, Gunupur*.
- **Interactive Contact Cards**:
  - One-click copy buttons for email (`arpitaengineer08@gmail.com`) and phone (`+91 8091192397`) with animated toast feedback.
  - Direct links to GitHub (`arpitaengineer08-source`) and LinkedIn.
- **Fast Navigation & Resume Access**:
  - Seamless header navigation with one-click direct PDF resume download.
- **Zero Build Tools Required**:
  - Blazing fast vanilla HTML5, CSS3, and JavaScript — no `npm install` needed to run or deploy.


---

## 🚀 Quick Start / Local Preview

You can open the website right in your browser using any of the following methods:

### Option 1: Direct File Opening
Simply double-click `index.html` in your file explorer, or open it in your favorite browser (Chrome, Safari, Edge, Firefox).

### Option 2: Using Python (Recommended)
In this folder, run:
```bash
python3 -m http.server 3000
```
Then open [http://localhost:3000](http://localhost:3000) in your browser.

### Option 3: VS Code Live Server
If you use VS Code, install the **Live Server** extension, right-click `index.html`, and select **Open with Live Server**.

---

## 🌐 Free Deployment Options

### 1. Deploy to GitHub Pages (Recommended)
1. Push this repository to your GitHub account (`arpitaengineer08-source`).
2. Go to **Settings** > **Pages** in your repository.
3. Under **Branch**, select `main` and root `/`.
4. Click **Save**. Your site will be live at `https://arpitaengineer08-source.github.io/arpita-portfolio/` in seconds!

### 2. Deploy to Vercel or Netlify
- Drag and drop this folder onto [Netlify Drop](https://app.netlify.com/drop) or import the GitHub repository in [Vercel](https://vercel.com) — zero configuration needed!

---

## 🛠️ How to Customize

### Adding or Modifying Projects
All project data lives in [`js/projects-data.js`](js/projects-data.js). To add a new project, simply add a new object to `projectsData`:
```javascript
{
  id: "my-new-project",
  title: "Project Name",
  subtitle: "Domain / Category Subtitle",
  category: "ai", // "ai", "vision", "web", or "hardware"
  categoryLabel: "AI & Deep Learning",
  badge: "New",
  badgeColor: "cyan",
  shortDesc: "Summary for card display...",
  fullDesc: "Detailed case study description...",
  tech: ["Python", "PyTorch", "Flask"],
  highlights: ["Highlight 1", "Highlight 2"],
  github: "https://github.com/arpitaengineer08-source/your-repo",
  liveDemo: null
}
```

### Swapping the Avatar Monogram with a Photo
1. Place your headshot photo (e.g., `arpita.jpg`) into the `assets/images/` folder.
2. In `index.html`, locate:
   ```html
   <div class="avatar-inner">
     <span class="avatar-monogram">AS</span>
   </div>
   ```
3. Replace `<span class="avatar-monogram">AS</span>` with:
   ```html
   <img src="assets/images/arpita.jpg" alt="Arpita Sharma" style="width: 100%; height: 100%; object-fit: cover;">
   ```

---

## 📁 Project Structure

```
arpita-portfolio/
├── index.html           # Main semantic HTML structure
├── css/
│   ├── style.css        # Themes (dark/light), layout, typography, hero
│   └── components.css   # Modals, project cards, timeline, form, toast
├── js/
│   ├── projects-data.js # Structured project case studies
│   └── main.js          # Theme toggle, filter logic, modals, copy utils
├── assets/
│   ├── icons/           # SVG icons
│   └── images/          # Images and headshots
├── arpita_resume.docx   # Original resume document (downloadable)
└── README.md            # Documentation and deployment guide
```
