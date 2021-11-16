from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from backend.plugins.default.module_name import MODULE_NAME
from . import models


class InlineAlignmentPlugin(CMSPluginBase):
    model = models.InlineAlignmentModel
    module = MODULE_NAME
    name = _("Inline Alignment")
    render_template = 'bs4_inline_alignment/plugins/inline_alignment.html'

    allow_children = True

plugin_pool.register_plugin(InlineAlignmentPlugin)
