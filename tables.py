import pandas as pd # type: ignore
import numpy as np
import plotly.graph_objects as go # type: ignore
from PIL import Image, ImageChops # type: ignore
import os

# ---------------------------------------------------------------------------
#  таблица - strict_table.png
# color - цвет таблицы (чередуется с белым)
# m - пример данных
# ---------------------------------------------------------------------------
color = "#cbd6db"


def _make_table(df: pd.DataFrame) -> go.Figure:
    n = len(df) # for total height of figure to save
    row_colors = ['#ffffff', color]
    fill_colors_per_col = [row_colors * int(n//2 + n%2)]
    height = 30 # height of cells
    fig = go.Figure(data=[go.Table(
        header=dict(
                    #values=['', '', '', ''], # will show without any header, len(values) = len(df.columns)
                    fill_color=color,
                    height=0,
                    line_color='black',
                    line_width=1                    
                    ),
        cells=dict(
            values=df.values.T, 
            fill_color=fill_colors_per_col,
            align='center',
            font=dict(size=16),
            height=height,
            line_color='black',
            line_width=1  
        )
    )])
  
    fig.update_layout(
        title=dict(text="Table title", x=0.5, y=0.98, xanchor='center'),
        width=600, 
        height=n*height + 70,
        margin=dict(l=20, r=20, t=30, b=20),
    )
    return fig

def show_table(df: pd.DataFrame):
    fig = _make_table(df)
    fig.show()

def save_table(df: pd.DataFrame, path: str) -> None:
    fig = _make_table(df)
    try:
        fig.write_image(path, scale=2)
    except FileNotFoundError:
        print(f"Путя'{path} не существует")
        return
    except PermissionError:
        print("Ошибка доступа - возможно, файл уже открыт в другой программе")
        return

m = np.array([[1, 2, 3, 5],
                  [4, 5, 6, 5],
                  [7, 8, 9, 3],
                  [7, 8, 9, 3],
                  [1, 2, 3, 5],
                  [4, 5, 6, 5],
                  [7, 8, 9, 3],
                  [7, 8, 9, 3],
                  [1, 2, 3, 5],
                  [4, 5, 6, 5] ,
                  [4, 5, 6, 5]])
df1 = pd.DataFrame(m)

#show_table(df1)
save_table(df1, "C:\\library\\strict_table.png")