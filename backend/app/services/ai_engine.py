from typing import Optional

DEPARTMENT_KEYWORDS = {
    "Police": ["police", "crime", "theft", "assault", "murder", "dacoity", "cyber", "chor", "chori", "jaach", "jail", "fir", "criminal"],
    "Water Supply": ["water", "tap", "pipe", "nala", "supply", "leak", "pani", "paanee", "paani", "pipeline", "jale", "sewage", "drainage"],
    "Electricity": ["electricity", "light", "meter", "current", "power", "line", "bijli", "bijlee", "supply", "blackout", "strom"],
    "Municipal Corporation": ["road", "drain", "garbage", "swachhata", "street", "park", "sadak", "nali", "safai", "pothole", "maidan", "waste"],
    "Health Department": ["hospital", "doctor", "health", "medical", "clinic", "aspatal", "bimari", "dawai", "vaccine", "medicine", "surgery"],
    "Education": ["school", "college", "university", "student", "teacher", "admission", "exam", "fees", "shiksha"],
    "Road & Highways": ["road", "highway", "toll", "construction", "pothole", "traffic", "accident"],
    "Transport": ["bus", "transport", "ticket", "vehicle", "auto", "taxi", "registration"],
    "Revenue": ["land", "property", "document", "revenue", "record", "zameen", "kagaz"],
    "Urban Development": ["development", "construction", "building", "planning", "project"],
    "Agriculture": ["farm", "crop", "agriculture", "fertilizer", "kheti", "fasal"],
    "Labour": ["labour", "labor", "worker", "employment", "wage"],
    "Social Welfare": ["welfare", "pension", "benefit", "scheme", "ration"],
    "Banking": ["bank", "account", "loan", "credit", "debit"],
    "RTO": ["vehicle", "registration", "rto", "driving", "license"],
    "Postal": ["post", "courier", "mail", "letter", "parcel"],
    "Fire Safety": ["fire", "emergency", "rescue", "safety", "danger"],
    "Sanitation": ["sanitation", "waste", "garbage", "cleaning", "sewage"],
    "Parks & Recreation": ["park", "recreation", "garden", "playground", "sports"],
    "Taxation": ["tax", "income", "gst", "toll", "duty"],
    "Food Safety": ["food", "restaurant", "hotel", "hygiene", "contamination"],
    "Consumer Protection": ["consumer", "complaint", "fraud", "defective", "quality"],
    "Housing": ["housing", "slum", "residential", "apartment", "building"],
    "Telecom": ["phone", "internet", "mobile", "broadband", "network"],
    "Grievance Redressal": ["grievance", "complaint", "issue", "problem", "concern"],
    "Sports": ["sports", "stadium", "facility", "committee", "khel"],
    "Tourism": ["tourism", "tourist", "monument", "heritage", "travel"],
    "Community Development": ["community", "program", "event", "assembly"],
    "Disability Services": ["disability", "disabled", "wheelchair", "assistance"],
    "Women Empowerment": ["women", "safety", "harassment", "violence", "mahila"],
    "Child Welfare": ["child", "kid", "minor", "protection", "abuse"],
    "Disaster Management": ["disaster", "flood", "earthquake", "emergency", "relief"],
    "Environment": ["environment", "pollution", "air", "water", "climate", "tree"],
    "Wildlife": ["wildlife", "animal", "forest", "conservation", "sanctuary"],
    "Flood Control": ["flood", "rain", "inundation", "waterlogging"],
    "Public Works": ["public", "infrastructure", "bridge", "construction"],
    "Minority Affairs": ["minority", "community", "religious", "ethnic"],
    "Veterans Affairs": ["veteran", "military", "soldier", "armed"],
    "Pension": ["pension", "retirement", "gratuity", "allowance"],
    "Audit": ["audit", "finance", "compliance", "account"],
    "Cyber Crime": ["cyber", "fraud", "hacking", "scam", "online"],
    "Traffic": ["traffic", "accident", "signal", "vehicle", "fine"],
}

PRIORITY_KEYWORDS = {
    "High": ["urgent", "danger", "emergency", "critical", "immediate", "now", "turant", "jaldi", "tatkal", "turante", "bahut zaroori", "bahut bura", "life"],
    "Low": ["minor", "small", "non-urgent", "suggestion", "sujaav", "sujhav", "chhota", "kam mahatvapurn"],
}

DEPARTMENT_INFO = {
    "Police": {"name": "Police Department", "contact": "🚔 Emergency: 100 | Non-emergency: 1930", "redressal_link": "https://crimesurvey.delhi.gov.in/", "suggestions": ["File an FIR at nearest police station", "Keep all evidence copies", "Follow up every 48 hours", "Escalate to commissioner if no action in 10 days", "Preserve CCTV footage", "Document witness statements"]},
    "Water Supply": {"name": "Water Supply Department", "contact": "💧 Delhi JJM: 1916 | Municipal Corporation", "redressal_link": "https://www.delhijal.gov.in/", "suggestions": ["Report with meter number and photos", "Check water cuts scheduled", "Request meter inspection", "Document shortage duration", "Follow up every 48 hours", "Claim compensation for 24+ hour outage"]},
    "Electricity": {"name": "Electricity Distribution", "contact": "⚡ Emergency: 1912 | DISCOM Helpline", "redressal_link": "https://www.delhipower.gov.in/", "suggestions": ["Provide consumer number and meter reading", "Check if issue is localized", "Request technical inspection", "File for SLA compensation", "Record outage hours", "Request detailed inspection report"]},
    "Municipal Corporation": {"name": "Municipal Corporation", "contact": "🏛️ Toll-free: 1800-11-1111 | MCD Office", "redressal_link": "https://mcdonline.nic.in/", "suggestions": ["Provide GPS coordinates and photos", "Report via online portal", "Request repair timeline", "File RTI for budget allocation", "Escalate to commissioner", "Involve local ward councilor"]},
    "Health Department": {"name": "Health & Hospital Department", "contact": "🏥 Emergency: 108 | Hospital Helpline", "redressal_link": "https://health.delhi.gov.in/", "suggestions": ["Contact hospital director immediately", "Get complaint acknowledgment", "Request medical records", "File with Medical Council if negligence", "Get expert second opinion", "Document all communications"]},
    "Education": {"name": "Education Department", "contact": "📚 District Education Officer | State Board", "redressal_link": "https://education.delhi.gov.in/", "suggestions": ["Submit to Principal first", "Request written acknowledgment", "Provide admission proofs", "Escalate to Commissioner", "File with Consumer Court", "Involve PTA for systemic issues"]},
    "Road & Highways": {"name": "Road & Highways Department", "contact": "🚗 PWD | Highway Authority: 1800-234-5555", "redressal_link": "https://www.highways.gov.in/", "suggestions": ["Report with GPS and landmark", "Submit high-quality photos/video", "Request maintenance timeline", "File accident report with police", "Claim insurance compensation", "Escalate via local representative"]},
    "Transport": {"name": "Transport Department", "contact": "🚌 RTO: 1800-11-1500 | Transport Commissioner", "redressal_link": "https://transport.delhi.gov.in/", "suggestions": ["Provide PUC and insurance details", "Report bus/auto with route number", "Keep tickets as evidence", "File with consumer court", "Request fitness certificate", "Escalate to Chief Transport Commissioner"]},
    "Revenue": {"name": "Revenue Department", "contact": "📋 Tehsildar Office | District Collector", "redressal_link": "https://revenue.delhi.gov.in/", "suggestions": ["Provide survey number and property details", "Request official land records", "Provide sale deeds", "File RTI for transfer history", "Escalate to District Collector", "Get legal opinion for disputes"]},
    "Urban Development": {"name": "Urban Development Authority", "contact": "🏗️ DDA: 1800-11-4444 | Municipal Corporation", "redressal_link": "https://dda.org.in/", "suggestions": ["Provide project details and DDA reference", "Request status and timeline", "File RTI for budget and contractor", "Verify property allocation", "Escalate to Vice-Chairperson", "Consult lawyer for disputes"]},
    "Agriculture": {"name": "Agriculture & Farmer Services", "contact": "🌾 District Agriculture Officer | Kisan: 1800-180-1551", "redressal_link": "https://agriculture.delhi.gov.in/", "suggestions": ["Provide land ownership proof", "Report crop loss with officer", "Apply for crop insurance (72 hours)", "Request soil testing", "File for MSP if price below rate", "Escalate to District Collector"]},
    "Labour": {"name": "Labour & Employment Department", "contact": "👷 Labour Commissioner: 1800-11-2234", "redressal_link": "https://labour.delhi.gov.in/", "suggestions": ["Provide employment contract and slips", "File for wage theft complaint", "Report workplace hazards", "Request inspection report", "File at Labour Court", "Escalate to Chief Labour Commissioner"]},
    "Social Welfare": {"name": "Social Welfare Department", "contact": "🤝 District Welfare Officer | State Board", "redressal_link": "https://welfare.delhi.gov.in/", "suggestions": ["Provide BPL/APL card and Aadhaar", "Check pension status", "Apply for widow/disability pension", "File RTI for eligibility", "Escalate through district administration", "Use welfare helpline for issues"]},
    "Banking": {"name": "Banking & Financial Services", "contact": "🏦 Bank Manager | RBI Ombudsman: 1800-22-2266", "redressal_link": "https://rbidocs.rbi.org.in/", "suggestions": ["Provide account and transaction details", "File formal complaint with acknowledgment", "Report unauthorized transactions (30 days)", "File RTI for loan criteria", "Escalate to RBI Ombudsman", "Report suspicious charges"]},
    "RTO": {"name": "Regional Transport Office", "contact": "🚗 RTO: 1800-11-1500 | VAHAN Portal", "redressal_link": "https://vahan.parivahan.gov.in/", "suggestions": ["Provide vehicle registration number", "Submit medical fitness certificate", "Apply renewal 30 days before expiry", "Request inspection report", "Appeal license suspension", "Report duplicate registration"]},
    "Postal": {"name": "Postal Services", "contact": "📮 Post Office: 1800-11-6666 | Regional Office", "redressal_link": "https://indiapost.gov.in/", "suggestions": ["Report with proof of posting", "For COD: verify sender complaint", "File claim within 30 days", "Request delivery certificate", "Escalate to Regional Office", "Use online portal for tracking"]},
    "Fire Safety": {"name": "Fire Safety & Emergency Services", "contact": "🚒 Emergency: 101 | Fire Station", "redressal_link": "https://fire.delhi.gov.in/", "suggestions": ["Report hazard with detailed location", "Request fire safety certificate", "For accidents: file with police", "Lodge FIR if rescue delayed", "Claim property loss through insurance", "Escalate to Fire Commissioner"]},
    "Sanitation": {"name": "Sanitation & Waste Management", "contact": "♻️ MCD: 1800-11-1111 | Sanitation Officer", "redressal_link": "https://swachhbharat.mygov.in/", "suggestions": ["Report with location and severity", "Request collection schedule", "Report health hazard to officer", "File RTI for disposal site", "Escalate to MCD Commissioner", "Organize community awareness"]},
    "Parks & Recreation": {"name": "Parks & Recreation Department", "contact": "🌳 Parks Officer | Municipal Corp Recreation Cell", "redressal_link": "https://mcdonline.nic.in/", "suggestions": ["Report maintenance issues with photos", "Request facility schedule", "Report discrimination in enrollment", "File complaint for fund misuse", "Request program details in writing", "Escalate through block administration"]},
    "Taxation": {"name": "Taxation & Revenue Department", "contact": "💰 Income Tax: 1800-180-1961 | State Tax", "redressal_link": "https://www.incometax.gov.in/", "suggestions": ["Provide PAN and assessment order", "File appeal within 30 days", "Request assessment file copy", "Apply for refund with bank details", "Escalate to Commissioner", "Consult tax consultant"]},
    "Food Safety": {"name": "Food Safety & Quality Assurance", "contact": "🍽️ FSSAI: 1800-11-4646 | Food Inspector", "redressal_link": "https://www.fssai.gov.in/", "suggestions": ["Report with shop details and proof", "Request inspection and report", "File if food certificate missing", "File consumer court with medical report", "Request public health notice", "Report poisoning to health dept"]},
    "Consumer Protection": {"name": "Consumer Protection Authority", "contact": "👥 District Court | DCCRN: 1800-180-9191", "redressal_link": "https://consumeronline.nic.in/", "suggestions": ["Keep bills and warranty cards", "File within 2 years", "Request refund/replacement with proof", "Escalate to state court", "Submit to national court if ₹1cr+", "Claim compensation with evidence"]},
    "Housing": {"name": "Housing & Slum Development", "contact": "🏠 District Housing Officer | Slum Board", "redressal_link": "https://housing.delhi.gov.in/", "suggestions": ["Provide address proof and BPL card", "Submit residence proof for rehab", "Request allotment status", "File RTI for quota and beneficiary list", "Escalate to Housing Commissioner", "Engage lawyer for disputes"]},
    "Telecom": {"name": "Telecom Services", "contact": "📱 TRAI: 1800-180-1100 | Service Provider", "redressal_link": "https://www.trai.gov.in/", "suggestions": ["Provide account and service details", "Report dropouts with test results", "Request bill breakdown", "File with TRAI if unresponsive", "Request plan downgrade", "Claim SLA compensation"]},
    "Grievance Redressal": {"name": "General Grievance Redressal", "contact": "📋 CPGRAMS: 1916 | District Officer", "redressal_link": "https://cpgrams.nic.in/", "suggestions": ["File at nearest Service Centre", "Use CPGRAMS for escalation", "Keep communication records", "Request RTI for status", "Follow up within 30 days", "Escalate through MLA/MP"]},
    "Sports": {"name": "Sports & Youth Affairs", "contact": "⚽ District Sports Officer | Youth Cell", "redressal_link": "https://sports.delhi.gov.in/", "suggestions": ["Contact district sports office", "Request coaching enrollment details", "File complaint with evidence", "Request facility schedule", "Apply for sports scholarship", "Escalate to Sports Minister"]},
    "Tourism": {"name": "Tourism Department", "contact": "✈️ Tourism Board: 1800-11-4500 | Officer", "redressal_link": "https://tourism.delhi.gov.in/", "suggestions": ["Report maintenance with location", "Request visitor info and facilities", "File against tour operators", "Report unsanitary conditions", "Request preservation details", "Escalate to Chief Tourism Secretary"]},
    "Community Development": {"name": "Community Development", "contact": "👫 District Officer | Community Center", "redressal_link": "https://community.delhi.gov.in/", "suggestions": ["Provide community details", "Request facility booking schedule", "Report discrimination", "File complaint for fund misuse", "Request program details", "Escalate through block admin"]},
    "Disability Services": {"name": "Disability Services & Support", "contact": "♿ Welfare Board | Disability Commissioner", "redressal_link": "https://www.disabilityindia.org/", "suggestions": ["Apply for disability certificate", "Request infrastructure compliance", "File for accessibility violations", "Apply for disability pension", "Request job priority", "Escalate to Commissioner"]},
    "Women Empowerment": {"name": "Women Safety & Empowerment", "contact": "👩 Helpline: 181 | District Officer", "redressal_link": "https://wcd.delhi.gov.in/", "suggestions": ["Report to police immediately", "Contact women's shelter", "Request police protection", "File in women's court", "Apply for maintenance/custody", "Escalate to State Commission"]},
    "Child Welfare": {"name": "Child Welfare & Protection", "contact": "👶 Childline: 1800-425-4949", "redressal_link": "https://childline.org.in/", "suggestions": ["Report abuse to CWPC", "File FIR if in danger", "Request protection order", "Apply for guardianship", "File for adoption", "Escalate to National Commission"]},
    "Disaster Management": {"name": "Disaster Management & Relief", "contact": "🚨 Helpline: 1800-11-1111 | Emergency: 112", "redressal_link": "https://ddma.delhi.gov.in/", "suggestions": ["Report damage with photos", "Request relief eligibility", "File damage assessment", "Apply for shelter and ration", "Request insurance claim help", "Escalate to NDMA"]},
    "Environment": {"name": "Environment & Pollution Control", "contact": "🌍 Pollution Board: 1800-11-6464", "redressal_link": "https://www.delhipollution.nic.in/", "suggestions": ["Report pollution source", "Request air/water quality test", "File RTI for compliance certificates", "Report illegal waste disposal", "Escalate to National Green Tribunal", "Support community petitions"]},
    "Wildlife": {"name": "Wildlife Protection & Conservation", "contact": "🦁 Department: 1800-11-1515 | Forest Office", "redressal_link": "https://wildlife.delhi.gov.in/", "suggestions": ["Report trafficking immediately", "Request sanctuary accessibility", "File for illegal deforestation", "Report animal cruelty", "Request encroachment action", "Escalate to MOEF"]},
    "Flood Control": {"name": "Flood Control & Water Management", "contact": "🌊 Relief: 1800-11-2222 | Drainage Officer", "redressal_link": "https://ddma.delhi.gov.in/", "suggestions": ["Report waterlogging with depth", "Submit blockage complaint", "Request flood-proofing measures", "Apply for relief and CRZ cert", "Request flood warning system", "Escalate to District Collector"]},
    "Public Works": {"name": "Public Works Department", "contact": "🏗️ PWD Office | Executive Engineer", "redressal_link": "https://pwd.delhi.gov.in/", "suggestions": ["Report defect with location", "Request maintenance schedule", "File RTI for project details", "Report quality issues", "Escalate to Chief Engineer", "Request structural audit"]},
    "Minority Affairs": {"name": "Minority Affairs & Community", "contact": "🕌 Commission: 1800-11-3333", "redressal_link": "https://www.minorityaffairs.gov.in/", "suggestions": ["Report violence to police", "File with National Commission", "Request investigation", "Apply for development schemes", "Request worship place protection", "Escalate to State Commission"]},
    "Veterans Affairs": {"name": "Veterans Affairs & Military", "contact": "🎖️ Helpline: 1800-11-5555 | Defense", "redressal_link": "https://indianarmy.nic.in/", "suggestions": ["Request pension status", "Apply for medical treatment", "Request war widow pension", "File compensation claim", "Request military hospital access", "Escalate to Chief of Defense"]},
    "Pension": {"name": "Pension & Retirement Benefits", "contact": "💼 Pension Board: 1800-11-7777", "redressal_link": "https://pensioners.gov.in/", "suggestions": ["Provide pension account number", "Request payment verification", "Apply for pension increase", "Request discontinuation reason", "File appeal within 60 days", "Escalate to Chief Pension Officer"]},
    "Audit": {"name": "Audit & Finance Compliance", "contact": "📊 Audit Office | Comptroller General", "redressal_link": "https://cag.gov.in/", "suggestions": ["Report financial irregularity", "Provide evidence documentation", "Request audit report", "File RTI for budget", "Escalate to CAG", "Report fraud to CBI"]},
    "Cyber Crime": {"name": "Cyber Crime & Digital Security", "contact": "🔒 Cybercrime: 155260 | Cyber Cell", "redressal_link": "https://cybercrime.gov.in/", "suggestions": ["Report fraud with transaction IDs", "File FIR if account compromised", "Request money recovery", "Report phishing to ISP", "Request security audit", "Escalate to national unit"]},
    "Traffic": {"name": "Traffic & Road Safety", "contact": "🚦 Traffic Police: 1968 | Accident Cell", "redressal_link": "https://traffic.delhi.gov.in/", "suggestions": ["Report violation with evidence", "File accident report with police", "Request insurance assistance", "File RTI for signal maintenance", "Appeal fine within 30 days", "Escalate to Traffic Commissioner"]},
}

CATEGORY_GUIDANCE = {
    "Service Disruption": {
        "title": "Service Disruption Issue",
        "action": "Request immediate service restoration with timeline",
        "links": ["https://cpgrams.nic.in/", "https://www.india.gov.in/"],
        "steps": ["Contact service provider immediately", "Request compensation for service downtime", "File written complaint with acknowledgment", "Escalate to ombudsman if unresolved in 24 hours"]
    },
    "Infrastructure Damage": {
        "title": "Infrastructure Damage Report",
        "action": "File damage repair complaint with photos/GPS",
        "links": ["https://mcdonline.nic.in/", "https://pwd.delhi.gov.in/"],
        "steps": ["Submit high-quality photos and GPS coordinates", "Request inspection and repair timeline", "File RTI for repair schedule", "Follow up every 7 days"]
    },
    "Safety Hazard": {
        "title": "Safety & Emergency Concern",
        "action": "Report to emergency services immediately",
        "links": ["https://fire.delhi.gov.in/", "https://crimesurvey.delhi.gov.in/"],
        "steps": ["Call emergency number (Police: 100, Fire: 101, Medical: 108)", "File formal FIR/report", "Request investigation status", "Document hazard evidence"]
    },
    "Billing/Payment Issue": {
        "title": "Billing Dispute Resolution",
        "action": "Request bill breakdown and recalculation",
        "links": ["https://www.delhipower.gov.in/", "https://www.delhijal.gov.in/", "https://consumeronline.nic.in/"],
        "steps": ["Provide old bills and usage records", "Request itemized bill explanation", "File RTI for rate determination", "Escalate to consumer court if unjust"]
    },
    "Money/Financial Problem": {
        "title": "Financial Loss or Fraud",
        "action": "File police complaint and bank dispute",
        "links": ["https://rbidocs.rbi.org.in/", "https://cybercrime.gov.in/", "https://consumeronline.nic.in/"],
        "steps": ["File FIR with police immediately", "Initiate bank dispute/chargeback", "Request transaction investigation", "File with consumer court for compensation"]
    },
    "Documentation/Records": {
        "title": "Document & Records Management",
        "action": "Request official document copy/verification",
        "links": ["https://revenue.delhi.gov.in/", "https://indiapost.gov.in/", "https://www.digitalindia.gov.in/"],
        "steps": ["Submit document request form", "Request acknowledgment receipt", "Follow up within specified time", "Escalate through RTI if denied"]
    },
    "Staff Misconduct": {
        "title": "Employee Conduct Complaint",
        "action": "File formal complaint with department head",
        "links": ["https://cpgrams.nic.in/", "https://www.india.gov.in/"],
        "steps": ["Document misconduct with date, time, and witnesses", "File complaint with supervisor/director", "Request investigation status updates", "Escalate to ombudsman if unaddressed"]
    },
    "Quality/Standard Violation": {
        "title": "Quality & Standards Violation",
        "action": "File compliance violation report",
        "links": ["https://www.fssai.gov.in/", "https://consumeronline.nic.in/", "https://www.delhipollution.nic.in/"],
        "steps": ["Provide evidence of violation", "Request inspection and certification", "File consumer/health complaint", "Request public notice if violation confirmed"]
    },
    "Security Issue": {
        "title": "Security & Data Protection",
        "action": "Report security breach immediately",
        "links": ["https://cybercrime.gov.in/", "https://crimesurvey.delhi.gov.in/", "https://www.incometax.gov.in/"],
        "steps": ["Change passwords and enable 2FA", "File cybercrime complaint with evidence", "Request account freeze if hacked", "File FIR for identity theft"]
    },
    "Medical Help": {
        "title": "Medical Assistance Required",
        "action": "Request emergency or ambulance service",
        "links": ["https://health.delhi.gov.in/", "https://consumeronline.nic.in/"],
        "steps": ["Call ambulance (108) for emergency", "Request hospital admission assistance", "Get medical certificate of treatment", "File negligence complaint if unsatisfied"]
    },
    "Links/Resources Help": {
        "title": "Additional Resources & Links",
        "action": "Get information on government services",
        "links": ["https://www.india.gov.in/", "https://cpgrams.nic.in/", "https://www.digitalindia.gov.in/", "https://www.mygov.in/"],
        "steps": ["Visit official government portals", "Check scheme eligibility criteria", "Download required forms", "Call helpline for additional support"]
    },
    "Suggestion/Feedback": {
        "title": "Suggestion or Feedback",
        "action": "Submit improvement suggestion",
        "links": ["https://www.mygov.in/", "https://cpgrams.nic.in/"],
        "steps": ["Describe suggestion clearly", "Submit through online portal", "Suggest implementation benefits", "Provide contact for follow-up"]
    },
    "Complaint Review": {
        "title": "Complaint Status Review",
        "action": "Request complaint progress update",
        "links": ["https://cpgrams.nic.in/", "https://tracking.india.gov.in/"],
        "steps": ["Provide original complaint ticket number", "Request status report with timeline", "Ask for pending action details", "Escalate if response insufficient"]
    },
    "Fraud/Scam Report": {
        "title": "Fraud & Scam Reporting",
        "action": "File cybercrime and police complaint",
        "links": ["https://cybercrime.gov.in/", "https://crimesurvey.delhi.gov.in/", "https://www.fssai.gov.in/"],
        "steps": ["File FIR with police immediately", "Report to relevant authority (cyber, food, etc)", "Freeze affected accounts/services", "File consumer complaint for compensation"]
    },
    "Accessibility Issue": {
        "title": "Accessibility Compliance Problem",
        "action": "Report accessibility violation",
        "links": ["https://www.disabilityindia.org/", "https://consumeronline.nic.in/"],
        "steps": ["Document accessibility barrier with photos", "File compliance violation report", "Request accessibility improvements", "Escalate to Disability Commissioner"]
    },
    "Discrimination": {
        "title": "Discrimination or Prejudice",
        "action": "File anti-discrimination complaint",
        "links": ["https://www.minorityaffairs.gov.in/", "https://wcd.delhi.gov.in/", "https://crimesurvey.delhi.gov.in/"],
        "steps": ["Document incident with witnesses", "File police FIR if criminal nature", "File with human rights commission", "Request official investigation"]
    },
    "Delayed Service": {
        "title": "Service Delay Complaint",
        "action": "Request expedited service with penalty waiver",
        "links": ["https://cpgrams.nic.in/", "https://consumeronline.nic.in/"],
        "steps": ["Document delay with proof", "Request SLA compliance report", "Demand compensation for delay", "Escalate through consumer court"]
    },
    "Other": {
        "title": "General Complaint",
        "action": "File general grievance complaint",
        "links": ["https://cpgrams.nic.in/", "https://www.india.gov.in/"],
        "steps": ["Describe issue clearly", "Provide supporting documents", "File through nearest citizen service center", "Track through CPGRAMS portal"]
    }
}

def classify_department(description: str, department_name: Optional[str] = None) -> str:
    if department_name and department_name != 'Grievance Redressal':
        return department_name
    text = description.lower()
    for department, keywords in DEPARTMENT_KEYWORDS.items():
        if any(word in text for word in keywords):
            return department
    return "Grievance Redressal"

def detect_priority(description: str, priority: Optional[str] = None) -> str:
    if priority:
        return priority
    text = description.lower()
    for level, keywords in PRIORITY_KEYWORDS.items():
        if any(word in text for word in keywords):
            return level
    return "Medium"

def generate_ai_reply(message: str, issue_category: Optional[str] = None) -> str:
    message_lower = message.lower()
    department = classify_department(message_lower)
    priority = detect_priority(message_lower)
    dept_info = DEPARTMENT_INFO.get(department, DEPARTMENT_INFO["Grievance Redressal"])
    
    # Get category guidance if provided
    category_info = None
    if issue_category:
        category_info = CATEGORY_GUIDANCE.get(issue_category, CATEGORY_GUIDANCE.get("Other"))
    
    reply = f"""🎯 {dept_info['name']} - {priority} Priority\n\n"""
    reply += f"""Your issue has been identified as requiring {dept_info['name']} attention.\n\n{dept_info['contact']}\n🔗 Redressal Link: {dept_info['redressal_link']}\n\n"""
    
    # Add category-specific guidance if available
    if category_info:
        reply += f"""📌 Category: {category_info['title']}\n{category_info['action']}\n\n"""
        reply += f"""🔗 Useful Links:\n"""
        for link in category_info['links'][:3]:
            reply += f"   • {link}\n"
        reply += f"\n"""
    
    reply += f"""💡 Action Steps:\n"""
    for i, suggestion in enumerate(dept_info['suggestions'][:4], 1):
        reply += f"{i}. {suggestion}\n"
    
    reply += f"\n⏱️ Timeline: """
    if priority == "High":
        reply += "24-48 hours acknowledgment, 7-14 days action"
    elif priority == "Medium":
        reply += "48-72 hours acknowledgment, 15-30 days action"
    else:
        reply += "1-2 weeks acknowledgment, 30-45 days action"
    reply += "\n\n✅ Next: Submit form below → Reference this ticket → Follow up every 7 days"
    return reply

def redressal_link_for_department(department_name: str) -> str:
    return DEPARTMENT_INFO.get(department_name, DEPARTMENT_INFO["Grievance Redressal"]).get("redressal_link", "https://cpgrams.nic.in/")
