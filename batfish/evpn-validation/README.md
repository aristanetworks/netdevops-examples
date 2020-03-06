# arista-demo
Repo to work on joint demo with Arista focusing on CVP + Batfish for change automation

This demo requires the latest Batfish docker image. Follow the steps below:
```
docker rm batfish
docker pull batfish/allinone:test-428
docker run --name batfish -v batfish-data:/data -p 8888:8888 -p 9997:9997 -p 9996:9996 batfish/allinone:test-428
```

To run pytest:
```
python -m pytest -s policies/ --html=report.html --tb=no --css=./policies/custom.css
```
