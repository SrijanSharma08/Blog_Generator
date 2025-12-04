# ui.py
import streamlit as st
from backend import generate_blog

# ---------- Page & Global Styles ---------- #

st.set_page_config(
    page_title="Generate Blogs",
    page_icon="✍🏻",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    .stApp {
        background: radial-gradient(circle at top left, #1f2933 0, #020617 40%, #000000 100%);
        color: #f9fafb;
    }

    /* Layout container */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 2rem !important;
        max-width: 1400px !important;
        margin: 0 auto !important;
    }

    /* Wrapper (no visible box) */
    .app-card {
        padding: 0 0 2.3rem 0;
        margin-top: 0.2rem;
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
    }

    /* ------------------------------
            PAGE TITLE
    ------------------------------ */
    .app-title {
        font-size: 3.1rem;
        font-weight: 900;
        letter-spacing: 0.04em;
        text-align: center;

        background: linear-gradient(90deg, #ffffff 0%, #ff7b7b 50%, #ff4b4b 100%);
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;

        margin-bottom: 0.3rem;

        transition: transform 0.25s ease, text-shadow 0.25s ease, letter-spacing 0.25s ease;
    }

    .app-title:hover {
        transform: translateY(-2px) scale(1.015);
        letter-spacing: 0.055em;
        text-shadow: 0 0 18px rgba(248, 113, 113, 0.55);
    }

    .app-subtitle {
        font-size: 1rem;
        color: #b6c2d1;
        text-align: center;
        max-width: 650px;
        margin: 0.4rem auto 1.4rem auto;
        transition: color 0.25s ease, transform 0.25s ease;
    }

    .app-subtitle:hover {
        color: #e5e7eb;
        transform: translateY(-1px);
    }

    /* Labels */
    .field-label {
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        color: #9ca3af;
        font-weight: 600;
        margin-bottom: 0.12rem;
        transition: color 0.2s ease, letter-spacing 0.2s ease, transform 0.2s ease;
    }

    .field-label:hover {
        color: #e5e7eb;
        letter-spacing: 0.11em;
        transform: translateY(-1px);
    }

    /* Accent color palette */
    :root {
        --accent-red: #ff4b4b;
        --warning-bg: rgba(255, 75, 75, 0.14);
        --warning-border: rgba(255, 75, 75, 0.4);
        --warning-text: #ffb4b4;
    }

    /* ------------------------------
           BUTTON STYLING
    ------------------------------ */
    div.stButton > button {
        border-radius: 0.75rem !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        padding: 0.6rem 0.9rem !important;
        background-color: var(--accent-red) !important;
        color: white !important;
        border: none !important;
        transition: background-color 0.2s ease, transform 0.15s ease, box-shadow 0.15s ease;
    }

    div.stButton > button:hover {
        background-color: #e24343 !important;
        transform: translateY(-1px);
        box-shadow: 0 8px 20px rgba(248, 113, 113, 0.35);
    }

    div.stButton > button:active {
        transform: translateY(0px) scale(0.99);
        box-shadow: 0 3px 10px rgba(15, 23, 42, 0.9);
    }

    /* Generate button container */
    .generate-btn {
        width: 100%;
        margin-top: 0.9rem;
        display: flex;
        justify-content: flex-start;  /* left align under Tone */
    }

    .generate-btn div.stButton > button {
        width: 160px;  /* smaller button */
    }

    /* ------------------------------
          FORM CONTROLS
    ------------------------------ */
    .stTextInput, .stSelectbox, .stSlider {
        margin-top: 0.18rem !important;
        margin-bottom: 0.75rem !important;
    }

    /* Inputs & dropdowns */
    .stSelectbox > div > div,
    .stTextInput > div > div {
        border-radius: 0.70rem !important;
        background-color: #020617 !important;
        border: 1px solid #374151 !important;
        height: 42px !important;
        transition: border-color 0.2s ease, box-shadow 0.2s ease, transform 0.2s ease;
    }

    .stSelectbox > div > div:hover,
    .stTextInput > div > div:hover {
        border-color: rgba(248, 113, 113, 0.85) !important;
        box-shadow: 0 0 0 1px rgba(248, 113, 113, 0.55);
        transform: translateY(-1px);
    }

    .stTextInput input {
        border-radius: 0.70rem !important;
        background-color: #020617 !important;
        color: #e5e7eb !important;
    }

    .stTextInput input::placeholder {
        color: #6b7280 !important;
    }

    .stSlider [role="slider"] {
        background-color: var(--accent-red) !important;
        box-shadow: 0 0 0 3px rgba(255, 120, 120, 0.35) !important;
    }

    /* ------------------------------
          WARNING MESSAGE
    ------------------------------ */
    .stAlert {
        background-color: var(--warning-bg) !important;
        border: 1px solid var(--warning-border) !important;
        color: var(--warning-text) !important;
        border-radius: 0.75rem !important;
        padding: 0.9rem !important;
        margin-top: 1rem !important;
        transition: border-color 0.2s ease, box-shadow 0.2s ease, transform 0.2s ease;
    }

    .stAlert:hover {
        border-color: rgba(255, 129, 129, 0.9) !important;
        box-shadow: 0 10px 25px rgba(248, 113, 113, 0.35);
        transform: translateY(-1px);
    }

    /* ------------------------------
         GENERATED BLOG CARD
    ------------------------------ */
    .blog-box {
        margin-top: 1.2rem;
        padding: 1.0rem 1.3rem;    /* LESS TOP PADDING = no big empty area */
        border-radius: 1.0rem;
        background: rgba(15, 23, 42, 0.96);
        border: 1px solid rgba(75, 85, 99, 0.6);
        transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease;
    }

    .blog-box:hover {
        transform: translateY(-3px);
        border-color: rgba(248, 113, 113, 0.8);
        box-shadow: 0 18px 40px rgba(15, 23, 42, 0.95);
    }

    .blog-box h1, .blog-box h2, .blog-box h3 {
        color: #f1f5f9 !important;
        font-weight: 700 !important;
        transition: color 0.2s ease, transform 0.2s ease;
        margin-top: 0.2rem;   /* tighter to top of card */
    }

    .blog-box h1:hover, .blog-box h2:hover, .blog-box h3:hover {
        color: #fee2e2 !important;
        transform: translateY(-1px);
    }

    /* Download button inside blog card */
    div.stDownloadButton > button {
        border-radius: 0.6rem !important;
        padding: 0.45rem 0.95rem !important;
        font-size: 0.9rem !important;
        font-weight: 500 !important;
        background-color: transparent !important;
        color: #fecaca !important;
        border: 1px solid rgba(248, 113, 113, 0.85) !important;
        transition: background-color 0.2s ease, color 0.2s ease,
                    box-shadow 0.2s ease, transform 0.2s ease;
    }

    div.stDownloadButton > button:hover {
        background-color: rgba(248, 113, 113, 0.15) !important;
        color: #ffe4e6 !important;
        box-shadow: 0 8px 20px rgba(248, 113, 113, 0.35);
        transform: translateY(-1px);
    }

    /* ------------------------------
         PREVIOUS BLOGS
    ------------------------------ */
    .history-empty {
        margin-top: 0.3rem;
        padding: 0.9rem 1rem;
        border-radius: 0.9rem;
        background: rgba(30, 64, 175, 0.18);
        border: 1px solid rgba(59, 130, 246, 0.45);
        font-size: 0.9rem;
        color: #dbeafe;
        transition: border-color 0.2s ease, background-color 0.2s ease, transform 0.2s ease;
    }

    .history-empty:hover {
        background: rgba(37, 99, 235, 0.25);
        border-color: rgba(96, 165, 250, 0.95);
        transform: translateY(-1px);
    }

    .stExpander {
        border-radius: 0.9rem !important;
        border: 1px solid rgba(75, 85, 99, 0.7) !important;
        background: rgba(15, 23, 42, 0.92) !important;
        transition: border-color 0.2s ease, transform 0.2s ease, box-shadow 0.2s ease;
    }

    .stExpander:hover {
        border-color: rgba(148, 163, 184, 0.9) !important;
        transform: translateY(-1px);
        box-shadow: 0 16px 35px rgba(15, 23, 42, 0.95);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- Session State (History) ---------- #

if "history" not in st.session_state:
    st.session_state.history = []  # {topic, audience, tone, words, content}

# ---------- UI ---------- #

with st.container():
    st.markdown('<div class="app-card">', unsafe_allow_html=True)

    st.markdown('<div class="app-title">Generate Blogs</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="app-subtitle">Give a topic, choose the audience and tone, '
        'and let the model craft a structured blog for you.</div>',
        unsafe_allow_html=True,
    )

    left_col, right_col = st.columns([5, 3])

    # ===== LEFT (Form) ===== #
    with left_col:
        st.markdown('<div class="field-label">Enter the Topic for the Blog</div>', unsafe_allow_html=True)
        topic = st.text_input(
            label="Topic",
            placeholder="e.g. F1, Quantum Computing for Beginners, Climate Change and Policy",
            key="topic_input",
            label_visibility="collapsed",
        )

        c1, c2 = st.columns([1, 1])

        with c1:
            st.markdown('<div class="field-label">Number of Words</div>', unsafe_allow_html=True)
            n_words = st.slider(
                label="Number of Words",
                min_value=50,
                max_value=1000,
                value=200,
                step=50,
                key="word_slider",
                label_visibility="collapsed",
            )

        with c2:
            st.markdown('<div class="field-label">Writing the blog for</div>', unsafe_allow_html=True)
            audience = st.selectbox(
                label="Writing the blog for",
                options=(
                    "Researchers",
                    "Data Scientists",
                    "College Students",
                    "High School Students",
                    "Complete Beginners",
                    "Tech Enthusiasts",
                    "Business Executives",
                    "Product Managers",
                    "Software Developers",
                    "Marketing Professionals",
                    "General Audience",
                    "Domain Experts",
                ),
                index=10,
                key="audience_select",
                label_visibility="collapsed",
            )

        st.markdown('<div class="field-label">Tone</div>', unsafe_allow_html=True)
        tone = st.selectbox(
            label="Tone",
            options=("Formal", "Casual", "Storytelling", "Persuasive", "Technical", "Friendly"),
            index=0,
            key="tone_select",
            label_visibility="collapsed",
        )

        # Generate button – smaller & aligned under Tone
        st.markdown('<div class="generate-btn">', unsafe_allow_html=True)
        submit = st.button("Generate")
        st.markdown("</div>", unsafe_allow_html=True)

        blog = None
        if submit:
            if not topic.strip():
                st.warning("Please enter a topic for the blog.")
            else:
                with st.spinner("✨ Generating your blog..."):
                    blog = generate_blog(topic, n_words, audience, tone)

        if blog:
            st.markdown('<div class="blog-box">', unsafe_allow_html=True)
            st.subheader("📝 Generated Blog")
            st.markdown(blog)

            word_count = len(blog.split())

            info_col, dl_col = st.columns([3, 1])
            with info_col:
                st.caption(f"Approximate word count: {word_count} words")
            with dl_col:
                st.download_button(
                    label="Download .txt",
                    data=blog,
                    file_name=f"{topic[:40].replace(' ', '_') or 'blog'}.txt",
                    mime="text/plain",
                    key="download_blog_txt",
                )

            st.markdown("</div>", unsafe_allow_html=True)

            st.session_state.history.append(
                {
                    "topic": topic,
                    "audience": audience,
                    "tone": tone,
                    "words": word_count,
                    "content": blog,
                }
            )
            if len(st.session_state.history) > 10:
                st.session_state.history.pop(0)

    # ===== RIGHT (History) ===== #
    with right_col:
        st.markdown('<div class="field-label">Previous Blogs</div>', unsafe_allow_html=True)

        if not st.session_state.history:
            st.markdown(
                '<div class="history-empty">📝 No previous blogs yet. Generate one to begin!</div>',
                unsafe_allow_html=True,
            )
        else:
            for item in reversed(st.session_state.history):
                label = f"{item['topic']} · {item['audience']} · {item['tone']} ({item['words']} words)"
                with st.expander(label):
                    st.markdown(item["content"])
                    st.caption("Saved from a previous generation.")

    st.markdown("</div>", unsafe_allow_html=True)
