import streamlit as st
import leafmap.foliumap as leafmap


def app():
    st.title("Kansas Real-Time Flood Mapping")

    st.markdown(
        """
    This is a test of building the Kansas real-time flood mapping web application using leafmap and streamlit.
    """
    )

    url = 'https://fldpln.blob.core.windows.net/maps/spring_NumOfFsps.tif' # localtileserver won't render a regular GeoTIFF
    # print(leafmap.cog_validate(url))

    # create a leafmap Map and center it to east Kansas
    m = leafmap.Map(center=(37.170873920888894, -94.62906139455085),zoom = 10, locate_control=True) # breaks at level 7
    m.add_basemap("HYBRID")

    # add flood maps
    # Map.add_local_tile(gtif, palette='Blues', layer_name=f'Spring Flood Map')
    # or
    m.add_geotiff(url, palette='Blues', layer_name='Spring Flood Map')

    
    m.to_streamlit(height=700)
