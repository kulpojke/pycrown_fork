
# As a reasearcher/forester/other user I would like to be able to easily query the pointcloud of an arbitrarliy large region by extent to create a CHM/ and or DSM/ and or DTM.  (a stand alone comand line soluting would be good here, prefereably in a container)
    # e.g. ept_toolz query ([21231.12312, -231231.12312],[12312.23123, 123123.1231231]) -chm -dsm -dtm -las -srs 3857

# As a reasearcher I would like to be able to easily query the pointcloud of an arbitrarliy large region by extent and have the resulting points returned as a numpy array.

def ept_query(bbox, srs="EPSG:3857" chm=True, dsm=True, dtm=True, las=True):
    ''' Reads pointcloud for the given bbox, optionally creates a canopy heght model,
    digital surface model, and digital terrain model.  Returns a numpy array of points.

    bbox -- Tuple  - Bounding box in srs coordintes (default srs is EPSG:3857),
                     in the form: ([xmin, xmax], [ymin, ymax]).
    srs  -- String - EPSG identifier for srs  being used. Defaults to EPSG:3857,
                     because that is what ept files tend to use.
    chm  -- Bool   - Toggles CHM output, default is True.
    dsm  -- Bool   - Toggles DSM output, default is True.
    dtm  -- Bool   - Toggles DTM output, default is True.
    '''

    # I have largely done this for ept files except,
    # TODO: Challenging part.  If the region is large too many points for memory, need to divide the rgion into tiles then mosaic them together.
    # I have not been able to do this without seems or edge effects.

# -----------------------------------------------------

# As a researcher/forester/other I would like to be able to easily delineate crowns in a canopy so that I might know how many trees are present (perhaps as a first step to identifying the species of those trees)  (again a stand alone in a container)
    # This can be done with pycrown, the above tools are a first step for this

# -----------------------------------------------------

# As a researcher/forester I would would like to find individual (and areas of) tree mortality so that I can determine (perhaps as a first step to identifying the species of those trees)  (again a stand alone in a container)
    # This builds on the above tools.  Would combine them with 4 band NAIP or other imagery.

# ------------------------------------------------------
# GAP measurements?
