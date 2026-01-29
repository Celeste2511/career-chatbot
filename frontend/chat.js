// Career Guidance Chatbot - Frontend Logic (Enhanced with Industry/Domain)

// API URL - Change to deployed URL when ready
const API_URL = 'http://localhost:8000';

// Conversation state
const state = {
    step: 0,
    salary_range: null,
    time_horizon: null,
    risk_appetite: null,
    industry: null,
    lastRecommendations: null
};

// Career explanations database (expanded)
const careerExplanations = {
    // Technology
    "AI Engineer": "Shape the future of automation with excellent pay.",
    "Machine Learning Lead": "Lead AI/ML initiatives at top tech companies.",
    "Data Scientist": "Combines analytical skills with AI/ML technologies for high growth.",
    "Cloud Architect": "Design scalable cloud infrastructure for enterprises.",
    "Senior Software Engineer": "Stable role with clear progression and work-life balance.",
    "Engineering Manager": "Lead engineering teams to deliver impactful products.",
    "Technical Architect": "Design complex systems with deep technical expertise.",
    "Startup CTO": "Lead technology vision at fast-growing startups.",
    "Tech Entrepreneur": "Build your own tech company with unlimited potential.",
    "DevOps Lead": "Bridge development and operations for faster delivery.",
    "Solutions Architect": "Design end-to-end solutions for enterprise clients.",
    "Principal Engineer": "Senior technical leadership with high compensation.",
    "Full Stack Developer": "Build complete web applications from front to back.",
    "Cybersecurity Analyst": "Protect organizations from cyber threats.",
    "Product Manager": "Bridge tech and business with diverse growth paths.",
    "Database Administrator": "Manage critical data infrastructure.",
    "System Administrator": "Maintain and secure IT infrastructure.",
    "Blockchain Developer": "Build decentralized applications.",
    "IoT Specialist": "Connect the physical and digital worlds.",
    "Junior Developer": "Entry point into tech with growth potential.",
    "QA Engineer": "Ensure software quality and reliability.",
    "IT Support Engineer": "Help organizations run smoothly.",
    "UX Designer": "Design user experiences in high-demand field.",
    "Technical Writer": "Document complex systems clearly.",
    "Mobile App Developer": "Build apps for billions of smartphone users.",
    "Help Desk Analyst": "First line of IT support.",
    "Data Entry Operator": "Accurate data management role.",

    // Healthcare
    "Medical Specialist": "Prestigious career with job security and high earnings.",
    "Surgeon": "Save lives with specialized medical skills.",
    "Healthcare AI Lead": "Apply AI to transform healthcare.",
    "Hospital Administrator": "Manage healthcare facilities effectively.",
    "Senior Physician": "Experienced medical professional with leadership role.",
    "Medical Director": "Lead medical teams and clinical operations.",
    "Clinical Research Director": "Advance medical knowledge through research.",
    "Pharmaceutical Lead": "Lead drug development and approval.",
    "Pharmacist": "Dispense medications and advise patients.",
    "Physiotherapist": "Help patients recover mobility and strength.",
    "Clinical Researcher": "Conduct medical research studies.",
    "General Practitioner": "Primary care physician for communities.",
    "Radiologist": "Diagnose conditions using medical imaging.",
    "Nurse": "Provide essential patient care.",
    "Lab Technician": "Conduct diagnostic tests.",
    "Medical Coder": "Translate medical records into codes.",
    "Dietitian": "Advise on nutrition and healthy eating.",
    "Occupational Therapist": "Help patients with daily activities.",
    "Medical Assistant": "Support healthcare delivery.",
    "Pharmacy Technician": "Assist pharmacists in dispensing medications.",
    "Healthcare Worker": "Essential frontline healthcare role.",
    "Patient Care Coordinator": "Coordinate patient care journeys.",

    // Finance
    "Investment Banker": "High-reward finance career with exceptional compensation.",
    "Quantitative Analyst": "Apply math and statistics to finance.",
    "Portfolio Manager": "Manage investment portfolios for clients.",
    "High Frequency Trader": "Rapid returns for high-stakes decision makers.",
    "Hedge Fund Manager": "Manage alternative investment strategies.",
    "CFO": "Lead financial strategy for organizations.",
    "Risk Director": "Manage enterprise risk at senior level.",
    "VP Finance": "Senior leadership in corporate finance.",
    "Private Equity Associate": "Invest in and grow companies.",
    "M&A Analyst": "Analyze mergers and acquisitions.",
    "Financial Analyst": "Analyze markets with strong earning potential.",
    "Credit Analyst": "Assess creditworthiness of borrowers.",
    "Equity Research Analyst": "Analyze stocks and make recommendations.",
    "Actuary": "Assess financial risk using statistics.",
    "Compliance Officer": "Ensure regulatory compliance.",
    "Bank PO": "Stable banking career with good benefits.",
    "Accountant": "Manage financial records and reports.",
    "Auditor": "Verify financial accuracy and compliance.",
    "Tax Consultant": "Advise on tax optimization.",
    "Wealth Advisor": "Help clients manage wealth.",
    "Bank Clerk": "Entry-level banking role.",
    "Accounts Executive": "Handle accounts and transactions.",
    "Teller": "Customer-facing banking role.",

    // Consulting
    "Management Consultant": "Solve complex problems with fast career progression.",
    "Strategy Director": "Lead strategic initiatives for clients.",
    "Partner": "Senior leadership at consulting firms.",
    "Senior Consultant": "Experienced consulting professional.",
    "Practice Lead": "Lead a consulting practice area.",
    "Consulting Director": "Direct consulting engagements.",
    "Client Partner": "Manage key client relationships.",
    "Business Analyst": "Analyze business processes and requirements.",
    "IT Consultant": "Advise on technology solutions.",
    "Operations Consultant": "Improve operational efficiency.",
    "Digital Transformation Consultant": "Lead digital change initiatives.",
    "Startup Advisor": "Guide startups to success.",
    "Change Management Consultant": "Lead organizational change.",
    "HR Consultant": "Advise on human resources strategy.",
    "Junior Consultant": "Entry-level consulting role.",
    "Research Analyst": "Conduct research for consulting projects.",
    "Marketing Consultant": "Advise on marketing strategy.",
    "Sales Consultant": "Improve sales performance.",
    "Associate Analyst": "Junior analytical role.",
    "Data Analyst Trainee": "Entry-level data analysis.",

    // Public Sector
    "IAS Officer": "Lead government administration at highest levels.",
    "IPS Officer": "Lead law enforcement at senior levels.",
    "Judge": "Prestigious legal career requiring long-term commitment.",
    "Senior Bureaucrat": "Senior government administration role.",
    "University Professor": "Academic prestige with research opportunities.",
    "DRDO Scientist": "Defense research and development.",
    "Public Sector Executive": "Lead public sector organizations.",
    "ISRO Scientist": "Space research and exploration.",
    "State Civil Services": "State-level government administration.",
    "Public Sector Manager": "Manage public sector operations.",
    "Defense Officer": "Serve in armed forces.",
    "Foreign Service Officer": "Represent country abroad.",
    "Government Clerk": "Administrative government role.",
    "Railway Officer": "Railway management and operations.",
    "School Teacher": "Fulfilling career with job stability.",
    "College Lecturer": "Teach at higher education level.",
    "Police Sub-Inspector": "Law enforcement role.",
    "Postal Officer": "Postal service management.",
    "Clerk": "Stable administrative role with benefits.",
    "Postman": "Postal delivery role.",
    "Peon": "Office support role.",
    "Primary Teacher": "Teach young children.",
    "Anganwadi Worker": "Child development support."
};

// Conversation flow configuration (4 steps)
const conversationFlow = [
    {
        question: "Hello! 👋 I'm your **AI Career Guidance Counsellor**. I'll recommend the **top careers** that match your preferences.\n\nLet's start! What is your **target salary range**?",
        options: ["18+ LPA", "12–18 LPA", "6–12 LPA", "3–6 LPA"],
        field: "salary_range"
    },
    {
        question: "Great choice! Now, what is your **time horizon** for achieving this career goal?",
        options: ["Short-term", "Medium-term", "Long-term"],
        field: "time_horizon"
    },
    {
        question: "What is your **risk appetite**?",
        options: ["Stable", "Moderate", "High-growth"],
        field: "risk_appetite"
    },
    {
        question: "Finally, which **industry or domain** interests you most?",
        options: ["Technology", "Healthcare", "Finance", "Consulting", "Public Sector"],
        field: "industry"
    }
];

// DOM Elements
const chatMessages = document.getElementById('chatMessages');
const chatOptions = document.getElementById('chatOptions');
const userInput = document.getElementById('userInput');
const sendBtn = document.getElementById('sendBtn');

// Initialize chat
document.addEventListener('DOMContentLoaded', () => {
    setTimeout(() => showBotMessage(conversationFlow[0].question, conversationFlow[0].options), 500);
});

// Add message to chat
function addMessage(text, isUser = false) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${isUser ? 'user' : 'bot'}`;
    const formattedText = text.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
    messageDiv.innerHTML = formattedText;
    chatMessages.appendChild(messageDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

// Add HTML message directly
function addHTMLMessage(html) {
    const messageDiv = document.createElement('div');
    messageDiv.className = 'message bot';
    messageDiv.innerHTML = html;
    chatMessages.appendChild(messageDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

// Show typing indicator
function showTyping() {
    const typingDiv = document.createElement('div');
    typingDiv.className = 'typing-indicator';
    typingDiv.id = 'typingIndicator';
    typingDiv.innerHTML = '<span></span><span></span><span></span>';
    chatMessages.appendChild(typingDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

function hideTyping() {
    const typing = document.getElementById('typingIndicator');
    if (typing) typing.remove();
}

// Show bot message with options
function showBotMessage(text, options = null) {
    showTyping();
    setTimeout(() => {
        hideTyping();
        addMessage(text);
        if (options) {
            showOptions(options);
        }
    }, 800);
}

// Show quick reply options
function showOptions(options, handlers = null) {
    chatOptions.innerHTML = '';
    options.forEach((option, index) => {
        const btn = document.createElement('button');
        btn.className = 'option-btn';
        btn.textContent = option;
        btn.onclick = handlers ? handlers[index] : () => handleUserChoice(option);
        chatOptions.appendChild(btn);
    });
}

// Clear options
function clearOptions() {
    chatOptions.innerHTML = '';
}

// Handle user selection
function handleUserChoice(choice) {
    clearOptions();
    addMessage(choice, true);

    const currentStep = conversationFlow[state.step];
    state[currentStep.field] = choice;
    state.step++;

    if (state.step < conversationFlow.length) {
        const nextStep = conversationFlow[state.step];
        setTimeout(() => {
            showBotMessage(nextStep.question, nextStep.options);
        }, 300);
    } else {
        getPrediction();
    }
}

// Call prediction API
async function getPrediction() {
    showTyping();

    try {
        const response = await fetch(`${API_URL}/predict`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                salary_range: state.salary_range,
                time_horizon: state.time_horizon,
                risk_appetite: state.risk_appetite,
                industry: state.industry
            })
        });

        if (!response.ok) throw new Error('API request failed');

        const data = await response.json();
        hideTyping();
        state.lastRecommendations = data.recommendations;
        showMultipleRecommendations(data.recommendations);

    } catch (error) {
        hideTyping();
        addMessage("Sorry, I couldn't connect to the prediction service. Please make sure the API server is running on port 8000.");
        console.error('API Error:', error);
    }
}

// Display multiple career recommendations
function showMultipleRecommendations(recommendations) {
    // Filter out careers with 0% confidence - only show meaningful matches
    const meaningfulRecs = recommendations.filter(rec => rec.confidence > 0);

    const recCount = meaningfulRecs.length;
    let html = `<div style="margin-bottom: 12px;">Based on your preferences, here are your <strong>Top ${recCount} Career Recommendation${recCount !== 1 ? 's' : ''}</strong>:</div>`;

    meaningfulRecs.forEach((rec, index) => {
        const medal = index === 0 ? '🥇' : index === 1 ? '🥈' : index === 2 ? '🥉' : '⭐';
        const explanation = careerExplanations[rec.career] || "Aligns well with your preferences.";

        html += `
            <div class="recommendation-card" style="margin-bottom: 10px; padding: 14px;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <h3 style="margin: 0; font-size: 15px;">${medal} ${rec.career}</h3>
                    <span style="background: rgba(167,139,250,0.3); padding: 4px 10px; border-radius: 12px; font-size: 12px;">${rec.confidence}% match</span>
                </div>
                <p style="margin: 8px 0 0 0; font-size: 12px; opacity: 0.85;">${explanation}</p>
            </div>
        `;
    });

    addHTMLMessage(html);

    // Show follow-up options
    setTimeout(() => {
        addMessage("What would you like to do next?");
        showOptions(
            ["🔄 Try Different Preferences", "🏢 Change Industry", "👋 Thank You!"],
            [
                () => restartChat(),
                () => changeIndustry(),
                () => endChat()
            ]
        );
    }, 600);
}

// Change only industry
function changeIndustry() {
    clearOptions();
    addMessage("Change Industry", true);
    state.step = 3;  // Go to industry step
    state.industry = null;

    setTimeout(() => {
        showBotMessage("Sure! Let's explore a different industry. Which **industry or domain** interests you?",
            ["Technology", "Healthcare", "Finance", "Consulting", "Public Sector"]);
    }, 300);
}

// End chat
function endChat() {
    clearOptions();
    addMessage("Thank You!", true);
    addMessage("You're welcome! Best of luck with your career journey! 🚀✨ Remember, our AI recommendations are based on patterns in the data and should be used as a starting point for your career exploration.");
}

// Restart conversation
function restartChat() {
    clearOptions();
    addMessage("Try Different Preferences", true);

    state.step = 0;
    state.salary_range = null;
    state.time_horizon = null;
    state.risk_appetite = null;
    state.industry = null;
    state.lastRecommendations = null;

    setTimeout(() => {
        showBotMessage("Let's start fresh! What is your **target salary range**?",
            ["18+ LPA", "12–18 LPA", "6–12 LPA", "3–6 LPA"]);
    }, 300);
}
