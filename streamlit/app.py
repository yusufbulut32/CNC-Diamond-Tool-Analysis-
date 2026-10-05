import streamlit as st
import pandas as pd
from pathlib import Path
import streamlit.components.v1 as components

st.set_page_config(
    page_title="CNC Takım Aşınma Analizi",
    page_icon="⚙️",
    layout="wide"
)

file_path = Path(__file__).parent / "analysis_data.csv"

if not file_path.exists():
    st.error("analysis_data.csv bulunamadı.")
    st.stop()

analysis_df = pd.read_csv(file_path)

analysis_df["wear_mm"] = pd.to_numeric(
    analysis_df["wear_mm"],
    errors="coerce"
)

analysis_df["parts"] = pd.to_numeric(
    analysis_df["parts"],
    errors="coerce"
)

analysis_df["cutting_time"] = pd.to_numeric(
    analysis_df["cutting_time"],
    errors="coerce"
)

analysis_df["rpm"] = pd.to_numeric(
    analysis_df["rpm"],
    errors="coerce"
)


if "wear_status" not in analysis_df.columns:

    bins = [0, 0.10, 0.20, float("inf")]

    labels = [
        "Normal",
        "Monitor",
        "Replacement Recommend"
    ]

    analysis_df["wear_status"] = pd.cut(
        analysis_df["wear_mm"],
        bins=bins,
        labels=labels,
        right=False
    )


if "recommended_action" not in analysis_df.columns:

    action_map = {
        "Normal": "Continue Production",
        "Monitor": "Monitor Tool",
        "Replacement Recommend": "Replace Tool"
    }

    analysis_df["recommended_action"] = (
        analysis_df["wear_status"].map(action_map)
    )



st.title("CNC Takım Aşınma Analizi")

st.write(
    "CNC takımlarındaki aşınmanın izlenmesi ve "
    "kesici uç değişim kararlarının desteklenmesi için "
    "geliştirilen karar destek prototipi."
)

components.html(
    """
    <div style="
        width: 100%;
        height: 250px;
        display: flex;
        justify-content: center;
        align-items: center;
        background: transparent;
        overflow: hidden;
    ">

    <svg width="520" height="240" viewBox="0 0 520 240"
         xmlns="http://www.w3.org/2000/svg">

        <defs>

            <!-- Ana metal yüzey -->
            <linearGradient id="mainMetal"
                x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#f4f4f4"/>
                <stop offset="22%" stop-color="#bcbcbc"/>
                <stop offset="48%" stop-color="#eeeeee"/>
                <stop offset="72%" stop-color="#999999"/>
                <stop offset="100%" stop-color="#d6d6d6"/>
            </linearGradient>

            <!-- Üst parlaklık -->
            <linearGradient id="topMetal"
                x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#ffffff"/>
                <stop offset="50%" stop-color="#cfcfcf"/>
                <stop offset="100%" stop-color="#8d8d8d"/>
            </linearGradient>

            <!-- Yan yüzey -->
            <linearGradient id="sideMetal"
                x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" stop-color="#686868"/>
                <stop offset="50%" stop-color="#a3a3a3"/>
                <stop offset="100%" stop-color="#555555"/>
            </linearGradient>

            <!-- Delik -->
            <radialGradient id="hole">
                <stop offset="0%" stop-color="#181818"/>
                <stop offset="55%" stop-color="#363636"/>
                <stop offset="100%" stop-color="#8b8b8b"/>
            </radialGradient>

            <!-- Gölge -->
            <filter id="shadow" x="-30%" y="-30%" width="160%" height="180%">
                <feDropShadow
                    dx="0"
                    dy="12"
                    stdDeviation="10"
                    flood-opacity="0.30"/>
            </filter>

        </defs>


        <!-- ZEMİN GÖLGESİ -->
        <ellipse
            cx="260"
            cy="205"
            rx="170"
            ry="18"
            fill="#000000"
            opacity="0.18"/>


        <!-- ALT / ARKA EKSTRÜZYON
             3D kalınlık hissi -->
        <polygon
            points="105,70 345,70 440,120 345,192 105,192 55,120"
            fill="url(#sideMetal)"
            stroke="#444"
            stroke-width="3"
            transform="translate(0,14)"
            filter="url(#shadow)"
        />


        <!-- ANA GÖVDE -->
        <polygon
            points="105,55 345,55 440,105 345,177 105,177 55,105"
            fill="url(#mainMetal)"
            stroke="#3d3d3d"
            stroke-width="4"
        />


        <!-- ÜST BEVEL -->
        <polygon
            points="108,62 341,62 425,106 341,165 108,165 70,105"
            fill="url(#topMetal)"
            stroke="#777"
            stroke-width="2"
        />


        <!-- KESİCİ KENAR VURGULARI -->

        <polyline
            points="105,55 345,55 440,105"
            fill="none"
            stroke="#ffffff"
            stroke-width="5"
            opacity="0.75"/>

        <polyline
            points="440,105 345,177"
            fill="none"
            stroke="#555"
            stroke-width="5"/>

        <polyline
            points="105,177 55,105"
            fill="none"
            stroke="#555"
            stroke-width="5"/>

        <polyline
            points="55,105 105,55"
            fill="none"
            stroke="#ffffff"
            stroke-width="4"
            opacity="0.65"/>


        <!-- ORTA MONTAJ DELİĞİ -->

        <!-- Dış bevel -->
        <ellipse
            cx="250"
            cy="110"
            rx="34"
            ry="23"
            fill="#8a8a8a"
            stroke="#444"
            stroke-width="3"/>

        <!-- İç delik -->
        <ellipse
            cx="250"
            cy="110"
            rx="22"
            ry="15"
            fill="url(#hole)"
            stroke="#333"
            stroke-width="3"/>

        <!-- Delik iç parlaklığı -->
        <ellipse
            cx="245"
            cy="106"
            rx="7"
            ry="4"
            fill="#777"
            opacity="0.35"/>


        <!-- 4 KULLANILABİLİR KÖŞE -->

        <circle cx="105" cy="55" r="5" fill="#555"/>
        <circle cx="345" cy="55" r="5" fill="#555"/>
        <circle cx="440" cy="105" r="5" fill="#555"/>
        <circle cx="345" cy="177" r="5" fill="#555"/>


        <!-- KÖŞE NOKTALARI -->
        <circle cx="50"  cy="108" r="4.5" fill="#e53935" stroke="#fff" stroke-width="1.5"/>
        <circle cx="52"  cy="144" r="4.5" fill="#e53935" stroke="#fff" stroke-width="1.5"/>
        <circle cx="436" cy="108" r="4.5" fill="#e53935" stroke="#fff" stroke-width="1.5"/>
        <circle cx="436" cy="144" r="4.5" fill="#e53935" stroke="#fff" stroke-width="1.5"/>

        <!-- KÖŞE NUMARALARI -->
        <text x="30" y="106"
            font-family="Arial" font-size="18" font-weight="bold"
            fill="#333">1</text>

        <text x="32" y="168"
            font-family="Arial" font-size="18" font-weight="bold"
            fill="#333">2</text>

        <text x="451" y="106"
            font-family="Arial" font-size="18" font-weight="bold"
            fill="#333">3</text>

        <text x="451" y="168"
            font-family="Arial" font-size="18" font-weight="bold"
            fill="#333">4</text>


        <!-- İSİM -->

        <text
            x="250"
            y="226"
            text-anchor="middle"
            font-family="Arial"
            font-size="16"
            font-weight="bold"
            fill="#900">
            RHOMBOID Elmas Uç
        </text>

    </svg>

    </div>
    """,
    height=260
)


st.sidebar.header("Filtreler")

if "machine_id" in analysis_df.columns:

    machine_options = sorted(
        analysis_df["machine_id"].dropna().unique()
    )

    selected_machines = st.sidebar.multiselect(
        "Makine",
        machine_options,
        default=machine_options
    )

else:
    selected_machines = None

if "tool_id" in analysis_df.columns:

    tool_options = sorted(
        analysis_df["tool_id"].dropna().unique()
    )

    selected_tools = st.sidebar.multiselect(
        "Takım",
        tool_options,
        default=tool_options
    )

else:
    selected_tools = None


if "material" in analysis_df.columns:

    material_options = sorted(
        analysis_df["material"].dropna().unique()
    )

    selected_materials = st.sidebar.multiselect(
        "Malzeme",
        material_options,
        default=material_options
    )

else:
    selected_materials = None


status_options = [
    "Normal",
    "Monitor",
    "Replacement Recommend"
]

available_statuses = [
    status for status in status_options
    if status in analysis_df["wear_status"].astype(str).unique()
]

selected_statuses = st.sidebar.multiselect(
    "Aşınma Durumu",
    available_statuses,
    default=available_statuses
)


if "position_number" in analysis_df.columns:

    position_options = sorted(
        analysis_df["position_number"].dropna().unique()
    )

    selected_positions = st.sidebar.multiselect(
        "Pozisyon",
        position_options,
        default=position_options
    )

else:
    selected_positions = None



filtered_df = analysis_df.copy()

if selected_machines is not None:
    filtered_df = filtered_df[
        filtered_df["machine_id"].isin(selected_machines)
    ]

if selected_tools is not None:
    filtered_df = filtered_df[
        filtered_df["tool_id"].isin(selected_tools)
    ]

if selected_materials is not None:
    filtered_df = filtered_df[
        filtered_df["material"].isin(selected_materials)
    ]

filtered_df = filtered_df[
    filtered_df["wear_status"].astype(str).isin(selected_statuses)
]

if selected_positions is not None:
    filtered_df = filtered_df[
        filtered_df["position_number"].isin(selected_positions)
    ]



if filtered_df.empty:

    st.warning(
        "Seçilen filtrelere uygun veri bulunamadı."
    )

    st.stop()



st.header("Temel Göstergeler")

total_measurements = filtered_df["measurement_id"].nunique()

average_wear = filtered_df["wear_mm"].mean()

max_wear = filtered_df["wear_mm"].max()

replacement_count = (
    filtered_df["wear_status"]
    .astype(str)
    .eq("Replacement Recommend")
    .sum()
)

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "Toplam Ölçüm",
        total_measurements
    )

with col2:

    st.metric(
        "Ortalama Aşınma",
        f"{average_wear:.2f} mm"
    )

with col3:

    st.metric(
        "Maksimum Aşınma",
        f"{max_wear:.2f} mm"
    )

with col4:

    st.metric(
        "Değişim Önerilen",
        replacement_count
    )



st.header("Aşınma Durumu Dağılımı")

status_counts = (
    filtered_df["wear_status"]
    .astype(str)
    .value_counts()
    .reindex(status_options, fill_value=0)
)

st.bar_chart(status_counts)



st.header("Parça Sayısı ve Takım Aşınması")

parts_wear_df = filtered_df[
    ["parts", "wear_mm"]
].dropna()

st.scatter_chart(
    parts_wear_df,
    x="parts",
    y="wear_mm"
)



st.header("Takım Bazında Ortalama Aşınma")

tool_wear = (
    filtered_df
    .groupby("tool_id")["wear_mm"]
    .mean()
    .sort_values(ascending=False)
)

st.bar_chart(tool_wear)



if "material" in filtered_df.columns:

    st.header("Malzeme Bazında Ortalama Aşınma")

    material_wear = (
        filtered_df
        .groupby("material")["wear_mm"]
        .mean()
        .sort_values(ascending=False)
    )

    st.bar_chart(material_wear)



st.header("Karar Destek")

st.write(
    "Aşağıdaki karar mantığı sentetik veri senaryosu "
    "için tanımlanan aşınma eşiklerine dayanmaktadır."
)

decision_col1, decision_col2 = st.columns(2)

with decision_col1:

    selected_tool = st.selectbox(
        "Takım seçin",
        sorted(filtered_df["tool_id"].unique())
    )

with decision_col2:

    tool_positions = sorted(
        filtered_df[
            filtered_df["tool_id"] == selected_tool
        ]["position_number"]
        .dropna()
        .unique()
    )

    selected_position = st.selectbox(
        "Pozisyon seçin",
        tool_positions
    )



selected_records = filtered_df[
    (filtered_df["tool_id"] == selected_tool)
    & (
        filtered_df["position_number"]
        == selected_position
    )
]


if not selected_records.empty:

    selected_record = selected_records.sort_values(
        "measurement_id"
    ).iloc[-1]

    wear = selected_record["wear_mm"]
    status = selected_record["wear_status"]
    action = selected_record["recommended_action"]

    st.subheader("Karar Sonucu")

    result_col1, result_col2, result_col3 = st.columns(3)

    with result_col1:

        st.metric(
            "Takım",
            selected_tool
        )

    with result_col2:

        st.metric(
            "Pozisyon",
            int(selected_position)
        )

    with result_col3:

        st.metric(
            "Aşınma",
            f"{wear:.2f} mm"
        )

    st.write(
        f"**Aşınma Durumu:** {status}"
    )

    st.write(
        f"**Önerilen Aksiyon:** {action}"
    )

    if status == "Normal":

        st.success(
            "Takım aşınma seviyesi normal aralıktadır. "
            "Üretime devam edilebilir."
        )

    elif status == "Monitor":

        st.warning(
            "Takım izleme aralığındadır. "
            "Aşınmanın takip edilmesi önerilir."
        )

    else:

        st.error(
            "Takım aşınması değişim eşiğine ulaşmıştır. "
            "Takım değişimi önerilir."
        )



st.header("Değişim Önerilen Takımlar")

replacement_df = filtered_df[
    filtered_df["wear_status"].astype(str)
    == "Replacement Recommend"
].copy()

replacement_columns = [
    "measurement_id",
    "tool_id",
    "position_number",
    "machine_id",
    "parts",
    "cutting_time",
    "rpm",
    "wear_mm",
    "visual_condition",
    "wear_status",
    "recommended_action"
]


replacement_columns = [
    column
    for column in replacement_columns
    if column in replacement_df.columns
]

if replacement_df.empty:

    st.info(
        "Seçilen filtrelerde değişim önerilen takım bulunmuyor."
    )

else:

    st.dataframe(
        replacement_df[replacement_columns],
        use_container_width=True
    )



st.header("Veri Önizleme")

st.dataframe(
    filtered_df.head(50),
    use_container_width=True
)