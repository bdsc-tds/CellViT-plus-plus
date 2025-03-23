# -*- coding: utf-8 -*-
# GeoJson templates
#
# @ Fabian Hörst, fabian.hoerst@uk-essen.de
# Institute for Artifical Intelligence in Medicine,
# University Medicine Essen


def get_template_point() -> dict:
    """Return a template for a Point geojson object

    Returns:
        dict: Template
    """
    template_point = {
        "type": "Feature",
        "id": "TODO",
        "geometry": {
            "type": "MultiPoint",
            "coordinates": [
                [],
            ],
        },
        "properties": {
            "objectType": "annotation",
            "classification": {"name": "TODO", "color": []},
        },
    }
    return template_point


def get_template_segmentation() -> dict:
    """Return a template for a MultiPolygon geojson object

    Returns:
        dict: Template
    """
    template_multipolygon = {
        "type": "Feature",
        "id": "TODO",
        "geometry": {
            "type": "MultiPolygon",
            "coordinates": [
                [],
            ],
        },
        "properties": {
            "objectType": "annotation",
            "classification": {"name": "TODO", "color": []},
        },
    }
    return template_multipolygon

def create_template_segmentation(
    entry_id: str,
    coords: list,
    name: str,
    gemo_type: str = "Polygon",
    obj_type: str = "annotation",
    color: list[int] | None = None,
) -> dict:
    for i, j in zip(coords[0], coords[-1]):
        if i != j:
            coords.append(coords[0])
            break

    ret: dict = {
        "type": "Feature",
        "id": entry_id,
        "geometry": {
            "type": gemo_type,
            "coordinates": [coords],
        },
        "properties": {
            "objectType": obj_type,
            "classification": {"name": name,},
        },
    }

    if color is not None:
        ret["properties"]["classification"]["color"] = color

    return ret
