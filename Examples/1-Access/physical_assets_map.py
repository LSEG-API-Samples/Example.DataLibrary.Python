from ipyleaflet import Map, Marker,basemaps,LayersControl,ScaleControl,FullScreenControl,basemap_to_tiles,SplitMapControl,SearchControl
import pandas
class PhysicalAssetsMap():
    def __init__(self,zoom=None):
        #self.right_layer = basemap_to_tiles(basemaps.NASAGIBS.ModisTerraTrueColorCR, "2017-04-08")
        self.right_layer = basemap_to_tiles(basemaps.Gaode.Satellite)
        self.left_layer = basemap_to_tiles(basemaps.OpenStreetMap.HOT)
        if zoom is None:
            self.zoom = 5
        else:
            self.zoom = zoom


    def _add_map_controls(self,center):
        m = Map(center=center,zoom=5)
        control = LayersControl(position='topright')
        m.add_control(control)
        m.add_control(ScaleControl(position='bottomleft'))
        m.add_control(FullScreenControl())
        m.add_control(SplitMapControl(left_layer=self.left_layer, right_layer=self.right_layer))
        m.add_control(SearchControl(
            position="topleft",
            url='https://nominatim.openstreetmap.org/search?format=json&q={s}',
            zoom=self.zoom))
        self.map = m


    def plot(self,df):
        count = 0
        center = None
        if 'Latitude' not in df.columns:
            self.map = Map(zoom=self.zoom)
            return self

        for index,row in df.iterrows():
            name = row['DTSubjectName']
            lat = row['Latitude']
            lon = row['Longitude']
            if type(lat) == pandas._libs.missing.NAType or type(lon) == pandas._libs.missing.NAType:
                continue
            if center is None:
                center = (lat,lon)
        if center is not None:
            self._add_map_controls(center)
        else:
            self.map = Map(zoom=self.zoom)

        for index,row in df.iterrows():
            name = row['DTSubjectName']
            lat = row['Latitude']
            lon = row['Longitude']
            if type(lat) == pandas._libs.missing.NAType or type(lon) == pandas._libs.missing.NAType:
                continue
            count+= 1
            marker = Marker(name=name,location=tuple([lat,lon]), draggable=False)
            self.map.add_layer(marker)
        return self

    def show(self):
        display(self.map)
