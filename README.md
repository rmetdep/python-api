# python-api
## List of chapters
- [About](#about)
- [Endpoints](#endpoints)
- [Backend](#backend)
- [Frontend](#frontend)
- [Screenshots](#screenshots)
- [Author](#author)
## About
This project was made for the course API development. It contains an api that can be used to get a random F1 driver and team or to add a circuit to the database. The API is built in python with fastAPI. To host it, an image gets build by docker hub and then pulled to okteto cloud.
## Endpoints
| endpoint | function |
| --- | --- |
| / | return the link to this document |
| /driver | returns a random driver |
| /team | returns a random team |
| /addciruit | add a circuit to the database |
| /docs | lists fastAPI documentation |
## Backend
The API backend can be accessed on tthe following link:  
[api-service-rmetdep](https://api-service-rmetdep.cloud.okteto.net/)  
If this iisnt the case that might be because the api didnt receive enough requests lately wich causes it to enter sleep mode. If for some reason the backend wont restart, please contact me.
## Frontend
The API frontend can be accessed on the following link:  
[rmetdep/python-api](https://rmetdep.github.io/python-api)  
Due to this being build with github actions (wich could have had a build error), there is also a second backup url:  
[rmetdep/python-api backup](https://bacbat32.sinners.be/apidev/)
## Screenshots
- API docs page  
![image](https://github.com/rmetdep/python-api/blob/main/images/docs.png)
- GET /driver  
![image](https://github.com/rmetdep/python-api/blob/main/images/driver.png)
- GET /team  
![image](https://github.com/rmetdep/python-api/blob/main/images/team.png)
- POST /addciruit succes  
![image](https://github.com/rmetdep/python-api/blob/main/images/addciruit-added.png)
- POST /addciruit failed  
![image](https://github.com/rmetdep/python-api/blob/main/images/addciruit-alreadyadded.png)
---
## Author
Roel Metdepenningen  
[roel@metdepenningen.com](mailto:roel@metdeenningen.com)  
[roel.metdepenningen.com](roel.metdepenningen.com)