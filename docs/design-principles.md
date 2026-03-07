# Design Principles: Building an AI System for ADHD

Jake-OS was designed ADHD-first. Every architectural decision addresses a specific friction point that causes traditional productivity systems to fail for neurodivergent users.

## The Four ADHD Friction Points

1. **Planning paralysis:** An open task list with 50+ items causes decision fatigue. You stare at the list and do nothing.
2. **Forgetting to check:** The system exists, but you forget to open it. Two days pass. Tasks accumulate. Guilt compounds.
3. **Context switching:** Slack notification during deep work. You check it. 45 minutes disappear. You can't remember what you were doing.
4. **Not sticking to systems:** You set up a system on Sunday. You use it Monday and Tuesday. By Thursday it's abandoned. By next Monday you're starting over.

## How Each Principle Addresses These

### 1. One inbox, not six.
**Friction point:** Planning paralysis, forgetting to check.

Every task from every source enters one Notion database. Not a separate list for work tasks, personal tasks, follow-ups, ideas, and meeting action items. One database with views that slice by context.

**Why it works:** You never ask "where did I put that?" There's only one place. Views (Today, This Week, Overdue, Inbox) give you focused slices without maintaining separate systems.

### 2. The system comes to you.
**Friction point:** Forgetting to check.

Agents push briefs to Slack. You don't navigate to a dashboard. You don't open a special app. The Morning Commander is sitting in your Slack DM when you check messages, which you're going to do anyway.

**Why it works:** The behavior of checking Slack is already automatic. Piggybacking on existing habits eliminates the "remember to open the system" failure mode.

### 3. Priority-driven, not theme-driven.
**Friction point:** Planning paralysis.

No "Marketing Monday" or "Admin Wednesday." The Morning Commander selects today's top 3-5 tasks based on due dates, energy requirements, and available time. You pick from a short list, not an infinite backlog.

**Why it works:** Theme days create rigidity that ADHD brains rebel against. "I'm supposed to do marketing but I have energy for strategy" leads to doing neither. Priority-driven means the system adapts to your state.

### 4. Friction-free capture.
**Friction point:** Context switching, forgetting to check.

10 seconds max to add anything. Open Notion, type a title, save. Status defaults to Inbox. No categorization, no prioritization, no project assignment. Just capture. Process later.

**Why it works:** If capture takes more than 10 seconds, you'll "remember it later" (you won't). The lower the friction, the higher the capture rate.

### 5. Built-in recovery.
**Friction point:** Not sticking to systems.

Agents run whether you use the system or not. Miss a day: the Morning Commander runs tomorrow with your overdue items. Miss a week: the Weekly Architect runs Sunday with everything. Miss a month: the Monthly Strategist resets you on the 1st.

**Why it works:** Traditional systems punish absence with a growing backlog that feels impossible to tackle. Jake-OS agents accumulate context and present a manageable re-entry point. You're never "too far behind to start again."

### 6. Guardrails, not willpower.
**Friction point:** Context switching.

Time-boxed deep work blocks. Two designated comms windows per day. Research timer (25 minutes, then stop). Phone on DND during focus blocks.

**Why it works:** ADHD means willpower is an unreliable resource. External constraints (timers, scheduled blocks, phone out of reach) replace the willpower requirement with environmental design.

### 7. Energy-aware scheduling.
**Friction point:** Planning paralysis, not sticking to systems.

Deep work mapped to morning hours (medication peak, highest cognitive capacity). Lighter work after lunch. Creative work during energy peaks. Admin during energy troughs.

**Why it works:** Scheduling hard work during low-energy periods guarantees failure, which compounds into "the system doesn't work for me." Matching work type to energy state means the system respects your biology.

### 8. The system learns.
**Friction point:** Not sticking to systems.

Weekly pattern tracking. Monthly trend analysis. Quarterly audit. The system notices when you've skipped AI mastery sessions for 3 weeks, when Tuesday deep work gets interrupted every week, when follow-ups are piling up.

**Why it works:** Drift is invisible in the moment. A system that tracks its own usage and surfaces patterns catches problems before they become habits. And it does it without guilt: "AI Mastery skipped 3/4 weeks. Consider mornings only." Data, not judgment.

## The Meta-Principle

Every component asks: "Will this still work when the user has a bad week?"

If the answer is no, the design is wrong. ADHD means bad weeks are not exceptions; they're part of the operating model. The system must be robust to them, not fragile against them.
