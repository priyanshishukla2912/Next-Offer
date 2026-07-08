import streamlit as st

def footer():
    st.markdown("""
    <hr style="margin-top:40px; margin-bottom:15px; border:0.5px solid #30363d;">

    <div style="
        text-align:center;
        color:#A0AEC0;
        font-size:15px;
        padding-bottom:20px;
    ">
        <b>Next Offer</b><br>
        Built with ❤️ by <span style="color:#4F9DFF;">Priyanshi Shukla</span><br>
        <span style="font-size:12px;">
            Your Personalised Placement Prediction Platform :)
        </span>
    </div>
    """, unsafe_allow_html=True)