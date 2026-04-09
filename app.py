import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go  # needed for the donut charts

# --- TITLE ---
st.title("MarketMetrics: Campaign Performance Dashboard")

# --- DESCRIPTION ---
st.write("Enter your campaign data manually or upload a CSV to calculate CTR and Conversion Rate for your campaigns.")

st.divider()

# --- HELPER FUNCTION: builds all 3 charts from a dataframe ---
def show_charts(df):
    st.divider()
    st.subheader("📊 Charts")

    # --- CHARTS 1 & 2: Donut charts for CTR and Conversion Rate ---
    # We put them side by side using columns
    col1, col2 = st.columns(2)

    # Loop through each campaign row and show a donut for each
    for _, row in df.iterrows():
        ctr_val = row["CTR"]
        cr_val  = row["Conversion Rate"]
        name    = row["Campaign"]

        # --- CHART 1: CTR Donut ---
        # The donut shows the CTR % as a slice, and the rest as grey
        fig1 = go.Figure(go.Pie(
            values=[ctr_val, 1 - ctr_val],        # slice = CTR, remainder = the rest
            labels=["CTR", ""],
            hole=0.6,                              # 0.6 makes it a donut (bigger hole = thinner ring)
            marker_colors=["#636EFA", "#e8e8e8"],  # blue for CTR, grey for the rest
            textinfo="none",                       # hide labels on the slices themselves
        ))
        fig1.update_layout(
            title=f"CTR — {name}<br><b>{ctr_val:.2%}</b>",  # show campaign name + % in title
            showlegend=False,
            margin=dict(t=80, b=20, l=20, r=20),
        )

        # --- CHART 2: Conversion Rate Donut ---
        fig2 = go.Figure(go.Pie(
            values=[cr_val, 1 - cr_val],
            labels=["Conversion Rate", ""],
            hole=0.6,
            marker_colors=["#00CC96", "#e8e8e8"],  # green for conversion rate
            textinfo="none",
        ))
        fig2.update_layout(
            title=f"Conversion Rate — {name}<br><b>{cr_val:.2%}</b>",
            showlegend=False,
            margin=dict(t=80, b=20, l=20, r=20),
        )

        # Place the two donuts side by side
        with col1:
            st.plotly_chart(fig1, use_container_width=True)
        with col2:
            st.plotly_chart(fig2, use_container_width=True)

    # --- CHART 3: Impressions, Clicks, Conversions grouped bar chart ---
    melted = df.melt(
        id_vars="Campaign",
        value_vars=["Impressions", "Clicks", "Conversions"],
        var_name="Metric",
        value_name="Count"
    )
    fig3 = px.bar(
        melted,
        x="Campaign",
        y="Count",
        color="Metric",
        barmode="group",
        title="Impressions, Clicks & Conversions by Campaign",
        text="Count",
        color_discrete_map={
            "Impressions": "#636EFA",
            "Clicks":      "#EF553B",
            "Conversions": "#00CC96"
        }
    )
    fig3.update_traces(textposition="outside")
    st.plotly_chart(fig3, use_container_width=True)


# --- CSV UPLOADER ---
uploaded_file = st.file_uploader(
    "Upload a CSV with your campaign data (optional)",
    type=["csv"]
)

# --- CSV PROCESSING ---
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    df["CTR"] = df["Clicks"] / df["Impressions"]
    df["Conversion Rate"] = df.apply(
        lambda row: row["Conversions"] / row["Clicks"] if row["Clicks"] > 0 else 0,
        axis=1
    )

    st.subheader("📋 Campaign Data")
    st.dataframe(df)

    st.download_button(
        "⬇️ Download results as CSV",
        df.to_csv(index=False),
        file_name="campaign_results.csv"
    )

    show_charts(df)

else:
    # --- MANUAL INPUTS ---
    st.subheader("Or enter your campaign data manually:")

    campaign_name = st.text_input("Campaign Name", placeholder="e.g. Summer Sale, Holiday Promo...")
    channel       = st.selectbox("Channel", ["Instagram", "Facebook", "Google Ads", "Email", "TikTok", "Other"])
    impressions   = st.number_input("Impressions (people who saw your ad)", min_value=0, step=1)
    clicks        = st.number_input("Clicks (people who clicked)", min_value=0, step=1)
    conversions   = st.number_input("Conversions (people who took action)", min_value=0, step=1)

    st.divider()

    st.subheader("📊 Your Results")

    if campaign_name == "":
        st.info("👆 Start by typing your campaign name above!")

    elif impressions == 0:
        st.info("👆 Enter how many people saw your ad to get started.")

    elif clicks > impressions:
        st.error("❌ Clicks can't be more than Impressions. Please check your numbers.")

    elif conversions > clicks:
        st.error("❌ Conversions can't be more than Clicks. Please check your numbers.")

    else:
        ctr             = clicks / impressions
        conversion_rate = conversions / clicks if clicks > 0 else 0

        st.write(f"**Campaign Name:** {campaign_name}")
        st.write(f"**Channel:** {channel}")

        st.divider()

        st.write(f"👁️ **Impressions:** {impressions:,}  —  people who saw your ad")
        st.write(f"🖱️ **Clicks:** {clicks:,}  —  people who clicked your ad")
        st.write(f"✅ **Conversions:** {conversions:,}  —  people who took action")

        st.divider()

        st.write(f"📈 **CTR (Click-Through Rate):** {ctr:.2%}")
        st.caption("CTR = Clicks ÷ Impressions")

        st.write(f"🎯 **Conversion Rate:** {conversion_rate:.2%}")
        st.caption("Conversion Rate = Conversions ÷ Clicks")

        st.divider()

        st.subheader("💡 Quick Verdict")
        if ctr >= 0.05:
            st.success(f"Great job! A {ctr:.2%} CTR is strong.")
        elif ctr >= 0.02:
            st.warning(f"Not bad! A {ctr:.2%} CTR is average.")
        else:
            st.error(f"A {ctr:.2%} CTR is low. Consider improving your ad.")

        manual_df = pd.DataFrame({
            "Campaign":        [campaign_name],
            "CTR":             [ctr],
            "Conversion Rate": [conversion_rate],
            "Impressions":     [impressions],
            "Clicks":          [clicks],
            "Conversions":     [conversions]
        })

        show_charts(manual_df)