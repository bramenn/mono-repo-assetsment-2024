Aquí tienes una lista de los comandos más comunes de `kubectl`, organizados por categorías para facilitar su uso:

### 1. **Gestión de Pods**

- **Listar todos los Pods**:
  ```bash
  kubectl get pods
  ```
- **Ver detalles de un Pod específico**:
  ```bash
  kubectl describe pod <nombre-del-pod>
  ```
- **Eliminar un Pod**:
  ```bash
  kubectl delete pod <nombre-del-pod>
  ```
- **Ver logs de un Pod**:
  ```bash
  kubectl logs <nombre-del-pod>
  ```
- **Acceder a un Pod en modo interactivo**:
  ```bash
  kubectl exec -it <nombre-del-pod> -- /bin/bash
  ```

### 2. **Gestión de Deployments**

- **Listar todos los Deployments**:
  ```bash
  kubectl get deployments
  ```
- **Crear o actualizar un Deployment desde un archivo YAML**:
  ```bash
  kubectl apply -f <archivo-deployment.yaml>
  ```
- **Ver detalles de un Deployment específico**:
  ```bash
  kubectl describe deployment <nombre-del-deployment>
  ```
- **Escalar un Deployment**:
  ```bash
  kubectl scale deployment <nombre-del-deployment> --replicas=<número>
  ```
- **Eliminar un Deployment**:
  ```bash
  kubectl delete deployment <nombre-del-deployment>
  ```

### 3. **Gestión de Servicios (Services)**

- **Listar todos los Services**:
  ```bash
  kubectl get services
  ```
- **Ver detalles de un Service específico**:
  ```bash
  kubectl describe service <nombre-del-service>
  ```
- **Eliminar un Service**:
  ```bash
  kubectl delete service <nombre-del-service>
  ```

### 4. **Gestión de ConfigMaps y Secrets**

- **Listar todos los ConfigMaps**:
  ```bash
  kubectl get configmaps
  ```
- **Crear un ConfigMap desde un archivo**:
  ```bash
  kubectl create configmap <nombre-del-configmap> --from-file=<archivo>
  ```
- **Listar todos los Secrets**:
  ```bash
  kubectl get secrets
  ```
- **Crear un Secret desde un archivo**:
  ```bash
  kubectl create secret generic <nombre-del-secret> --from-file=<archivo>
  ```

### 5. **Gestión de Namespaces**

- **Listar todos los Namespaces**:
  ```bash
  kubectl get namespaces
  ```
- **Crear un Namespace**:
  ```bash
  kubectl create namespace <nombre-del-namespace>
  ```
- **Eliminar un Namespace**:
  ```bash
  kubectl delete namespace <nombre-del-namespace>
  ```

### 6. **Información del Clúster**

- **Ver información básica del clúster**:
  ```bash
  kubectl cluster-info
  ```
- **Ver nodos en el clúster**:
  ```bash
  kubectl get nodes
  ```
- **Ver detalles de un nodo específico**:
  ```bash
  kubectl describe node <nombre-del-nodo>
  ```

### 7. **Otros Comandos Útiles**

- **Aplicar cambios desde un archivo YAML**:
  ```bash
  kubectl apply -f <archivo.yaml>
  ```
- **Eliminar recursos desde un archivo YAML**:
  ```bash
  kubectl delete -f <archivo.yaml>
  ```
- **Ver recursos en tiempo real (ej. Pods)**:
  ```bash
  kubectl get pods -w
  ```
- **Autocompletar en la terminal** (para `bash`):
  ```bash
  source <(kubectl completion bash)
  ```

Estos comandos cubren los usos más comunes de `kubectl` y son una buena base para trabajar en Kubernetes.
