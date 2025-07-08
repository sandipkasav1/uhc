from flask import Blueprint, render_template, request
from .funcs import db

bp = Blueprint("pages", __name__)


@bp.route("/")
def home():
    jobs = db.get_jobs()
    if len(jobs) > 10:
        jobs = jobs[:10]
    return render_template("home.html", jobs=jobs)


@bp.route("/jobs")
def jobs():
    keywords = request.args.get("keywords", "")
    location = request.args.get("location", "")
    jobs = db.get_jobs(keywords, location)
    if len(jobs) > 10:
        jobs = jobs[:10]

    job = request.args.get("job_code")
    if job:
        print(job)
        job = db.get_job_by_id(job)
        print(job)
        print(type(job))
        print(job["description"])
        return render_template(
            "jobs.html", jobs=jobs, job_description=job["description"]
        )
    else:
        job = jobs[0]["description"] if jobs else "No job with such keywords available."

    return render_template("jobs.html", jobs=jobs, job_description=job)


@bp.route("/about")
def about():
    return render_template("about.html")


@bp.route("/contact")
def contact():
    return render_template("contact.html")


@bp.route("/faqs")
def faqs():
    return render_template("faqs.html")


@bp.route("/client")
def client():
    return render_template(
        "client.html",
        testimonials=[
            {
                "quote": "Lorem ipsum … blandit.",
                "name": "John Carter",
                "role": "Web Designer",
            },
            {
                "quote": "Ultrices eros … integer.",
                "name": "Sophie Moore",
                "role": "Head of Marketing",
            },
            # …
        ],
    )


@bp.route("/pillars/nursing")
def nursing():
    jobs = db.get_jobs()
    nursing_jobs = []
    nursing_jobs = [job for job in jobs if "nurse" in job["job_title"].lower() or "nursing" in job["job_title"].lower()]
    if len(nursing_jobs) > 10:
        nursing_jobs = nursing_jobs[:10]

    roles = [
    {
        "title": "Registered Nurse (RN)",
        "qualifications": [
            "Associate Degree in Nursing (ADN)",
            "Bachelor of Science in Nursing (BSN)"
        ],
        "certifications": [
            "State approved RN (required)",
            "BLS (Basic Life Support)",
            "ACLS (Advanced Cardiac Life Support – for acute settings)"
        ]
    },
    {
        "title": "Licensed Practical Nurse (LPN) / Licensed Vocational Nurse (LVN)",
        "qualifications": [
            "State‑approved Practical Nursing Program (≈1 year)"
        ],
        "certifications": [
            "NCLEX‑PN (required)",
            "BLS",
            "IV Therapy Certification (state‑dependent)"
        ]
    },
    {
        "title": "Nurse Practitioner (NP)",
        "qualifications": [
            "Master of Science in Nursing (MSN)",
            "Doctor of Nursing Practice (DNP)"
        ],
        "certifications": [
            "National NP Certification (AANP or ANCC)",
            "State NP License",
            "BLS/ACLS"
        ]
    },
    {
        "title": "Certified Nursing Assistant (CNA)",
        "qualifications": [
            "State‑approved CNA training program"
        ],
        "certifications": [
            "CNA License",
            "BLS or CPR"
        ]
    },
    {
        "title": "Critical Care Nurse (ICU Nurse)",
        "qualifications": [
            "RN with clinical experience in critical care"
        ],
        "certifications": [
            "CCRN (via AACN)",
            "ACLS",
            "BLS"
        ]
    },
    {
        "title": "Emergency Room Nurse (ER Nurse)",
        "qualifications": [
            "RN with experience or training in emergency settings"
        ],
        "certifications": [
            "BLS",
            "ACLS",
            "PALS (Pediatric Advanced Life Support)",
            "TNCC (Trauma Nursing Core Course)"
        ]
    },
    {
        "title": "Operating Room Nurse (Perioperative Nurse)",
        "qualifications": [
            "RN with perioperative training"
        ],
        "certifications": [
            "CNOR (Certified Nurse Operating Room)",
            "BLS",
            "ACLS"
        ]
    },
    {
        "title": "Pediatric Nurse",
        "qualifications": [
            "RN with pediatric clinical experience"
        ],
        "certifications": [
            "PALS",
            "BLS",
            "CPN (Certified Pediatric Nurse – optional but preferred)"
        ]
    },
    {
        "title": "Travel Nurse",
        "qualifications": [
            "RN with at least 1–2 years of experience"
        ],
        "certifications": [
            "Compact State RN License (if applicable)",
            "BLS",
            "ACLS",
            "Other facility‑required credentials"
        ]
    },
    {
        "title": "Home Health Nurse",
        "qualifications": [
            "RN or LPN with home care experience"
        ],
        "certifications": [
            "BLS",
            "OASIS documentation training (for Medicare patients)"
        ]
    }
]
    faqs = [
    {
        "question": "What qualifications do I need to apply?",
        "answer": "It depends on the role. Check the individual job description for exact qualifications."
    },
    {
        "question": "Is relocation assistance provided?",
        "answer": "Yes, some roles may include relocation support depending on the location and urgency."
    },
    {
        "question": "Are certifications mandatory?",
        "answer": "Yes, certifications like BLS or ACLS are required for clinical roles."
    },
    {
        "question": "Can I apply to multiple roles?",
        "answer": "Absolutely! You can apply to as many roles as you’re qualified for."
    }
]

    return render_template("pillars/nursing.html", jobs=nursing_jobs, roles=roles, faqs=faqs)


@bp.route("/pillars/allied")
def allied():
    jobs = db.get_jobs()
    allied_jobs = []
    allied_jobs = [job for job in jobs if "allied" in job["job_title"].lower() or "ally" in job["job_title"].lower()]
    if len(allied_jobs) > 10:
        allied_jobs = allied_jobs[:10]

    roles = [
    {
        "title": "Physical Therapist (PT)",
        "qualifications": [
            "Doctor of Physical Therapy (DPT)"
        ],
        "certifications": [
            "NPTE (National Physical Therapy Exam)",
            "State Licensure"
        ]
    },
    {
        "title": "Occupational Therapist (OT)",
        "qualifications": [
            "Master’s or Doctorate in Occupational Therapy"
        ],
        "certifications": [
            "NBCOT Certification",
            "State Licensure"
        ]
    },
    {
        "title": "Speech-Language Pathologist (SLP)",
        "qualifications": [
            "Master’s in Speech-Language Pathology"
        ],
        "certifications": [
            "Praxis Exam",
            "ASHA CCC-SLP",
            "State Licensure"
        ]
    },
    {
        "title": "Radiologic Technologist (X-ray/Imaging Tech)",
        "qualifications": [
            "Associate’s or Bachelor’s in Radiologic Technology"
        ],
        "certifications": [
            "ARRT Certification",
            "State Licensure"
        ]
    },
    {
        "title": "Respiratory Therapist (RT)",
        "qualifications": [
            "Associate’s or Bachelor’s in Respiratory Therapy"
        ],
        "certifications": [
            "CRT or RRT from NBRC",
            "State Licensure"
        ]
    },
    {
        "title": "Medical Laboratory Scientist (MLS)",
        "qualifications": [
            "Bachelor’s in Clinical Laboratory Science"
        ],
        "certifications": [
            "ASCP MLS Certification"
        ]
    },
    {
        "title": "Diagnostic Medical Sonographer (Ultrasound Tech)",
        "qualifications": [
            "Associate’s or Bachelor’s in Sonography"
        ],
        "certifications": [
            "ARDMS (RDMS credential)"
        ]
    },
    {
        "title": "Clinical Dietitian / Registered Dietitian (RD)",
        "qualifications": [
            "Bachelor’s or Master’s in Nutrition",
            "Supervised Internship"
        ],
        "certifications": [
            "CDR RD Credential",
            "State Licensure"
        ]
    },
    {
        "title": "Physician Assistant (PA)",
        "qualifications": [
            "Master’s from ARC-PA accredited PA Program"
        ],
        "certifications": [
            "PANCE Certification",
            "State Licensure"
        ]
    },
    {
        "title": "Physical Therapist Assistant (PTA)",
        "qualifications": [
            "Associate Degree from a CAPTE-accredited Physical Therapist Assistant program (≈2 years)"
        ],
        "certifications": [
            "State License",
            "BLS"
        ]
    }
]

    faqs = [
    {
        "question": "Which allied professionals do you staff?",
        "answer": "We staff radiology techs, respiratory therapists, surgical techs, dietitians, sonographers, and more."
    },
    {
        "question": "Do you verify certifications for specialized roles?",
        "answer": "Yes. All allied professionals are verified for national and state-specific credentials like ARRT, NBRC, or CDR."
    },
    {
        "question": "Are short-term contracts available for allied roles?",
        "answer": "Yes, we support everything from weekend coverage to long-term contracts and temp-to-perm roles."
    },
    {
        "question": "How do you match allied professionals with the right facility?",
        "answer": "We match based on skill, certification, location, and facility type — not just availability."
    },
    {
        "question": "Can you staff allied professionals in outpatient and rehab centers?",
        "answer": "Yes. We support allied staffing across hospitals, outpatient clinics, and ambulatory care centers."
    }
]


    return render_template("pillars/allied.html", jobs=allied_jobs, roles=roles, faqs=faqs)


@bp.route("/pillars/therapy")
def therapy():
    jobs = db.get_jobs()
    therapy_jobs = []
    therapy_jobs = [job for job in jobs if "therapist" in job["job_title"].lower() or "therapy" in job["job_title"].lower()]
    if len(therapy_jobs) > 10:
        therapy_jobs = therapy_jobs[:10]

    roles = [
    {
        "title": "Physical Therapist (PT)",
        "qualifications": [
            "Doctor of Physical Therapy (DPT)"
        ],
        "certifications": [
            "National Physical Therapy Exam (NPTE)",
            "State Licensure",
            "BLS (Basic Life Support)"
        ]
    },
    {
        "title": "Physical Therapist Assistant (PTA)",
        "qualifications": [
            "Associate Degree from CAPTE-accredited PTA program"
        ],
        "certifications": [
            "NPTE for PTAs",
            "State Licensure",
            "BLS"
        ]
    },
    {
        "title": "Occupational Therapist (OT)",
        "qualifications": [
            "Master’s or Doctorate in Occupational Therapy"
        ],
        "certifications": [
            "NBCOT Certification",
            "State Licensure",
            "BLS"
        ]
    },
    {
        "title": "Certified Occupational Therapy Assistant (COTA)",
        "qualifications": [
            "Associate Degree from an ACOTE-accredited program"
        ],
        "certifications": [
            "NBCOT for COTAs",
            "State Licensure",
            "BLS"
        ]
    },
    {
        "title": "Speech-Language Pathologist (SLP)",
        "qualifications": [
            "Master’s in Speech-Language Pathology (from CAA-accredited program)"
        ],
        "certifications": [
            "Praxis Exam in Speech-Language Pathology",
            "CCC-SLP from ASHA",
            "State Licensure"
        ]
    },
    {
        "title": "Recreational Therapist",
        "qualifications": [
            "Bachelor’s in Recreational Therapy or related field"
        ],
        "certifications": [
            "CTRS (Certified Therapeutic Recreation Specialist – via NCTRC)",
            "BLS"
        ]
    },
    {
        "title": "Respiratory Therapist (RT or RRT)",
        "qualifications": [
            "Associate or Bachelor’s in Respiratory Therapy"
        ],
        "certifications": [
            "NBRC Credential (CRT or RRT)",
            "State Licensure",
            "BLS, ACLS"
        ]
    },
    {
        "title": "Massage Therapist",
        "qualifications": [
            "Completion of accredited massage therapy program (500–1000 hours)"
        ],
        "certifications": [
            "MBLEx (Massage & Bodywork Licensing Exam)",
            "State Licensure",
            "CPR/BLS"
        ]
    },
    {
        "title": "Behavioral Therapist (ABA Therapist)",
        "qualifications": [
            "Bachelor’s in Psychology/Education or RBT Training"
        ],
        "certifications": [
            "RBT (Registered Behavior Technician – via BACB)",
            "Supervised by a BCBA"
        ]
    },
    {
        "title": "Licensed Clinical Social Worker (LCSW – Therapy Role)",
        "qualifications": [
            "Master of Social Work (MSW)"
        ],
        "certifications": [
            "State LCSW License",
            "Clinical Supervision Hours (2,000–4,000 hours typically)",
            "Optional: Certifications in trauma, CBT, etc."
        ]
    }
]

    
    faqs = [
    {
        "question": "What therapy roles do you specialize in?",
        "answer": "We staff physical therapists (PT), occupational therapists (OT), and speech-language pathologists (SLP) across clinical and school settings."
    },
    {
        "question": "Are your therapists licensed and ASHA/APTA/NBCOT certified?",
        "answer": "Yes. Every therapist is fully licensed and verified via ASHA, APTA, or NBCOT databases."
    },
    {
        "question": "Do you offer placements in both rehab and educational settings?",
        "answer": "Yes. Our therapists work in SNFs, outpatient clinics, hospitals, and school districts nationwide."
    },
    {
        "question": "Can therapists choose between onsite and telehealth roles?",
        "answer": "Absolutely. We support onsite, hybrid, and remote (teletherapy) assignments based on state laws and clinician preferences."
    },
    {
        "question": "Do you provide assistance with continuing education?",
        "answer": "Yes. We support CEUs and license renewal planning as part of our long-term clinician support program."
    },
    {
        "question": "What documentation support do SLPs and OTs receive?",
        "answer": "We help with Medicaid billing training, IEP compliance resources, and EMR onboarding for all therapy roles."
    }
]


    return render_template("pillars/therapy.html", jobs=therapy_jobs, roles=roles, faqs=faqs)


@bp.route("/pillars/pharmacy")
def pharmacy():
    jobs = db.get_jobs()
    pharmacy_jobs = []
    pharmacy_jobs = [job for job in jobs if "pharmacist" in job["job_title"].lower() or "pharmacy" in job["job_title"].lower()]
    if len(pharmacy_jobs) > 10:
        pharmacy_jobs = pharmacy_jobs[:10]

    roles = [
    {
        "title": "Pharmacist (Retail/Community)",
        "qualifications": [
            "Doctor of Pharmacy (PharmD)"
        ],
        "certifications": [
            "NAPLEX (North American Pharmacist Licensure Exam)",
            "MPJE (Multistate Pharmacy Jurisprudence Exam – state-specific)",
            "State Pharmacist License",
            "Immunization Certification (optional but common)"
        ]
    },
    {
        "title": "Hospital/Clinical Pharmacist",
        "qualifications": [
            "PharmD",
            "Postgraduate Residency (PGY1; PGY2 preferred for specialties)"
        ],
        "certifications": [
            "NAPLEX + MPJE",
            "BPS Certification (e.g., BCPS – Pharmacotherapy)",
            "BLS/ACLS (required in many hospitals)"
        ]
    },
    {
        "title": "Pharmacy Technician",
        "qualifications": [
            "High school diploma",
            "Completion of pharmacy tech program (varies by state)"
        ],
        "certifications": [
            "PTCB (Pharmacy Technician Certification Board) or NHA (ExCPT)",
            "State Registration or License (as required)"
        ]
    },
    {
        "title": "Pharmacy Manager",
        "qualifications": [
            "Licensed Pharmacist (PharmD)",
            "Management experience"
        ],
        "certifications": [
            "NAPLEX, MPJE, and State License",
            "Business/Leadership certifications (optional)"
        ]
    },
    {
        "title": "Nuclear Pharmacist",
        "qualifications": [
            "PharmD",
            "Specialized training in nuclear pharmacy"
        ],
        "certifications": [
            "Board Certification in Nuclear Pharmacy (BCNP)",
            "State Licensure",
            "700 hours of nuclear pharmacy training (didactic + practical)"
        ]
    },
    {
        "title": "Informatics Pharmacist",
        "qualifications": [
            "PharmD",
            "Experience or degree in health informatics"
        ],
        "certifications": [
            "BCIP (Board Certified in Informatics Pharmacy – emerging)",
            "State Pharmacist License"
        ]
    },
    {
        "title": "Pharmaceutical Industry Pharmacist",
        "qualifications": [
            "PharmD",
            "Fellowship or industry experience"
        ],
        "certifications": [
            "State Licensure (if dispensing or clinical activities involved)",
            "Optional: Regulatory or research certifications (e.g., RAC)"
        ]
    },
    {
        "title": "Long-Term Care Pharmacist",
        "qualifications": [
            "PharmD"
        ],
        "certifications": [
            "State Pharmacist License",
            "BCGP (Board Certified Geriatric Pharmacist – optional but preferred)"
        ]
    },
    {
        "title": "Compounding Pharmacist",
        "qualifications": [
            "PharmD",
            "Training in sterile/non-sterile compounding"
        ],
        "certifications": [
            "State Pharmacist License",
            "Compounding certifications (e.g., ACA/ACVP or PCCA training)"
        ]
    },
    {
        "title": "Ambulatory Care Pharmacist",
        "qualifications": [
            "PharmD",
            "PGY1/PGY2 residency in ambulatory care"
        ],
        "certifications": [
            "BCACP (Board Certified Ambulatory Care Pharmacist)",
            "State Pharmacist License",
            "Collaborative Practice Agreement (in some states)"
        ]
    }
]

    
    faqs = [
    {
        "question": "What pharmacy roles do you support?",
        "answer": "We place pharmacists, pharmacy technicians, IV techs, and sterile compounding professionals."
    },
    {
        "question": "Do your candidates meet state board and PTCB standards?",
        "answer": "Yes. All pharmacy professionals are verified against NABP, state boards, and certifications like PTCB or NHA."
    },
    {
        "question": "Can you support hospital, retail, and LTC pharmacy settings?",
        "answer": "Absolutely. We tailor placements for acute care, ambulatory, long-term care, and retail pharmacy environments."
    },
    {
        "question": "Are temp-to-perm pharmacy roles available?",
        "answer": "Yes. We offer flexible engagement models including PRN, temp, temp-to-perm, and permanent placements."
    },
    {
        "question": "Do you offer 24/7 pharmacy coverage options?",
        "answer": "Yes. We can source and rotate pharmacists to maintain around-the-clock operations for high-volume sites."
    }
]

    return render_template("pillars/pharmacy.html", jobs=pharmacy_jobs, roles=roles, faqs=faqs)


@bp.route("/pillars/radiology")
def radiology():
    jobs = db.get_jobs()
    radiology_jobs = []
    radiology_jobs = [job for job in jobs if "radiologist" in job["job_title"].lower() or "radiology" in job["job_title"].lower()]
    if len(radiology_jobs) > 10:
        radiology_jobs = radiology_jobs[:10]

    roles = [
    {
        "title": "Radiologic Technologist (X-Ray Tech)",
        "qualifications": [
            "Associate’s or Bachelor’s in Radiologic Technology"
        ],
        "certifications": [
            "ARRT (American Registry of Radiologic Technologists)",
            "Licensure required in most states"
        ]
    },
    {
        "title": "Computed Tomography (CT) Technologist",
        "qualifications": [
            "ARRT-certified Radiologic Technologist",
            "CT-specific training"
        ],
        "certifications": [
            "ARRT (CT) Postprimary Certification",
            "Licensure varies by state"
        ]
    },
    {
        "title": "Magnetic Resonance Imaging (MRI) Technologist",
        "qualifications": [
            "ARRT-certified RT or Associate’s in MRI"
        ],
        "certifications": [
            "ARRT (MRI) Postprimary Certification",
            "Licensure varies by state"
        ]
    },
    {
        "title": "Diagnostic Medical Sonographer (Ultrasound Tech)",
        "qualifications": [
            "Associate’s or Bachelor’s in Diagnostic Medical Sonography"
        ],
        "certifications": [
            "ARDMS (RDMS) or CCI credentials",
            "Licensure not mandatory in most states, but preferred"
        ]
    },
    {
        "title": "Nuclear Medicine Technologist",
        "qualifications": [
            "Associate’s or Bachelor’s in Nuclear Medicine Technology"
        ],
        "certifications": [
            "NMTCB or ARRT (N)",
            "Licensure required in most states"
        ]
    },
    {
        "title": "Interventional Radiologic Technologist",
        "qualifications": [
            "Associate’s in Radiologic Technology",
            "Specialized Interventional Radiology (IR) training"
        ],
        "certifications": [
            "ARRT (VI – Vascular Interventional Radiography)",
            "State licensure required"
        ]
    },
    {
        "title": "Mammography Technologist",
        "qualifications": [
            "ARRT-certified Radiologic Technologist",
            "Mammography training"
        ],
        "certifications": [
            "ARRT (M) Postprimary Certification",
            "Licensure required in most states"
        ]
    },
    {
        "title": "Radiation Therapist",
        "qualifications": [
            "Associate’s or Bachelor’s in Radiation Therapy"
        ],
        "certifications": [
            "ARRT (T) – Radiation Therapy Certification",
            "State licensure required"
        ]
    },
    {
        "title": "Cardiovascular Technologist (CVT)",
        "qualifications": [
            "Associate’s or Bachelor’s in Cardiovascular Technology"
        ],
        "certifications": [
            "CCI (RCS, RCIS) or ARRT (CI)",
            "Licensure varies by state"
        ]
    },
    {
        "title": "Radiology Physician Assistant (RPA)",
        "qualifications": [
            "ARRT-certified RT",
            "Advanced RA program",
            "Clinical experience"
        ],
        "certifications": [
            "Certification by CBRPA",
            "State-specific licensure and physician supervision"
        ]
    }
]

    
    faqs = [
    {
        "question": "What is the difference between a radiologist and a radiologic technologist?",
        "answer": "A radiologist is a medical doctor (MD or DO) who interprets medical images and provides diagnoses, while a radiologic technologist is trained to perform imaging procedures like X-rays, MRIs, and CT scans under the supervision of a radiologist."
    },
    {
        "question": "What certifications are required to become a radiologic technologist in the U.S.?",
        "answer": "To work as a radiologic technologist, you typically need to pass the ARRT certification exam after completing an accredited radiologic technology program. Some states also require additional licensure."
    },
    {
        "question": "How long does it take to become a radiologic technologist?",
        "answer": "It usually takes 2 years to complete an Associate’s Degree in Radiologic Technology. Bachelor’s programs (4 years) are also available for advanced career opportunities."
    },
    {
        "question": "What are the common types of radiology specializations?",
        "answer": "Specializations include MRI, CT, Mammography, Interventional Radiology, Nuclear Medicine, and Ultrasound. Each requires post-primary certification through ARRT or other relevant boards."
    },
    {
        "question": "Is there a high demand for radiology professionals in the U.S.?",
        "answer": "Yes, the demand is strong and growing due to the increased use of diagnostic imaging in healthcare. The Bureau of Labor Statistics projects continued growth, especially for MRI and CT technologists."
    }
]

    return render_template("pillars/radiology.html", jobs=radiology_jobs, roles=roles, faqs=faqs)

@bp.route("/pillars/mental")
def mental():
    jobs = db.get_jobs()
    mental_health_jobs = []
    mental_health_jobs = [job for job in jobs if "mental health" in job["job_title"].lower() or "psychologist" in job["job_title"].lower()]
    if len(mental_health_jobs) > 10:
        mental_health_jobs = mental_health_jobs[:10]

    roles = [
    {
        "title": "Psychiatrist",
        "qualifications": [
            "M.D. or D.O.",
            "Psychiatry Residency"
        ],
        "certifications": [
            "Board Certification from ABPN (American Board of Psychiatry and Neurology)",
            "State Medical License"
        ]
    },
    {
        "title": "Clinical Psychologist",
        "qualifications": [
            "Doctorate in Psychology (Ph.D. or Psy.D.)"
        ],
        "certifications": [
            "State Board Licensure",
            "ABPP Certification for specialties (optional)"
        ]
    },
    {
        "title": "Licensed Clinical Social Worker (LCSW)",
        "qualifications": [
            "Master’s in Social Work (MSW)"
        ],
        "certifications": [
            "LCSW Licensure through State Board",
            "Supervised Clinical Hours"
        ]
    },
    {
        "title": "Licensed Professional Counselor (LPC)",
        "qualifications": [
            "Master’s in Counseling or Psychology"
        ],
        "certifications": [
            "State LPC Licensure (varies by state)",
            "Supervised Clinical Hours"
        ]
    },
    {
        "title": "Marriage and Family Therapist (LMFT)",
        "qualifications": [
            "Master’s in Marriage & Family Therapy or related field"
        ],
        "certifications": [
            "State LMFT Licensure",
            "Required Clinical Hours"
        ]
    },
    {
        "title": "Mental Health Counselor",
        "qualifications": [
            "Master’s in Mental Health Counseling or Clinical Psychology"
        ],
        "certifications": [
            "NCC (National Certified Counselor – optional)",
            "State Licensure"
        ]
    },
    {
        "title": "Psychiatric Mental Health Nurse Practitioner (PMHNP)",
        "qualifications": [
            "MSN or DNP with PMHNP focus"
        ],
        "certifications": [
            "ANCC PMHNP-BC Certification",
            "RN + NP Licensure"
        ]
    },
    {
        "title": "Substance Abuse Counselor / Addiction Counselor (CADC, LADC)",
        "qualifications": [
            "Associate’s, Bachelor’s, or Master’s in Addiction Counseling"
        ],
        "certifications": [
            "State Certification (CADC, LADC)",
            "Supervised Hours",
            "NAADAC Certification (optional)"
        ]
    },
    {
        "title": "Behavioral Health Technician / Mental Health Technician",
        "qualifications": [
            "High School Diploma or Associate’s Degree",
            "On-the-job Training"
        ],
        "certifications": [
            "CBHT (Certified Behavioral Health Technician – optional)"
        ]
    },
    {
        "title": "School Psychologist",
        "qualifications": [
            "Specialist-level Degree (Ed.S., or Master’s in School Psychology)"
        ],
        "certifications": [
            "Praxis Exam",
            "NASP Certification (NCSP – optional)",
            "State Licensure"
        ]
    }
]

    
    faqs = [
    {
        "question": "Who do you staff in behavioral health?",
        "answer": "We place LMFTs, LCSWs, psychologists, psychiatric nurses, behavior techs, and counselors."
    },
    {
        "question": "Do your clinicians have experience in trauma-informed care?",
        "answer": "Yes. Many of our professionals specialize in trauma care, crisis intervention, and evidence-based therapy."
    },
    {
        "question": "Can you support residential and outpatient programs?",
        "answer": "Yes. We staff mental health roles across inpatient units, outpatient clinics, school programs, and group homes."
    },
    {
        "question": "Are background checks and state board verifications included?",
        "answer": "Yes. We complete full credentialing, including background checks, board license verification, and abuse registry screening."
    },
    {
        "question": "Do you staff for correctional behavioral health settings?",
        "answer": "Yes, we place behavioral health professionals in correctional, government, and crisis response roles."
    }
]


    return render_template("pillars/mental.html", jobs=mental_health_jobs, roles=roles, faqs=faqs)

@bp.route("/pillars/gov")
def government():
    jobs = db.get_jobs()
    government_jobs = []
    government_jobs = [job for job in jobs if "government" in job["job_title"].lower() or "public health" in job["job_title"].lower()]
    if len(government_jobs) > 10:
        government_jobs = government_jobs[:10]

    roles = [
    {
        "title": "School Nurse",
        "qualifications": [
            "RN License (BSN preferred)"
        ],
        "certifications": [
            "State RN/LVN/LPN License",
            "BLS",
            "Optional: NCSN (National Certified School Nurse)"
        ]
    },
    {
        "title": "Public Health Nurse",
        "qualifications": [
            "RN with BSN (often required by public health departments)"
        ],
        "certifications": [
            "State RN License",
            "BLS",
            "Optional: CPH (Certified in Public Health)"
        ]
    },
    {
        "title": "Health Educator (School or Community-Based)",
        "qualifications": [
            "Bachelor’s in Health Education, Public Health, or related field"
        ],
        "certifications": [
            "CHES (Certified Health Education Specialist)",
            "BLS"
        ]
    },
    {
        "title": "School Counselor (Mental Health Focused)",
        "qualifications": [
            "Master’s in School Counseling or Clinical Counseling"
        ],
        "certifications": [
            "State Credential for School Counseling",
            "Optional: LPC, LMHC, or LCSW (depending on state)"
        ]
    },
    {
        "title": "Speech-Language Pathologist (School-Based SLP)",
        "qualifications": [
            "Master’s in Speech-Language Pathology"
        ],
        "certifications": [
            "CCC-SLP from ASHA",
            "Praxis SLP Exam",
            "State SLP License",
            "Often requires state teaching certification or credential"
        ]
    },
    {
        "title": "Occupational Therapist (School-Based)",
        "qualifications": [
            "Master’s or Doctorate in Occupational Therapy"
        ],
        "certifications": [
            "NBCOT Certification",
            "State OT License",
            "May need school-based credentials in some districts"
        ]
    },
    {
        "title": "School Psychologist",
        "qualifications": [
            "Education Specialist Degree (Ed.S.) or Doctorate in School Psychology"
        ],
        "certifications": [
            "State Certification",
            "Optional: NCSP (Nationally Certified School Psychologist)"
        ]
    },
    {
        "title": "Community Health Worker (Government Programs)",
        "qualifications": [
            "High school diploma or Associate’s/Bachelor's + state-approved training"
        ],
        "certifications": [
            "CHW Certification (state-specific)",
            "BLS (often required)"
        ]
    },
    {
        "title": "Environmental Health Specialist (Public Health Dept.)",
        "qualifications": [
            "Bachelor’s in Environmental Science, Public Health, or related field"
        ],
        "certifications": [
            "REHS (Registered Environmental Health Specialist – varies by state)",
            "Valid driver’s license and field safety certifications"
        ]
    },
    {
        "title": "Case Manager (Public Health or School-Based)",
        "qualifications": [
            "RN, LCSW, or Bachelor’s in Social Work/Health Services"
        ],
        "certifications": [
            "CCM (Certified Case Manager – optional but preferred)",
            "State License (RN or LCSW if applicable)"
        ]
    }
]

    
    faqs = [
    {
        "question": "What agencies do you work with for government staffing?",
        "answer": "We support federal, state, and county agencies — including VA hospitals, public health, and correctional facilities."
    },
    {
        "question": "Can you staff school-based clinicians?",
        "answer": "Yes. We place school nurses, therapists, counselors, and behavior specialists in K-12 settings."
    },
    {
        "question": "Are clinicians familiar with IEPs and IDEA compliance?",
        "answer": "Yes. Our school-based therapists and psychologists are trained in IEP documentation and special education standards."
    },
    {
        "question": "Do you staff long-term government contracts?",
        "answer": "Yes. We support both short-term surge coverage and long-term contract engagements with built-in compliance."
    },
    {
        "question": "Can you provide clinicians with public health credentials or clearances?",
        "answer": "Yes. We ensure all required security clearances, immunization records, and regulatory credentials are completed pre-placement."
    }
]


    return render_template("pillars/gov.html", jobs=government_jobs, roles=roles, faqs=faqs)

