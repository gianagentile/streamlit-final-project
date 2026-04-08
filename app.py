import streamlit as st   
import pandas as pd

# --- TITLE ---
st.title("MarketMetrics: Campaign Performance Dashboard")

# --- DESCRIPTION ---
st.write("Enter your own campaign data below and we'll calculate how well your ad performed.")

st.divider()

# --- OPTIONAL: Upload Data ---
st.subheader("📂 Upload Campaign Data (Optional)")
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Preview of Uploaded Data:")
    st.dataframe(df)

st.divider()

# --- INPUT SECTION ---
st.header("Enter Campaign Details")

campaign_name = st.text_input("What is your campaign called?", placeholder="e.g. Summer Sale, Holiday Promo...")

channel = st.selectbox("Where did your ad run?", ["Instagram", "Facebook", "Google Ads", "Email", "TikTok", "Other"])

impressions = st.number_input("How many people SAW your ad? (Impressions)", min_value=0, step=1)

clicks = st.number_input("How many people CLICKED your ad? (Clicks)", min_value=0, step=1)

conversions = st.number_input("How many people took action after clicking? (Conversions)", min_value=0, step=1)

st.divider()

# --- OUTPUT ---
st.subheader("📊 Your Results")

if campaign_name == "":
    st.info(" Start by typing your campaign name above!")

elif impressions == 0:
    st.info(" Enter how many people saw your ad to get started.")

elif clicks > impressions:
    st.error("❌ Clicks can't be more than Impressions. Please check your numbers.")

elif conversions > clicks:
    st.error("❌ Conversions can't be more than Clicks. Please check your numbers.")

else:
    ctr = clicks / impressions

    if clicks > 0:
        conversion_rate = conversions / clicks
    else:
        conversion_rate = 0

    st.write(f"**Campaign Name:** {campaign_name}")
    st.write(f"**Channel:** {channel}")

    st.divider()

    st.write(f"👁️ **Impressions:** {impressions:,}")
    st.write(f"🖱️ **Clicks:** {clicks:,}")
    st.write(f"✅ **Conversions:** {conversions:,}")

    st.divider()

    st.write(f"📈 **CTR (Click-Through Rate):** {ctr:.2%}")
    st.write(f"🎯 **Conversion Rate:** {conversion_rate:.2%}")

    st.divider()

    # --- NEW: CHART ---
    st.subheader("📊 Performance Chart")

    chart_data = pd.DataFrame({
        'Metric': ['Impressions', 'Clicks', 'Conversions'],
        'Value': [impressions, clicks, conversions]
    })

    st.bar_chart(chart_data.set_index('Metric'))

    st.divider()

    # --- Verdict ---
    st.subheader("💡 Quick Verdict")
    if ctr >= 0.05:
        st.success(f"Great job! A {ctr:.2%} CTR is strong.")
    elif ctr >= 0.02:
        st.warning(f"A {ctr:.2%} CTR is average.")
    else:
        st.error(f"A {ctr:.2%} CTR is low. Consider improving your ad.")