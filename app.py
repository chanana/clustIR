import base64

import dash
import dash_bootstrap_components as dbc
import pandas as pd
from dash import dcc
from dash.dependencies import Input, Output, State

from functions import (calculate_L2_norm_all_v_all, make_and_cleanup_dataframe,
                       read_opus_data)
from html_functions import (make_dash_table_from_dataframe,
                            make_heatmap_from_distance_matrix)
import dash_daq as daq

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.ZEPHYR],
    prevent_initial_callbacks=True,
)

upload_files_button = dbc.Row(
    dbc.Col(
        dcc.Upload(
            id="upload-data-multiple",
            children=dbc.Button("Upload IR files", color="primary"),
            multiple=True,
        ),
        width=12,
    ),
    align="center",
    class_name="mt-3 mb-3",
)
# text_area = dbc.Row(dbc.Col(dcc.Textarea(id="text-area", value="")))
figure = dbc.Row(dbc.Col(children=[dcc.Graph(id="L2-heatmap", figure={})]))
euc_cosine_selector=
# spectrum_table = dbc.Row(dbc.Col(id='spectrum-table', children=[]))
app.layout = dbc.Container([upload_files_button, figure])


@app.callback(
    Output("L2-heatmap", "figure"),
    # Output('spectrum-table', 'children'),
    Input("upload-data-multiple", "contents"),
    State("upload-data-multiple", "filename"),
)
def convert_uploaded_files(list_of_contents, list_of_filenames):
    if list_of_contents is not None:
        df = pd.DataFrame(data=None)
        x_values = None
        for content, filename in zip(list_of_contents, list_of_filenames):
            content_type, content_string = content.split(",")
            decoded = base64.b64decode(content_string)
            x, y = read_opus_data(decoded)

            df[filename] = y

            # we just need one set of x_values that will be common across all files
            if x_values is None:
                x_values = x

        clean_df = make_and_cleanup_dataframe(dataframe=df, columns=x_values)
        distance_matrix = calculate_L2_norm_all_v_all(clean_df)
        # table = make_dash_table_from_dataframe(clean_df)
        fig = make_heatmap_from_distance_matrix(
            distance_matrix, clean_df.index, clean_df.index
        )
        return fig


if __name__ == "__main__":
    app.run_server(host="0.0.0.0", debug=True)
