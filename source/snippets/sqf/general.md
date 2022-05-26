# General SQF Snippets

## Get Marker Position

```
outposts apply { getMarkerPos _x }
resourcesX apply { getMarkerPos _x }
factories apply { getMarkerPos _x }
airportsX apply { getMarkerPos _x }
seaports apply { getMarkerPos _x }
citiesX apply { getMarkerPos _x }
```

### Get all Marker Pos to Clipboard (try)

```
_br = toString [13,10];
_outposts = outposts apply { getMarkerPos _x };
_resourcesX = resourcesX apply { getMarkerPos _x };
_factories = factories apply { getMarkerPos _x };
_airportsX = airportsX apply { getMarkerPos _x };
_seaports = seaports apply { getMarkerPos _x };
_citiesX = citiesX apply { getMarkerPos _x };

_all_outposts = outposts + _outposts;
_all_resourcesX = resourcesX + _resourcesX;
_all_factories = factories + _factories;
_all_airportsX = airportsX + _airportsX;
_all_seaports = seaports + _seaports;
_all_citiesX = citiesX + _citiesX;

_out = "outposts: " + _br + str _all_outposts + _br + _br + "resourcesX: " + _br + str _all_resourcesX + _br + _br + "factories: " + _br + str _all_factories + _br + _br + "airportsX: " + _br + str _all_airportsX + _br + _br + "seaports: " + _br + str _all_seaports + _br + _br + "citiesX: " + _br + str _all_citiesX;
_all_out = str _out;
copyToClipboard _all_out;
```

#### better

```
private _out = "";
{
    _out = _out + ((_x#0) + ":" + endl + str (_x apply {[_x, getMarkerPos _x]}) + endl + endl)
} forEach [outposts, resourcesX, factories, airportsX, seaports, citiesX];
copyToClipboard _out;
```

## worldsize

```
copyToClipboard worldsize
```

## Line break

```
_br = toString [13,10];
```

## To Clipboard

```
_string = "Line 1"
copyToClipboard _string;
```

## log

```
["<message>"] remoteExec ["diag_log"]
```

## what is attached to player

```
attachedObjects cursorObject apply { typeof _x }

```

instead of `cursorObject` -> `player`
