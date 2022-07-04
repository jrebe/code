# basebull
Have you seen my baseball

# Development

1. Setup a local pyenv to 3.6
```
$ pyenv local basebull 
```
2. Run tox
```
$ tox
```

## Generating and storing maps.key
Go to https://console.developers.google.com/apis/dashboard
Enable Maps Static API, Directions API, and Distance Matrix API
Generate API keyu that is restricted to those APIs
Put key into `maps.key`