from tethys_sdk.base import TethysAppBase, url_map_maker
from tethys_sdk.app_settings import PersistentStoreDatabaseSetting, PersistentStoreConnectionSetting


class GloCv(TethysAppBase):
    """
    Tethys app class for Customized Views'
    """

    name = 'Customized Views'
    index = 'glo_cv:home'
    icon = 'glo_cv/images/logo.jpg'
    package = 'glo_cv'
    root_url = 'glo-cv'
    color = '#16a085'
    description = 'Customized Views'
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='glo-cv',
                controller='glo_cv.controllers.home'
            ),
            UrlMap(
                name='popup-info',
                url='glo-cv/popup-info',
                controller='glo_cv.controllers_ajax.get_popup_info'
            ),
            UrlMap(
                name='get-meta-file',
                url='glo-cv/get-meta-file',
                controller='glo_cv.controllers_ajax.get_meta_file'
            ),
            UrlMap(
                name='add-point',
                url='glo-cv/add-point',
                controller='glo_cv.controllers.add_point'
            ),
            UrlMap(
                name='delete-layer',
                url='glo-cv/delete-layer',
                controller='glo_cv.controllers.delete_layer'
            ),
            UrlMap(
                name='submit-delete-layer',
                url='glo-cv/delete-layer/submit',
                controller='glo_cv.controllers_ajax.layer_delete'
            ),
            UrlMap(
                name='add-point-ajax',
                url='glo-cv/add-point/submit',
                controller='glo_cv.controllers_ajax.point_add'
            ),
            UrlMap(
                name='approve-points',
                url='glo-cv/approve-points',
                controller='glo_cv.controllers.approve_points'
            ),
            UrlMap(
                name='approve-points_tabulator',
                url='glo-cv/approve-points/tabulator',
                controller='glo_cv.controllers_ajax.points_tabulator'
            ),
            UrlMap(
                name='update-points-ajax',
                url='glo-cv/approve-points/submit',
                controller='glo_cv.controllers_ajax.point_update'
            ),
            UrlMap(
                name='delete-points-ajax',
                url='glo-cv/approve-points/delete',
                controller='glo_cv.controllers_ajax.point_delete'
            ),
            UrlMap(
                name='add-polygon',
                url='glo-cv/add-polygon',
                controller='glo_cv.controllers.add_polygon'
            ),
            UrlMap(
                name='add-polygon-ajax',
                url='glo-cv/add-polygon/submit',
                controller='glo_cv.controllers_ajax.polygon_add'
            ),
            UrlMap(
                name='approve-polygons',
                url='glo-cv/approve-polygons',
                controller='glo_cv.controllers.approve_polygons'
            ),
            UrlMap(
                name='approve-polygons-tabulator',
                url='glo-cv/approve-polygons/tabulator',
                controller='glo_cv.controllers_ajax.polygons_tabulator'
            ),
            UrlMap(
                name='update-polygons-ajax',
                url='glo-cv/approve-polygons/submit',
                controller='glo_cv.controllers_ajax.polygon_update'
            ),
            UrlMap(
                name='delete-polygons-ajax',
                url='glo-cv/approve-polygons/delete',
                controller='glo_cv.controllers_ajax.polygon_delete'
            ),
            UrlMap(
                name='add-new-layer',
                url='glo-cv/add-new-layer',
                controller='glo_cv.controllers.add_new_layer'
            ),
            UrlMap(
                name='get-new-layer-attributes',
                url='glo-cv/add-new-layer/get-attributes',
                controller='glo_cv.controllers_ajax.get_shp_attributes'
            ),
            UrlMap(
                name='add-new-layer-ajax',
                url='glo-cv/add-new-layer/submit',
                controller='glo_cv.controllers_ajax.new_layer_add'
            ),
            UrlMap(
                name='set-layer-style',
                url='glo-cv/set-layer-style',
                controller='glo_cv.controllers.set_layer_style'
            ),
            UrlMap(
                name='set-layer-style-ajax',
                url='glo-cv/set-layer-style/submit',
                controller='glo_cv.controllers_ajax.layer_style_set'
            ),
            UrlMap(
                name='add-endpoint',
                url='glo-cv/add-endpoint',
                controller='glo_cv.controllers.add_endpoint'
            ),
            UrlMap(
                name='add-endpoint-submit',
                url='glo-cv/add-endpoint/submit',
                controller='glo_cv.controllers_ajax.endpoint_add'
            ),
            UrlMap(
                name='delete-endpoint',
                url='glo-cv/delete-endpoint',
                controller='glo_cv.controllers.delete_endpoint'
            ),
            UrlMap(
                name='delete-endpoint-submit',
                url='glo-cv/delete-endpoint/submit',
                controller='glo_cv.controllers_ajax.endpoint_delete'
            ),
            UrlMap(
                name='get-layers-info',
                url='glo-cv/api/get-layers-info',
                controller='glo_cv.api.get_layers_info'
            ),
            UrlMap(
                name='get-layers-by-county',
                url='glo-cv/api/get-layers-by-county',
                controller='glo_cv.api.get_layers_by_county'
            ),
            UrlMap(
                name='get-points-by-county',
                url='glo-cv/api/get-points-by-county',
                controller='glo_cv.api.get_points_by_county'
            ),
            UrlMap(
                name='get-polygons-by-county',
                url='glo-cv/api/get-polygons-by-county',
                controller='glo_cv.api.get_polygons_by_county'
            ),
            UrlMap(
                name='get-points-by-layer',
                url='glo-cv/api/get-points-by-layer',
                controller='glo_cv.api.get_points_by_layer'
            ),
            UrlMap(
                name='get-polygons-by-layer',
                url='glo-cv/api/get-polygons-by-layer',
                controller='glo_cv.api.get_polygons_by_layer'
            ),
            UrlMap(
                name='get-points-by-geometry',
                url='glo-cv/api/get-points-by-geometry',
                controller='glo_cv.api.get_points_by_geom'
            ),
            UrlMap(
                name='get-polygons-by-geometry',
                url='glo-cv/api/get-polygons-by-geometry',
                controller='glo_cv.api.get_polygons_by_geom'
            ),
            UrlMap(
                name='dowloand-layers',
                url='glo-cv/download-layers',
                controller='glo_cv.controllers_ajax.download_layers'
            ),
            UrlMap(
                name='download-interaction',
                url='glo-cv/download-interaction',
                controller='glo_cv.controllers_ajax.download_interaction'
            ),
            UrlMap(
                name='download-points-csv',
                url='glo-cv/api/download-points-csv',
                controller='glo_cv.api.download_points_csv'
            ),
            UrlMap(
                name='download-polygons-csv',
                url='glo-cv/api/download-polygons-csv',
                controller='glo_cv.api.download_polygons_csv'
            ),
            UrlMap(
                name='download-layer-csv',
                url='glo-cv/api/download-layer-csv',
                controller='glo_cv.api.download_layer_csv'
            ),
        )

        return url_maps

    def persistent_store_settings(self):
        """
        Define Persistent Store Settings.
        """
        ps_settings = (
            PersistentStoreDatabaseSetting(
                name='layers',
                description='layers database',
                initializer='glo_cv.model.init_layer_db',
                required=True,
                spatial=True
            ),
        )

        return ps_settings
