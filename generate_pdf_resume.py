#!/usr/bin/env python3
"""
Generates an executive, elegant vector A4 PDF resume for Arpita Sharma.
Pure Python, 100% compliant PDF-1.4 with zero external dependencies.
"""

class ResumePDFBuilder:
    def __init__(self):
        self.stream = []
        self.page_width = 595.28  # A4 width in pt
        self.page_height = 841.89 # A4 height in pt
        self.margin_x = 42.0
        self.current_y = 805.0

    def escape(self, text):
        return text.replace('\\', '\\\\').replace('(', '\\(').replace(')', '\\)')

    def text(self, x, y, string, font='F1', size=10, r=0.1, g=0.12, b=0.15):
        escaped = self.escape(string)
        self.stream.append(f"{r:.2f} {g:.2f} {b:.2f} rg BT /{font} {size} Tf {x:.1f} {y:.1f} Td ({escaped}) Tj ET")

    def line(self, x1, y1, x2, y2, width=0.75, r=0.7, g=0.75, b=0.8):
        self.stream.append(f"{r:.2f} {g:.2f} {b:.2f} RG {width:.2f} w {x1:.1f} {y1:.1f} m {x2:.1f} {y2:.1f} l S")

    def section_heading(self, title):
        self.current_y -= 14
        self.text(self.margin_x, self.current_y, title.upper(), font='F2', size=11, r=0.08, g=0.18, b=0.36)
        self.current_y -= 4
        self.line(self.margin_x, self.current_y, self.page_width - self.margin_x, self.current_y, width=0.8, r=0.2, g=0.3, b=0.5)
        self.current_y -= 12

    def build(self, filename='arpita_resume.pdf'):
        # Header
        self.text(self.margin_x, self.current_y, "ARPITA SHARMA", font='F2', size=22, r=0.06, g=0.12, b=0.25)
        self.current_y -= 14
        contact_line = "+91 8091192397  |  Shimla Rural, Himachal Pradesh  |  arpitaengineer08@gmail.com"
        self.text(self.margin_x, self.current_y, contact_line, font='F1', size=9.5, r=0.3, g=0.35, b=0.4)
        self.current_y -= 12
        links_line = "LinkedIn: linkedin.com/in/arpitasharma-9ala38lb7   |   GitHub: github.com/arpitaengineer08-source"
        self.text(self.margin_x, self.current_y, links_line, font='F1', size=9.5, r=0.15, g=0.35, b=0.7)
        self.current_y -= 8
        self.line(self.margin_x, self.current_y, self.page_width - self.margin_x, self.current_y, width=1.2, r=0.15, g=0.25, b=0.45)
        self.current_y -= 6

        # Education
        self.section_heading("Education")
        self.text(self.margin_x, self.current_y, "SRM University, Sonepat, Haryana", font='F2', size=10, r=0.1, g=0.15, b=0.2)
        self.text(self.page_width - self.margin_x - 110, self.current_y, "Expected Aug 2027", font='F3', size=9.5, r=0.35, g=0.4, b=0.45)
        self.current_y -= 12
        self.text(self.margin_x, self.current_y, "Bachelor of Technology in Computer Science & Engineering (Data Science & AI)", font='F1', size=9.5, r=0.2, g=0.25, b=0.3)
        self.current_y -= 12

        # Technical Skills
        self.section_heading("Technical Skills")
        skills = [
            ("Technical:", "Python, Data Structures & Algorithms, DBMS, Machine Learning, Data Analysis"),
            ("Development:", "Web Development (HTML5, CSS3, JS), Mobile App Development, Flask, REST APIs"),
            ("Languages:", "English (C2 Proficient), Hindi (C2 Native), French (Intermediate)")
        ]
        for cat, vals in skills:
            self.text(self.margin_x, self.current_y, cat, font='F2', size=9.5, r=0.15, g=0.2, b=0.25)
            self.text(self.margin_x + 85, self.current_y, vals, font='F1', size=9.5, r=0.2, g=0.25, b=0.3)
            self.current_y -= 13

        # Experience & Leadership
        self.section_heading("Experience & Leadership")
        
        # AI Lytics
        self.text(self.margin_x, self.current_y, "AI Lytics (Coding Society)", font='F2', size=10, r=0.1, g=0.15, b=0.2)
        self.text(self.page_width - self.margin_x - 90, self.current_y, "Sep 2025 - Present", font='F3', size=9.5, r=0.35, g=0.4, b=0.45)
        self.current_y -= 11
        self.text(self.margin_x, self.current_y, "Co-ordinator", font='F3', size=9.5, r=0.15, g=0.35, b=0.6)
        self.current_y -= 11
        self.text(self.margin_x + 12, self.current_y, "- Coordinated nationwide and campus technical events, workshops, and hackathons focused on AI/ML.", font='F1', size=9, r=0.25, g=0.3, b=0.35)
        self.current_y -= 10
        self.text(self.margin_x + 12, self.current_y, "- Managed team operations, peer mentoring sessions, and hands-on coding competitions.", font='F1', size=9, r=0.25, g=0.3, b=0.35)
        self.current_y -= 14

        # SPNF-HP
        self.text(self.margin_x, self.current_y, "SPNF-HP, Shimla", font='F2', size=10, r=0.1, g=0.15, b=0.2)
        self.text(self.page_width - self.margin_x - 90, self.current_y, "Jul 2024 - Aug 2024", font='F3', size=9.5, r=0.35, g=0.4, b=0.45)
        self.current_y -= 11
        self.text(self.margin_x, self.current_y, "Engineering Intern", font='F3', size=9.5, r=0.15, g=0.35, b=0.6)
        self.current_y -= 11
        self.text(self.margin_x + 12, self.current_y, "- Assisted engineering staff in software tasks and gained practical knowledge of production workflows.", font='F1', size=9, r=0.25, g=0.3, b=0.35)
        self.current_y -= 14

        # Projects
        self.section_heading("Projects")
        
        projects = [
            ("Amazon Clone Web App", "Flask, SQLite, HTML5, CSS3, JavaScript", "Full-stack e-commerce web platform featuring user authentication, session security, product catalogs, and cart workflows."),
            ("Emotion-Based Music Player", "Python, OpenCV, Computer Vision, Deep Learning", "Affective computing pipeline analyzing facial landmarks via webcam in real-time to curate tailored mood-enhancing playlists."),
            ("AI Chat Assistant for PDFs", "Python, NLP, Document Parsing, REST APIs", "Natural language Q&A assistant indexing multi-page research documents to deliver context-grounded citations without hallucination."),
            ("Hand Gesture Piano System", "Python, OpenCV, MediaPipe, Real-Time Audio", "Contactless virtual musical instrument tracking 21 skeletal hand coordinates in real time to synthesize harmonic piano notes."),
            ("Smart India Hackathon 2025 Hardware System", "Embedded Systems, Prototyping, IoT", "Engineered national-finalist embedded system as part of Team Vajraa under strict 36-hour physical hackathon constraints.")
        ]

        for p_title, p_tech, p_desc in projects:
            self.text(self.margin_x, self.current_y, p_title, font='F2', size=9.5, r=0.1, g=0.15, b=0.2)
            self.text(self.page_width - self.margin_x - 170, self.current_y, f"[{p_tech}]", font='F3', size=8.5, r=0.35, g=0.4, b=0.5)
            self.current_y -= 10
            self.text(self.margin_x + 12, self.current_y, f"- {p_desc}", font='F1', size=8.8, r=0.25, g=0.3, b=0.35)
            self.current_y -= 12

        # Honors & Achievements
        self.section_heading("Honors & Achievements")
        self.text(self.margin_x, self.current_y, "Finalist - Smart India Hackathon (SIH) 2025 (Hardware Edition)", font='F2', size=9.8, r=0.1, g=0.15, b=0.2)
        self.text(self.page_width - self.margin_x - 50, self.current_y, "2025", font='F3', size=9.5, r=0.35, g=0.4, b=0.45)
        self.current_y -= 11
        self.text(self.margin_x + 12, self.current_y, "- Represented Team Vajraa at GIET University, Gunupur in India's premier nationwide hackathon.", font='F1', size=9, r=0.25, g=0.3, b=0.35)
        self.current_y -= 10
        self.text(self.margin_x + 12, self.current_y, "- Recognized by judges for rapid physical prototyping, real-time debugging, and innovative problem solving.", font='F1', size=9, r=0.25, g=0.3, b=0.35)

        # Assemble PDF
        content = '\n'.join(self.stream).encode('latin1')
        objs = [
            b'<< /Type /Catalog /Pages 2 0 R >>',
            b'<< /Type /Pages /Kids [3 0 R] /Count 1 >>',
            f'<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {self.page_width} {self.page_height}] /Contents 4 0 R /Resources << /Font << /F1 5 0 R /F2 6 0 R /F3 7 0 R >> >> >>'.encode('latin1'),
            f'<< /Length {len(content)} >>\nstream\n'.encode('latin1') + content + b'\nendstream',
            b'<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>',
            b'<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold >>',
            b'<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Oblique >>'
        ]

        pdf = bytearray(b'%PDF-1.4\n')
        xref = [0]
        for obj in objs:
            xref.append(len(pdf))
            pdf.extend(f'{len(xref)-1} 0 obj\n'.encode('latin1') + obj + b'\nendobj\n')

        xref_pos = len(pdf)
        pdf.extend(f'xref\n0 {len(xref)}\n0000000000 65535 f \n'.encode('latin1'))
        for offset in xref[1:]:
            pdf.extend(f'{offset:010d} 00000 n \n'.encode('latin1'))

        pdf.extend(f'trailer\n<< /Size {len(xref)} /Root 1 0 R >>\nstartxref\n{xref_pos}\n%%EOF\n'.encode('latin1'))

        with open(filename, 'wb') as f:
            f.write(pdf)
        print(f"Successfully generated {filename} ({len(pdf)} bytes)")

if __name__ == '__main__':
    builder = ResumePDFBuilder()
    builder.build('arpita_resume.pdf')
