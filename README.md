[![N|Solid](https://bobit.us/wp-content/uploads/2021/04/bobit-logo.png)](https://bobit37.github.io/Resume/)

# Mac Address API Query

A python solution to query the https://macaddress.io MAC address lookup API over the network and fetch the company name

## Create an account

If you don't have an account, first create an account on https://macaddress.io/api/documentation/making-requests

Get API key

## Clone the repository
```
git clone https://github.com/BobIT37/mac_query_with_python.git

```

### To run

##### With Docker
```
docker-compose up
```

##### Without Docker
```
# create virtual environment
python3 -m venv venv
source venv/bin/activate

# install dependencies
pip3 install -r requirements.txt

# run project with cli argument
python3 mac_addr_query.py --addr=REPLACE_WITH_YOURS

# example cmd
python3 mac_addr_query.py --addr=88:66:5a:35:5e:e2



```

### The parameters are passed as Environment variables in .env

```
API_KEY=ADDYOURS
API_TOKEN=ADDYOURS
```

The environment variable values can be changed by changing the values in Dockerfile
