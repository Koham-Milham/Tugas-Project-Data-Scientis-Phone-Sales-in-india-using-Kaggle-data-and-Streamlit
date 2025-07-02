import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("📱 Dashboard Analisis Penjualan Smartphone")

# === HEADER ===
st.markdown("""
# 📱 Dashboard Penjualan Smartphone

### 👤 Mohammad Ilham  
🔗 [LinkedIn](https://www.linkedin.com/in/yourusername) | 🌐 [GitHub](https://github.com/yourusername) | 🧾 [Dokumentasi Proyek](https://yourlink.com)

> Dashboard interaktif ini dibuat sebagai bagian dari tugas akhir program **Faculty of Data - DBIMBING**.  
Terima kasih kepada mentor dan teman-teman yang telah memberikan bimbingan serta dukungan. 🙌  
""")


# Load data
df = pd.read_csv("Sales Phone.csv")

# Preprocessing singkat
df['Rating'] = df['Rating'].apply(lambda x: x / 10 if x > 5 else x)
df['Discount'].fillna(0, inplace=True)
df['discount percentage'].fillna(0, inplace=True)
df.dropna(subset=['Selling Price', 'Original Price'], inplace=True)

# === SIDEBAR FILTER ===
st.sidebar.header("🎛️ Filter Data")
brands = st.sidebar.multiselect("Pilih Brand:", sorted(df['Brands'].unique()), default=sorted(df['Brands'].unique()))
rating_range = st.sidebar.slider("Range Rating", 0.0, 5.0, (3.0, 5.0), step=0.1)
price_range = st.sidebar.slider("Range Harga Jual", 0, int(df['Selling Price'].max()), (0, int(df['Selling Price'].max())))

# Filter data
df_filtered = df[
    (df['Brands'].isin(brands)) &
    (df['Rating'] >= rating_range[0]) & (df['Rating'] <= rating_range[1]) &
    (df['Selling Price'] >= price_range[0]) & (df['Selling Price'] <= price_range[1])
]
# === METRICS ===
st.markdown("## 📊 Ringkasan Data")
col1, col2, col3 = st.columns(3)
col1.metric("Jumlah Produk", len(df_filtered))
col2.metric("Rata-rata Harga Jual", f"Rp {int(df_filtered['Selling Price'].mean()):,}")
col3.metric("Rata-rata Rating", f"{df_filtered['Rating'].mean():.2f}")

# === VISUALISASI ===
col1, col2 = st.columns(2)

with col1:
    st.subheader("Rata-rata Harga Jual dan Harga Asli per Brand")
    fig, ax = plt.subplots(figsize=(8, 4))
    mean_prices = df_filtered.groupby('Brands')[['Selling Price', 'Original Price']].mean()
    mean_prices.plot(kind='bar', ax=ax)
    ax.set_ylabel("Rata-rata Harga (Rp)")
    st.pyplot(fig)

with col2:
    st.subheader("Rating vs Harga Jual")
    fig, ax = plt.subplots(figsize=(8, 4))
    scatter = sns.scatterplot(data=df_filtered, x='Rating', y='Selling Price', hue='Brands', ax=ax)
    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title='Brands')
    ax.set_ylabel("Selling Price")
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

st.markdown("## 📲 Rekomendasi Produk Berdasarkan Filter")

# TOP 5 berdasarkan rating tertinggi & harga jual termurah
top_products = df_filtered.sort_values(by=['Rating', 'Selling Price'], ascending=[False, True]).head(5)

st.markdown("### 🔝 Top 5 Rekomendasi HP (Rating & Harga)")
st.dataframe(top_products[['Mobile', 'Rating', 'Selling Price', 'Original Price', 'Memory', 'Storage', 'Camera']].reset_index(drop=True))

# Alternatif tambahan: berdasarkan spesifikasi teknis
st.markdown("### ⚙️ Alternatif Terbaik Berdasarkan Spesifikasi")

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
