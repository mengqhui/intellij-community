# Stubs for boto.s3 (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .connection import S3Connection

from boto.connection import AWSAuthConnection
from boto.regioninfo import RegionInfo

from typing import List, Type, Text

class S3RegionInfo(RegionInfo):
    def connect(self, name: Text=None, endpoint: str=None, connection_cls: Type[AWSAuthConnection]=None, **kw_params) -> S3Connection: ...

def regions() -> List[S3RegionInfo]: ...
def connect_to_region(region_name: Text, **kw_params): ...
