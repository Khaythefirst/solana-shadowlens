
# 🕵️‍♂️ Solana ShadowLens

**Solana ShadowLens** is an open-source dashboard and reverse engineering toolkit designed to analyze closed-source Solana smart contracts. This tool aims to bring transparency to the Solana ecosystem by revealing non-trivial information from opaque programs.

## 🔍 Features

- Analyze Solana on-chain programs using their Program ID
- Extract and decode base64-encoded binary bytecode
- Identify potential account structures and program instructions
- Lay the foundation for pseudo-IDL generation and risk assessment

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/solana-shadowlens.git
cd solana-shadowlens
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the dashboard
```bash
streamlit run solana_shadowlens_dashboard.py
```

### 4. Use the dashboard
- Enter a Program ID from Solana Mainnet
- View base64-decoded bytecode
- Explore upcoming features for instruction and account inference

## 🌐 Deploy to Streamlit Cloud

1. Push this repository to your GitHub account.
2. Visit [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Click "New App", select your repository, and deploy `solana_shadowlens_dashboard.py`

Your app will be publicly available in minutes.

## 🧭 Roadmap

- 🔄 Instruction decoder based on discriminator patterns
- 🧠 Account role inference using transaction patterns
- 📤 Exportable pseudo-IDL files
- 🔐 Upgradeability and permission audit tools
- 📊 Graphical data visualization for program interactions

## 🙌 Contributing

We welcome contributions! Please open issues or submit PRs to improve the tool.

## 📄 License

This project is licensed under the MIT License.

---

Made with ❤️ to help bring **security by design** to the Solana ecosystem.
