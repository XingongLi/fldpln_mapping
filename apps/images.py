import streamlit as st
import leafmap.foliumap as leafmap


def app():

    st.title("Images")

    st.markdown(
        """
    Historical and recent imagery.
    """
    )

    m = leafmap.Map(center=(38.587981, -96.815613),zoom = 8, locate_control=True) # breaks at level 7
    m.add_basemap("TERRAIN")

    # naip_url = 'https://services.nationalmap.gov/arcgis/services/USGSNAIPImagery/ImageServer/WMSServer?' # This one seems not working
    naip_url = 'https://basemap.nationalmap.gov/arcgis/services/USGSImageryOnly/MapServer/WMSServer?'
    m.add_wms_layer(url=naip_url, layers='0', name='NAIP Imagery', format='image/png', shown=True)
    m
    m.to_streamlit(height=800)
