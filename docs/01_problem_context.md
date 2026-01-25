# Problem Context

## The Challenge
In low-bandwidth, resource-constrained settings (e.g., rural Northern Nigeria), synchronous telehealth is expensive:
- 4G/Wi-Fi coverage is unreliable
- Voice/video calls require sustained data
- Real-time sync with EHRs is not feasible

## The Concept
WhatsApp (text-first, offline-friendly) + message routing + async workflows:
1. Clinics send text summaries of patient complaints
2. A simple routing system flags emergencies vs. general consults
3. Responses can be sent asynchronously (text, voice notes, referral links)

## Why It Matters (For the Prototype)
- **Technically feasible:** Simple keyword matching, hashed audit logs, consent gates
- **Governance-infeasible:** Professional liability, lack of clinical partnerships, privacy/consent infrastructure don't exist yet

This prototype documents *what was built* and *why it stopped*.

