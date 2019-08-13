import uuid
from IPython.core.display import display, HTML
import json

class RenderJSON(object):
    
    def __init__(self, json_data):
        if isinstance(json_data, dict):
            self.json_str = json.dumps(json_data)
        else:
            self.json_str = json_data

        self.uuid = str(uuid.uuid4())

    def _ipython_display_(self):
        display(HTML('<div id="{}" style="height: auto; width:100%;"></div>'.format(self.uuid)))
        display(HTML("""<script>
        require(['https://rawgit.com/caldwell/renderjson/master/renderjson.js'],
        function() {
          renderjson.set_show_to_level(1)
          document.getElementById('%s').appendChild(renderjson(%s))
        });
        </script>""" % (self.uuid, self.json_str)))
