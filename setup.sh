mkdir -p ~/.streamlit/
echo "[general]
email = \"arya.shah82@nmims.edu.in\"
" > ~/.streamlit/credentials.toml
echo "[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml