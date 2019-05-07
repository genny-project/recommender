# Recommender

Recommender is a recommendation engine which compares two entities X and Y and suggests the best Y values for X. The recommendation engine uses content based filtering by using Natural Language processing. The search query input for X and Y should include only the columns which are needed for comparison.

# Running the service

  - Pull the image from Docker hub 
    ```sh
    docker pull gennyproject/recommender:latest
    ```
  - Run the docker container. Replace 5656 with the port needed
    ```sh
    docker run -d -p 5656:5000 gennyproject/recommender:latest
    ```
  - The service will run on port 5656

# Using the service
 - The recommender service runs on http://localhost:5656/scoring
 - The input to the API should be of the below format
   ```ssh
   {
        "base_Entity_X": [
            {SEARCH QUERY 1}
        
        ],
        "base_Entity_Y": [
            {SEARCH QUERY 2}
        }
   }
   ```
  - The output would be base entity codes in a list
    ```ssh
    ['BASENTITY1','BASEENTITYCODE2']


Example input for internship matching:
```ssh
{
	"base_Entity_X": [
	  {
    "baseEntityAttributes": [{
            "baseEntityCode": "SBE_INTERNSHIPS",
            "attributeCode": "COL_LNK_INDUSTRY",
            "attributeName": "Industry",
            "created": "2018-04-26T14:05:06.843",
            "weight": 5.0,
            "inferred": false,
            "privacyFlag": false
        },
	{
	"baseEntityCode": "SBE_INTERNSHIPS",
            "attributeCode": "COL_PRI_CODE",
            "attributeName": "Code",
            "created": "2018-04-26T14:05:06.843",
            "weight": 6.0,
            "inferred": false,
            "privacyFlag": false
	},
        {
            "baseEntityCode": "SBE_INTERNSHIPS",
            "attributeCode": "PRI_CODE",
            "attributeName": "LIKE",
            "created": "2018-04-26T14:05:06.843",
            "valueString": "BEG_%",
            "weight": 1.0,
            "inferred": false,
            "privacyFlag": false
        },
        {
            "baseEntityCode": "SBE_INTERNSHIPS",
            "attributeCode": "COL_PRI_POSITION_DESCRIPTION",
            "attributeName": "Position Description",
            "readonly": false,
            "created": "2019-04-09T04:15:51.785",
            "weight": 1.0,
            "inferred": false,
            "privacyFlag": false
        },
        {
            "baseEntityCode": "SBE_INTERNSHIPS",
            "attributeCode": "COL_LNK_OCCUPATION",
            "attributeName": "Occupation",
            "readonly": false,
            "created": "2019-04-09T04:15:51.785",
            "weight": 4.0,
            "inferred": false,
            "privacyFlag": false
        },
        {
            "baseEntityCode": "SBE_INTERNSHIPS",
            "attributeCode": "COL_PRI_INTERNSHIP_DESCRIPTION",
            "attributeName": "Internship Description",
            "readonly": false,
            "created": "2019-04-09T04:15:51.785",
            "weight": 3.0,
            "inferred": false,
            "privacyFlag": false
        },
        {
            "baseEntityCode": "SBE_INTERNSHIPS",
            "attributeCode": "COL_PRI_INTERNSHIP_LEARNING_OUTCOMES",
            "attributeName": "Learning Outcomes",
            "readonly": false,
            "created": "2019-04-09T04:15:51.785",
            "weight": 2.0,
            "inferred": false,
            "privacyFlag": false
        },
        {
            "baseEntityCode": "SBE_INTERNSHIPS",
            "attributeCode": "SCH_PAGE_START",
            "attributeName": "PageStart",
            "readonly": false,
            "created": "2019-04-09T04:15:51.786",
            "valueInteger": 0,
            "weight": 3.0,
            "inferred": false,
            "privacyFlag": false
        },
        {
            "baseEntityCode": "SBE_INTERNSHIPS",
            "attributeCode": "SCH_PAGE_SIZE",
            "attributeName": "PageSize",
            "created": "2018-04-26T14:05:06.843",
            "valueInteger": 10000,
            "weight": 3.0,
            "inferred": false,
            "privacyFlag": false
        },
        {
            "baseEntityCode": "SBE_INTERNSHIPS",
            "attributeCode": "SCH_PAGE_START",
            "attributeName": "PageStart",
            "created": "2018-04-26T14:05:06.843",
            "valueInteger": 0,
            "weight": 3.0,
            "inferred": false,
            "privacyFlag": false
        }
    ],
    "links": [],
    "code": "SBE_INTERNSHIPS",
    "index": 0,
    "created": "2018-04-26T14:05:06.842",
    "name": "List of Users",
    "realm": "genny"
}
	],
	"base_Entity_Y": [
	  {        
"baseEntityAttributes": [
		{
                 "baseEntityCode": "SBE_USERS",
                 "attributeCode": "COL_PRI_INTERN_DETAILS",
                 "attributeName": "Intern Details",
                 "created": "2018-04-26T14:05:06.843",
                 "weight": 9.0,
                 "inferred": false,
                 "privacyFlag": false
               },
		{
                 "baseEntityCode": "SBE_USERS",
                 "attributeCode": "COL_LNK_INDUSTRY",
                 "attributeName": "Industry",
                 "created": "2018-04-26T14:05:06.843",
                 "weight": 8.0,
                 "inferred": false,
                 "privacyFlag": false
               },
		{
                 "baseEntityCode": "SBE_USERS",
                 "attributeCode": "COL_LNK_OCCUPATION",
                 "attributeName": "Occupation",
                 "created": "2018-04-26T14:05:06.843",
                 "weight": 7.0,
                 "inferred": false,
                 "privacyFlag": false
               },

               {
                 "baseEntityCode": "SBE_USERS",
                 "attributeCode": "PRI_CODE",
                 "attributeName": "LIKE",
                 "created": "2018-04-26T14:05:06.843",
                 "valueString": "PER_543384923_AT_QQCOM",
                 "weight": 1.0,
                 "inferred": false,
                 "privacyFlag": false
               },

               {
                 "baseEntityCode": "SBE_USERS",
                 "attributeCode": "SCH_PAGE_SIZE",
                 "attributeName": "PageSize",
                 "created": "2018-04-26T14:05:06.843",
                 "valueInteger": 10000,
                 "weight": 3.0,
                 "inferred": false,
                 "privacyFlag": false
               },
               {
                 "baseEntityCode": "SBE_USERS",
                 "attributeCode": "SCH_PAGE_START",
                 "attributeName": "PageStart",
                 "created": "2018-04-26T14:05:06.843",
                 "valueInteger": 0,
                 "weight": 3.0,
                 "inferred": false,
                 "privacyFlag": false
               }
             ],
             "links": [],
             "code": "SBE_USERS",
             "index": 0,
             "created": "2018-04-26T14:05:06.842",
             "name": "List of Users",
             "realm": "genny"
           }
	
	]
}
```




