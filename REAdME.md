# National ID Information Extractor
Python Django REST framework application for Extracting information from Egyption National ID


## To run the app on docker:
- Clone the repo to your local `git clone https://github.com/Omar-Aboelsoud/EgyptionNationalIDInformationExtractor.git`
- cd into cloned folder.
- run the following command `docker-compose up --build -d`
- To check the status of the running containers, run the following command `docker ps -a`


## To run test cases docker:
- cd into cloned folder.
- run the following command `docker compose  -f docker-compose-tests.yml up`
- To check the status of the running containers, run the following command `docker ps -a`


......

### To test the endpoints by postman



-- For extract information from national ID --
```
POST http://localhost:8000/nid/data/ : 
RequestBody :
{
    "national_id": "29503022300145"
}
```

Enjoy :)