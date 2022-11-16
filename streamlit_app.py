# cspell:includeRegExp comments

import streamlit as st
from streamlit_option_menu import option_menu
from apps import ahps_gauges, flood_map, images, upload  # import your app modules here

st.set_page_config(page_title="Kansas Flood Mapping", layout="wide")

# A dictionary of apps in the format of {"App title": "App icon"}
# More icons can be found here: https://icons.getbootstrap.com

apps = {
    "flood_map": {"title": "Flood Map", "icon": "water"},
    "ahps_gauges": {"title": "AHPS Gauges", "icon": "moisture"},
    "images": {"title": "Images", "icon": "images"},
    "upload": {"title": "Upload", "icon": "cloud-upload"},
}

titles = [app["title"] for app in apps.values()]
icons = [app["icon"] for app in apps.values()]

params = st.experimental_get_query_params()

if "page" in params:
    default_index = int(titles.index(params["page"][0].lower()))
else:
    default_index = 0

with st.sidebar:
    selected = option_menu(
        "Main Menu",
        options=titles,
        icons=icons,
        menu_icon="cast",
        default_index=default_index,
    )

    st.sidebar.title("About")
    st.sidebar.info(
        """
        Kansas flood mapping uses observed and forecast gauge stage from NOAA Advanced Hydrologic Prediction Service to map potential inundation for 25 floodplains
        in eastern Kansas. The inundattion mapping method is developed by Jude Kastens at Kansas Biological Survey nnd this application is developed by a group of students and
        faculty members, including David Weekley, Jim Coll, Ken Ekpetere, James Halgren and Xingong Li, at the Department of Geography & Atmospheric Science, University of Kansas and 
        beyond. The project is funded by Kansas Water Office.
    """
    )

for app in apps:
    if apps[app]["title"] == selected:
        eval(f"{app}.app()")
        break
