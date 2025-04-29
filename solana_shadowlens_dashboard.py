
import streamlit as st
import requests
import base64
import json

st.title("Solana ShadowLens Dashboard")
st.markdown("Analyze and extract information from closed-source Solana programs.")

program_id = st.text_input("Enter Solana Program ID:")

if program_id:
    st.write(f"Analyzing Program ID: {program_id}")

    response = requests.post(
        "https://api.mainnet-beta.solana.com",
        headers={"Content-Type": "application/json"},
        data=json.dumps({
            "jsonrpc": "2.0",
            "id": 1,
            "method": "getAccountInfo",
            "params": [program_id, {"encoding": "base64"}]
        })
    )

    if response.status_code == 200:
        result = response.json().get("result")
        if result and result.get("value"):
            data = result["value"]["data"][0]
            decoded_data = base64.b64decode(data)
            st.write("Program Data (Base64 Decoded):")
            st.code(decoded_data.hex())
        else:
            st.error("No data found for the provided Program ID.")
    else:
        st.error("Failed to fetch program data.")
