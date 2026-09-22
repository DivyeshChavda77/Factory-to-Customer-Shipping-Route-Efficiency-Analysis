# 📦 Factory-to-Customer Shipping Route Efficiency Analysis

A Data Science and Business Analytics project that analyzes shipping performance, sales, profitability, and route efficiency for the **Nassau Candy Distributor** dataset.

The project includes **EDA, data ingestion, data transformation, route analysis, and an interactive Streamlit dashboard**.

---

## 🎯 Project Objectives

- Analyze shipping efficiency
- Identify fastest and slowest routes
- Compare shipping modes
- Identify regional shipping bottlenecks
- Analyze sales and profitability
- Create business KPIs
- Build an interactive Streamlit dashboard

---

## 📊 Dataset

The dataset contains **10,194 records** and **18 original features**, including:

`Order Date`, `Ship Date`, `Ship Mode`, `City`, `State/Province`, `Region`, `Product Name`, `Sales`, `Units`, `Gross Profit`, and `Cost`.

### Engineered Features

**Shipping Days**

```text
Shipping Days = Ship Date - Order Date
```

**Profit Margin**

```text
Profit Margin (%) = (Gross Profit / Sales) × 100
```

---

## 🏗️ Project Structure

```text
Factory-to-Customer-Shipping-Route-Efficiency/
│
├── data/
├── artifacts/
├── notebook/
│   └── EDA.ipynb
│
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── route_analysis.py
│   ├── exception.py
│   └── logger.py
│
├── app.py
├── requirements.txt
├── setup.py
└── README.md
```

---

## ⚙️ Project Workflow

```text
Raw Data
   ↓
Data Ingestion
   ↓
Data Transformation
   ↓
Feature Engineering
   ↓
Route Analysis
   ↓
Business KPIs
   ↓
Streamlit Dashboard
```

---

## 📈 Key KPIs

| KPI | Value |
|---|---:|
| Total Sales | $141,783.63 |
| Gross Profit | $93,442.80 |
| Total Order | 8549 |
| Units Sold | 38,654 |
| Avg. Shipping Days | 1,344.24 |
| Avg. Profit Margin | 66.51% |

---

## 💡 Key Insights

- Sales and Gross Profit have a strong positive correlation of approximately **0.98**.
- The **Pacific** region has the highest average Sales and Gross Profit.
- **Second Class** has the highest average Sales among ship modes.
- The **Atlantic** region has the highest average Shipping Days.
- **New York City** achieved the highest Route Score among analyzed high-volume routes.
- Shipping duration differences across ship modes and regions are relatively small.

> **Dataset Note:** Shipping durations are unusually high compared with real-world logistics. Therefore, Shipping Days is used primarily for comparative analysis within this dataset.

---

## 📊 Streamlit Dashboard

The interactive dashboard provides:

- KPI cards
- Region, State and Ship Mode filters
- Sales and Profit analysis
- Shipping efficiency analysis
- Best and Worst Route analysis
- Top Cities and Products
- Business summary tables
- Filtered CSV download

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Streamlit

---

## 🚀 Run Locally

```bash
git clone <your-repository-url>
cd Factory-to-Customer-Shipping-Route-Efficiency

pip install -r requirements.txt

streamlit run app.py
```

---

## 👤 Author

**Divyesh Chavda**  
B.E. Artificial Intelligence & Data Science

---

⭐ If you found this project useful, consider giving the repository a star.
