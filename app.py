import streamlit as st   

# --- TITLE ---
st.title("MarketMetrics: Campaign Performance Dashboard")

# --- DESCRIPTION ---
st.write("Enter your own campaign data below and we'll calculate how well your ad performed.")

st.divider()

# --- INPUT 1: Campaign name (the user types what they want) ---
campaign_name = st.text_input("What is your campaign called?", placeholder="e.g. Summer Sale, Holiday Promo...")

# --- INPUT 2: Channel selectbox (where did the ad run?) ---
channel = st.selectbox("Where did your ad run?", ["Instagram", "Facebook", "Google Ads", "Email", "TikTok", "Other"])

# --- INPUT 3: Impressions (how many people saw it?) ---
impressions = st.number_input("How many people SAW your ad? (Impressions)", min_value=0, step=1)

# --- INPUT 4: Clicks (how many people clicked it?) ---
clicks = st.number_input("How many people CLICKED your ad? (Clicks)", min_value=0, step=1)

# --- INPUT 5: Conversions (how many people took action?) ---
conversions = st.number_input("How many people took action after clicking? (Conversions)", min_value=0, step=1)

st.divider()

# --- OUTPUT ---
st.subheader("📊 Your Results")

# Only show results if the user has filled in a name and some numbers
if campaign_name == "":
    st.info(" Start by typing your campaign name above!")

elif impressions == 0:
    st.info(" Enter how many people saw your ad to get started.")

elif clicks > impressions:
    st.error("❌ Clicks can't be more than Impressions. Please check your numbers.")

elif conversions > clicks:
    st.error("❌ Conversions can't be more than Clicks. Please check your numbers.")

else:
    # Calculate the metrics
    ctr = clicks / impressions

    # Conversion rate = conversions divided by clicks
    if clicks > 0:
        conversion_rate = conversions / clicks
    else:
        conversion_rate = 0

    # Show a summary of what the user entered
    st.write(f"**Campaign Name:** {campaign_name}")
    st.write(f"**Channel:** {channel}")

    st.divider()

    # Show the raw numbers the user typed in
    st.write(f"👁️ **Impressions:** {impressions:,}  —  people who saw your ad")
    st.write(f"🖱️ **Clicks:** {clicks:,}  —  people who clicked your ad")
    st.write(f"✅ **Conversions:** {conversions:,}  —  people who took action")

    st.divider()

    # Show the calculated results
    st.write(f"📈 **CTR (Click-Through Rate):** {ctr:.2%}")
    st.caption("CTR = Clicks ÷ Impressions. This tells you what % of people who saw the ad actually clicked it.")

    st.write(f"🎯 **Conversion Rate:** {conversion_rate:.2%}")
    st.caption("Conversion Rate = Conversions ÷ Clicks. This tells you what % of people who clicked actually did something.")

    st.divider()

    # Give the user a simple based on CTR
    st.subheader("💡 Quick Verdict")
    if ctr >= 0.05:
        st.success(f"Great job! A {ctr:.2%} CTR is strong. Your ad is grabbing people's attention.")
    elif ctr >= 0.02:
        st.warning(f"Not bad! A {ctr:.2%} CTR is average. There might be room to improve your ad.")
    else:
        st.error(f"A {ctr:.2%} CTR is on the low side. Consider changing your ad image or wording.")