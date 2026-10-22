import pandas as pd # type: ignore
import numpy as np
import plotly.graph_objects as go # type: ignore
from PIL import Image, ImageChops # type: ignore

# ---------------------------------------------------------------------------
#  таблица - strict_table.png
# color - цвет таблицы (чередуется с белым)
# m - пример данных
# ---------------------------------------------------------------------------
color = "#cbd6db"
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
                  [4, 5, 6, 5]        
                  ])
def save_table():
    df = pd.DataFrame(m)
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
    fig.show()
    filename = "strict_table.png"
    #fig.write_image(filename, scale=2)

save_table()