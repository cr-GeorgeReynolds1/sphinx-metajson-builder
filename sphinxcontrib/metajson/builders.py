from sphinxcontrib.serializinghtml import JSONHTMLBuilder
from sphinx.environment.adapters.toctree import TocTree

class JSONMETAHTMLBuilder(JSONHTMLBuilder):

    name = 'metajson'

    def get_doc_context(self, docname, body, metatags):

        out_dict = super(JSONMETAHTMLBuilder, self).get_doc_context(docname, body, metatags)

        self_toctree = TocTree(self.env).get_toctree_for(docname, self, True)
        toctree = self.render_partial(self_toctree)['fragment']
        out_dict['fulltoc'] = toctree

        return out_dict
