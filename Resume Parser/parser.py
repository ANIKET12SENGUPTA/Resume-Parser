import re

def parse_resume(text: str):
    lines = [l.strip() for l in text.split("\n") if l.strip()]

    # ---------- NAME ----------
    name = "Name not found"

    blacklist = {
        "resume","curriculum vitae","cv","profile","summary",
        "experience","education","skills","contact"
    }

    for line in lines[:10]:
        words = line.split()

        if 2 <= len(words) <= 3:
            if not any(char.isdigit() for char in line):
                if line.lower() not in blacklist:
                    if all(word[0].isupper() for word in words):
                        name = line
                        break

    # ---------- EMAIL ----------
    emails = re.findall(
        r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b',
        text
    )

    # ---------- PHONE ----------
    phones = re.findall(
        r'(?:\+?\d{1,3}[\s-]?)?(?:\(?\d{2,4}\)?[\s-]?)?\d{6,10}',
        text
    )

    # ---------- UNIVERSAL SKILL BANK ----------
    skill_bank = {
    # Technology
    "python","java","c","c++","c#","javascript","typescript","go","rust","kotlin","swift","dart","r","matlab","scala",
    "html","css","react","angular","vue","nodejs","django","flask","fastapi",
    "sql","mysql","postgresql","mongodb","redis","oracle",
    "machine learning","deep learning","nlp","data science","data analysis",
    "tensorflow","pytorch","scikit-learn","pandas","numpy",
    "aws","azure","gcp","docker","kubernetes","git",
    "streamlit","tableau","power bi","excel",

    # Business
    "marketing","digital marketing","seo","sem","branding","sales",
    "business analysis","project management","product management",
    "market research","customer service","crm","account management",

    # Finance
    "accounting","financial analysis","budgeting","taxation","auditing",
    "investment","risk management","banking","bookkeeping",

    # Healthcare
    "patient care","clinical research","nursing","pharmacy","medical coding",
    "healthcare management","diagnostics","surgery","public health",

    # Education
    "teaching","curriculum development","classroom management",
    "academic research","lesson planning","student mentoring",

    # Design / Creative
    "graphic design","photoshop","illustrator","figma","ui design","ux design",
    "video editing","animation","photography","content creation",

    # Writing
    "copywriting","technical writing","editing","blogging","journalism",
    "content writing","storytelling",

    # Engineering
    "mechanical engineering","civil engineering","electrical engineering",
    "cad","autocad","solidworks","manufacturing","quality control",

    # Science
    "biology","chemistry","physics","laboratory research","data modeling",
    "statistical analysis",

    # Soft Skills
    "communication","leadership","teamwork","problem solving",
    "critical thinking","adaptability","time management",
    "decision making","negotiation","presentation",

    # Languages
    "english","spanish","french","german","hindi","bengali","mandarin",
    "arabic","japanese","korean"
    
    # Legal
    "legal research","litigation","contract drafting","compliance","corporate law","intellectual property",

    # HR
    "recruitment","talent acquisition","payroll","employee relations","hr management","performance management",

    # Operations
    "operations management","supply chain","logistics","inventory management","procurement","vendor management",

    # Hospitality
    "hotel management","food service","customer relations","event management","tourism","front desk",

    # Media
    "video production","broadcasting","script writing","media relations","public relations",

    # Architecture
    "architecture","urban planning","revit","3d modeling","construction management",

    # Agriculture
    "agriculture","crop management","soil analysis","farm management","agronomy",

    # Psychology / Social Work
    "counseling","psychology","mental health","social work","behavioral analysis",

    # Sports
    "coaching","fitness training","sports management","nutrition","physical training",

    # Administration
    "administration","office management","documentation","data entry","scheduling","record management"
    
    }

    text_lower = text.lower()
    skills = []

    for skill in skill_bank:
        if skill in text_lower:
            skills.append(skill.title())

    skills = list(set(skills))[:12]

    return {
        "name": name,
        "email": emails[:2],
        "phone": phones[:2],
        "skills": skills,
    }