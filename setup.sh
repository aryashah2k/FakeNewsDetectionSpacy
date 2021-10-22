mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"arya.shah82@nmims.edu.in\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml