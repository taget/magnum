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

class V1beta3_ReplicationControllerSpec(object):
    """NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'replicas': 'int',
            
            
            'selector': 'any',
            
            
            'template': 'v1beta3_PodTemplateSpec',
            
            
            'templateRef': 'v1beta3_ObjectReference'
            
        }

        self.attributeMap = {
            
            'replicas': 'replicas',
            
            'selector': 'selector',
            
            'template': 'template',
            
            'templateRef': 'templateRef'
            
        }       

        
        #number of replicas desired
        
        self.replicas = None # int
        
        #label keys and values that must match in order to be controlled by this replication controller
        
        self.selector = None # any
        
        #object that describes the pod that will be created if insufficient replicas are detected; takes precendence over templateRef
        
        self.template = None # v1beta3_PodTemplateSpec
        
        #reference to an object that describes the pod that will be created if insufficient replicas are detected
        
        self.templateRef = None # v1beta3_ObjectReference
        
