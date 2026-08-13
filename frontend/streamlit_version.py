import streamlit as st
import requests

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Car Price Predictor",
    page_icon="🚗",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>

    /* =========================
       GLOBAL APP
       ========================= */

    .stApp {
        background:
            radial-gradient(
                circle at 20% 10%,
                rgba(59, 130, 246, 0.18),
                transparent 30%
            ),
            radial-gradient(
                circle at 80% 90%,
                rgba(139, 92, 246, 0.15),
                transparent 30%
            ),
            #070b14;

        color: #ffffff;
    }

    /* Hide Streamlit branding */
    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        visibility: hidden;
    }

    /* Main page width */
    .block-container {
        max-width: 900px !important;
        padding-top: 45px !important;
        padding-bottom: 40px !important;
    }


    /* =========================
       HERO SECTION
       ========================= */

    .hero {
        text-align: center;
        margin-bottom: 30px;
    }

    .hero-icon {
        font-size: 55px;
        margin-bottom: 5px;
    }

    .hero h1 {
        font-size: 42px;
        font-weight: 800;
        letter-spacing: -1px;
        margin: 0 0 8px 0;

        background: linear-gradient(
            90deg,
            #ffffff,
            #93c5fd,
            #c4b5fd
        );

        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .hero p {
        color: #94a3b8;
        font-size: 16px;
        margin: 0;
    }


    /* =========================
       FORM CONTAINER
       ========================= */

    /* This targets the Streamlit container */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(15, 23, 42, 0.88) !important;

        border: 1px solid rgba(148, 163, 184, 0.16) !important;

        border-radius: 24px !important;

        padding: 30px 35px !important;

        box-shadow:
            0 25px 70px rgba(0, 0, 0, 0.45),
            inset 0 1px 0 rgba(255, 255, 255, 0.04);

        backdrop-filter: blur(18px);

        margin-bottom: 25px;
    }


    /* =========================
       SECTION TITLE
       ========================= */

    .section-title {
        font-size: 18px;
        font-weight: 700;
        color: #f8fafc;

        margin-top: 0;
        margin-bottom: 18px;

        padding-bottom: 12px;

        border-bottom:
            1px solid rgba(148, 163, 184, 0.12);
    }


    /* =========================
       LABELS
       ========================= */

    label {
        color: #cbd5e1 !important;
        font-weight: 600 !important;
    }


    /* =========================
       TEXT / NUMBER INPUTS
       ========================= */

    .stTextInput input,
    .stNumberInput input {

        background-color:
            rgba(15, 23, 42, 0.95) !important;

        border:
            1px solid #334155 !important;

        border-radius: 12px !important;

        color: #ffffff !important;

        min-height: 45px;
    }


    .stTextInput input:focus,
    .stNumberInput input:focus {

        border-color: #60a5fa !important;

        box-shadow:
            0 0 0 1px #60a5fa !important;
    }


    /* =========================
       SELECTBOX
       ========================= */

    div[data-baseweb="select"] > div {

        background-color:
            rgba(15, 23, 42, 0.95) !important;

        border:
            1px solid #334155 !important;

        border-radius: 12px !important;

        color: #ffffff !important;

        min-height: 45px;
    }

    div[data-baseweb="select"] span {
        color: #f8fafc !important;
    }

    div[data-baseweb="select"] svg {
        fill: #cbd5e1 !important;
    }


    /* =========================
       NUMBER INPUT BUTTONS
       ========================= */

    .stNumberInput button {

        background-color:
            rgba(30, 41, 59, 0.9) !important;

        color: #cbd5e1 !important;

        border: none !important;
    }

    .stNumberInput button:hover {
        background-color:
            rgba(51, 65, 85, 1) !important;
    }


    /* =========================
       PREDICT BUTTON
       ========================= */

    .stButton > button {

        width: 100%;

        height: 55px;

        border-radius: 14px;

        border: none;

        background:
            linear-gradient(
                135deg,
                #2563eb,
                #7c3aed
            );

        color: white;

        font-size: 17px;

        font-weight: 700;

        letter-spacing: 0.3px;

        box-shadow:
            0 10px 30px
            rgba(37, 99, 235, 0.3);

        transition:
            all 0.25s ease;
    }


    .stButton > button:hover {

        transform:
            translateY(-2px);

        box-shadow:
            0 15px 35px
            rgba(124, 58, 237, 0.4);

        background:
            linear-gradient(
                135deg,
                #3b82f6,
                #8b5cf6
            );
    }


    /* =========================
       PREDICTION BOX
       ========================= */

    .prediction-box {

        margin-top: 25px;

        padding: 25px;

        border-radius: 18px;

        text-align: center;

        background:
            linear-gradient(
                135deg,
                rgba(16, 185, 129, 0.15),
                rgba(59, 130, 246, 0.12)
            );

        border:
            1px solid
            rgba(52, 211, 153, 0.25);
    }


    .prediction-title {

        color: #94a3b8;

        font-size: 14px;

        margin-bottom: 8px;
    }


    .prediction-value {

        font-size: 32px;

        font-weight: 800;

        color: #6ee7b7;
    }


    /* =========================
       FOOTER
       ========================= */

    .footer {

        text-align: center;

        color: #64748b;

        font-size: 13px;

        margin-top: 25px;
    }


    /* =========================
       STREAMLIT SPACING
       ========================= */

    div[data-testid="stVerticalBlock"] {
        gap: 0.8rem;
    }


    /* =========================
       MOBILE RESPONSIVE
       ========================= */

    @media (max-width: 768px) {

        .block-container {
            padding-left: 20px !important;
            padding-right: 20px !important;
        }

        .hero h1 {
            font-size: 32px;
        }

        div[data-testid="stVerticalBlockBorderWrapper"] {
            padding: 22px 20px !important;
        }
    }

</style>
""", unsafe_allow_html=True)


# -----------------------------
# Header
# -----------------------------
st.markdown(
    """
    <div style="
        text-align: center;
        margin-bottom: 30px;
    ">
        <div style="
            font-size: 55px;
            margin-bottom: 5px;
        ">
            🚗
        </div>

       
    </div>
    """,
    unsafe_allow_html=True
)


# -----------------------------
# API
# -----------------------------
API_URL = "http://51.20.8.108:8000/predict"


# ============================================================
# FORM CONTAINER
# ============================================================

with st.container(border=True):

    st.markdown(
        '<div class="section-title">🚘 Vehicle Information</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2, gap="large")


    # -------------------------
    # LEFT COLUMN
    # -------------------------

    with col1:

        brand = st.text_input(
            "Car Brand",
            value="Ford",
            placeholder="e.g. Toyota"
        )

        model_year = st.number_input(
            "Model Year",
            min_value=1980,
            max_value=2026,
            value=2024
        )

        milage = st.number_input(
            "Mileage",
            min_value=0,
            value=51000,
            step=1000
        )

        fuel_type = st.selectbox(
            "Fuel Type",
            options=[
                "Gasoline",
                "Hybrid",
                "Diesel",
                "Other"
            ]
        )

        engine_size = st.number_input(
            "Engine Size (L)",
            min_value=0.5,
            max_value=10.0,
            value=3.7,
            step=0.1
        )


    # -------------------------
    # RIGHT COLUMN
    # -------------------------

    with col2:

        horsepower = st.number_input(
            "Horsepower",
            min_value=50.0,
            max_value=2000.0,
            value=600.0,
            step=10.0
        )

        cylinders = st.number_input(
            "Cylinders",
            min_value=2,
            max_value=16,
            value=6,
            step=1
        )

        transmission = st.selectbox(
            "Transmission",
            options=[
                "CVT",
                "Manual",
                "Automatic",
                "Other"
            ]
        )

        accident = st.selectbox(
            "Previous Accident?",
            options=[
                "No",
                "Yes"
            ]
        )

        # Empty space to make columns visually balanced
        st.write("")


    # -------------------------
    # BUTTON
    # -------------------------

    st.markdown("<br>", unsafe_allow_html=True)

    predict_button = st.button(
        "🔮  Predict Car Price",
        use_container_width=True
    )


# ============================================================
# PREDICTION
# ============================================================

if predict_button:

    data = {
        "brand": brand,
        "model_year": model_year,
        "milage": milage,
        "fuel_type": fuel_type,
        "engine_size": engine_size,
        "horsepower": horsepower,
        "cylinders": cylinders,
        "transmission": transmission,
        "accident": accident
    }

    try:

        with st.spinner("Analyzing your vehicle..."):

            response = requests.post(
                API_URL,
                json=data,
                timeout=30
            )


        if response.status_code == 200:

            prediction = response.json()

            price = prediction["price"]

            st.markdown(
                f"""
                <div class="prediction-box">
                        ${price}
                  

                </div>
                """,
                unsafe_allow_html=True
            )


        else:

            st.error(
                f"API Error: {response.status_code}"
            )


    except requests.exceptions.RequestException as e:

        st.error(
            f"Could not connect to prediction API: {e}"
        )


# -----------------------------
# Footer
# -----------------------------

st.markdown("""
<div class="footer">
    Powered by Machine Learning • FastAPI • Streamlit
</div>
""", unsafe_allow_html=True)