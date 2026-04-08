import streamlit as st
import pandas as pd

# --- TITLE ---
st.title("MarketMetrics: Campaign Performance Dashboard")

# --- DESCRIPTION ---
st.write("Enter your campaign data manually or upload a CSV to calculate CTR and Conversion Rate for your campaigns.")

st.divider()

# --- CSV UPLOADER ---
uploaded_file = st.file_uploader(
    "Upload a CSV with your campaign data (optional)",
    type=["csv"]
)

# --- CSV PROCESSING ---
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("📊 Campaign Results from CSV")

    # Calculate CTR and Conversion Rate
    df["CTR"] = df["Clicks"] / df["Impressions"]
    df["Conversion Rate"] = df.apply(
        lambda row: row["Conversions"] / row["Clicks"] if row["Clicks"] > 0 else 0,
        axis=1
    )

    st.dataframe(df)

    # Bar chart for CTR
    st.subheader("📈 CTR Chart")
    st.bar_chart(df.set_index("Campaign")["CTR"])

    # Bar chart for Conversion Rate
    st.subheader("🎯 Conversion Rate Chart")
    st.bar_chart(df.set_index("Campaign")["Conversion Rate"])

    # Optional: download results
    st.download_button(
        "Download results as CSV",
        df.to_csv(index=False),
        file_name="campaign_results.csv"
    )

else:
    # --- MANUAL INPUTS ---
    st.subheader("Or enter campaign data manually:")

    campaign_name = st.text_input("Campaign Name", placeholder="e.g. Summer Sale, Holiday Promo...")
    channel = st.selectbox("Channel", ["Instagram", "Facebook", "Google Ads", "Email", "TikTok", "Other"])
    impressions = st.number_input("Impressions (people who saw your ad)", min_value=0, step=1)
    clicks = st.number_input("Clicks (people who clicked)", min_value=0, step=1)
    conversions = st.number_input("Conversions (people who took action)", min_value=0, step=1)

    st.divider()

    # --- OUTPUT ---
    st.subheader("📊 Your Results")

    if campaign_name == "":
        st.info("Start by typing your campaign name above!")

    elif impressions == 0:
        st.info("Enter how many people saw your ad to get started.")

    elif clicks > impressions:
        st.error("❌ Clicks can't be more than Impressions. Please check your numbers.")

    elif conversions > clicks:
        st.error("❌ Conversions can't be more than Clicks. Please check your numbers.")

    else:
        ctr = clicks / impressions
        conversion_rate = conversions / clicks if clicks > 0 else 0

        st.write(f"**Campaign Name:** {campaign_name}")
        st.write(f"**Channel:** {channel}")

        st.divider()

        st.write(f"👁️ **Impressions:** {impressions:,}")
        st.write(f"🖱️ **Clicks:** {clicks:,}")
        st.write(f"✅ **Conversions:** {conversions:,}")

        st.divider()

        st.write(f"📈 **CTR (Click-Through Rate):** {ctr:.2%}")
        st.caption("CTR = Clicks ÷ Impressions")

        st.write(f"🎯 **Conversion Rate:** {conversion_rate:.2%}")
        st.caption("Conversion Rate = Conversions ÷ Clicks")

        st.divider()

        # --- Quick Verdict ---
        st.subheader("💡 Quick Verdict")
        if ctr >= 0.05:
            st.success(f"Great job! A {ctr:.2%} CTR is strong.")
        elif ctr >= 0.02:
            st.warning(f"Not bad! A {ctr:.2%} CTR is average.")
        else:
            st.error(f"A {ctr:.2%} CTR is low. Consider improving your ad.")

        # --- CHARTS FOR MANUAL INPUT ---
        manual_df = pd.DataFrame({
            "Campaign": [campaign_name],
            "CTR": [ctr],
            "Conversion Rate": [conversion_rate],
            "Impressions": [impressions],
            "Clicks": [clicks],
            "Conversions": [conversions]
        })

        st.subheader("📈 CTR Chart")
        st.bar_chart(manual_df.set_index("Campaign")["CTR"])

        st.subheader("🎯 Conversion Rate Chart")
        st.bar_chart(manual_df.set_index("Campaign")["Conversion Rate"])