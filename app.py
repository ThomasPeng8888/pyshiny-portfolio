import pandas as pd
import plotly.express as px
import palmerpenguins
from shiny.express import input, render, ui

# -----------------
# 1. 數據與設定
# -----------------
# 載入企鵝數據並清理缺失值
data = palmerpenguins.load_penguins()
data = data.dropna()
COLUMNS = ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]

# 設定頁面標題
ui.page_opts(title="極簡 Plotly 企鵝儀表板", fillable=True)

# -----------------
# 2. 應用程式介面 (UI)
# -----------------

# 側邊欄：只放一個輸入元件
with ui.sidebar(title="選擇變數"):
    ui.input_select(
        "selected_var",
        "要分析的變數:",
        choices=COLUMNS,
        selected="body_mass_g",
    )
    ui.hr()
    ui.div("此圖表展示了所選變數的分佈情況。", style="padding: 10px; opacity: 0.7;")

# 主畫面：顯示 Plotly 圖表
ui.h3("互動式數據分佈圖")

# 使用 @render.express 裝飾器來渲染 Plotly 圖表
@render.express
def histogram():
    # 讀取使用者輸入的值 (響應式)
    var = input.selected_var()
    
    # 使用 Plotly Express 創建直方圖
    fig = px.histogram(
        data, 
        x=var, 
        color="species",
        title=f"直方圖: {var} (按物種劃分)",
        opacity=0.8
    )
    
    # 將 Plotly 圖表物件 'fig' 傳遞給 Shiny 顯示
    fig