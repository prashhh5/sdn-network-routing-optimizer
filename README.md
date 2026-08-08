# SDN Network Routing Optimizer 🔀

Software-Defined Networking (SDN) path controller that dynamic calculates low-latency, high-throughput network paths using graph algorithm optimization (`NetworkX`).

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![PyTest](https://img.shields.io/badge/PyTest-Automated-green)

---

## 🏗 Topology & Path Decision Flow

```mermaid
graph LR
    A[Switch_A] -- Direct High Latency --> B[Switch_C]
    A -- Low Latency / High BW --> C[Switch_D]
    C -- Optimal Link --> B
