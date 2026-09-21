import streamlit as st

def route_summary(df):
    
    total_factory = 5
    total_region = df["Region"].nunique()
    total_state = df["State/Province"].nunique()
    total_city = df["City"].nunique()
    total_orders = df["Order ID"].nunique()
    avg_shipping = df["Shipping Days"].mean()
    best_city = (
        df.groupby("City")["Shipping Days"]
        .mean()
        .idxmin()
    )
    slowest_city = (
        df.groupby("City")["Shipping Days"]
        .mean()
        .idxmax()
    )

    st.markdown(f"""
    <div class="route-summary">

    <h3 class="route-summary-title">
    📊 Route Summary
    </h3>

    <div class="summary-grid">

    <div class="summary-item">
        <span class="summary-icon">🏭</span>
        <span class="summary-label">Factories</span>
        <span class="summary-value">{total_factory}</span>
    </div>

    <div class="summary-item">
        <span class="summary-icon">🌎</span>
        <span class="summary-label">Regions</span>
        <span class="summary-value">{total_region}</span>
    </div>

    <div class="summary-item">
        <span class="summary-icon">🗺️</span>
        <span class="summary-label">States</span>
        <span class="summary-value">{total_state}</span>
    </div>

    <div class="summary-item">
        <span class="summary-icon">🏙️</span>
        <span class="summary-label">Cities</span>
        <span class="summary-value">{total_city}</span>
    </div>

    <div class="summary-item">
        <span class="summary-icon">📦</span>
        <span class="summary-label">Orders</span>
        <span class="summary-value">{total_orders:,}</span>
    </div>

    <div class="summary-item">
        <span class="summary-icon">🚚</span>
        <span class="summary-label">Avg Shipping</span>
        <span class="summary-value">{avg_shipping:.0f} Days</span>
    </div>

    <div class="summary-item">
        <span class="summary-icon">⚡</span>
        <span class="summary-label">Best City</span>
        <span class="summary-value">{best_city}</span>
    </div>

    <div class="summary-item">
        <span class="summary-icon">🐢</span>
        <span class="summary-label">Slowest City</span>
        <span class="summary-value">{slowest_city}</span>
    </div>

    </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<h3 class="route-summary-title">📋 Route Performance</h3>',
        unsafe_allow_html=True
    )

    route_performance = (
        df.groupby("City", as_index=False)
        .agg(
            Orders=("Order ID", "nunique"),
            Sales=("Sales", "sum"),
            Profit=("Gross Profit", "sum"),
            Avg_Shipping_Days=("Shipping Days", "mean")
        )
        .sort_values(
            "Avg_Shipping_Days",
            ascending=False
        )
    )

    route_performance["Profit Margin"] = (
        route_performance["Profit"]
        .div(route_performance["Sales"])
        .mul(100)
        .fillna(0)
    )

    route_performance["Sales"] = (
    route_performance["Sales"].round(0)
    )

    route_performance["Profit"] = (
        route_performance["Profit"].round(0)
    )

    route_performance["Avg_Shipping_Days"] = (
        route_performance["Avg_Shipping_Days"].round(1)
    )

    route_performance["Profit Margin"] = (
        route_performance["Profit Margin"].round(1)
    )

    st.dataframe(
        route_performance,
        use_container_width=True,
        hide_index=True
    )
