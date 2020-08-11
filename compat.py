# -*- coding: utf-8 -*-
import sys
try:  # pragma: nocover
    from urllib.parse import quote
except:  # pragma: nocover
    from urllib import quote


PY3 = sys.version_info > (3, )
