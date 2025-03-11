# The proxy between VScode continue and Nvidia Chainserver
To connect to Nvidia RAG environment via their chain server from VScode Continue plugin.
Just converting HTTP request/response to fit VScode Continue plugin. 

## Refereces
- [Nvidia Chain Server](https://github.com/NVIDIA/GenerativeAIExamples/tree/main)
- [Continue Custom code RAG](https://docs.continue.dev/customize/tutorials/custom-code-rag)

## Installation
You can install this proxy onto your kubernetes by helm.

```bash
helm install myproxy ./helm 
```

If you want to expose this proxy, you can use [istio virtual service](example/virtual-service.yaml).

## Configuration of Continue
Set some parameters for contextProviders on config.json of Continue.

```json
  "contextProviders": [
    {
      "name": "http",
      "params": {
        "url": "http://continue-chain-proxy.ezua.fumi.jp/retrieve",
        "title": "http",
        "description": "Custom HTTP Context Provider",
        "displayTitle": "RAG_ON_HPE_PRIVATE_CLOUD_AI"
      }
    }
  ]
```

![](/pics/sample.png)