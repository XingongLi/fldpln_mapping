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
    # leafmap.Map()
    m = leafmap.Map(center=(38.587981, -96.815613),zoom = 8, locate_control=True) # breaks at level 7
    # add Google Terrain as a basemap
    m.add_basemap("TERRAIN")

    # add FLDPLN basemaps (LIDAR terrain hillshade, floodplains, streams, ...)
    fldplnBasemapUrl = 'https://services.kars.geoplatform.ku.edu/arcgis/services/fldpln_kansas/Basemap/MapServer/WMSServer?'
    # add floodplains and strems (i.e., flood source pixels) layers. Layers added later are on the top!
    m.add_wms_layer(url=fldplnBasemapUrl, layers='0', name='Floodplains', format='image/png', transparent=True, shown=True) # But this layer is layer 1 on MapServer!
    m.add_wms_layer(url=fldplnBasemapUrl, layers='1', name='Streams', format='image/png', transparent=True, shown=True)

    # add additional FLDPLN reference layers (MinDtf, flood category layes (Action, Flood, Moderate, and Major))
    mindtfUrl = 'https://services.kars.geoplatform.ku.edu/arcgis/services/fldpln_kansas/MinDtf/ImageServer/WMSServer'
    m.add_wms_layer(url=mindtfUrl, layers='0', name='mindtf', format='image/png', transparent=True, shown=True)

    # add current and 14-day max flood maps
    testUrl = 'https://services.kars.geoplatform.ku.edu/arcgis/services/fldpln_kansas/ConstantStage/ImageServer/WMSServer'
    m.add_wms_layer(url=testUrl, layers='0', name='Random Constant Stage', format='image/png', transparent=True, shown=True)
    # m.add_cog_layer('https://fldpln.blob.core.windows.net/maps/spring_MinDtf.tif', name="Minimum Depth-to-Flood", palette="reds",shown=False)
    # m.add_cog_layer('https://fldpln.blob.core.windows.net/maps/spring_Major.tif', name="Major flood map", palette="reds")
    # m.add_cog_layer('https://fldpln.blob.core.windows.net/maps/spring_Action.tif', name="Action flood map", palette="reds")
    # m.add_cog_layer('https://fldpln.blob.core.windows.net/maps/spring_fcst000.tif', name="Current flood map", palette="reds")

    m
    m.to_streamlit(height=800)

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
