import PySimpleGUI as sg;
from constants.uiComponents import FETCH_SONG, WINDOW_TITLE, YOUTUBE_URL;
from constants.uiOptions import BG_COLOR;
from service.downloadService import runYoutubeDl;

sg.theme(BG_COLOR);
layout = [
    [sg.Text(YOUTUBE_URL), sg.Input('', enable_events=True, key='urlInput', justification='left')], 
    [sg.Button(FETCH_SONG)]
];

window = sg.Window(WINDOW_TITLE, layout);
while True:
    event, values = window.read();
    if event == sg.WIN_CLOSED:
        break;
    elif event == FETCH_SONG:
        currentUrl = values['urlInput'];
        if currentUrl == '':
            continue;
        runYoutubeDl(currentUrl);

window.close();