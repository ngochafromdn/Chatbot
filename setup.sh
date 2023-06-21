mkdir -p ~/.streamlit/

echo '''
[general]
email = "nguyenhoangngocha.vn@gmail.com"
''' > ~/.streamlit/credentials.toml

echo '''
[server]
headless = true
enableCORS=false


[theme]
base = "light"
primaryColor = "#89CFF0"
backgroundColor = "#E0F7FE"
secondaryBackgroundColor = "#FFFCE4"
textColor = "#000000"
font = "sans serif"
''' > ~/.streamlit/config.toml