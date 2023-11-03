import plotly.subplots as sp
import plotly.graph_objects as go
import numpy as np
from typing import Union
def multiple_signals_same_graph(X:Union[list,np.array],dict_Y:dict):
    """
    Plot multiple signals on a same graph
    Args:
        X (list or np.array): list representing the axis X
        dict_Y (dict): dictionnary containing list of signals

    Returns:
        None , the figure is displayed in your browser
    """

    fig = go.Figure()
    for keys in list(dict_Y):
        fig.add_trace(go.Scatter(x=X,
                             y=dict_Y[keys],
                             mode='lines',
                             name=str(keys)))
    fig.show()

def subplots_plotly(X:Union[list,np.array],dict_Y:dict):
    """
    Plotting multiple signals on different graph with the same X axis

    Args:
        X (list or np.array): list representing the axis X
        dict_Y (dict): dictionnary containing list of signals

    Returns:

    """

    # Create a subplot grid
    fig = sp.make_subplots(rows=len(dict_Y), cols=1, shared_xaxes=True, vertical_spacing=0.05)

    n = 1
    for keys in list(dict_Y):
        fig.add_trace(go.Scatter(x=X, y=dict_Y[keys], mode='lines', name=keys, showlegend=False), row=n , col=1)
        n+=1

    # Update the layout
    fig.update_layout(
        title="Signals",
        xaxis=dict(title="Time"),
        height=900,
    )

    # Show the interactive plot
    fig.show()

