import base64
import json

import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output
from functions import read_opus_data

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.VAPOR],
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
text_area = dbc.Row(dbc.Col(dcc.Textarea(id="text-area", value="")))
app.layout = dbc.Container([upload_files_button, text_area])


@app.callback(Output("text-area", "value"), Input("upload-data-multiple", "contents"))
def convert_uploaded_files(contents):
    if contents is not None:
        for content in contents:
            content_type, content_string = content.split(",")
            decoded = base64.b64decode(content_string)
            x, y = read_opus_data(decoded)
            


if __name__ == "__main__":
    app.run_server(host="0.0.0.0", debug=True)
