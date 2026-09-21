import streamlit as st

def show_business_insights(df):

    if df.empty:
        st.warning("No data available for the selected filters.")
        return
    
    top_region = (
        df.groupby("Region")["Sales"]
        .sum()
        .idxmax()
    )

    slow_region = (
        df.groupby("Region")["Shipping Days"]
        .mean()
        .idxmax()
    )

    best_ship_mode = (
        df.groupby("Ship Mode")["Sales"]
        .mean()
        .idxmax()
    )

    top_product = (
        df.groupby("Product Name")["Gross Profit"]
        .sum()
        .idxmax()
    )

    avg_shipping = df["Shipping Days"].mean()

    total_sales = df["Sales"].sum()
    total_profit = df["Gross Profit"].sum()

    profit_margin = (
        (total_profit / total_sales) * 100
        if total_sales != 0
        else 0
    )

    st.markdown(
        """
        <div class="chart-card">
        <div class="chart-title">
        💡 Executive Business Insights
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(f"""
    <div class="insight-card insight-success">
    <span class="insight-icon">🏆</span>
    {top_region} region generated the highest Sales.
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="insight-card insight-warning">
    <span class="insight-icon">⚠️</span>
    {slow_region} region has the highest average Shipping Days.
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="insight-card insight-info">
    <span class="insight-icon">📦</span>
    {best_ship_mode} has the highest average Sales per record among Ship Modes.
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="insight-card insight-success">
    <span class="insight-icon">💰</span>
    {top_product} generated the highest Gross Profit.
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="insight-card insight-info">
    <span class="insight-icon">🚚</span>
    Average Shipping Days: {avg_shipping:.0f}
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="insight-card insight-success">
    <span class="insight-icon">📈</span>
    Overall Profit Margin: {profit_margin:.2f}%
    </div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)