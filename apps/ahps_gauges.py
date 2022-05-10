import streamlit as st
import leafmap.foliumap as leafmap


def app():

    st.title("Gauge Observation and Forecast")

    m = leafmap.Map(center=(38.587981, -96.815613),zoom = 8, locate_control=True) # breaks at level 7
    m.add_basemap("TERRAIN")

    # add Advanced Hydrologic Prediction Service (AHPS) River Gauge Current and Forecast Flood Stages WMS/WFS services
    # WFS URL
    # ahpsUrl = 'http://idpgis.ncep.noaa.gov/arcgis/services/NWS_Observations/ahps_riv_gauges/MapServer/WFSServer?'
    # WMS URL
    ahpsUrl = 'http://idpgis.ncep.noaa.gov/arcgis/services/NWS_Observations/ahps_riv_gauges/MapServer/WmsServer?'

    # add forecast layers, layers added later are on the top!
    m.add_wms_layer(url=ahpsUrl, layers='14', name='Maximum Forecast 14-Day', format='image/png', transparent=True, shown=False)
    m.add_wms_layer(url=ahpsUrl, layers='7', name='Maximum Forecast 7-Day', format='image/png', transparent=True, shown=False)
    m.add_wms_layer(url=ahpsUrl, layers='0', name='Current Observation', format='image/png', transparent=True, shown=True)

    # show leafmap
    m
    m.to_streamlit(height=800)
