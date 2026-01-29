import pandas as pd
import random

def generate_data():
    """
    Generate a large, balanced synthetic dataset for NLP-based career guidance.
    Features: salary_range, time_horizon, risk_appetite, industry
    Label: career
    """
    
    # Input parameter options
    salary_ranges = ["18+ LPA", "12–18 LPA", "6–12 LPA", "3–6 LPA"]
    time_horizons = ["Short-term", "Medium-term", "Long-term"]
    risk_appetites = ["Stable", "Moderate", "High-growth"]
    industries = ["Technology", "Healthcare", "Finance", "Consulting", "Public Sector"]
    
    # Comprehensive career mappings by (salary, time, risk, industry)
    # Each combination maps to a list of suitable careers
    careers = {
        # TECHNOLOGY sector
        ("18+ LPA", "Long-term", "High-growth", "Technology"): ["AI Engineer", "Machine Learning Lead", "Data Scientist", "Cloud Architect"],
        ("18+ LPA", "Long-term", "Stable", "Technology"): ["Senior Software Engineer", "Engineering Manager", "Technical Architect"],
        ("18+ LPA", "Short-term", "High-growth", "Technology"): ["Startup CTO", "Tech Entrepreneur"],
        ("18+ LPA", "Medium-term", "Moderate", "Technology"): ["DevOps Lead", "Solutions Architect", "Principal Engineer"],
        ("12–18 LPA", "Medium-term", "Moderate", "Technology"): ["Full Stack Developer", "Cybersecurity Analyst", "Product Manager"],
        ("12–18 LPA", "Long-term", "Stable", "Technology"): ["Database Administrator", "System Administrator"],
        ("12–18 LPA", "Short-term", "High-growth", "Technology"): ["Blockchain Developer", "IoT Specialist"],
        ("6–12 LPA", "Short-term", "Stable", "Technology"): ["Junior Developer", "QA Engineer", "IT Support Engineer"],
        ("6–12 LPA", "Medium-term", "Moderate", "Technology"): ["UX Designer", "Technical Writer", "Mobile App Developer"],
        ("3–6 LPA", "Short-term", "Stable", "Technology"): ["Help Desk Analyst", "Data Entry Operator"],
        
        # HEALTHCARE sector
        ("18+ LPA", "Long-term", "High-growth", "Healthcare"): ["Medical Specialist", "Surgeon", "Healthcare AI Lead"],
        ("18+ LPA", "Long-term", "Stable", "Healthcare"): ["Hospital Administrator", "Senior Physician", "Medical Director"],
        ("18+ LPA", "Medium-term", "Moderate", "Healthcare"): ["Clinical Research Director", "Pharmaceutical Lead"],
        ("12–18 LPA", "Medium-term", "Moderate", "Healthcare"): ["Pharmacist", "Physiotherapist", "Clinical Researcher"],
        ("12–18 LPA", "Long-term", "Stable", "Healthcare"): ["General Practitioner", "Radiologist"],
        ("6–12 LPA", "Short-term", "Stable", "Healthcare"): ["Nurse", "Lab Technician", "Medical Coder"],
        ("6–12 LPA", "Medium-term", "Moderate", "Healthcare"): ["Dietitian", "Occupational Therapist"],
        ("3–6 LPA", "Short-term", "Stable", "Healthcare"): ["Medical Assistant", "Pharmacy Technician"],
        ("3–6 LPA", "Long-term", "Stable", "Healthcare"): ["Healthcare Worker", "Patient Care Coordinator"],
        
        # FINANCE sector
        ("18+ LPA", "Long-term", "High-growth", "Finance"): ["Investment Banker", "Quantitative Analyst", "Portfolio Manager"],
        ("18+ LPA", "Short-term", "High-growth", "Finance"): ["High Frequency Trader", "Hedge Fund Manager"],
        ("18+ LPA", "Long-term", "Stable", "Finance"): ["CFO", "Risk Director", "VP Finance"],
        ("18+ LPA", "Medium-term", "Moderate", "Finance"): ["Private Equity Associate", "M&A Analyst"],
        ("12–18 LPA", "Medium-term", "Moderate", "Finance"): ["Financial Analyst", "Credit Analyst", "Equity Research Analyst"],
        ("12–18 LPA", "Long-term", "Stable", "Finance"): ["Actuary", "Compliance Officer"],
        ("6–12 LPA", "Short-term", "Stable", "Finance"): ["Bank PO", "Accountant", "Auditor"],
        ("6–12 LPA", "Medium-term", "Moderate", "Finance"): ["Tax Consultant", "Wealth Advisor"],
        ("3–6 LPA", "Short-term", "Stable", "Finance"): ["Bank Clerk", "Accounts Executive", "Teller"],
        
        # CONSULTING sector
        ("18+ LPA", "Long-term", "High-growth", "Consulting"): ["Management Consultant", "Strategy Director", "Partner"],
        ("18+ LPA", "Medium-term", "Moderate", "Consulting"): ["Senior Consultant", "Practice Lead"],
        ("18+ LPA", "Long-term", "Stable", "Consulting"): ["Consulting Director", "Client Partner"],
        ("12–18 LPA", "Medium-term", "Moderate", "Consulting"): ["Business Analyst", "IT Consultant", "Operations Consultant"],
        ("12–18 LPA", "Short-term", "High-growth", "Consulting"): ["Digital Transformation Consultant", "Startup Advisor"],
        ("12–18 LPA", "Long-term", "Stable", "Consulting"): ["Change Management Consultant", "HR Consultant"],
        ("6–12 LPA", "Short-term", "Stable", "Consulting"): ["Junior Consultant", "Research Analyst"],
        ("6–12 LPA", "Medium-term", "Moderate", "Consulting"): ["Marketing Consultant", "Sales Consultant"],
        ("3–6 LPA", "Short-term", "Stable", "Consulting"): ["Associate Analyst", "Data Analyst Trainee"],
        
        # PUBLIC SECTOR
        ("18+ LPA", "Long-term", "High-growth", "Public Sector"): ["IAS Officer", "IPS Officer", "Judge"],
        ("18+ LPA", "Long-term", "Stable", "Public Sector"): ["Senior Bureaucrat", "University Professor", "DRDO Scientist"],
        ("18+ LPA", "Medium-term", "Moderate", "Public Sector"): ["Public Sector Executive", "ISRO Scientist"],
        ("12–18 LPA", "Long-term", "Stable", "Public Sector"): ["State Civil Services", "Public Sector Manager"],
        ("12–18 LPA", "Medium-term", "Moderate", "Public Sector"): ["Defense Officer", "Foreign Service Officer"],
        ("6–12 LPA", "Short-term", "Stable", "Public Sector"): ["Government Clerk", "Railway Officer", "Bank PO"],
        ("6–12 LPA", "Long-term", "Stable", "Public Sector"): ["School Teacher", "College Lecturer"],
        ("6–12 LPA", "Medium-term", "Moderate", "Public Sector"): ["Police Sub-Inspector", "Postal Officer"],
        ("3–6 LPA", "Short-term", "Stable", "Public Sector"): ["Clerk", "Postman", "Peon"],
        ("3–6 LPA", "Long-term", "Stable", "Public Sector"): ["Primary Teacher", "Anganwadi Worker"],
    }
    
    data = []
    
    # Generate balanced samples from defined mappings
    for (salary, time, risk, industry), role_list in careers.items():
        for role in role_list:
            # Generate multiple samples per career (30-40 per career for balance)
            sample_count = random.randint(30, 40)
            for _ in range(sample_count):
                data.append({
                    "salary_range": salary,
                    "time_horizon": time,
                    "risk_appetite": risk,
                    "industry": industry,
                    "career": role
                })
    
    # Add some cross-industry variations (careers that can span industries)
    cross_industry_careers = [
        ("Data Scientist", ["Technology", "Finance", "Healthcare", "Consulting"]),
        ("Product Manager", ["Technology", "Healthcare", "Consulting"]),
        ("Business Analyst", ["Finance", "Consulting", "Technology"]),
        ("UX Designer", ["Technology", "Healthcare", "Consulting"]),
        ("Project Manager", ["Technology", "Finance", "Consulting", "Public Sector"]),
    ]
    
    for career, applicable_industries in cross_industry_careers:
        for industry in applicable_industries:
            for salary in ["12–18 LPA", "18+ LPA"]:
                for _ in range(15):
                    data.append({
                        "salary_range": salary,
                        "time_horizon": random.choice(["Medium-term", "Long-term"]),
                        "risk_appetite": random.choice(["Moderate", "High-growth"]),
                        "industry": industry,
                        "career": career
                    })
    
    # Shuffle and save
    df = pd.DataFrame(data)
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)  # Shuffle
    df.to_csv("data/raw_data.csv", index=False)
    
    print(f"✅ Generated {len(df)} samples")
    print(f"📊 Unique careers: {df['career'].nunique()}")
    print(f"📈 Samples per industry:")
    print(df['industry'].value_counts())
    print(f"\n📋 Sample data:")
    print(df.head(10).to_string())

if __name__ == "__main__":
    generate_data()
