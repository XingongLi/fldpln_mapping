import streamlit as st
import leafmap.foliumap as leafmap


def app():

    st.title("Images")

    st.markdown(
        """
    Historical and recent imagery.
    """
    )

    m = leafmap.Map(center=(37.170873920888894, -94.62906139455085),zoom = 6, locate_control=True) # breaks at level 7
    m.add_basemap("TERRAIN")

    naip_url = 'https://services.nationalmap.gov/arcgis/services/USGSNAIPImagery/ImageServer/WMSServer?'
    m.add_wms_layer(url=naip_url, layers='0', name='NAIP Imagery', format='image/png', shown=True)
    m
    m.to_streamlit(height=700)
