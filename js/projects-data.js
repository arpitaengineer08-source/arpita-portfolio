/**
 * Portfolio Projects Data
 * Arpita Sharma - Data Science & AI Engineer
 */

const projectsData = [
  {
    id: "sih-hardware",
    title: "Smart India Hackathon 2025 Project",
    subtitle: "Hardware Edition National Finalist",
    category: "hardware",
    categoryLabel: "Hardware & IoT",
    featured: true,
    badge: "SIH '25 Finalist",
    badgeColor: "amber",
    shortDesc: "National finalist hardware innovation built with Team Vajraa at GIET University, featuring real-time sensor processing and rapid prototype engineering.",
    fullDesc: "Represented Team Vajraa as a National Finalist at the prestigious Smart India Hackathon (SIH) 2025 Hardware Edition hosted at GIET University, Gunupur. Built an end-to-end hardware system designed to tackle critical real-world challenges through rapid prototyping, sensor fusion, robust system design, and rigorous stress testing under strict 36-hour hackathon constraints. Highly praised by judges for swift execution and innovative problem solving.",
    tech: ["Hardware Prototyping", "Embedded Systems", "Sensors & Actuators", "Python", "C++", "IoT Protocols"],
    highlights: [
      "National Finalist out of thousands of teams across India",
      "End-to-end embedded system designed and assembled in 36 hours",
      "Real-time sensor telemetry and data acquisition",
      "Praised by jury for strong execution and pragmatic problem-solving"
    ],
    github: "https://github.com/arpitaengineer08-source",
    liveDemo: null,
    icon: "cpu"
  },
  {
    id: "emotion-music-player",
    title: "Emotion-Based Music Player",
    subtitle: "Computer Vision & Affective Computing",
    category: "ai",
    categoryLabel: "AI & Computer Vision",
    featured: true,
    badge: "Computer Vision",
    badgeColor: "cyan",
    shortDesc: "Real-time affective AI system using facial expression analysis to dynamically detect mood states and recommend tailored music playlists.",
    fullDesc: "Engineered an intelligent computer vision application that captures video feed via webcam, analyzes facial landmarks using deep convolutional models, and predicts emotional states (happy, sad, neutral, focused). Integrates with music recommendation services to immediately generate custom playback queues that match or enhance the listener's mood.",
    tech: ["Python", "OpenCV", "Machine Learning", "Deep Learning", "NumPy", "Audio APIs"],
    highlights: [
      "Real-time facial landmark extraction and low-latency classification",
      "Adaptive mood-to-music recommendation mapping",
      "Intuitive web/desktop dashboard with live feedback overlay",
      "Robust detection across diverse lighting conditions"
    ],
    github: "https://github.com/arpitaengineer08-source",
    liveDemo: null,
    icon: "music"
  },
  {
    id: "ai-pdf-chat",
    title: "AI Chat Assistant for PDFs",
    subtitle: "Natural Language Processing & Document AI",
    category: "ai",
    categoryLabel: "NLP & AI",
    featured: true,
    badge: "NLP & GenAI",
    badgeColor: "purple",
    shortDesc: "Intelligent document conversational assistant that parses complex multi-page PDFs to deliver contextual, hallucination-free answers.",
    fullDesc: "Created an NLP-driven document assistant capable of ingesting complex PDF documents, extracting textual and tabular data, chunking context, and answering user questions with high fidelity and citations. Employs modern semantic search and natural language processing to empower users to converse directly with research papers, reports, and manuals.",
    tech: ["Python", "NLP", "Flask", "Vector Search", "Document Parsing", "REST API"],
    highlights: [
      "Parses multi-page PDFs with text and tabular data extraction",
      "Context-aware question answering with direct page citations",
      "Interactive conversational web interface with query history",
      "Optimized document indexing for fast response times"
    ],
    github: "https://github.com/arpitaengineer08-source",
    liveDemo: null,
    icon: "file-text"
  },
  {
    id: "hand-gesture-piano",
    title: "Hand Gesture Piano System",
    subtitle: "Real-Time Computer Vision & Audio Synthesis",
    category: "vision",
    categoryLabel: "Computer Vision",
    featured: false,
    badge: "Computer Vision",
    badgeColor: "emerald",
    shortDesc: "Interactive virtual instrument tracking 21 hand landmarks to translate mid-air finger coordinates into synthesized musical notes.",
    fullDesc: "Designed an interactive contactless musical instrument leveraging computer vision and real-time hand tracking. Uses webcam video to track 21 hand keypoints in 3D space, mapping fingertip positions and hover/strike gestures to virtual piano keys and synthesizing harmonic frequencies with minimal latency.",
    tech: ["Python", "OpenCV", "MediaPipe", "Audio Synthesis", "Real-Time Tracking"],
    highlights: [
      "Tracks 21 hand landmarks in real time with high precision",
      "Sub-50ms latency from gesture strike to audio output",
      "Virtual augmented piano interface rendered on camera feed",
      "Touchless interactive human-computer interaction (HCI)"
    ],
    github: "https://github.com/arpitaengineer08-source",
    liveDemo: null,
    icon: "activity"
  },
  {
    id: "amazon-clone",
    title: "Amazon Clone Web Application",
    subtitle: "Full-Stack E-Commerce Platform",
    category: "web",
    categoryLabel: "Full-Stack Web",
    featured: false,
    badge: "Full-Stack",
    badgeColor: "blue",
    shortDesc: "End-to-end e-commerce application with Flask, relational database integration, user authentication, and interactive product management.",
    fullDesc: "Developed a full-stack e-commerce web platform inspired by Amazon. Implemented comprehensive authentication workflows (signup, login, session security), database schemas for products and orders, cart management, and dynamic filtering by category with a responsive client-side interface.",
    tech: ["Python", "Flask", "HTML5", "CSS3", "JavaScript", "DBMS", "Jinja2"],
    highlights: [
      "Secure user authentication and session management",
      "Relational database schema for users, products, and transactions",
      "Interactive shopping cart with real-time total calculation",
      "Responsive UI designed for both mobile and desktop screens"
    ],
    github: "https://github.com/arpitaengineer08-source",
    liveDemo: null,
    icon: "shopping-bag"
  }
];

if (typeof module !== "undefined" && module.exports) {
  module.exports = projectsData;
}
