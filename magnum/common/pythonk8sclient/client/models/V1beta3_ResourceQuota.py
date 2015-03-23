#!/usr/bin/env python
"""
Copyright 2015 Reverb Technologies, Inc.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

class V1beta3_ResourceQuota(object):
    """NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'annotations': 'any',
            
            
            'apiVersion': 'str',
            
            
            'creationTimestamp': 'str',
            
            
            'deletionTimestamp': 'str',
            
            
            'generateName': 'str',
            
            
            'kind': 'str',
            
            
            'labels': 'any',
            
            
            'name': 'str',
            
            
            'namespace': 'str',
            
            
            'resourceVersion': 'str',
            
            
            'selfLink': 'str',
            
            
            'spec': 'v1beta3_ResourceQuotaSpec',
            
            
            'status': 'v1beta3_ResourceQuotaStatus',
            
            
            'uid': 'str'
            
        }

        self.attributeMap = {
            
            'annotations': 'annotations',
            
            'apiVersion': 'apiVersion',
            
            'creationTimestamp': 'creationTimestamp',
            
            'deletionTimestamp': 'deletionTimestamp',
            
            'generateName': 'generateName',
            
            'kind': 'kind',
            
            'labels': 'labels',
            
            'name': 'name',
            
            'namespace': 'namespace',
            
            'resourceVersion': 'resourceVersion',
            
            'selfLink': 'selfLink',
            
            'spec': 'spec',
            
            'status': 'status',
            
            'uid': 'uid'
            
        }       

        
        #map of string keys and values that can be used by external tooling to store and retrieve arbitrary metadata about objects
        
        self.annotations = None # any
        
        #version of the schema the object should have
        
        self.apiVersion = None # str
        
        #RFC 3339 date and time at which the object was created; populated by the system, read-only; null for lists
        
        self.creationTimestamp = None # str
        
        #RFC 3339 date and time at which the object will be deleted; populated by the system when a graceful deletion is requested, read-only; if not set, graceful deletion of the object has not been requested
        
        self.deletionTimestamp = None # str
        
        #an optional prefix to use to generate a unique name; has the same validation rules as name; optional, and is applied only name if is not specified
        
        self.generateName = None # str
        
        #kind of object, in CamelCase; cannot be updated
        
        self.kind = None # str
        
        #map of string keys and values that can be used to organize and categorize objects; may match selectors of replication controllers and services
        
        self.labels = None # any
        
        #string that identifies an object. Must be unique within a namespace; cannot be updated
        
        self.name = None # str
        
        #namespace of the object; cannot be updated
        
        self.namespace = None # str
        
        #string that identifies the internal version of this object that can be used by clients to determine when objects have changed; populated by the system, read-only; value must be treated as opaque by clients and passed unmodified back to the server: https://github.com/GoogleCloudPlatform/kubernetes/blob/master/docs/api-conventions.md#concurrency-control-and-consistency
        
        self.resourceVersion = None # str
        
        #URL for the object; populated by the system, read-only
        
        self.selfLink = None # str
        
        #spec defines the desired quota; https://github.com/GoogleCloudPlatform/kubernetes/blob/master/docs/api-conventions.md#spec-and-status
        
        self.spec = None # v1beta3_ResourceQuotaSpec
        
        #status defines the actual enforced quota and current usage; https://github.com/GoogleCloudPlatform/kubernetes/blob/master/docs/api-conventions.md#spec-and-status
        
        self.status = None # v1beta3_ResourceQuotaStatus
        
        #unique UUID across space and time; populated by the system; read-only
        
        self.uid = None # str
        
