

## Cache ID extractor 

https://tyk.io/tyk-documentation/customise-tyk/plugins/auth-plugins/

```
"custom_middleware": {
  "pre": [
    {
      "name": "MyPreMiddleware",
      "require_session": false
    }
  ],
  "id_extractor": {
    "extract_from": "header",
    "extract_with": "value",
    "extractor_config": {
      "header_name": "Authorization"
    }
  },
  "driver": "grpc"
},

```

