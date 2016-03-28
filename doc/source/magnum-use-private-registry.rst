==================================
Using Magnum with private registry
==================================

By default Magnum requires internet access to build a bay, in some cases,
you may limited to access internet especially you are limited to get
specify container images.

Alternative, Magnum supports to using your own private docker registry.

Prepare your own registry
=========================
Prepare a private insecure registry, you can find some documents quickly on
`Docker Registry <https://docs.docker.com/registry/>`_.


k8s
===

Prepare follow images on your registry ::

    google_containers/kube-ui     v4
    google_containers/hyperkube   v1.0.6
    google_containers/podmaster   1.1
    google_containers/pause       0.8.0

Swarm
=====

Prepare follow images on your registry ::

    swarm                         1.0.0

Mesos
=====
*To be filled in*


Create Baymodel
===============

When creating a baymodel, add --insecure-registry
${your_private_registry_url} ::

    magnum baymodel-create --name swarmbaymodel \
                       --image-id fedora-21-atomic-5 \
                       --keypair-id testkey \
                       --external-network-id public \
                       --dns-nameserver 8.8.8.8 \
                       --flavor-id m1.small \
                       --coe swarm \
                       --insecure-registry 192.168.0.100:50000
