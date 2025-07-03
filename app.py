import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

# === HEADER ===
st.markdown("""
# 📱 Dashboard Penjualan Smartphone

### 👤 Mohammad Ilham  
🔗 [LinkedIn](https://www.linkedin.com/in/immohilham/) | 🌐 [GitHub](https://github.com/ilhamsaang/ilhamsaang-Tugas-Project-Data-Scientis-Phone-Sales-using-Kaggle-data-and-Streamlit) | 🧾 [Dokumentasi Proyek](https://yourlink.com) | [resource] (https://www.kaggle.com/datasets/yaminh/smartphone-sale-dataset/data)
> Dashboard interaktif ini dibuat sebagai bagian dari tugas akhir program **Faculty of Data : Data Scientis - Dibimbing**.  
Terima kasih kepada mentor dan teman-teman yang telah memberikan bimbingan serta dukungan. 🙌  
""")

# === KONFIGURASI KONVERSI HARGA ===
conversion_rate = 190  # 1 INR = 190 IDR
show_rupiah = st.sidebar.toggle("💱 Tampilkan Harga dalam Rupiah (IDR)", value=False)

# Load data
df = pd.read_csv("Sales Phone.csv")

# Preprocessing singkat
df['Rating'] = df['Rating'].apply(lambda x: x / 10 if x > 5 else x)
df['Discount'].fillna(0, inplace=True)
df['discount percentage'].fillna(0, inplace=True)
df.dropna(subset=['Selling Price', 'Original Price'], inplace=True)

# Tambahkan kolom harga IDR
df['Selling Price (IDR)'] = df['Selling Price'] * conversion_rate
df['Original Price (IDR)'] = df['Original Price'] * conversion_rate

# Format harga ke mata uang
def format_currency(val, rupiah=False):
    if rupiah:
        return f"Rp {val:,.0f}".replace(",", ".")
    else:
        return f"₹ {val:,.0f}"

# === SIDEBAR FILTER ===
st.sidebar.header("🎛️ Filter Data")
brands = st.sidebar.multiselect("Pilih Brand:", sorted(df['Brands'].unique()), default=sorted(df['Brands'].unique()))
rating_range = st.sidebar.slider("Range Rating", 0.0, 5.0, (3.0, 5.0), step=0.1)
price_col = 'Selling Price (IDR)' if show_rupiah else 'Selling Price'
price_range = st.sidebar.slider(
    "Range Harga Jual",
    int(df[price_col].min()),
    int(df[price_col].max()),
    (int(df[price_col].min()), int(df[price_col].max()))
)

# Filter data
df_filtered = df[
    (df['Brands'].isin(brands)) &
    (df['Rating'] >= rating_range[0]) & (df['Rating'] <= rating_range[1]) &
    (df[price_col] >= price_range[0]) & (df[price_col] <= price_range[1])
]

# === METRICS ===
st.markdown("## 📊 Ringkasan Data")
col1, col2, col3 = st.columns(3)
col1.metric("Jumlah Produk", len(df_filtered))
avg_price = df_filtered[price_col].mean()
col2.metric("Rata-rata Harga Jual", format_currency(avg_price, show_rupiah))
col3.metric("Rata-rata Rating", f"{df_filtered['Rating'].mean():.2f}")

# === VISUALISASI ===
col1, col2 = st.columns(2)

with col1:
    st.markdown("<h4>Rata-rata Harga Jual dan Harga Asli per Brand</h4>", unsafe_allow_html=True)
    fig, ax = plt.subplots(figsize=(8, 4))
    group_col1 = 'Selling Price (IDR)' if show_rupiah else 'Selling Price'
    group_col2 = 'Original Price (IDR)' if show_rupiah else 'Original Price'
    mean_prices = df_filtered.groupby('Brands')[[group_col1, group_col2]].mean()
    mean_prices.plot(kind='bar', ax=ax)
    ax.set_ylabel("Harga (Rp)" if show_rupiah else "Harga (₹)")
    st.pyplot(fig)

with col2:
    st.subheader("Rating vs Harga Jual")
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.scatterplot(data=df_filtered, x='Rating', y=price_col, hue='Brands', ax=ax)
    ax.set_ylabel("Harga Jual (Rp)" if show_rupiah else "Selling Price (₹)")
    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title='Brands')
    st.pyplot(fig)

st.subheader("Korelasi Fitur Numerik")
fig, ax = plt.subplots(figsize=(10, 5))
sns.heatmap(df_filtered.select_dtypes('number').corr(), annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig)

st.subheader("Distribusi Persentase Diskon per Brand")
fig, ax = plt.subplots(figsize=(12, 4))
sns.boxplot(data=df_filtered, x='Brands', y='discount percentage', ax=ax)
ax.set_ylabel("Diskon (%)")
st.pyplot(fig)

# === REKOMENDASI PRODUK ===
st.markdown("<h4 style='margin-bottom: 10px;'>📲 Rekomendasi Produk Berdasarkan Filter", unsafe_allow_html=True)
# TOP 5 berdasarkan rating tertinggi & harga jual termurah
top_products = df_filtered.sort_values(by=['Rating', price_col], ascending=[False, True]).head(5)

st.markdown("<h5 style='margin-bottom: 10px;'>🔝 Top 5 Rekomendasi HP (Rating & Harga)", unsafe_allow_html=True)
top_display = top_products.copy()
top_display['Harga'] = top_display[price_col].apply(lambda x: format_currency(x, show_rupiah))
st.dataframe(top_display[['Mobile', 'Rating', 'Harga', 'Original Price', 'Memory', 'Storage', 'Camera']].reset_index(drop=True))

# Alternatif tambahan: berdasarkan spesifikasi teknis
st.markdown("<h5 style='margin-bottom: 10px;'>⚙️ Alternatif Terbaik Berdasarkan Spesifikasi", unsafe_allow_html=True)

alt_col1, alt_col2, alt_col3 = st.columns(3)

with alt_col1:
    best_storage = df_filtered.sort_values(by='Storage', ascending=False).head(1)
    st.markdown("**📦 Storage Tertinggi**")
    st.write(f"{best_storage.iloc[0]['Mobile']} - {best_storage.iloc[0]['Storage']}")

with alt_col2:
    best_discount = df_filtered.sort_values(by='discount percentage', ascending=False).head(1)
    st.markdown("**💸 Diskon Tertinggi**")
    st.write(f"{best_discount.iloc[0]['Mobile']} - {best_discount.iloc[0]['discount percentage']}%")

# === FOOTER ===
st.markdown("---")
st.markdown("© 2025 Mohammad Ilham | Dibuat dengan ❤️ menggunakan Streamlit")