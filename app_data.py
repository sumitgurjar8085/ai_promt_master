"""
AI Prompt Master - Database & Settings Module (app_data.py)
Contains application configuration, prompt engineering course guide, and categorized prompts database.
"""

APP_SETTINGS = {
    "app_title": "AI Prompt Master",
    "initial_tokens": 100,
    "daily_bonus": 20,
    "ad_reward": 15,
    "theme_mode": "dark",
    "window_width": 390,
    "window_height": 740,
}

AI_COURSE_GUIDE = [
    {
        "chapter": 1,
        "title": "Prompt Engineering Fundamentals",
        "tag": "Basics",
        "icon": "school",
        "summary": "Master the core structure of effective prompts: Role, Context, Task, and Constraints.",
        "content": (
            "1. Role & Persona: Explicitly tell the AI who it is (e.g., 'Act as a Senior Principal Engineer').\n"
            "2. Context: Provide clear background facts, domain boundaries, and target audience expectations.\n"
            "3. Specific Task: Define single unambiguous directives with expected deliverables.\n"
            "4. Constraints & Formatting: Specify what NOT to do, preferred output schema (Markdown, JSON), and length limits."
        ),
    },
    {
        "chapter": 2,
        "title": "Zero-Shot vs Few-Shot Prompting",
        "tag": "Zero-shot / Few-shot",
        "icon": "psychology",
        "summary": "Learn when to rely on model pre-training versus providing concrete input-output demonstrations.",
        "content": (
            "• Zero-Shot Prompting: Providing a directive without examples. Ideal for general translation, summarization, and direct Q&A.\n\n"
            "• Few-Shot Prompting: Supplying 2-5 high-quality input/output pairs in the prompt. "
            "Essential for nuanced classification, strict styling, custom JSON structure, and complex reasoning patterns.\n\n"
            "Tip: Ensure few-shot examples demonstrate edge cases and preserve balanced distribution."
        ),
    },
    {
        "chapter": 3,
        "title": "Chain-of-Thought (CoT) Reasoning",
        "tag": "Chain-of-Thought",
        "icon": "auto_awesome",
        "summary": "Unlock superior reasoning in LLMs by forcing step-by-step intermediate deduction.",
        "content": (
            "• The Core Technique: Adding cues like 'Think step-by-step before answering' or providing worked-out examples.\n\n"
            "• Why it works: Breaks down multi-hop logic, math, and code debugging into verifiable sub-steps.\n\n"
            "• Advanced CoT: Combine with Least-to-Most decomposition or Self-Consistency sampling for mission-critical workflows."
        ),
    },
]

PROMPTS_DATABASE = [
    {
        "id": "prompt_coding_bug_finder",
        "category": "Development",
        "title": "Coding Bug Finder",
        "desc": "Detect syntax errors, memory leaks, race conditions, and edge-case security bugs in any language.",
        "token_cost": 25,
        "full_prompt": (
            "Act as an Elite Principal Software Security & Reliability Engineer. "
            "Review the provided code snippet below thoroughly:\n\n"
            "```[language]\n[PASTE YOUR CODE HERE]\n```\n\n"
            "Perform an exhaustive line-by-line inspection to identify:\n"
            "1. Critical bugs, runtime errors, and unhandled exceptions.\n"
            "2. Performance bottlenecks (Time/Space complexity) and memory leaks.\n"
            "3. Security vulnerabilities (OWASP Top 10, injection, sanitization).\n"
            "4. Race conditions or thread-safety hazards.\n\n"
            "Format your response with: \n"
            "- Root Cause Analysis\n"
            "- Corrected Production-Ready Code with inline comments\n"
            "- Regression Unit Tests covering edge cases"
        ),
    },
    {
        "id": "prompt_ats_resume_writer",
        "category": "Career",
        "title": "ATS Resume Writer",
        "desc": "Optimize resume bullet points using the Google XYZ formula to conquer ATS filters and impress hiring managers.",
        "token_cost": 30,
        "full_prompt": (
            "Act as an Executive Tech Recruiter and certified ATS (Applicant Tracking System) optimization specialist.\n\n"
            "Target Job Title: [TARGET ROLE]\n"
            "Target Industry/Company: [TARGET COMPANY/DOMAIN]\n"
            "Target Job Description keywords: [PASTE KEY REQUIREMENTS]\n\n"
            "My Raw Experience/Draft:\n[PASTE YOUR CURRENT RESUME / DRAFT EXPERIENCE]\n\n"
            "Rewrite each bullet point applying Google's formula: 'Accomplished [X] as measured by [Y], by doing [Z]'.\n"
            "Requirements:\n"
            "- Maximize high-impact action verbs (Engineered, Architected, Spearheaded).\n"
            "- Embed missing industry keywords naturally without keyword stuffing.\n"
            "- Quantify impact with metrics, % increases, latency reductions, and revenue gains.\n"
            "- Provide a compelling 3-sentence Executive Professional Summary at the top."
        ),
    },
    {
        "id": "prompt_topic_simplifier",
        "category": "Learning",
        "title": "Topic Simplifier (Feynman Technique)",
        "desc": "Break down dense, complex technical or scientific concepts into crystal-clear everyday analogies.",
        "token_cost": 20,
        "full_prompt": (
            "Act as a master educator utilizing the Feynman Technique to explain complex subjects with utmost clarity.\n\n"
            "Topic to Explain: [ENTER COMPLEX TOPIC, e.g., Quantum Entanglement / Transformer Attention / Zero-Knowledge Proofs]\n"
            "Audience Level: [Select: Curious 12-Year Old / Junior College Student / Executive Non-Tech Stakeholder]\n\n"
            "Structure your breakdown as follows:\n"
            "1. The 10-Second Elevator Metaphor: A vivid, everyday real-world analogy.\n"
            "2. Core Mechanism (Zero Jargon): How it actually works step-by-step using plain language.\n"
            "3. Why It Matters: Real-world impact and why people care about it today.\n"
            "4. Quick Intuition Check: Two simple questions with answers to test understanding."
        ),
    },
    {
        "id": "prompt_youtube_script_generator",
        "category": "Content",
        "title": "YouTube Script Generator",
        "desc": "Generate high-retention video scripts with scroll-stopping psychological hooks, retention resets, and CTAs.",
        "token_cost": 35,
        "full_prompt": (
            "Act as a Viral YouTube Scriptwriter and Content Strategist specializing in high viewer retention.\n\n"
            "Video Topic: [YOUR VIDEO TOPIC]\n"
            "Target Audience: [TARGET AUDIENCE & NICHE]\n"
            "Desired Video Length: [e.g., 8-10 minutes]\n\n"
            "Generate a complete production script with audio and visual cues:\n"
            "1. The 3-Second Hook: Create 3 punchy opening variations (Curiosity Gap, High Stakes, Counter-Intuitive Truth).\n"
            "2. The Re-Hook / Intro (0:03 - 0:45): Validate viewer curiosity and establish payoff promise.\n"
            "3. Core Body Sections with Retention Resets: Pattern interrupts, b-roll suggestions, text popups, sound cues.\n"
            "4. Seamless Sponsor/CTA Transition (Natural segue, zero viewer drop-off).\n"
            "5. Climax & End Screen: Final payoff with immediate loop to next suggested video."
        ),
    },
    {
        "id": "prompt_cold_email_pitch",
        "category": "Business",
        "title": "B2B Cold Email Pitch",
        "desc": "High-converting B2B outreach email with tailored personalization and irresistible soft call-to-action.",
        "token_cost": 20,
        "full_prompt": (
            "Act as a Top 1% B2B Enterprise Sales Copywriter.\n\n"
            "Prospect Name: [NAME]\n"
            "Prospect Role & Company: [ROLE, COMPANY]\n"
            "Recent Company Trigger/News: [TRIGGER EVENT OR OBSERVATION]\n"
            "Our Value Proposition: [WHAT WE SOLVE]\n\n"
            "Write a concise cold email following these rules:\n"
            "- Under 90 words total.\n"
            "- Subject line in all lowercase, 2-4 words, looking like an internal email.\n"
            "- First line must be hyper-specific to their company trigger.\n"
            "- No generic fluff ('hope this email finds you well', 'I wanted to reach out').\n"
            "- Low-friction, interest-based CTA ('Open to checking a 2-min loom on this?')."
        ),
    },
]
