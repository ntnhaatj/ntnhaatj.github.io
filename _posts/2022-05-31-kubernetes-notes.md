---
layout: post
title:  "Containerized Notes"
date:   2022-05-31
categories: unknown
author: ntnhaatj
tags: work devops
---


# Docker
```sh
# remove dangling docker images
$ docker image prune

# remove all containers
$ docker rm -f $(docker ps -aq)

# attach to running container, display the output of ENTRYPOINT/CMD process
$ docker run -d --name topdemo ubuntu /usr/bin/top -b
$ docker attach topdemo
<display top command, interrupt signal could be sent by this cmd>
```

# Kubernetes

## Commands

```sh
# run pod
$ kubectl apply -f hello-kube.yaml
$ kubectl get pod
$ kubectl port-forward pod/hello-kube 3000:3000
$ kubectl delete pod hello-kube

# get pod with label
$ kubectl get pod --show-labels
$ kubectl get pod -L enviroment
$ kubectl get pod -l enviroment=production

# namespace
$ kubectl get ns
$ kubectl get pod --namespace kube-system
```

## Sample pod file

```yaml
apiVersion: v1 # Descriptor conforms to version v1 of Kubernetes API
kind: Pod # Select Pod resource
metadata:
  name: hello-kube # The name of the pod
spec:
  containers:
    - image: 080196/hello-kube # Image to create the container
      name: hello-kube # The name of the container
      ports:
        - containerPort: 3000 # The port the app is listening on 
          protocol: TCP
```

## Labeling Pods

```yaml
metadata:
  name: hello-kube-testing
  labels:
    enviroment: testing # label with key is enviroment and value is testing
    project: kubernetes-series
...
---
metadata:
  name: hello-kube-staging
  labels:
    enviroment: staging # label with key is enviroment and value is staging
    project: kubernetes-series
...
---
metadata:
  name: hello-kube-production
  labels:
    enviroment: production # label with key is enviroment and value is production
    project: kubernetes-series
...
```

## Namespace
```sh
$ kubectl create ns <project>:<env> # create namespace

$ cat hello-kube.yaml
apiVersion: v1
kind: Pod
metadata:
  name: hello-kube-testing
  namespace: <project>:<env> # namespace name
spec:
  containers:
    - image: 080196/hello-kube
      name: hello-kube
      ports:
        - containerPort: 3000
          protocol: TCP

$ kubectl delete ns testing
```

## ReplicationControllers and other controllers

```yaml
apiVersion: v1
kind: ReplicationController
spec:
  replicas: 2 # number of the pod
  selector: # The pod selector determining what pods the RC is operating on
    app: hello-kube # label value
  template: # pod template
    metadata:
      labels:
        app: hello-kube # label value
```

### ReplicaSet (new version of ReplicationControllers)

```yaml
apiVersion: apps/v1 # change version API
kind: ReplicaSet # change resource name
spec:
  replicas: 2
  selector:
    matchLabels: # change here 
      app: hello-kube
  template:
    metadata:
      labels:
        app: hello-kube
```

### DaemonSet

- deploy 1 pod for all node
- used for logging and monitoring

- label your node

```sh
$ kubectl label nodes <your-node-name> disk=ssd
```

- template to select your nodes to deploy monitor

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: ssd-monitor
spec:
  selector:
    matchLabels:
      app: ssd-monitor
  template:
    metadata:
      labels:
        app: ssd-monitor
    spec:
      nodeSelector:
        disk: ssd
      containers:
        - name: main
          image: luksa/ssd-monitor
```

## Service

- Pods are ephemeral
- service manage multiple pods

```yaml
apiVersion: v1
kind: Service
metadata:
  name: hello
spec:
  selector:
    app: hello-kube # label selectors Pod
  ports:
    - port: 80 # port of the serivce
      targetPort: 3000 # port of the container that service will forward to 
```

- There are 4 sorts of service:
    - ClusterIP
    - NodePort
    - ExternalName
    - LoadBalancer

## Ingress service

provide load balancing

https://kubernetes.io/docs/concepts/services-networking/ingress/

