from shiny import App, render, ui
import pandas as pd
import matplotlib.pyplot as plt

app_ui = ui.page_fluid(
    ui.input_slider("n", "樣本數量", 10, 100, 50),
    ui.output_plot("hist")
)

def server(input, output, session):
    @output
    @render.plot
    def hist():
        # 簡單的數據生成和繪圖
        df = pd.DataFrame({"value": [i for i in range(input.n())]})
        fig, ax = plt.subplots()
        ax.hist(df['value'], bins=5)
        return fig

app = App(app_ui, server)