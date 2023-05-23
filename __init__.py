# -*- coding: utf-8 -*-
"""
/***************************************************************************
 IPP
                                 A QGIS plugin
 This plugin calculates IPP
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-05-16
        copyright            : (C) 2023 by Truong Anh Huy LE
        email                : huymop.lee@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load IPP class from file IPP.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .IPP import IPP
    return IPP(iface)
