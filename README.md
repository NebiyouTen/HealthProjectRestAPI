# Health Project RestAPI
## Database Tables
- **Clients:** The clients table stores basic information about the clients. The basic informations stored are name, gender, age or estimated age and address.  
- **Calls:** The calls table keeps records of the phone calls made. The records include phone number, purpose of the call, time of the call, type of the issue being reported and extra notes related to the call. The table will have a reference to the client in the client table.
- **Staff:** This table will keep records of staffs and their basic information. 
- **Police Stations:** A record of available police stations and their location. 
- **Health Centers:** A record of available health stations and their location. 
- **Safe Spaces:** A table that stores the RWN safe spaces. 
- **Service:** This table serves as a parent table for the all the provided services. The service provided might include a safe space, a police station and/or a health center. Addition information in this table include the staff handling the service, the safe space and some additional notes. 
- **Police station Service:** This table stores reference to a police station and a service, if the service involves police.         
- **Health center Service:** This table stores reference to a health center and a service, if the service involves a health center.


## API  
The database was created using MySql. An API that allows access to the database was created using DJango rest framework. Requests can be sent as GET or POST requests and data in JSON format is responded. 

## Resources

Each table or resource can be accessed, updated or deleted using http request. 
 **http://nyismaw.pythonanywhere.com/api/resource_name/**  
#### Resource name for each table. <br/>
- **clients**<br/>
- **calls**<br/>
- **staffs**<br/>
- **safe_spaces**<br/>
- **police_stations**<br/>
- **health_centers**<br/>
- **services**<br/>
- **police_station_services**<br/>
- **health_center_services**<br/>

The request bodies can include JSON objects when updating or creating new entries.
## Authentication
The authentication method used for the API is OAUTH 2.0. Afters Users are registered, they will be provided with a client ID and a client secret. Using these credentials, users can request for an application token using the link, http://<url>/auth/token. After getting the token, users will be allowed to access resources. 
   
.  


 
  
