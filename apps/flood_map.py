import streamlit as st
import leafmap.foliumap as leafmap


def app():
    st.title("Current and Forecast Flood Map")

    st.markdown(
        """
    This is a test of building flood mapping web application using leafmap and streamlit.
    """
    )

    # #
    # # Streamlit doesn't support localtile server!!!
    # #
    # url = 'https://fldpln.blob.core.windows.net/maps/spring_NumOfFsps.tif' # localtileserver won't render a regular GeoTIFF
    # # print(leafmap.cog_validate(url))

    # # create a leafmap Map and center it to east Kansas
    # m = leafmap.Map(center=(37.170873920888894, -94.62906139455085),zoom = 10, locate_control=True) # breaks at level 7
    # m.add_basemap("HYBRID")

    # # add flood maps
    # # m.add_local_tile(url, palette='Blues', layer_name=f'Spring Flood Map')
    # # or
    # # m.add_geotiff(url, palette='Blues', layer_name='Spring Flood Map')

    #
    # show single COG using titiler
    #
    # url = 'https://fldpln.blob.core.windows.net/maps/spring_Flood.tif' # localtileserver won't render a regular GeoTIFF
    # print(leafmap.cog_validate(url))

    # create a leafmap Map and center it to east Kansas
    leafmap.Map()
    m = leafmap.Map(center=(37.5, -94.7),zoom=7, locate_control=True) # breaks at level 7
    m.add_basemap("TERRAIN")

    # add flood maps
    m.add_cog_layer('https://fldpln.blob.core.windows.net/maps/spring_MinDtf.tif', name="Minimum Depth-to-Flood", palette="reds",shown=False)
    m.add_cog_layer('https://fldpln.blob.core.windows.net/maps/spring_Major.tif', name="Major flood map", palette="reds")
    m.add_cog_layer('https://fldpln.blob.core.windows.net/maps/spring_Action.tif', name="Action flood map", palette="reds")
    m.add_cog_layer('https://fldpln.blob.core.windows.net/maps/spring_fcst000.tif', name="Current flood map", palette="reds")
    m
    m.to_streamlit(height=700)

    # #
    # # Show mosaic COG
    # #
    # mosaicJsonUrl = 'https://fldpln.blob.core.windows.net/maps/spring.json.gz'

    # # create a leafmap Map and center it to east Kansas
    # m = leafmap.Map(center=(37.170873920888894, -94.62906139455085),zoom = 10, locate_control=True) # breaks at level 7
    # m.add_basemap("HYBRID")

    # # NOTE: have to set the rescale parameter!
    # m.add_mosaic_layer(mosaicJsonUrl, colormap_name='blues', rescale='0,20')
    # m

    # m.to_streamlit(height=700)
