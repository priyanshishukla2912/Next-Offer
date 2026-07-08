import streamlit as st
from groq import Groq

# ----------------------------
# Initialize Groq Client
# ----------------------------
client = Groq(api_key=st.secrets["GROQ_API_KEY"])


def chatbot_page():

    # ----------------------------
    # Initialize Chat History
    # ----------------------------
    if "messages" not in st.session_state:
        st.session_state["messages"] = [
            {
                "role": "assistant",
                "content": "👋 Hi! I'm your AI Career Assistant. Ask me anything about placements, resumes, interviews, DSA, AI/ML, internships, or career guidance."
            }
        ]

    st.title("🤖 AI Career Chatbot")

    st.write(
        "Ask anything about placements, resumes, interviews, DSA, internships, AI/ML, or career guidance."
    )

    # ----------------------------
    # Clear Chat Button
    # ----------------------------
    col1, col2 = st.columns([4, 1])

    with col2:
        if st.button("🗑 Clear Chat"):
            st.session_state["messages"] = [
                {
                    "role": "assistant",
                    "content": "👋 Hi! I'm your AI Career Assistant. Ask me anything about placements, resumes, interviews, DSA, AI/ML, internships, or career guidance."
                }
            ]
            st.rerun()

    # ----------------------------
    # Display Chat History
    # ----------------------------
    for message in st.session_state["messages"]:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # ----------------------------
    # User Input
    # ----------------------------
    user_question = st.text_area(
        "Ask your question",
        placeholder="Example: How should I prepare for Amazon SDE interviews?"
    )

    # ----------------------------
    # Ask AI
    # ----------------------------
    if st.button("Ask AI"):

        if not user_question.strip():
            st.warning("Please enter a question.")
            st.stop()

        with st.spinner("🤖 Thinking..."):

            try:

                system_prompt = """
You are CareerGPT, an expert AI Career Mentor.

You help B.Tech students with:

- Placements
- Resume Improvement
- ATS Optimization
- DSA Preparation
- Software Engineering
- Data Science
- Machine Learning
- Artificial Intelligence
- Interview Preparation
- Internship Guidance
- Career Roadmaps
- Company-specific Preparation
- HR Interviews
- Technical Interviews
- Career Growth

Always:
1. Give clear explanations.
2. Give practical advice.
3. Explain step-by-step.
4. Use bullet points.
5. Be motivational.
6. Give industry-relevant guidance.
7. Suggest useful resources whenever appropriate.
"""

                conversation = [
                    {
                        "role": "system",
                        "content": system_prompt
                    }
                ] + st.session_state["messages"] + [
                    {
                        "role": "user",
                        "content": user_question
                    }
                ]

                completion = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=conversation,
                    temperature=0.5,
                    max_tokens=800,
                )

                answer = completion.choices[0].message.content

                # Save User Message
                st.session_state["messages"].append(
                    {
                        "role": "user",
                        "content": user_question
                    }
                )

                # Save AI Response
                st.session_state["messages"].append(
                    {
                        "role": "assistant",
                        "content": answer
                    }
                )

                st.rerun()

            except Exception as e:
                st.error(f"❌ Error: {e}")