import plotly.express as px
import pandas as pd

def chart_layout(fig, x_title="", y_title=""):
    fig.update_layout(
        template="plotly_dark",

        paper_bgcolor="#1E293B",
        plot_bgcolor="#1E293B",

        font=dict(
            family="Segoe UI",
            size=13,
            color="#F8FAFC"
        ),

        title="",
        showlegend=False,
        hovermode="closest",

        margin=dict(
            l=20,
            r=20,
            t=20,
            b=20
        ),

        hoverlabel=dict(
            bgcolor="#0F172A",
            bordercolor="#3B82F6",
            font=dict(
                color="#F8FAFC",
                size=14,
                family="Segoe UI"
            )
        ),

        xaxis=dict(
            title=x_title,
            showgrid=False,
            zeroline=False,
            showline=True,
            linecolor="#475569",

            tickfont=dict(
                size=12,
                color="#CBD5E1"
            )
        ),

        yaxis=dict(
            title=y_title,
            showgrid=True,
            gridcolor="#334155",
            gridwidth=1,
            zeroline=False,
            showline=True,
            linecolor="#475569",

            tickfont=dict(
                size=12,
                color="#CBD5E1"
            )
        )
    )

    return fig

# Sales By Region
def sales_by_region(df):
    sales = (
        df.groupby("Region",as_index=False)["Sales"]
        .sum()
        .sort_values("Sales",ascending=False)
    )
    fig = px.bar(
        sales,
        x="Region",
        y="Sales",
        color="Sales",
        text_auto=".2s",
        color_continuous_scale="Blues"
    )
    fig.update_layout(
        coloraxis_showscale=False
    )

    return chart_layout(
        fig,
         x_title="Region",
        y_title="Sales ($)"
        )

# Profit by Region
def profit_by_region(df):

    profit = (
        df.groupby("Region", as_index=False)["Gross Profit"]
        .sum()
        .sort_values("Gross Profit", ascending=False)
    )

    fig = px.bar(
        profit,
        x="Region",
        y="Gross Profit",
        color="Gross Profit",
        text_auto=".2s",
        color_continuous_scale="Greens"
    )
    fig.update_layout(
        coloraxis_showscale=False
    )

    return chart_layout(
        fig,
        x_title="Region",
        y_title="Gross Profit ($)"
    )

# Sales vs Profit
def sales_vs_profit(df):
    summary = (
        df.groupby("Region", as_index=False)
        .agg({
            "Sales": "sum",
            "Gross Profit": "sum",
            "Units": "sum"
        })
    )

    fig = px.scatter(
        summary,
        x="Sales",
        y="Gross Profit",
        color="Region",
        size="Units",
        hover_name="Region",
        labels={
            "Sales": "Sales",
            "Gross Profit": "Gross Profit",
            "Units": "Units"
        },
        hover_data={
            "Sales": ":,.0f",
            "Gross Profit": ":,.0f",
            "Units": ":,.0f"
        }
    )
    fig.update_layout(
        title_text="",
        coloraxis_showscale=False
    )      

    return chart_layout(
        fig,
        x_title="Sales ($)",
        y_title="Gross Profit ($)"
    )

# Shiping by Shipmode
def shipping_by_shipmode(df):
    shipping = (
        df.groupby("Ship Mode", as_index=False)["Shipping Days"]
        .mean()
        .sort_values("Shipping Days")
    )

    fig = px.bar(
        shipping,
        x="Ship Mode",
        y="Shipping Days",
        color="Shipping Days",
        text_auto=".0f",
        color_continuous_scale="Oranges"
    )
    fig.update_layout(
     coloraxis_showscale=False
    )

    return chart_layout(
        fig,
        x_title="Ship Mode",
        y_title="Average Shipping Days"
    )

# -----------------Route Analysis Tab --------------
# Fastest and slowest city

def fastest_cities(df):

    fastest = (
        df.groupby("City", as_index=False)
        .agg({
            "Shipping Days": "mean"
        })
        .sort_values("Shipping Days")
        .head(10)
    )

    fig = px.bar(
        fastest,
        x="Shipping Days",
        y="City",
        orientation="h",
        text_auto=".0f",
        color="Shipping Days",
        color_continuous_scale="Tealgrn",
        title="Top 10 Fastest Shipping Cities"
    )
    fig.update_traces(
        hovertemplate="<b>%{y}</b><br>Value: %{x:,.2f}<extra></extra>"
    )

    fig.update_layout(
        title=None,
        coloraxis_showscale=False,
        yaxis=dict(categoryorder="total ascending")
    )

    return chart_layout(
        fig,
        x_title="Average Shipping Days",    
        y_title="City")

def slowest_cities(df):

    slowest = (
        df.groupby("City", as_index=False)
        .agg({
            "Shipping Days": "mean"
        })
        .sort_values("Shipping Days", ascending=False)
        .head(10)
    )

    fig = px.bar(
        slowest,
        x="Shipping Days",
        y="City",
        orientation="h",
        text_auto=".0f",
        color="Shipping Days",
        color_continuous_scale="Sunset",
        title="Top 10 Slowest Shipping Cities"
    )

    fig.update_layout(
        title=None,
        coloraxis_showscale=False
    )

    return chart_layout(
        fig,
        x_title="Average Shipping Days",
        y_title="City"
        )

# Shipping by State
def shipping_by_state(df):
    state = (
        df.groupby("State/Province", as_index=False)
        .agg({"Shipping Days":"mean"})
        .sort_values("Shipping Days", ascending=False)
        .head(10)
    )

    fig = px.bar(
        state,
        x="Shipping Days",
        y="State/Province",
        orientation="h",
        color="Shipping Days",
        color_continuous_scale="Mint",
        text_auto=".0f"
    )
    fig.update_layout(
        title=None,
        coloraxis_showscale=False,
        yaxis=dict(categoryorder="total ascending")
    )

    return chart_layout(
        fig,
        x_title="Average Shipping Days",
        y_title="State/Province"
    )

# Shipping by Region
def shipping_by_region(df):
    region = (
        df.groupby("Region", as_index=False)
        .agg({"Shipping Days":"mean"})
    )

    fig = px.bar(
        region,
        x="Region",
        y="Shipping Days",
        color="Shipping Days",
        color_continuous_scale="Oranges",
        text_auto=".0f"
    )

    fig.update_layout(
        title=None,
        coloraxis_showscale=False
    )

    return chart_layout(
        fig,
        x_title="Region",
        y_title="Average Shipping Days"
    )

# --------------Salse Tab Charts----------------

# Monthly Sales Trend
def monthly_sales(df):

    data = df.copy()

    data["Order Date"] = pd.to_datetime(
        data["Order Date"],
        errors="coerce"
    )

    monthly = (
        data.dropna(subset=["Order Date"])
        .assign(
            Month=data["Order Date"].dt.to_period("M")
        )
        .groupby("Month", as_index=False)
        .agg({
            "Sales": "sum"
        })
        .sort_values("Month")
    )

    monthly["Month"] = monthly["Month"].astype(str)

    fig = px.line(
        monthly,
        x="Month",
        y="Sales",
        markers=True
    )

    fig.update_traces(
        line=dict(width=4),
        marker=dict(size=8)
    )

    fig.update_layout(
        title=None,
        coloraxis_showscale=False
    )

    return chart_layout(
        fig,
        x_title="Order Month",
        y_title="Sales"
    )

# Sales by shipMode
def sales_by_ship_mode(df):
    ship = (
        df.groupby("Ship Mode", as_index=False)
        .agg({"Sales": "sum"})
    )
    fig = px.bar(
        ship,
        x="Ship Mode",
        y="Sales",
        color="Sales",
        text_auto=".2s",
        color_continuous_scale="Blues"
    )
    fig.update_layout(
        title=None,
        coloraxis_showscale=False
    )

    return chart_layout(
        fig,
        x_title="Ship Mode",
        y_title="Sales ($)"
    )

# Sales by Division
def sales_by_division(df):
    division = (
        df.groupby("Division", as_index=False)
        .agg({"Sales": "sum"})
    )
    fig = px.pie(
        division,
        names="Division",
        values="Sales",
        hole=.55,
        color_discrete_sequence=[
            "#2563EB",
            "#10B981",
            "#F59E0B",
            "#8B5CF6",
            "#EF4444",
            "#06B6D4"
        ]
    )
    fig.update_layout(
        title=None,
        coloraxis_showscale=False
    )

    return chart_layout(
        fig,
        x_title="Division",
        y_title="Sales ($)"
    )

# Sales Distribution
def sales_distribution(df):
    fig = px.histogram(
        df,
        x="Sales",
        nbins=30,
        marginal="box",
        color_discrete_sequence=["#06B6D4"]
    )
    fig.update_layout(
        title=None,
        coloraxis_showscale=False
    )
    return chart_layout(
        fig,
        x_title="Sales ($)",
        y_title="Number of Orders"
    )

# -------------Product Analysis Tab Charts-------------

# Profit By Products
def profit_by_product(df):
    product = (
        df.groupby("Product Name", as_index=False)
        .agg({"Gross Profit":"sum"})
        .sort_values("Gross Profit", ascending=False)
        .head(10)
    )
    fig = px.bar(
        product,
        x="Gross Profit",
        y="Product Name",
        orientation="h",
        color="Gross Profit",
        color_continuous_scale="Aggrnyl",
        text_auto=".2s"
    )
    fig.update_layout(
        title=None,
        coloraxis_showscale=False,
        yaxis=dict(categoryorder="total ascending")
    )

    return chart_layout(
        fig,
        x_title="Gross Profit ($)",
        y_title="Product Name"
    )

# Top Products
def top_products(df):
    product = (
        df.groupby("Product Name", as_index=False)
        .agg({"Sales": "sum"})
        .sort_values("Sales", ascending=False)
        .head(10)
    )
    fig = px.bar(
        product,
        x="Sales",
        y="Product Name",
        orientation="h",
        text_auto=".2s",
        color="Sales",
        color_continuous_scale="Purples"
    )

    fig.update_layout(
        title=None,
        coloraxis_showscale=False,
        yaxis=dict(categoryorder="total ascending")
    )

    return chart_layout(
        fig,
        x_title="Sales ($)",
        y_title="Product Name"
    )

# Sales vs Profit Buble Chart
def bubble_sales_profit(df):
    fig = px.scatter(
        df,
        x="Sales",
        y="Gross Profit",
        size="Units",
        color="Division",
        hover_name="Product Name",
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    fig.update_layout(
        title=None,
        coloraxis_showscale=False
    )

    return chart_layout(
        fig,
        x_title="Sales ($)",
        y_title="Gross Profit ($)"
    )

