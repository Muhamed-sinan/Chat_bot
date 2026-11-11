import streamlit as st
from langgraph_backend import chatbot
from langchain_core.messages import HumanMessage


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="PERSONAL BOT",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

    /* MAIN APP */
    .stApp {
        background:
            radial-gradient(circle at 20% 10%, rgba(0,120,255,0.12), transparent 30%),
            radial-gradient(circle at 80% 20%, rgba(80,0,255,0.10), transparent 30%),
            #070b13;
        color: white;
    }

    .block-container {
        max-width: 1100px;
        padding-top: 30px;
        padding-bottom: 130px;
    }


    /* REMOVE STREAMLIT DEFAULT */

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        background: transparent !important;
    }


    /* SIDEBAR */

    [data-testid="stSidebar"] {
        background:
            linear-gradient(
                180deg,
                #091525 0%,
                #050a12 100%
            );

        border-right: 1px solid rgba(255,255,255,0.08);
    }


    /* BRAND HEADER */

    .brand {
        text-align: center;
        padding: 35px 20px 30px 20px;

        background:
            linear-gradient(
                145deg,
                rgba(20,55,95,0.85),
                rgba(8,20,38,0.95)
            );

        border: 1px solid rgba(120,180,255,0.15);

        border-radius: 28px;

        box-shadow:
            0 20px 60px rgba(0,0,0,0.35);
    }


    .brand-icon {
        font-size: 75px;
        line-height: 1;
        margin-bottom: 15px;
    }


    .brand-title {
        font-size: 42px;
        font-weight: 900;
        letter-spacing: 5px;
        color: #ffffff;
        margin-bottom: 8px;
    }


    .brand-subtitle {
        font-size: 16px;
        color: #9fb3c8;
        letter-spacing: 1px;
    }


    .online {
        display: inline-block;

        margin-top: 18px;

        padding: 6px 14px;

        border-radius: 20px;

        background: rgba(0,200,120,0.10);

        border: 1px solid rgba(0,220,130,0.25);

        color: #55e6a5;

        font-size: 13px;
    }


    /* WELCOME CARD */

    .welcome-card {

        margin-top: 25px;

        padding: 28px;

        border-radius: 24px;

        background:
            linear-gradient(
                145deg,
                rgba(255,255,255,0.055),
                rgba(255,255,255,0.02)
            );

        border: 1px solid rgba(255,255,255,0.08);

        box-shadow:
            0 15px 45px rgba(0,0,0,0.20);
    }


    .welcome-title {

        font-size: 25px;

        font-weight: 700;

        color: white;

        margin-bottom: 8px;
    }


    .welcome-text {

        color: #94a7bb;

        font-size: 15px;

        line-height: 1.6;
    }


    /* QUICK ACTION CARDS */

    .quick-card {

        padding: 18px;

        min-height: 110px;

        border-radius: 20px;

        background: rgba(255,255,255,0.035);

        border: 1px solid rgba(255,255,255,0.07);

        text-align: left;
    }


    .quick-icon {
        font-size: 28px;
        margin-bottom: 8px;
    }


    .quick-title {

        color: white;

        font-weight: 600;

        font-size: 15px;
    }


    .quick-description {

        color: #8295aa;

        font-size: 12px;

        margin-top: 5px;
    }


    /* CHAT AREA */

    [data-testid="stChatMessage"] {

        border-radius: 20px;

        padding: 10px 15px;

        margin-bottom: 12px;
    }


    /* CHAT INPUT */

    [data-testid="stChatInput"] {

        background: #111722 !important;

        border: 1px solid rgba(120,170,255,0.18) !important;

        border-radius: 20px !important;
    }


    [data-testid="stChatInput"] textarea {

        color: white !important;

        font-size: 15px !important;
    }


    /* SIDEBAR TEXT */

    .side-title {

        color: white;

        font-size: 20px;

        font-weight: 800;

        text-align: center;

        letter-spacing: 2px;
    }


    .side-subtitle {

        color: #8094a9;

        font-size: 12px;

        text-align: center;

        margin-top: 5px;
    }


    .side-item {

        padding: 12px 15px;

        margin: 7px 0;

        border-radius: 12px;

        background: rgba(255,255,255,0.035);

        color: #b4c3d3;

        font-size: 14px;
    }


    /* FOOTER */

    .app-footer {

        text-align: center;

        color: #536579;

        font-size: 12px;

        margin-top: 35px;
    }

</style>
""", unsafe_allow_html=True)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown(
        """
        <div style="text-align:center; font-size:60px; margin-top:20px;">
            🤖
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="side-title">
            PERSONAL BOT
        </div>

        <div class="side-subtitle">
            Personal AI Assistant
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown(
        '<div class="side-item">💬 AI Chat</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="side-item">🧠 LangGraph Memory</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="side-item">⚡ Groq AI</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="side-item">🔒 Private Conversation</div>',
        unsafe_allow_html=True
    )

    st.divider()

    st.caption("PERSONAL BOT")
    st.caption("Powered by LangGraph + Groq")


# =========================================================
# MAIN HEADER
# =========================================================

st.html(
    """
    <div class="brand">

        <div class="brand-icon">
            🤖
        </div>

        <div class="brand-title">
            PERSONAL BOT
        </div>

        <div class="brand-subtitle">
            Your intelligent personal AI assistant
        </div>

        <div class="online">
            ● AI Online
        </div>

    </div>
    """
)


# =========================================================
# SESSION STATE
# =========================================================

if "message_history" not in st.session_state:

    st.session_state["message_history"] = []


# =========================================================
# WELCOME
# =========================================================

if len(st.session_state["message_history"]) == 0:

    st.html(
        """
        <div class="welcome-card">

            <div class="welcome-title">
                👋 Welcome to PERSONAL BOT
            </div>

            <div class="welcome-text">
                I'm your personal AI assistant.
                Ask me anything and I'll help you
                with your questions.
            </div>

        </div>
        """
    )

    st.write("")

    # =====================================================
    # QUICK ACTIONS
    # =====================================================

    col1, col2, col3 = st.columns(3)

    with col1:

        st.html(
            """
            <div class="quick-card">

                <div class="quick-icon">
                    💡
                </div>

                <div class="quick-title">
                    Ask a Question
                </div>

                <div class="quick-description">
                    Get quick answers
                    to your questions.
                </div>

            </div>
            """
        )


    with col2:

        st.html(
            """
            <div class="quick-card">

                <div class="quick-icon">
                    📚
                </div>

                <div class="quick-title">
                    Learn Something
                </div>

                <div class="quick-description">
                    Understand concepts
                    step by step.
                </div>

            </div>
            """
        )


    with col3:

        st.html(
            """
            <div class="quick-card">

                <div class="quick-icon">
                    🚀
                </div>

                <div class="quick-title">
                    Get Assistance
                </div>

                <div class="quick-description">
                    Let PERSONAL BOT
                    help you.
                </div>

            </div>
            """
        )


# =========================================================
# LANGGRAPH CONFIGURATION
# =========================================================

CONFIG = {
    "configurable": {
        "thread_id": "thread-1"
    }
}


# =========================================================
# LOAD CHAT HISTORY
# =========================================================

for message in st.session_state["message_history"]:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# =========================================================
# CHAT INPUT
# =========================================================

user_input = st.chat_input(
    "Message PERSONAL BOT..."
)


# =========================================================
# PROCESS MESSAGE
# =========================================================

if user_input:

    # USER MESSAGE

    st.session_state["message_history"].append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):

        st.markdown(user_input)


    # =====================================================
    # LANGGRAPH
    # =====================================================

    response = chatbot.invoke(
        {
            "messages": [
                HumanMessage(content=user_input)
            ]
        },
        config=CONFIG
    )


    # =====================================================
    # AI RESPONSE
    # =====================================================

    answer = response["messages"][-1].content


    # SAVE RESPONSE

    st.session_state["message_history"].append(
        {
            "role": "assistant",
            "content": answer
        }
    )


    # DISPLAY RESPONSE

    with st.chat_message("assistant"):

        st.markdown(answer)


# =========================================================
# FOOTER
# =========================================================

st.html(
    """
    <div class="app-footer">
        PERSONAL BOT • LangGraph • Groq AI
    </div>
    """
)