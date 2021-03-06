"""
Author: Anjana Vasudevan
Simple module for plotting curves
"""

# dependencies:
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.io as pio

# Template configuration:
pio.templates.default = 'plotly_white'


def plot_hist(dataframe, x_col, col_to_indicate, plot_title=None):
    """
    Plot a histogram to indicate things
    """
    figure = px.histogram(dataframe, x=x_col, color=col_to_indicate)
    figure.update_layout(title=plot_title)

    # Plotting configurations
    config = {
        'toImageButtonOptions': {
            'format': 'png',  # one of png, svg, jpeg, webp
            'height': 480,
            'width': 640,
            'scale': 3  # Multiply title/legend/axis/canvas sizes by this factor
        }
    }
    figure.show(config=config)
