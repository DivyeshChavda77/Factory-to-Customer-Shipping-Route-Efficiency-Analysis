import streamlit as st
from pathlib import Path

import pandas as pd

from src.components.route_analysis import RouteAnalysis

from src.ui.cards import kpi_card
from src.ui.filters import sidebar_filters
from src.ui.navigation import create_tabs
from src.ui.charts import (
    sales_by_region, profit_by_region, sales_vs_profit, shipping_by_shipmode,
    fastest_cities, slowest_cities, shipping_by_state, shipping_by_region,
    monthly_sales, sales_by_ship_mode,  sales_by_division, sales_distribution,
    profit_by_product, top_products, bubble_sales_profit
    )
from src.ui.chart_card import (open_chart_card,close_chart_card)
from src.ui.route_summary import route_summary
from src.ui.insights import show_business_insights
from src.ui.data_explorer import data_explorer

BASE_DIR = Path(__file__).resolve().parent


def load_css():
    css_path = BASE_DIR / "assets" / "style.css"

    with open(css_path, encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

# =========== Page Configuration ===========
st.set_page_config(
    page_title="Factory-to-Customer Shipping Dashboard",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded"
)

load_css()

def display_chart(fig):
    st.plotly_chart(
        fig,
        use_container_width=True,
        config={"displayModeBar": False}
    )

# =========== Load Data Set =============
analysis = RouteAnalysis("artifacts/processed_data.csv")

df = analysis.df

# =========== Sidebar ===========
with st.sidebar:

    st.image(
        "https://img.icons8.com/fluency/96/shipping-container.png",
        width=80
    )

    st.markdown("## Shipping Dashboard")

    st.caption("Business Intelligence")

    filtered_df = sidebar_filters(df)

    if filtered_df.empty:
        st.warning(
            "No records match the selected filters. "
            "Please adjust the filters and try again."
        )
        st.stop()

# =========== Hero Banner ===========
st.markdown(
"""
<div class="hero">

<h1>📦 Factory-to-Customer Shipping Route Efficiency Dashboard</h1>

<p>
Analyze shipping performance,
route efficiency,
sales,
and profitability
using interactive business analytics.
</p>

</div>
""",
unsafe_allow_html=True
)

# =========== Calculate KPIs ===========
total_sales = filtered_df["Sales"].sum()

total_profit = filtered_df["Gross Profit"].sum()

total_orders = filtered_df["Order ID"].nunique()

total_units = filtered_df["Units"].sum()

avg_shipping = filtered_df["Shipping Days"].mean()

profit_margin = (
    total_profit / total_sales
) * 100

# Display Cards
st.markdown(
    '<h2 class="section-title">Executive KPIs</h2>',
    unsafe_allow_html=True
)

col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    kpi_card(
        "💰","Sales",
        f"${total_sales:,.0f}"
    )

with col2:
    kpi_card(
        "📈","Profit",
        f"${total_profit:,.0f}"
    )

with col3:
    kpi_card(
        "📋",
        "Orders",
        f"{total_orders:,}"
    )

with col4:
    kpi_card(
        "📦","Units",
        f"{total_units:,}"
    )

with col5:
    kpi_card(
        "🚚","Shipping",
        f"{avg_shipping:.0f} Days"
    )

with col6:
    kpi_card(
        "📊","Margin",
        f"{profit_margin:.1f}%"
    )

st.markdown(
    '<div class="section-space"></div>',
    unsafe_allow_html=True
)
# =========== Create tabs ===========
overview_tab, route_tab, sales_tab, product_tab, data_tab = create_tabs()

# ------------- Overview Tab -------------
with overview_tab:
    st.markdown(
        '<h2 class="section-title">📊 Executive Overview</h2>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
    
        open_chart_card(
            "📊 Sales by Region",
            "Total Sales generated across regions"
        )
        display_chart(
            sales_by_region(filtered_df)
        )
        close_chart_card()

    with col2:
        open_chart_card(
            "📈 Gross Profit",
            "Regional profit comparison"
        )
        display_chart(
            profit_by_region(filtered_df)
        )
        close_chart_card()

    col3, col4 = st.columns(2)

    with col3:
        open_chart_card(
            "📉 Sales vs Profit",
            "Relationship between Sales and Gross Profit"
        )
        display_chart(
            sales_vs_profit(filtered_df),
        )
        close_chart_card()

    with col4:
        open_chart_card(
            "🚚 Shipping Days",
            "Average shipping time by ship mode"
        )
        display_chart(
            shipping_by_shipmode(filtered_df),
        )
        close_chart_card()

# ------------- Route Tab -------------
with route_tab:
    st.markdown(
        '<h2 class="section-title">🚚 Route Analysis</h2>',
        unsafe_allow_html=True
    )

    route_summary(filtered_df)

# Fastest and slowest city
    
    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        open_chart_card(
            "🏆 Fastest Shipping Cities",
            "Cities with the lowest average shipping time"
        )
        display_chart(
            fastest_cities(filtered_df),
        )
        close_chart_card()

    with col2:
        open_chart_card(
            "⚠ Slowest Shipping Cities",
            "Cities with the highest average shipping time"
        )
        display_chart(
            slowest_cities(filtered_df),
        )
        close_chart_card()

    # Shipping by State and Region
    st.markdown("<br>", unsafe_allow_html=True)

    left, right = st.columns(2)

    with left:
        open_chart_card(
            "🌎 Shipping Performance by State",
            "Top 10 states with highest average shipping days"
        )
        display_chart(
            shipping_by_state(filtered_df),
        )
        close_chart_card()

    with right:
        open_chart_card(
            "🚚 Shipping Performance by Region",
            "Average shipping days across regions"
        )
        display_chart(
            shipping_by_region(filtered_df),
        )
        close_chart_card()

# ------------- Sales Tab -------------
with sales_tab:
    st.markdown(
    '<h2 class="section-title">💰 Sales Analysis</h2>',
    unsafe_allow_html=True
    )

    row1_col1, row1_col2 = st.columns(2)

    with row1_col1:
        open_chart_card(
            "📈 Monthly Sales Trend",
            "Sales trend over time"
        )
        display_chart(
            monthly_sales(filtered_df),
        )
        close_chart_card()

    with row1_col2:
        open_chart_card(
            "🚚 Sales by Ship Mode",
            "Sales distribution by shipping method"
        )
        display_chart(
            sales_by_ship_mode(filtered_df),
        )
        close_chart_card()

    row2_col1, row2_col2 = st.columns(2)

    with row2_col1:
        open_chart_card(
            "📦 Sales by Division",
            "Contribution of each product division"
        )
        display_chart(
            sales_by_division(filtered_df),
        )
        close_chart_card()

    with row2_col2:
        open_chart_card(
                "💵 Sales Distribution",
                "Distribution of sales values"
            )
        display_chart(
                sales_distribution(filtered_df),
            )
        close_chart_card()
        
# ------------- Product Tab -------------
with product_tab:
    st.markdown(
    '<h2 class="section-title">📦 Product Analysis</h2>',
    unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        open_chart_card(
            "💰 Profit by Product",
            "Top profit generating products"
        )

        display_chart(
            profit_by_product(filtered_df),
        )

        close_chart_card()

    with col2:
        open_chart_card(
            "🏆 Top Products",
            "Products generating the highest sales"
        )

        display_chart(
            top_products(filtered_df),
        )

        close_chart_card()

    open_chart_card(
        "💵 Sales vs Profit",
        "Relationship between sales, profit and units sold"
    )
    display_chart(
        bubble_sales_profit(filtered_df),
    )
    close_chart_card()

# ------------- Data Tab -------------
with data_tab:
    data_explorer(filtered_df)

# =========== Business Insights ===========
st.markdown("---")

show_business_insights(filtered_df)

# =========== Footer ===========
st.markdown("---")

st.markdown(
    """
<div style="
text-align:center;
padding:20px;
color:#6B7280;
font-size:14px;
">

📦 <b>Factory-to-Customer Shipping Route Efficiency Analysis</b>
<br><br>
Developed by <b>Divyesh Chavda</b>
Artificial Intelligence & Data Science
© 2026 All Rights Reserved
</div>
""",
unsafe_allow_html=True
)