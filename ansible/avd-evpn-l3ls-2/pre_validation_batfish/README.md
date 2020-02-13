## Validation for Arista EVPN design guide

Collection of Batfish checks to ensure that an Arista EVPN network is setup correctly.

### Usage

1. Edit `pytest.ini`. Ensure `snapshot` parameter is pointing at the directory containing your config files
2. Have python/virtual environment available
3. Run `python -m pip install -r requirements.txt`
4. Run `python -m pytest .`


### Advanced usage/debugging

* Modify `pytest.ini` to adjust enable console logging and log level as needed. 