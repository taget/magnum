#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from oslo_versionedobjects import fields

from magnum.db import api as dbapi
from magnum.objects import base


@base.MagnumObjectRegistry.register
class BayLock(base.MagnumPersistentObject, base.MagnumObject,
              base.MagnumObjectDictCompat):
    # Version 1.0: Initial version
    VERSION = '1.0'

    dbapi = dbapi.get_instance()

    fields = {
        'id': fields.IntegerField(),
        'bay_uuid': fields.StringField(nullable=True),
        'conductor_id': fields.StringField(nullable=True),
    }

    @base.remotable_classmethod
    def create(cls, bay_uuid, conductor_id):
        return cls.dbapi.create_bay_lock(bay_uuid, conductor_id)

    @base.remotable_classmethod
    def steal(cls, bay_uuid, old_conductor_id, new_conductor_id):
        return cls.dbapi.steal_bay_lock(bay_uuid, old_conductor_id,
                                        new_conductor_id)

    @base.remotable_classmethod
    def release(cls, bay_uuid, conductor_id):
        return cls.dbapi.release_bay_lock(bay_uuid, conductor_id)
