# LTA DataMall API User Guide

*An LTA Open Data Initiative — Version 6.11, 30 Oct 2026*

**Document Change Log ****Version ** **Change Details ****No. **

1.1 First release of document, reflecting specifications for each dataset.

1.2 Amended attributes for all datasets, and added the update frequency for

each dataset in specification section.

1.3 Inserted notes to denote fields that are new and upcoming; not yet

available on the data feed.

1.4 Minor revisions (typo errors).

1.5 Revisions to names of datasets, and removed listing for certain attributes

that are redundant at this point.

2.0 Revised document for newly revamped DataMall.

       - New Categorisation of Datasets

       - Moved Park & Ride Location, Premium Bus Service, and Carpark Rates

to Static Datasets listed on MyTransport.SG.

2.1 Corrected reference notes for Carpark Availability and ERP Rates.

2.2 Added Bus Arrival, and Taxi Availability APIs

2.2.1 Amended Update Freqs for Bus Arrival and Taxi Availability

3.0 Bus Arrival API is now enhanced! Latest *beta* release includes:

       - Additional 3rd set of ETA information

       - Estimated location (coordinates) of buses

Look out for blue-highlights!

3.1 **Public-Transport (Bus) Related APIs are enhanced (version 2)!**-**Bus Services and ** **Bus Routes are now consolidated across **Operators, e.g. SBST routes and SMRT routes in 1 single API

       - Attributes are renamed to be more meaningful

       -**Bus Stops now include location (lat/long) coordinates **Bug for Bus Arrival #VisitNumber fixed.

3.2 Changes to Traffic Related APIs:

       - URLs changed to point to version 2 of the APIs.

       - VCCType renamed to VehicleType (ERP Rates)

       - EstimatedTime renamed to EstTime (Estimated Travel Times)

       - RoadID renamed to EventID (Road Openings and Road Works)

       - ImageURL renamed to ImageLink (Traffic Images)

       - Band renamed to SpeedBand (Traffic Speed Bands)

3.3 Changes to API Response Size:

       -**Taxi Availability API now returns 500 records per call. **-**Traffic Images API now returns 70 records per call. **

       - Changes are reflected on Page 6, and on respective API URLs.

3.4 Changes to API authentication – now requiring only AccountKey.

|Version<br>No.|Change Details|Release Date|
|---|---|---|
|1.1|First release of document, reflecting specifications for each dataset.|04 Jun 2014|
|1.2|Amended attributes for all datasets, and added the update frequency for<br>each dataset in specification section.|15 Jun 2014|
|1.3|Inserted notes to denote fields that are new and upcoming; not yet<br>available on the data feed.|26 Jun 2014|
|1.4|Minor revisions (typo errors).|10 Mar 2015|
|1.5|Revisions to names of datasets, and removed listing for certain attributes<br>that are redundant at this point.|07 Apr 2015|
|2.0|Revised document for newly revamped DataMall.<br>• New Categorisation of Datasets<br>• Moved Park & Ride Location, Premium Bus Service, and Carpark Rates<br>to Static Datasets listed on MyTransport.SG.|13 Apr 2015|
|2.1|Corrected reference notes for Carpark Availability and ERP Rates.|14 Apr 2015|
|2.2<br>2.2.1|Added Bus Arrival, and Taxi Availability APIs<br>Amended Update Freqs for Bus Arrival and Taxi Availability|19 Apr 2015<br>03 Jun 2015|
|3.0|Bus Arrival API is now enhanced! Latest**beta** release includes:<br>• Additional 3rd set of ETA information<br>• Estimated location (coordinates) of buses<br>Look out for blue-highlights!|12 Dec 2015|
|3.1|**Public-Transport (Bus) Related APIs**are enhanced (version 2)!<br>•**Bus Services** and**Bus Routes**are now consolidated across<br>Operators, e.g. SBST routes and SMRT routes in 1 single API<br>• Attributes are renamed to be more meaningful<br>•**Bus Stops** now include location (lat/long) coordinates<br>Bug for Bus Arrival #VisitNumber fixed.|08 Mar 2016|
|3.2|Changes to**Traffic Related APIs**:<br>• URLs changed to point to version 2 of the APIs.<br>• VCCType renamed to VehicleType (ERP Rates)<br>• EstimatedTime renamed to EstTime (Estimated Travel Times)<br>• RoadID renamed to EventID (Road Openings and Road Works)<br>• ImageURL renamed to ImageLink (Traffic Images)<br>• Band renamed to SpeedBand (Traffic Speed Bands)|31 Mar 2016|
|3.3|Changes to**API Response Size:**<br>•**Taxi Availability API**now returns 500 records per call.<br>•**Traffic Images API**now returns 70 records per call.<br>• Changes are reflected on Page 6, and on respective API URLs.|08 Aug 2016|
|3.4|Changes to API authentication – now requiring only AccountKey.|01 Nov 2016|

3.5 Updated attribute description for location coordinates of **API. **3.6 **Traffic Images API now returns all records per call. **3.7 Updated guide to making API calls, using Postman.

4.0 **Bus Arrival API is now enhanced! Latest release includes:**- New Attribute – Bus Type

       - Inclusion of Short Working Trip (SWT) Supplementary Services

       - Relegation of OriginCode and DestinationCode to vehicle level

       - Removal of entire response structure from API during non
operating hours

       - Removal of Status Attribute

       - Renaming of values for Load Attribute

       - Renaming of SubsequentBus and SubsequentBus3 subset tags

       - Renaming of BusStopID Parameter to BusStopCode

       - Removal of SST Parameter. Timestamps are now in SST by default.

       - Rehashed advisement on Front-End Implementation for clarity.

4.1 Minor revisions to sample Bus Arrival API response.

4.2 Announcement on Changes to API Response Size is reflected on

4.3 Deployment date has postponed for the increase of

Please refer to Page 6 for the latest announcement.

4.4 **Response Size for all APIs (except Bus Arrival API) have been increased **to 500 records per call.

4.5 **Carpark Availability API is now enhanced! Latest release includes:**- Includes HDB, LTA and URA carpark availability data

       - New Attribute – Lot Type, Agency

       - Combined Attribute: Location

(previously Latitude and Longitude attributes)

4.6 New Train Service Alerts API is launched! It returns detailed information

on train service unavailability during scheduled operating hours, such as

affected Line and Stations etc.

4.7 **4 New Passenger Volume APIs are launched! Aggregated passenger **volume information such as number of trips, tap in and out by weekdays

and weekends (inclusive of holidays) are returned.

       - By Bus Stops

       - By Origin-Destination Bus Stops

       - By Origin-Destination Train Stations

       - By Train Stations

Sample output for Train Service Alerts API has been changed to Annex C.

4.8 **Traffic Speed Band API is now enhanced! Latest release includes:**

       - Speeds are classified into 8 bands at 10km/h interval.

|3.5|Updated attribute description for location coordinates of Bus Arrival<br>API.|23 Nov 2016|
|---|---|---|
|3.6|**Traffic Images API** now returns all records per call.|14 Dec 2016|
|3.7|Updatedguide to making API calls, using Postman.|05 Apr 2017|
|4.0|**Bus Arrival API** is now enhanced! Latest release includes:<br>• New Attribute – Bus Type<br>• Inclusion of Short Working Trip (SWT) Supplementary Services<br>• Relegation of OriginCode and DestinationCode to vehicle level<br>• Removal of entire response structure from API during non-<br>operating hours<br>• Removal of Status Attribute<br>• Renaming of values for Load Attribute<br>• Renaming of SubsequentBus and SubsequentBus3 subset tags<br>• Renaming of BusStopID Parameter to BusStopCode<br>• Removal of SST Parameter. Timestamps are now in SST by default.<br>• Rehashed advisement on Front-End Implementation for clarity.|28 Jul 2017|
|4.1|Minor revisions to sample Bus Arrival API response.|08 Sep 2017|
|4.2|Announcement on Changes to**API Response Size**is reflected on Page 6.|15 Sep 2017|
|4.3|Deployment date has postponed for the increase of**API Response Size.**<br>Please refer to Page 6 for the latest announcement.|06 Oct 2017|
|4.4|**Response Size for all APIs** (except Bus Arrival API) have been increased<br>to 500 records per call.|16 Oct 2017|
|4.5|**Carpark Availability API**is now enhanced! Latest release includes:<br>• Includes HDB, LTA and URA carpark availability data<br>• New Attribute – Lot Type, Agency<br>• Combined Attribute: Location<br>       (previously Latitude and Longitude attributes)|22 Jan 2018<br>(Soft released on<br>31 Dec 2017)|
|4.6|New**Train Service Alerts API** is launched! It returns detailed information<br>on train service unavailability during scheduled operating hours, such as<br>affected Line and Stations etc.|19 Mar 2018|
|4.7|**4 New Passenger Volume APIs** are launched! Aggregated passenger<br>volume information such as number of trips, tap in and out by weekdays<br>and weekends (inclusive of holidays) are returned.<br>• By Bus Stops<br>• By Origin-Destination Bus Stops<br>• By Origin-Destination Train Stations<br>• By Train Stations<br>Sample output for Train Service Alerts API has been changed to Annex C.|<br>17 Jul 2018|
|4.8|**Traffic Speed Band API**is now enhanced! Latest release includes:<br>• Speeds are classified into 8 bands at 10km/h interval.|21 Sep 2018|

4.9 **Bicycle Parking is launched! This API returns the information of bicycle **parking locations within a radius.

5.0 **Taxi Stands is launched! This API returns the detailed information of Taxi **facility locations.

5.1 **Traffic Images API is updated! Image links will be valid for 5 mins only. ****Geospatial Whole Island API is launched! It returns the SHP files of the **requested geospatial layer.

Added:

       -**ANNEX D (ZONE ID ATTRIBUTE TO SPECIFIC ERP GANTRY/GANTRIES **FOR 2.13 ERP RATES)

       -**ANNEX E (GEOSPATIAL WHOLE ISLAND LAYER ID FOR 2.23 **GEOSPATIAL WHOLE ISLAND)

5.2 **Facilities Maintenance **is launched! This API returns information on

Facilities Maintenance schedule for elevators in MRT station

5.3 **ANNEX E is updated, **Cycling Path Construction geospatial whole

island layer has been removed from Geospatial Whole Island API

5.4 **2 New Platform Crowd Density APIs **are launched! These two APIs

return real-time and forecasted platform crowdedness information for

the MRT/LRT stations of a train network line.

5.5 **Traffic Flow API **is launched! This API returns hourly average traffic

volume.

       - Added:**ANNEX F (DESCRIPTION OF ROAD CATEGORIES FOR **TRAFFIC FLOW)**Traffic Speed Band API **is now enhanced (version 3)! Latest release

includes:

       - Includes timestamp for last updated time

       - Split Attributes: StartLon, StartLat, EndLon, EndLat

(Previously Location attribute)

Minor revisions to Geospatial Whole Island API response.

Updated guide to generate Code Snippet using Postman.

5.5.1 **Road Openings API is renamed **to **Planned Road Openings API. ****Road Works API is renamed **to **Approved Road Works ** **API. **API endpoints remain unchanged.

6.0 **HTTPS is now supported for all APIs. ****Bus Arrival API is now enhanced (version 3)! Latest release includes:**- New attribute - Monitored **ANNEX G (LOCATION DESCRIPTION OF CAMERA ID FOR TRAFFIC **IMAGES) is added.

6.1 **ERP Rates API is removed. **

|4.9|Bicycle Parking is launched! This API returns the information of bicycle<br>parking locations within a radius.|11 Feb 2019|
|---|---|---|
|5.0|**Taxi Stands**is launched! This API returns the detailed information of Taxi<br>facility locations.|10 Jan 2020|
|5.1|**Traffic Images API** is updated! Image links will be valid for 5 mins only.<br>**Geospatial Whole Island API**is launched! It returns the SHP files of the<br>requested geospatial layer.<br>Added:<br>•**ANNEX D**(ZONE ID ATTRIBUTE TO SPECIFIC ERP GANTRY/GANTRIES<br>FOR 2.13 ERP RATES)<br>•**ANNEX E** (GEOSPATIAL WHOLE ISLAND LAYER ID FOR 2.23<br>GEOSPATIAL WHOLE ISLAND)|01 Apr 2020|
|5.2|**Facilities Maintenance**is launched! This API returns information on<br>Facilities Maintenance schedule for elevators in MRT station|28 May 2020|
|5.3|**ANNEX E** is updated,Cycling Path Construction geospatial whole<br>island layer has been removed from**Geospatial Whole Island API**.|19 Jan 2021|
|5.4|**2 New Platform Crowd Density APIs**are launched! These two APIs<br>return real-time and forecasted platform crowdedness information for<br>the MRT/LRT stations of a train network line.|02 Nov 2021|
|5.5<br>5.5.1|**Traffic Flow API**is launched! This API returns hourly average traffic<br>volume.<br>• Added:**ANNEX F** (DESCRIPTION OF ROAD CATEGORIES FOR<br>TRAFFIC FLOW)<br>**Traffic Speed Band API**is now enhanced (version 3)! Latest release<br>includes:<br>• Includes timestamp for last updated time<br>• Split Attributes: StartLon, StartLat, EndLon, EndLat<br> (Previously Location attribute)<br>Minor revisions to**Geospatial Whole Island** API response.<br>Updated guide to generate**Code Snippet**using Postman. <br>**Road Openings API**is renamed to:**Planned Road Openings API.**<br>**Road Works API**is renamed to:**Approved Road Works** **API.**<br>API endpoints remain unchanged.|04 Apr 2023<br>15 Mar 2024|
|6.0|**HTTPS is now supported for all APIs.**<br>**Bus Arrival API**is now enhanced (version 3)! Latest release includes:<br>• New attribute - Monitored<br>**ANNEX G** (LOCATION DESCRIPTION OF CAMERA ID FOR TRAFFIC<br>IMAGES) is added.|22 Aug 2024|
|6.1|**ERP Rates API**is removed.|30 Sep 2024|

You may now refer to ERP Rates static dataset on DataMall portal.

6.1.1 Previous month data of 4 Passenger Volume APIs

on 10th of the month.

6.2 **Bus Arrival API is now enhanced! Latest release includes:**- Update Frequency is changed to 20 seconds **Platform Crowd Density Real Time API is renamed **to **Density Real Time API. ****Platform Crowd Density Forecast API **is renamed to **Density Forecast ** **API. **API endpoints remain unchanged. **TEL data is now supported for Station Crowd Density APIs. **6.3 New Facilities Maintenance API (version 2) is launched! This API returns

information on adhoc lift maintenance in MRT stations. **Planned Bus Routes API is launched! This API provides planned **new/updated bus routes data in advance. Please only release the data in

your apps on/after the effective date.

6.4 New Traffic Speed Bands API (version 4) is launched! The values of

LinkID and RoadCategory are updated.

6.5 New EV Charging Points API is launched! This API

vehicle charging points in Singapore and their availabilities by Postal Code.

6.6 New **Flood Alerts API is launched! This API returns flood alert **information across Singapore, provided by PUB.

Minor revisions to Train Service Alerts API response.

6.7 New **EV Charging Points Batch API is launched! This API returns all **electric vehicle charging points in Singapore and their availabilities in a

single file.

6.8 **Bus Services API and Bus Stops API are enhanced. **Optional query parameters are now supported to filter by specific bus

service and specific bus stop respectively.

6.9 **3 New GTFS Schedule and Realtime APIs ** are launched! These three

APIs return train static schedule, real-time train service alerts and real time trip updates during train disruption in GTFS format.

6.10 New Faulty Traffic Lights API (version 2) is launched! XCoordinate and

YCoordinate are added.

|6.1.1|You may now refer to ERP Rates static dataset on DataMall portal.<br>Previous month data of 4 Passenger Volume APIs is now generated<br>on 10th of the month.|09 Oct 2024|
|---|---|---|
|6.2|**Bus Arrival API**is now enhanced! Latest release includes:<br>• Update Frequency is changed to 20 seconds<br>**Platform Crowd Density Real Time API**is renamed to:**Station Crowd**<br>**Density Real Time API.**<br>**Platform Crowd Density Forecast API**is renamed to:**Station Crowd**<br>**Density Forecast** **API.**<br>API endpoints remain unchanged.<br>**TEL** data is now supported for**Station Crowd Density APIs**.|21 Nov 2024|
|6.3|New** Facilities Maintenance API**(version 2) is launched! This API returns<br>information on adhoc lift maintenance in MRT stations.<br>**Planned Bus Routes API** is launched! This API provides planned<br>new/updated bus routes data in advance. Please only release the data in<br>your apps on/after the effective date.|10 Jul 2025|
|6.4|New** Traffic Speed Bands API**(version 4) is launched! The values of<br>LinkID and RoadCategory are updated.|20 Jul 2025|
|6.5|New** EV Charging Points API**is launched! This APIreturns electric<br>vehicle charging points in Singapore and their availabilities by Postal<br>Code.|03 Nov 2025|
|6.6|New**Flood Alerts API** is launched! This API returns flood alert<br>information across Singapore, provided by PUB.<br>Minor revisions to**Train Service Alerts API** response.|12 Jan 2026|
|6.7|New**EV Charging Points Batch API** is launched! This API returns all<br>electric vehicle charging points in Singapore and their availabilities in a<br>single file.|5 Feb 2026|
|6.8|**Bus Services API**and** Bus Stops API**are enhanced. <br>Optional query parameters are now supported to filter by specific bus<br>service and specific bus stop respectively.|21 Apr 2026|
|6.9|**3 New GTFS Schedule and Realtime APIs**are launched! These three<br>APIs return train static schedule, real-time train service alerts and real-<br>time trip updates during train disruption in GTFS format.|3 Aug 2026|
|6.10|New** Faulty Traffic Lights API**(version 2) is launched! XCoordinate and<br>YCoordinate are added.|1 Oct 2026|

**ANNEX G (LOCATION DESCRIPTION OF CAMERA ID FOR TRAFFIC **

IMAGES) is updated.

6.11 New Bicycle Parking API (version 3) is launched! Shared_Bicycle_Parking

and Type are added.

|Col1|ANNEX G (LOCATION DESCRIPTION OF CAMERA ID FOR TRAFFIC<br>IMAGES) is updated.|Col3|
|---|---|---|
|6.11|New** Bicycle Parking API**(version 3) is launched! Shared_Bicycle_Parking<br>and Type are added.|30 Oct 2026|

**TABLE OF CONTENTS **1. MAKING API CALLS ...................................................................................................................... 8

2. API DOCUMENTATION .............................................................................................................. 12

2.1 BUS ARRIVAL ..................................................................................................................... 14

2.2 BUS SERVICES .................................................................................................................... 21

2.3 BUS ROUTES ...................................................................................................................... 23

2.4 BUS STOPS ......................................................................................................................... 24

2.5 PASSENGER VOLUME BY BUS STOPS ............................................................................. 25

2.6 PASSENGER VOLUME BY ORIGIN DESTINATION BUS STOPS .................................... 26

2.7 PASSENGER VOLUME BY ORIGIN DESTINATION TRAIN STATIONS .......................... 27

2.8 PASSENGER VOLUME BY TRAIN STATIONS .................................................................. 28

2.9 TAXI AVAILABILITY ............................................................................................................ 29

2.10 TAXI STANDS ..................................................................................................................... 30

2.11 TRAIN SERVICE ALERTS .................................................................................................... 31

2.12 CARPARK AVAILABILITY ................................................................................................... 33

2.13 ESTIMATED TRAVEL TIMES .............................................................................................. 34

2.14 FAULTY TRAFFIC LIGHTS .................................................................................................. 35

2.15 PLANNED ROAD OPENINGS............................................................................................ 36

2.16 APPROVED ROAD WORKS ............................................................................................... 37

2.17 TRAFFIC IMAGES ............................................................................................................... 38

2.18 TRAFFIC INCIDENTS .......................................................................................................... 39

2.19 TRAFFIC SPEED BANDS .................................................................................................... 40

2.20 VMS / EMAS ....................................................................................................................... 42

2.21 BICYCLE PARKING ............................................................................................................. 43

2.22 GEOSPATIAL WHOLE ISLAND .......................................................................................... 44

2.23 FACILITIES MAINTENANCE .............................................................................................. 45

2.24 STATION CROWD DENSITY REAL TIME.......................................................................... 46

2.25 STATION CROWD DENSITY FORECAST .......................................................................... 47

2.26 TRAFFIC FLOW ................................................................................................................... 48

2.27 PLANNED BUS ROUTES .................................................................................................... 49

2.28 ELECTRIC VEHICLE CHARGING POINTS ......................................................................... 50

2.29 ELECTRIC VEHICLE CHARGING POINTS BATCH ............................................................ 53

2.30 FLOOD ALERTS .................................................................................................................. 54

2.31 GTFS SCHEDULE (TRAIN) .................................................................................................. 56

2.32 GTFS REALTIME (TRAIN SERVICE ALERTS) ..................................................................... 57

2.33 GTFS REALTIME (TRAIN TRIP UPDATES - DISRUPTION) .............................................. 58

ANNEX A .......................................................................................................................................... 59

ANNEX B .......................................................................................................................................... 60

ANNEX C .......................................................................................................................................... 61

ANNEX D .......................................................................................................................................... 77

ANNEX E .......................................................................................................................................... 80

ANNEX F .......................................................................................................................................... 81

ANNEX G .......................................................................................................................................... 82

## 1. MAKING API CALLS

API calls need to be made programmatically in regular intervals to obtain the constant stream

of data for your respective development or research needs. For illustration purposes, the API

call below is being made via a third-party application – Postman.

Steps to making an API call:

1. [Download and install the Postman from https://www.getpostman.com/. Fire it up!](https://www.getpostman.com/)

2. Make sure Https method is set to GET.

_3._ Enter the URL (refer to subsequent pages in this document) in the field request URL.

4. Enter your AccountKey under Headers.

5. **(OPTIONAL STEP) The “accept” header allows you to specify the response format of **your API call. Default is JSON. Specify “application/atom+xml” for XML.

6. Click on the Send button. **3 ****6 ****4 **
**5 **_Figure 2-1_

8 **3 ****6 ****4 **
**5 **Figure 2-2 below shows the JSON response of an API call made for the Traffic Incidents dataset.

_Figure 2-2: API (JSON) Response as shown on Postman._

With the exception of the following Bus Arrival API listed below (see Table 1), API responses

returned are limited to 500 records of the dataset per call. This number may be adjusted from

time to time.

To retrieve subsequent records of the dataset, you need to append the $skip operator to the

API call (URL). For example, to retrieve the next 500 records (501st to the 1000th), the API call

should be:

_https://datamall2.mytransport.sg/ltaodataservice/BusRoutes?$skip=500_

To retrieve the following set of 500 records, append ‘?$skip=1000’, and so on. Just remember,

each URL call returns only a max of 500 records!**API ** **Response Size **Bus Arrival Not Applicable. Depends on parameter supplied.
Train Service Alerts Not Applicable. Depends on the scenario.
Passenger Volume related Returns one record per request.
Taxi Stands Not Applicable. Dataset is too small.

_Table 1: API Response Size_

|API|Response Size|
|---|---|
|Bus Arrival|Not Applicable. Depends onparameter supplied.|
|Train Service Alerts|Not Applicable. Depends on the scenario.|
|Passenger Volume related|Returns one recordper request.|
|Taxi Stands|Not Applicable. Dataset is too small.|

Following is a guide on how you can generate sample code snippets from Postman.

1. After setting up on Postman to make an API call as per the steps in Figure 2-1, select

the code icon </> in the right panel of the Postman application.

_Figure 2-3_

2. Use the dropdown list to select the code snippet in the desired programming language.

_Figure 2-4_

3. Code snippet will be automatically generated in the chosen programming language.

_Figure 2-5_

## 2. API DOCUMENTATION

The following lists all real-time / dynamic datasets that are refreshed at regular intervals and

served out via APIs. Specification for each API can be found in the rest of this document.

_Note: any attributes not specified in this document but found on the data feed, should be ignored._**Public-Transport Related (Total **
**Description **18)

Returns real-time Bus Arrival information for Bus Services at a

1 Bus Arrival queried Bus Stop, including: Estimated Time of Arrival (ETA),

Estimated Location, Load info (i.e. how crowded the bus is).

Returns detailed service information for all buses currently in

2 Bus Services operation, including:

first stop, last stop, peak / offpeak frequency of dispatch.

Returns detailed route information for all services currently in

3 Bus Routes operation, including:

all bus stops along each route, first/last bus timings for each stop.

Returns detailed information for all bus stops currently being 4 Bus Stops serviced by buses, including: Bus Stop Code, location coordinates.

Returns tap in and tap out passenger volume by weekdays and 5 Passenger Volume by Bus Stops weekends for individual bus stop.

Passenger Volume by Origin Returns number of trips by weekdays and weekends from the 6
Destination Bus Stops origin to destination bus stops.

Passenger Volume by Origin Returns number of trips by weekdays and weekends from the 7
Destination Train Stations origin to destination train stations.

Returns tap in and tap out passenger volume by weekdays and 8 Passenger Volume by Train Stations weekends for individual train station.

Returns location coordinates of all Taxis that are currently 9 Taxi Availability available for hire. Does not include "Hired" or "Busy" Taxis.

Returns detailed information of Taxi stands, such as location and 10 Taxi Stands whether is it barrier free

Returns detailed information on train service unavailability during 11 Train Service Alerts scheduled operating hours, such as affected line and stations etc.

12 Facilities Maintenance Returns adhoc lift maintenance in MRT stations

Returns real-time MRT/LRT station crowdedness level of a 13 Station Crowd Density Real-time particular train network line

Returns forecasted MRT/LRT station crowdedness level of a 14 Station Crowd Density Forecast particular train network line at 30 minutes interval

15 Planned Bus Routes Returns planned new/updated bus routes information.

16 GTFS Schedule (Train) Returns the planned transit network.

Returns real-time information on service disruptions, 17 GTFS Realtime (Train Service Alerts) maintenance, and passenger advisories.

GTFS Realtime (Train Trip Updates - Returns real-time arrival/departure predictions, delays, 18
Disruption) cancellations, and skipped stops for scheduled trips.

|Col1|Public-Transport Related (Total<br>18)|Description|
|---|---|---|
|1|Bus Arrival|Returns real-time Bus Arrival information for Bus Services at a<br>queried Bus Stop, including: Estimated Time of Arrival (ETA),<br>Estimated Location, Load info(i.e. how crowded the bus is).|
|2|Bus Services|Returns detailed service information for all buses currently in<br>operation, including:<br>first stop, last stop, peak/ offpeak frequency of dispatch.|
|3|Bus Routes|Returns detailed route information for all services currently in<br>operation, including:<br>all bus stops along each route, first/last bus timings for each stop.|
|4|Bus Stops|Returns detailed information for all bus stops currently being<br>serviced by buses, including: Bus Stop Code, location coordinates.|
|5|Passenger Volume by Bus Stops|Returns tap in and tap out passenger volume by weekdays and<br>weekends for individual bus stop.|
|6|Passenger Volume by Origin<br>Destination Bus Stops|Returns number of trips by weekdays and weekends from the<br>origin to destination bus stops.|
|7|Passenger Volume by Origin<br>Destination Train Stations|Returns number of trips by weekdays and weekends from the<br>origin to destination train stations.|
|8|Passenger Volume by Train Stations|Returns tap in and tap out passenger volume by weekdays and<br>weekends for individual train station.|
|9|Taxi Availability|Returns location coordinates of all Taxis that are currently<br>available for hire. Does not include "Hired" or "Busy" Taxis.|
|10|Taxi Stands|Returns detailed information of Taxi stands, such as location and<br>whether is it barrier free|
|11|Train Service Alerts|Returns detailed information on train service unavailability during<br>scheduled operating hours, such as affected line and stations etc.|
|12|Facilities Maintenance|Returns adhoc lift maintenance in MRT stations|
|13|Station Crowd Density Real-time|Returns real-time MRT/LRT station crowdedness level of a<br>particular train network line|
|14|Station Crowd Density Forecast|Returns forecasted MRT/LRT station crowdedness level of a<br>particular train network line at 30 minutes interval|
|15|Planned Bus Routes|Returns planned new/updated bus routes information.|
|16|GTFS Schedule (Train)|Returns the planned transit network.|
|17|GTFS Realtime (Train Service Alerts)|Returns real-time information on service disruptions,<br>maintenance, and passenger advisories.|
|18|GTFS Realtime (Train Trip Updates -<br>Disruption)|Returns real-time arrival/departure predictions, delays,<br>cancellations, and skipped stops for scheduled trips.|**Traffic Related**(Total 11)**Description**Returns no. of available lots for HDB, LTA and URA carpark
data.

19 Carpark Availability The LTA carpark data consist of major shopping malls and

developments within Orchard, Marina, HarbourFront, Jurong Lake District.

20 Estimated Travel Times Returns estimated travel times of expressways (in segments).

Returns alerts of traffic lights that are currently faulty, or currently 21 Faulty Traffic Lights undergoing scheduled maintenance.

22 Planned Road Openings Information on planned road openings.

Information on approved road works to be carried out/being 23 Approved Road Works carried out.

Returns links to images of live traffic conditions along

24 Traffic Images expressways and Woodlands & Tuas Checkpoints.

Returns incidents currently happening on the roads, such as

25 Traffic Incidents Accidents, Vehicle Breakdowns, Road Blocks, Traffic Diversions

etc.

Returns current traffic speeds on expressways and arterial roads, 26 Traffic Speed Bands expressed in speed bands.

Returns traffic advisories (via variable message services)

27 VMS / EMAS concerning current traffic conditions that are displayed on EMAS

signboards along expressways and arterial roads.

28 Traffic Flow Returns hourly average traffic flow.

Returns flood alert information across Singapore, provided by 29 Flood Alerts PUB. **Active Mobility Related **(Total 1)**Description **30 Bicycle Parking Returns the bicycle parking locations within a radius. **Geospatial Related (Total 1)** **Description **31 Geospatial Whole Island Returns the SHP files of the requested geospatial layer **Electric Vehicle Related (Total 2)** **Description **

Returns electric vehicle charging points in Singapore and their 32 EV Charging Points availabilities by Postal Code.

Returns all electric vehicle charging points in Singapore and their 33 EV Charging Points Batch availabilities in a single file.

|Col1|Col2|Col3|
|---|---|---|
||**Traffic Related** (Total 11)|**Description**|
|19|Carpark Availability|Returns no. of available lots for HDB, LTA and URA carpark<br>data.<br>The LTA carpark data consist of major shopping malls and<br>developments within Orchard, Marina, HarbourFront,<br>Jurong Lake District.|
|20|Estimated Travel Times|Returns estimated travel times of expressways (in segments).|
|21|Faulty Traffic Lights|Returns alerts of traffic lights that are currently faulty, or currently<br>undergoing scheduled maintenance.|
|22|Planned Road Openings|Information on planned road openings.|
|23|Approved Road Works|Information on approved road works to be carried out/being<br>carried out.|
|24|Traffic Images|Returns links to images of live traffic conditions along<br>expressways and Woodlands & Tuas Checkpoints.|
|25|Traffic Incidents|Returns incidents currently happening on the roads, such as<br>Accidents, Vehicle Breakdowns, Road Blocks, Traffic Diversions<br>etc.|
|26|Traffic Speed Bands|Returns current traffic speeds on expressways and arterial roads,<br>expressed in speed bands.|
|27|VMS / EMAS|Returns traffic advisories (via variable message services)<br>concerning current traffic conditions that are displayed on EMAS<br>signboards along expressways and arterial roads.|
|28|Traffic Flow|Returns hourly average traffic flow.|
|29|Flood Alerts|Returns flood alert information across Singapore, provided by<br>PUB.|
||||
||**Active Mobility Related** (Total 1)|**Description**|
|30|Bicycle Parking|Returns the bicycle parking locations within a radius.|
||||
||**Geospatial Related**(Total 1)|**Description**|
|31|Geospatial Whole Island|Returns the SHP files of the requested geospatial layer|
||||
||**Electric Vehicle Related**(Total 2)|**Description**|
|32|EV Charging Points|Returns electric vehicle charging points in Singapore and their<br>availabilities by Postal Code.|
|33|EV Charging Points Batch|Returns all electric vehicle charging points in Singapore and their<br>availabilities in a single file.|

### 2.1 BUS ARRIVAL

**URL **https://datamall2.mytransport.sg/ltaodataservice/v3/BusArrival

Returns real-time Bus Arrival information of Bus Services at a queried Bus Stop, **Description **including Est. Arrival Time, Est. Current Location, Est. Current Load. **Update Freq **20 seconds **Request ****Parameters ** **Description ** **Mandatory **BusStopCode Bus stop reference code Yes ServiceNo Bus service number No _15_**Response ****Attributes ** **Description **
ServiceNo Bus service number _15_
Operator Public Transport Operator Codes: _GAS_

                 - SBST (for SBS Transit)

                 - SMRT (for SMRT Corporation)

                 - TTS (for Tower Transit Singapore)

                 - GAS (for Go Ahead Singapore)

NextBus Structural tags for all bus level attributes^ of the next 3 oncoming buses. Note that if NextBus2 there is only one last bus left on the roads (e.g. at night), attributes values in NextBus3 NextBus2 and NextBus3 will be empty / blank.
^ OriginCode Reference code of the first bus stop where this bus started its service

^ DestinationCode Reference code of the last bus stop where this bus will terminate its service

^ EstimatedArrival Date-time of this bus’ estimated time of arrival, expressed in the UTC standard, GMT+8 for Singapore Standard Time (SST)

^ Monitored Indicates if the bus arrival time is based on the _1_ schedule from operators.

                 - 0 (Value from EstimatedArrival is
based on schedule)

                 - 1 (Value from EstimatedArrival is
estimated based on bus location)

^ Latitude Current estimated location coordinates of this bus at point of published data

^ Longitude

^ VisitNumber Ordinal value of the nth visit of this vehicle at _1_ this bus stop; 1=1st visit, 2=2nd visit

^ Load Current bus occupancy / crowding level: _SEA_

                 - SEA (for Seats Available)

                 - SDA (for Standing Available)

                 - LSD (for Limited Standing)

^ Feature Indicates if bus is wheel-chair accessible: _WAB_

                 - WAB

                 - (empty / blank)

^ Type Vehicle type: _SD_

                 - SD (for Single Deck)

                 - DD (for Double Deck)

                 - BD (for Bendy)

|URL|https://datamall2.mytransport.sg/ltaodataservice/v3/BusArrival|Col3|Col4|
|---|---|---|---|
|**Description**|Returns real-time Bus Arrival information of Bus Services at a queried Bus Stop,<br>including Est. Arrival Time, Est. Current Location, Est. Current Load.|Returns real-time Bus Arrival information of Bus Services at a queried Bus Stop,<br>including Est. Arrival Time, Est. Current Location, Est. Current Load.|Returns real-time Bus Arrival information of Bus Services at a queried Bus Stop,<br>including Est. Arrival Time, Est. Current Location, Est. Current Load.|
|**Update Freq**|20 seconds|20 seconds|20 seconds|
|**Request**|**Request**|**Request**|**Request**|
|**Parameters**|**Description**|**Mandatory:**|**Example**|
|BusStopCode|Bus stop reference code|Yes|_83139_|
|ServiceNo|Bus service number|No|_15_|
|**Response**|**Response**|**Response**|**Response**|
|**Attributes**|**Description**|**Description**|**Example**|
|ServiceNo|Bus service number|Bus service number|_15_|
|Operator|Public Transport Operator Codes:<br>• SBST (for SBS Transit)<br>• SMRT (for SMRT Corporation)<br>• TTS (for Tower Transit Singapore)<br>• GAS(for Go Ahead Singapore)|Public Transport Operator Codes:<br>• SBST (for SBS Transit)<br>• SMRT (for SMRT Corporation)<br>• TTS (for Tower Transit Singapore)<br>• GAS(for Go Ahead Singapore)|_GAS_|
|NextBus|Structural tags for all bus level attributes^ of the next 3 oncoming buses. Note that if<br>there is only one last bus left on the roads (e.g. at night), attributes values in<br>NextBus2 and NextBus3 will be empty / blank.|Structural tags for all bus level attributes^ of the next 3 oncoming buses. Note that if<br>there is only one last bus left on the roads (e.g. at night), attributes values in<br>NextBus2 and NextBus3 will be empty / blank.|Structural tags for all bus level attributes^ of the next 3 oncoming buses. Note that if<br>there is only one last bus left on the roads (e.g. at night), attributes values in<br>NextBus2 and NextBus3 will be empty / blank.|
|NextBus2|NextBus2|NextBus2|NextBus2|
|NextBus3|NextBus3|NextBus3|NextBus3|
|^ OriginCode|Reference code of the first bus stop where this<br>bus started its service|Reference code of the first bus stop where this<br>bus started its service|_77009_|
|^ DestinationCode|Reference code of the last bus stop where this<br>bus will terminate its service|Reference code of the last bus stop where this<br>bus will terminate its service|_77131_|
|^ EstimatedArrival|Date-time of this bus’ estimated time of arrival,<br>expressed in the UTC standard, GMT+8 for<br>Singapore Standard Time(SST)|Date-time of this bus’ estimated time of arrival,<br>expressed in the UTC standard, GMT+8 for<br>Singapore Standard Time(SST)|_2017-04-29T07:20:24+08:00_|
|^ Monitored|Indicates if the bus arrival time is based on the<br>schedule from operators.<br>• 0 (Value from EstimatedArrival is<br>based on schedule)<br>• 1 (Value from EstimatedArrival is<br>estimated based on bus location)|Indicates if the bus arrival time is based on the<br>schedule from operators.<br>• 0 (Value from EstimatedArrival is<br>based on schedule)<br>• 1 (Value from EstimatedArrival is<br>estimated based on bus location)|_1 _|
|^ Latitude|Current estimated location coordinates of this<br>bus at point of published data|Current estimated location coordinates of this<br>bus at point of published data|_1.42117943692586_|
|^ Longitude|^ Longitude|^ Longitude|_103.831477233098_|
|^ VisitNumber|Ordinal value of the nth visit of this vehicle at<br>this bus stop; 1=1st visit, 2=2nd visit|Ordinal value of the nth visit of this vehicle at<br>this bus stop; 1=1st visit, 2=2nd visit|_1 _|
|^ Load|Current bus occupancy / crowding level:<br>• SEA (for Seats Available)<br>• SDA (for Standing Available)<br>• LSD(for Limited Standing)|Current bus occupancy / crowding level:<br>• SEA (for Seats Available)<br>• SDA (for Standing Available)<br>• LSD(for Limited Standing)|_SEA_|
|^ Feature|Indicates if bus is wheel-chair accessible:<br>• WAB<br>• (empty / blank)|Indicates if bus is wheel-chair accessible:<br>• WAB<br>• (empty / blank)|_WAB_|
|^ Type|Vehicle type:<br>• SD (for Single Deck)<br>• DD (for Double Deck)<br>• BD(for Bendy)|Vehicle type:<br>• SD (for Single Deck)<br>• DD (for Double Deck)<br>• BD(for Bendy)|_SD_|

Please note that Bus Arrival data (i.e. all attribute-value pairs above) will only appear on the API when the buses are in service (i.e. on the roads). When not in operation, OR when the API service is undergoing maintenance and temporarily unavailable, there will be no response returned on the API (not even the attribute tags).Please refer to Advisement Pt. 1 in following section for more.

**SAMPLE API CALL & RESPONSE ****API Call:**[https://datamall2.mytransport.sg/ltaodataservice/v3/BusArrival?BusStopCode=83139](https://datamall2.mytransport.sg/ltaodataservice/v3/BusArrival?BusStopCode=83139)**API Response:**
**{**
**"odata.metadata": "https://datamall2.mytransport.sg/ltaodataservice/v3/BusArrival", **
**"BusStopCode": "83139", **
**"Services": [**
**{**
**"ServiceNo": "15", **
**"Operator": "GAS", **
**"NextBus": {**
**"OriginCode": "77009", **
**"DestinationCode": "77009", **
**"EstimatedArrival": "2024-08-14T16:41:48+08:00", **
**"Monitored": 1, **
**"Latitude": "1.3154918333333334", **
**"Longitude": "103.9059125", **
**"VisitNumber": "1", **
**"Load": "SEA", **
**"Feature": "WAB", **
**"Type": "SD"**
**}, **
**"NextBus2": {**
**"OriginCode": "77009", **
**"DestinationCode": "77009", **
**"EstimatedArrival": "2024-08-14T16:49:22+08:00", **
**"Monitored": 1, **
**"Latitude": "1.3309621666666667", **
**"Longitude": "103.9034135", **
**"VisitNumber": "1", **
**"Load": "SEA", **
**"Feature": "WAB", **
**"Type": "SD"**
**}, **
**"NextBus3": {**
**"OriginCode": "77009", **
**"DestinationCode": "77009", **
**"EstimatedArrival": "2024-08-14T17:06:11+08:00", **
**"Monitored": 1, **
**"Latitude": "1.344761", **
**"Longitude": "103.94022316666667", **
**"VisitNumber": "1", **
**"Load": "SEA", **
**"Feature": "WAB", **
**"Type": "SD"**
**}**
**}, **15 **{**
**"ServiceNo": "150", **
**"Operator": "SBST", **
**"NextBus": {**
**"OriginCode": "82009", **
**"DestinationCode": "82009", **
**"EstimatedArrival": "2024-08-14T16:55:22+08:00", **
**"Monitored": 0, **
**"Latitude": "0.0", **
**"Longitude": "0.0", **
**"VisitNumber": "1", **
**"Load": "SEA", **
**"Feature": "WAB", **
**"Type": "SD"**
**}, **
**"NextBus2": {**
**"OriginCode": "82009", **
**"DestinationCode": "82009", **
**"EstimatedArrival": "2024-08-14T17:15:22+08:00", **
**"Monitored": 0, **
**"Latitude": "0.0", **
**"Longitude": "0.0", **
**"VisitNumber": "1", **
**"Load": "SEA", **
**"Feature": "WAB", **
**"Type": "SD"**
**}, **
**"NextBus3": {**
**"OriginCode": "", **
**"DestinationCode": "", **
**"EstimatedArrival": "", **
**"Monitored": 0, **
**"Latitude": "", **
**"Longitude": "", **
**"VisitNumber": "", **
**"Load": "", **
**"Feature": "", **
**"Type": ""**
**}**
**}, **
**{**
**"ServiceNo": "155", **
**"Operator": "SBST", **
**"NextBus": {**
**"OriginCode": "52009", **
**"DestinationCode": "84009", **
**"EstimatedArrival": "2024-08-14T16:45:23+08:00", **
**"Monitored": 1, **
**"Latitude": "1.3183185", **
**"Longitude": "103.9003205", **
**"VisitNumber": "1", **
**"Load": "SEA", **
**"Feature": "WAB", **
**"Type": "SD"**
**}, **
**"NextBus2": {**
**"OriginCode": "52009", **
**"DestinationCode": "84009", **16 **"EstimatedArrival": "2024-08-14T17:01:38+08:00", **
**"Monitored": 1, **
**"Latitude": "1.3254035", **
**"Longitude": "103.88185066666667", **
**"VisitNumber": "1", **
**"Load": "SEA", **
**"Feature": "WAB", **
**"Type": "SD"**
**}, **
**"NextBus3": {**
**"OriginCode": "52009", **
**"DestinationCode": "84009", **
**"EstimatedArrival": "2024-08-14T17:12:38+08:00", **
**"Monitored": 1, **
**"Latitude": "1.3282046666666667", **
**"Longitude": "103.8799955", **
**"VisitNumber": "1", **
**"Load": "SEA", **
**"Feature": "WAB", **
**"Type": "SD"**
**}**
**}**
**]**
**}**17 **ADVISEMENT ON FRONT-END IMPLEMENTATION (BUS APPS)****1. ** **[EstimatedArrival] Display of Advisement Messages when there is NO Bus Arrival Data **In the event where data is not available (be it in partial or in full) on the API, you may want to display

some form of ‘status texts’ to advise your app users on what’s going on, as far as bus service

availability is concerned. To do this, you will need to take reference from two data points – (1) the

presence or absence of Arrival data itself, and (2) the bus service operating hours at each bus **stop which you need to obtain via the Bus Routes API. **With those two data points gathered, you will arrive at the following possible scenarios:**#** **Operation Status ** **Data Availability ** **Advisement Message **a. Bus is in operation Arrival data is available (none required)

b. Bus is in operation Arrival data is NOT available “No Est. Available”

c. Bus is NOT in operation Arrival data is NOT available “Not In Operation”

d. Bus is NOT in operation Arrival data is available (none required)

For scenarios (b) and (c), you may display advisement messages like those suggested in the table

above, or any other user-friendly and appropriate variants at your discretion.

Next, you should note that Arrival data may be available on the API even when bus services are

supposedly NOT in operation (as per scheduled operating hours) – reflected as scenario (d) in the

table above. This happens,

a. before first bus(es) begin their service from Bus Interchanges / Depots in the mornings, and,

b. when last bus(es) at night are running behind schedule; slightly past operating hours.

Therefore, the general logic to be applied, is to always first display the Arrival data if it’s available **on the API, irrespective of the scheduled operating hours. Advisement messages like “No Est. **_Available” and “Not In Operation” are applicable ONLY when there is no Arrival data on the API._

|#|Operation Status|Data Availability|Advisement Message|
|---|---|---|---|
|a. <br>|Bus is in operation|Arrival data is available|(none required)|
|b.|Bus is in operation|Arrival data is NOT available|“_No Est. Available_”|
|c. <br>|Bus is NOT in operation|Arrival data is NOT available|“_Not In Operation_”|
|d.|Bus is NOT in operation|Arrival data is available|(none required)|**2.** **[EstimatedArrival] Rounding of Seconds**All derived bus arrival duration should be rounded down to the nearest minute.

Derived duration: 3:49 mins

Display duration: “3 min”

Derived duration: 2:07 mins

Display duration: “2 min”

Derived duration: 1:59 mins

Display duration: “1 min”

Derived duration: 0:59 mins

Display duration: “Arr”**3. ** **[Load] Colour Scheme Adoption **You may adopt this colour scheme to serve as visual indicators for the various loading values:

      - [Green] Seats Available

      - [Amber] Standing Available

      - [Red] Limited Standing

You are given the flexibility for the manner in which you display the colours, i.e. colour bars, coloured

timings, and accompanied with legends where appropriate and/or necessary. **4. ** **[Feature] Wheelchair Accessible Buses **You are given the flexibility to display any symbols or labels    to denote oncoming buses that

are wheelchair accessible. **5. ** **[Feature] Schedule Indicator **You are given the flexibility to display any symbols or labels to indicate if the bus arriving

times are based on the schedule from operators and may be subject to changes.

19 **ADDITIONAL NOTE ON LOOP SERVICES THAT RUNS BOTH DIRECTIONS **Please note that some Loop Services are appended with ‘G’ or ‘W’ to denote their direction of travel.

You should account for and display these services individually – 225G, 225W, 243G, 243W, 410G, 410W.

### 2.2 BUS SERVICES **URL **https://datamall2.mytransport.sg/ltaodataservice/BusServices

Returns detailed service information for all buses currently in **Description **operation, including: first stop, last stop, peak / offpeak frequency of

dispatch. **Update Freq **Ad hoc **Request ****Parameters ** **Description ** **Mandatory ** **Example **ServiceNo The bus service number No _107M_**Response ****Attributes ** **Description ** **Sample **

ServiceNo The bus service number _107M_

Operator Operator for this bus service _SBST_

Direction The direction in which the bus travels _1_

(1 or 2), loop services only have 1

direction

Category Category of the SBS bus service: _TRUNK_

EXPRESS, FEEDER, INDUSTRIAL,

TOWNLINK, TRUNK, 2 TIER FLAT FEE,

FLAT FEE $1.10 (or $1.90, $3.50, $3.80)

OriginCode Bus stop code for first bus stop _64009_

DestinationCode Bus stop code for last bus stop _64009_

(similar as first stop for loop services)

AM_Peak_Freq Freq of dispatch for AM Peak _14-17_

0630H - 0830H (range in minutes)

AM_Offpeak_Freq Freq of dispatch for AM Off-Peak _10-16_

0831H - 1659H (range in minutes)

PM_Peak_Freq Freq of dispatch for PM Peak _12-15_

1700H - 1900H (range in minutes)

|URL|https://datamall2.mytransport.sg/ltaodataservice/BusServices|Col3|Col4|
|---|---|---|---|
|**Description**|Returns detailed service information for all buses currently in<br>operation, including: first stop, last stop, peak / offpeak frequency of<br>dispatch.|Returns detailed service information for all buses currently in<br>operation, including: first stop, last stop, peak / offpeak frequency of<br>dispatch.|Returns detailed service information for all buses currently in<br>operation, including: first stop, last stop, peak / offpeak frequency of<br>dispatch.|
|**Update Freq**|Ad hoc|Ad hoc|Ad hoc|
|**Request**|**Request**|**Request**|**Request**|
|**Parameters**|**Description**|**Mandatory:**|**Example**|
|ServiceNo|The bus service number|No|_107M_|
|**Response**|**Response**|**Response**|**Response**|
|**Attributes**|**Description**|**Description**|**Sample**|
|ServiceNo|The bus service number|The bus service number|_107M_|
|Operator|Operator for this bus service|Operator for this bus service|_SBST_|
|Direction|The direction in which the bus travels<br>(1 or 2), loop services only have 1<br>direction|The direction in which the bus travels<br>(1 or 2), loop services only have 1<br>direction|_1 _|
|Category|Category of the SBS bus service:<br>EXPRESS, FEEDER, INDUSTRIAL,<br>TOWNLINK, TRUNK, 2 TIER FLAT FEE,<br>FLAT FEE $1.10 (or $1.90, $3.50, $3.80)|Category of the SBS bus service:<br>EXPRESS, FEEDER, INDUSTRIAL,<br>TOWNLINK, TRUNK, 2 TIER FLAT FEE,<br>FLAT FEE $1.10 (or $1.90, $3.50, $3.80)|_TRUNK_|
|OriginCode|Bus stop code for first bus stop|Bus stop code for first bus stop|_64009_|
|DestinationCode|Bus stop code for last bus stop<br>(similar as first stop for loop services)|Bus stop code for last bus stop<br>(similar as first stop for loop services)|_64009_|
|AM_Peak_Freq|Freq of dispatch for AM Peak<br>0630H - 0830H (range in minutes)|Freq of dispatch for AM Peak<br>0630H - 0830H (range in minutes)|_14-17_|
|AM_Offpeak_Freq|Freq of dispatch for AM Off-Peak<br>0831H - 1659H (range in minutes)|Freq of dispatch for AM Off-Peak<br>0831H - 1659H (range in minutes)|_10-16_|
|PM_Peak_Freq|Freq of dispatch for PM Peak<br>1700H - 1900H (range in minutes)|Freq of dispatch for PM Peak<br>1700H - 1900H (range in minutes)|_12-15_|

PM_Offpeak_Freq Freq of dispatch for PM Off-Peak _12-15_

after 1900H (range in minutes)

LoopDesc Location at which the bus service

loops, empty if not a loop service.

|PM Offpeak Freq<br>_ _|Freq of dispatch for PM Off-Peak<br>after 1900H (range in minutes)|12-15|
|---|---|---|
|LoopDesc|Location at which the bus service<br>loops, empty if not a loop service.|_Raffles Blvd_|

### 2.3 BUS ROUTES

**URL **https://datamall2.mytransport.sg/ltaodataservice/BusRoutes

Returns detailed route information for all services currently in operation, **Description **including: all bus stops along each route, first/last bus timings for each stop. **Update Freq **Ad hoc **Response ****Attributes ** **Description **

ServiceNo The bus service number _107M_

Operator Operator for this bus service _SBST_

Direction The direction in which the bus travels _1_

(1 or 2), loop services only have 1 direction

StopSequence The i-th bus stop for this route _28_

BusStopCode The unique 5-digit identifier for this _01219_

physical bus stop

Distance Distance travelled by bus from starting _10.3_

location to this bus stop (in kilometres)

WD_FirstBus Scheduled arrival of first bus on weekdays _2025_

WD_LastBus Scheduled arrival of last bus on weekdays _2352_

SAT_FirstBus Scheduled arrival of first bus on Saturdays _1427_

SAT_LastBus Scheduled arrival of last bus on Saturdays _2349_

SUN_FirstBus Scheduled arrival of first bus on Sundays _0620_

SUN_LastBus Scheduled arrival of last bus on Sundays _2349_

|URL|https://datamall2.mytransport.sg/ltaodataservice/BusRoutes|Col3|
|---|---|---|
|**Description**|Returns detailed route information for all services currently in operation,<br>including: all bus stops along each route, first/last bus timings for each stop.|Returns detailed route information for all services currently in operation,<br>including: all bus stops along each route, first/last bus timings for each stop.|
|**Update Freq**|Ad hoc|Ad hoc|
|**Response**|**Response**|**Response**|
|**Attributes**|**Description**|**Sample**|
|ServiceNo|The bus service number|_107M_|
|Operator|Operator for this bus service|_SBST_|
|Direction|The direction in which the bus travels<br>(1 or 2), loop services only have 1 direction|_1 _|
|StopSequence|The i-th bus stop for this route|_28_|
|BusStopCode|The unique 5-digit identifier for this<br>physical bus stop|_01219_|
|Distance|Distance travelled by bus from starting<br>location to this bus stop (in kilometres)|_10.3_|
|WD_FirstBus|Scheduled arrival of first bus on weekdays|_2025_|
|WD_LastBus|Scheduled arrival of last bus on weekdays|_2352_|
|SAT_FirstBus|Scheduled arrival of first bus on Saturdays|_1427_|
|SAT_LastBus|Scheduled arrival of last bus on Saturdays|_2349_|
|SUN_FirstBus|Scheduled arrival of first bus on Sundays|_0620_|
|SUN_LastBus|Scheduled arrival of last bus on Sundays|_2349_|

### 2.4 BUS STOPS

**URL **https://datamall2.mytransport.sg/ltaodataservice/BusStops

Returns detailed information for all bus stops currently being serviced by **Description **buses, including: Bus Stop Code, location coordinates. **Update Freq **Ad hoc **Request ****Parameters ** **Description ** **Mandatory ** **Example **BusStopCode The unique 5-digit No _01012_

identifier for this physical

bus stop **Response ****Attributes ** **Description ** **Sample **

BusStopCode The unique 5-digit identifier for this _01012_

physical bus stop

RoadName The road on which this bus stop is _Victoria St_

located

Description Landmarks next to the bus stop (if any)

to aid in identifying this bus stop

Latitude _1.29685_

Location coordinates for this bus stop

Longitude _103.853_

|URL|https://datamall2.mytransport.sg/ltaodataservice/BusStops|Col3|Col4|
|---|---|---|---|
|**Description**|Returns detailed information for all bus stops currently being serviced by<br>buses, including: Bus Stop Code, location coordinates.|Returns detailed information for all bus stops currently being serviced by<br>buses, including: Bus Stop Code, location coordinates.|Returns detailed information for all bus stops currently being serviced by<br>buses, including: Bus Stop Code, location coordinates.|
|**Update Freq**|Ad hoc|Ad hoc|Ad hoc|
|**Request**|**Request**|**Request**|**Request**|
|**Parameters**|**Description**|**Mandatory:**|**Example**|
|BusStopCode|The unique 5-digit<br>identifier for this physical<br>bus stop|No|_01012_|
|**Response**|**Response**|**Response**|**Response**|
|**Attributes**|**Description**|**Description**|**Sample**|
|BusStopCode|The unique 5-digit identifier for this<br>physical bus stop|The unique 5-digit identifier for this<br>physical bus stop|_01012_|
|RoadName|The road on which this bus stop is<br>located|The road on which this bus stop is<br>located|_Victoria St_|
|Description|Landmarks next to the bus stop (if any)<br>to aid in identifying this bus stop|Landmarks next to the bus stop (if any)<br>to aid in identifying this bus stop|_Hotel Grand Pacific_|
|Latitude|Location coordinates for this bus stop|Location coordinates for this bus stop|_1.29685_|
|Longitude|Longitude|Longitude|_103.853_|

### 2.5 PASSENGER VOLUME BY BUS STOPS

**URL **https://datamall2.mytransport.sg/ltaodataservice/PV/Bus

Returns tap in and tap out passenger volume by weekdays and **Description **weekends for individual bus stop

By 10th of every month, the passenger volume for previous month data **Update Freq **will be generated **Request ****Parameters ** **Description ** **Mandatory **Request for files up to Date No last three months **Response ****Attributes ** **Description **
Link - Link for downloading this file.

              - Refer to sample output on
Annex A for reference.

              - Link will expire after 15 minutes.

|URL|https://datamall2.mytransport.sg/ltaodataservice/PV/Bus|Col3|Col4|
|---|---|---|---|
|**Description**|Returns tap in and tap out passenger volume by weekdays and<br>weekends for individual bus stop|Returns tap in and tap out passenger volume by weekdays and<br>weekends for individual bus stop|Returns tap in and tap out passenger volume by weekdays and<br>weekends for individual bus stop|
|**Update Freq**|By 10th of every month, the passenger volume for previous month data<br>will begenerated|By 10th of every month, the passenger volume for previous month data<br>will begenerated|By 10th of every month, the passenger volume for previous month data<br>will begenerated|
|**Request**|**Request**|**Request**|**Request**|
|**Parameters**|**Description**|**Mandatory:**|**Example**|
|Date|Request for files up to<br>last three months|No|_Date=201803_|
|**Response**|**Response**|**Response**|**Response**|
|**Attributes**|**Description**|**Description**|**Example**|
|Link|• Link for downloading this file.<br>• Refer to sample output on<br>Annex Afor reference.<br>• Link will expire after 15 minutes.|• Link for downloading this file.<br>• Refer to sample output on<br>Annex Afor reference.<br>• Link will expire after 15 minutes.|_https://ltafarecard.s3.amazona_<br>_ws.com/201803/transport_node_<br>__bus_201803.zip?x-amz-_<br>_security-_<br>_token=FQoDYXdzEOf%2F%2F%_<br>_2F%2F%2F%2F%2F%2F%2F%..._|

### 2.6 PASSENGER VOLUME BY ORIGIN DESTINATION BUS STOPS

**URL **https://datamall2.mytransport.sg/ltaodataservice/PV/ODBus

Returns number of trips by weekdays and weekends from origin to **Description **destination bus stops

By 10th of every month, the passenger volume for previous month data **Update Freq **will be generated **Request ****Parameters ** **Description ** **Mandatory ** **Example **Request for files up to Date No _Date=201804_ last three months **Response ****Attributes ** **Description ** **Example **
Link - Link for downloading this file. _https://ltafarecard.s3.amazona_

              - Refer to sample output on _ws.com/201804/origin_destinat_
Annex B for reference. _ion_bus_201804.zip?x-amz-_

_security-_

              - Link will expire after 15 minutes.

_token=FQoDYXdzEOf%2F%2..._

|URL|https://datamall2.mytransport.sg/ltaodataservice/PV/ODBus|Col3|Col4|
|---|---|---|---|
|**Description**|Returns number of trips by weekdays and weekends from origin to<br>destination bus stops|Returns number of trips by weekdays and weekends from origin to<br>destination bus stops|Returns number of trips by weekdays and weekends from origin to<br>destination bus stops|
|**Update Freq**|By 10th of every month, the passenger volume for previous month data<br>will begenerated|By 10th of every month, the passenger volume for previous month data<br>will begenerated|By 10th of every month, the passenger volume for previous month data<br>will begenerated|
|**Request**|**Request**|**Request**|**Request**|
|**Parameters**|**Description**|**Mandatory:**|**Example**|
|Date|Request for files up to<br>last three months|No|_Date=201804_|
|**Response**|**Response**|**Response**|**Response**|
|**Attributes**|**Description**|**Description**|**Example**|
|Link|• Link for downloading this file.<br>• Refer to sample output on<br>Annex Bfor reference.<br>• Link will expire after 15 minutes.|• Link for downloading this file.<br>• Refer to sample output on<br>Annex Bfor reference.<br>• Link will expire after 15 minutes.|_https://ltafarecard.s3.amazona_<br>_ws.com/201804/origin_destinat_<br>_ion_bus_201804.zip?x-amz-_<br>_security-_<br>_token=FQoDYXdzEOf%2F%2..._|

### 2.7 PASSENGER VOLUME BY ORIGIN DESTINATION TRAIN

 STATIONS

**URL **https://datamall2.mytransport.sg/ltaodataservice/PV/ODTrain

Returns number of trips by weekdays and weekends from origin to **Description **destination train stations

By 10th of every month, the passenger volume for previous month data **Update Freq **will be generated **Request ****Parameters ** **Description ** **Mandatory ** **Example **Request for files up to Date No _Date=201803_ last three months **Response ****Attributes ** **Description ** **Example **
Link - Link for downloading this file. _https://ltafarecard.s3.amazona_

              - Refer to sample output on _ws.com/201803/origin_destinat_
Annex B for reference. _ion_train_201803.zip?x-amz-_

_security-_

              - Link will expire after 15 minutes.

_token=FQoDYXdzEOf%2F%2F%_
_..._

|STATIONS|Col2|Col3|Col4|
|---|---|---|---|
|**URL**|https://datamall2.mytransport.sg/ltaodataservice/PV/ODTrain|https://datamall2.mytransport.sg/ltaodataservice/PV/ODTrain|https://datamall2.mytransport.sg/ltaodataservice/PV/ODTrain|
|**Description**|Returns number of trips by weekdays and weekends from origin to<br>destination train stations|Returns number of trips by weekdays and weekends from origin to<br>destination train stations|Returns number of trips by weekdays and weekends from origin to<br>destination train stations|
|**Update Freq**|By 10th of every month, the passenger volume for previous month data<br>will begenerated|By 10th of every month, the passenger volume for previous month data<br>will begenerated|By 10th of every month, the passenger volume for previous month data<br>will begenerated|
|**Request**|**Request**|**Request**|**Request**|
|**Parameters**|**Description**|**Mandatory:**|**Example**|
|Date|Request for files up to<br>last three months|No|_Date=201803_|
|**Response**|**Response**|**Response**|**Response**|
|**Attributes**|**Description**|**Description**|**Example**|
|Link|• Link for downloading this file.<br>• Refer to sample output on<br>Annex Bfor reference.<br>• Link will expire after 15 minutes.|• Link for downloading this file.<br>• Refer to sample output on<br>Annex Bfor reference.<br>• Link will expire after 15 minutes.|_https://ltafarecard.s3.amazona_<br>_ws.com/201803/origin_destinat_<br>_ion_train_201803.zip?x-amz-_<br>_security-_<br>_token=FQoDYXdzEOf%2F%2F%_<br>_... _|

### 2.8 PASSENGER VOLUME BY TRAIN STATIONS

**URL **https://datamall2.mytransport.sg/ltaodataservice/PV/Train

Returns tap in and tap out passenger volume by weekdays and **Description **weekends for individual train station

By 10th of every month, the passenger volume for previous month data **Update Freq **will be generated **Request ****Parameters ** **Description ** **Mandatory **Request for files up to Date No last three months **Response ****Attributes ** **Description **
Link - Link for downloading this file.

              - Refer to sample output on
Annex A for reference.

              - Link will expire after 15 minutes.

|URL|https://datamall2.mytransport.sg/ltaodataservice/PV/Train|Col3|Col4|
|---|---|---|---|
|**Description**|Returns tap in and tap out passenger volume by weekdays and<br>weekends for individual train station|Returns tap in and tap out passenger volume by weekdays and<br>weekends for individual train station|Returns tap in and tap out passenger volume by weekdays and<br>weekends for individual train station|
|**Update Freq**|By 10th of every month, the passenger volume for previous month data<br>will begenerated|By 10th of every month, the passenger volume for previous month data<br>will begenerated|By 10th of every month, the passenger volume for previous month data<br>will begenerated|
|**Request**|**Request**|**Request**|**Request**|
|**Parameters**|**Description**|**Mandatory:**|**Example**|
|Date|Request for files up to<br>last three months|No|_Date=201805_|
|**Response**|**Response**|**Response**|**Response**|
|**Attributes**|**Description**|**Description**|**Example**|
|Link|• Link for downloading this file.<br>• Refer to sample output on<br>Annex Afor reference.<br>• Link will expire after 15 minutes.|• Link for downloading this file.<br>• Refer to sample output on<br>Annex Afor reference.<br>• Link will expire after 15 minutes.|_https://ltafarecard.s3.amazona_<br>_ws.com/201805/transport_node_<br>__train_201805.zip?x-amz-_<br>_security-_<br>_token=FQoDYXdzEOf%2F%2F%_<br>_2F..._|

### 2.9 TAXI AVAILABILITY

**URL **https://datamall2.mytransport.sg/ltaodataservice/Taxi-Availability

Returns location coordinates of all Taxis that are currently available for **Description **hire. Does not include "Hired" or "Busy" Taxis. **Update Freq **1 min **Response ****Attributes ** **Description ** **Sample **

Latitude Latitude location coordinates. _1.35667_

Longitude Longitude location coordinates. _103.93314_

|URL|https://datamall2.mytransport.sg/ltaodataservice/Taxi-Availability|Col3|
|---|---|---|
|**Description**|Returns location coordinates of all Taxis that are currently available for<br>hire. Does not include "Hired" or "Busy" Taxis.|Returns location coordinates of all Taxis that are currently available for<br>hire. Does not include "Hired" or "Busy" Taxis.|
|**Update Freq**|1 min|1 min|
|**Response**|**Response**|**Response**|
|**Attributes**|**Description**|**Sample**|
|Latitude|Latitude location coordinates.|_1.35667_|
|Longitude|Longitude location coordinates.|_103.93314_|

### 2.10 TAXI STANDS

**URL **https://datamall2.mytransport.sg/ltaodataservice/TaxiStands

Returns detailed information of Taxi stands, such as location and whether is it **Description **barrier free. **Update Freq **Monthly **Response ****Attributes ** **Description ** **Sample **

TaxiCode Code representation of Taxi facility. _A01_

Latitude Latitude map coordinates for the start point of _1.303980684_

this road incident.

Longitude Longitude map coordinates for the start point _103.9191828_

of this incident.

Bfa Indicate whether the Taxi stand is barrier free. _Yes_

Ownership Indicate the owner of the Taxi stand. _LTA_

_CCS_

LTA – Land Transport Authority

_Private_

CCS – Clear Channel Singapore

Private – Taxi facilities that are constructed and

maintained by private entities (e.g.

developers/owners of shopping malls,

commercial buildings).

Type Stand - allows Taxis to queue in the taxi bays _Stand_

and wait for passengers. _Stop_

Stop - allow Taxis to perform immediate pick

up and drop off of passengers.

Name Name of Taxi facility.

_ky Plaza_

|2.10 TAXI|STANDS|Col3|
|---|---|---|
|**URL**|https://datamall2.mytransport.sg/ltaodataservice/TaxiStands|https://datamall2.mytransport.sg/ltaodataservice/TaxiStands|
|**Description**|Returns detailed information of Taxi stands, such as location and whether is it<br>barrier free.|Returns detailed information of Taxi stands, such as location and whether is it<br>barrier free.|
|**Update Freq**|Monthly|Monthly|
|**Response**|**Response**|**Response**|
|**Attributes**|**Description**|**Sample**|
|TaxiCode|Code representation of Taxi facility.|_A01_|
|Latitude|Latitude map coordinates for the start point of<br>this road incident.|_1.303980684_|
|Longitude|Longitude map coordinates for the start point<br>of this incident.|_103.9191828_|
|Bfa|Indicate whether the Taxi stand is barrier free.|_Yes_|
|Ownership|Indicate the owner of the Taxi stand.<br>LTA – Land Transport Authority<br>CCS – Clear Channel Singapore<br>Private – Taxi facilities that are constructed and<br>maintained by private entities (e.g.<br>developers/owners of shopping malls,<br>commercial buildings).|_LTA_<br>_CCS_<br>_Private_|
|Type|Stand - allows Taxis to queue in the taxi bays<br>and wait for passengers.<br>Stop - allow Taxis to perform immediate pick<br>up and drop off of passengers.|_Stand_<br>_Stop_|
|Name|Name of Taxi facility.|_Orchard Rd along driveway of Luc_<br>_ky Plaza_|

### 2.11 TRAIN SERVICE ALERTS

**URL **https://datamall2.mytransport.sg/ltaodataservice/TrainServiceAlerts

Returns detailed information on train service **Description **operating hours, such as affected line and stations etc. **Update Freq **Ad hoc **Request ****Parameters ** **Description ** **Mandatory **(none) -**Response ****Attributes ** **Description **Status Indicates if train service is unavailable:

                - 1 (for Normal Train Service or Minor
Delays)

                - 2 (for Disrupted Train Service or Major
Delays)

Line Train network line affected:

                - EWL (for East West Line and Changi
Extension – Expo, Changi Airport)

                - NSL (for North South Line)

                - NEL (for North East Line)

                - CCL (for Circle Line and Circle Line
Extension – BayFront, Marina Bay)

                - DTL (for Downtown Line)

                - TEL (for Thomson-East Coast Line)

                - BPL (for Bukit Panjang LRT)

                - STL (for Sengkang LRT)

                  - PTL (for Punggol LRT)

Direction Indicates direction of service unavailability on the affected line:

                - Both

                - (towards station name)

Stations Indicates the list of affected stations on the affected line.

FreePublicBus Indicates the list of affected stations where free boarding onto normal public bus services are available.

                - (station code)

                - Free bus service island wide

FreeMRTShuttle Indicates the list of affected stations where free **MRT shuttle services^ are available. **

                - (station code)

                - EW21|CC22,EW23,EW24|NS1,
EW27;NS9,NS13,NS16,NS17|CC15;
EW8|CC9,EW5,EW2;NS1|EW24,NS4|BP1

|URL|https://datamall2.mytransport.sg/ltaodataservice/TrainServiceAlerts|Col3|Col4|
|---|---|---|---|
|**Description**|Returns detailed information on train service**unavailability** during scheduled<br>operating hours, such as affected line and stations etc.|Returns detailed information on train service**unavailability** during scheduled<br>operating hours, such as affected line and stations etc.|Returns detailed information on train service**unavailability** during scheduled<br>operating hours, such as affected line and stations etc.|
|**Update Freq**|Ad hoc|Ad hoc|Ad hoc|
|**Request**|**Request**|**Request**|**Request**|
|**Parameters**|**Description**|**Mandatory:**|**Example**|
|(none)|-|-|_- _|
|**Response**|**Response**|**Response**|**Response**|
|**Attributes**|**Description**|**Description**|**Example**|
|Status|Indicates if train service is unavailable:<br>• 1 (for Normal Train Service or Minor<br>Delays)<br>• 2 (for Disrupted Train Service or Major<br>Delays)|Indicates if train service is unavailable:<br>• 1 (for Normal Train Service or Minor<br>Delays)<br>• 2 (for Disrupted Train Service or Major<br>Delays)|_2 _|
|Line|Train network line affected:<br>• EWL (for East West Line and Changi<br>Extension – Expo, Changi Airport)<br>• NSL (for North South Line)<br>• NEL (for North East Line)<br>• CCL (for Circle Line and Circle Line<br>Extension – BayFront, Marina Bay)<br>• DTL (for Downtown Line)<br>• TEL (for Thomson-East Coast Line)<br>• BPL (for Bukit Panjang LRT)<br>• STL (for Sengkang LRT)<br>• PTL(for Punggol LRT)|Train network line affected:<br>• EWL (for East West Line and Changi<br>Extension – Expo, Changi Airport)<br>• NSL (for North South Line)<br>• NEL (for North East Line)<br>• CCL (for Circle Line and Circle Line<br>Extension – BayFront, Marina Bay)<br>• DTL (for Downtown Line)<br>• TEL (for Thomson-East Coast Line)<br>• BPL (for Bukit Panjang LRT)<br>• STL (for Sengkang LRT)<br>• PTL(for Punggol LRT)|_NEL_|
|Direction|Indicates direction of service unavailability on<br>the affected line:<br>• Both<br>• (towards station name)|Indicates direction of service unavailability on<br>the affected line:<br>• Both<br>• (towards station name)|_Punggol_|
|Stations|Indicates the list of affected stations on the<br>affected line.|Indicates the list of affected stations on the<br>affected line.|_NE1,NE3,NE4,NE5,NE6_|
|FreePublicBus|Indicates the list of affected stations where free<br>boarding onto**normal public bus services**are<br>available.<br>• (station code)<br>• Free bus service island wide|Indicates the list of affected stations where free<br>boarding onto**normal public bus services**are<br>available.<br>• (station code)<br>• Free bus service island wide|_NE1,NE3,NE4,NE5,NE6_|
|FreeMRTShuttle|Indicates the list of affected stations where**free**<br>**MRT shuttle services^** are available.<br>• (station code)<br>• EW21|CC22,EW23,EW24|NS1,<br>EW27;NS9,NS13,NS16,NS17|CC15;<br>EW8|CC9,EW5,EW2;NS1|EW24,NS4|BP1** **|Indicates the list of affected stations where**free**<br>**MRT shuttle services^** are available.<br>• (station code)<br>• EW21|CC22,EW23,EW24|NS1,<br>EW27;NS9,NS13,NS16,NS17|CC15;<br>EW8|CC9,EW5,EW2;NS1|EW24,NS4|BP1** **|_NE1,NE3,NE4,NE5,NE6_|

MRTShuttleDirection Indicates the direction of free MRT shuttle _Punggol_ services available:

                - Both

                - (towards station name)

Message Travel advisory notification service for train _1710hrs: NEL – No train_ commuters, published by LTA. This notice is also _service between_ broadcasted to commuters via the Find-My-Way _Harbourfront to Dhoby_ module in MyTransport mobile app. _Ghaut stations towards_

• Content Punggol station due to a
 • CreatedDate signalling fault. Free bus

_rides are available at_
_designated bus stops._

_2017-12-01 17:54:21_

Note:

  - This API relies on the static master list of Train Station Codes, Train Line Codes and Train Shuttle
[Service Direction which can be obtained on DataMall Portal .](http://www.mytransport.sg/content/mytransport/home/dataMall.html)

      - The Train Station Codes and Train Line Codes files are under Public Transport section.

      - The Train Shuttle Service Direction information can be found in Train Line Codes file.

  - During train unavailability, following attributes will be mandatory.

      - Status

      - Line

      - Direction

      - Stations

  - Each line that is affected will be published as separate clusters within the single API response.
Refer to sample output on Annex C for reference.

  - **^Free MRT Shuttle services will ferry commuters from station to station along the affected **stretch.

  -**There are scenarios which MRT Shuttle services do not run along the affected stretch but along **four predefined areas in both directions

      - Bouna Vista, Clementi, Jurong East and Boon Lay

      - Woodlands, Yishun, Ang Mo Kio, Bishan

      - Paya Lebar, Bedok, Tampines

      - Jurong East, Choa Chu Kang

      - “|” delimiter to denote an interchange station

      - “;” delimiter to denote end of an area

|MRTShuttleDirection|Indicates the direction of free MRT shuttle<br>services available:<br>• Both<br>• (towards station name)|Punggol|
|---|---|---|
|Message|Travel advisory notification service for train<br>commuters, published by LTA. This notice is also<br>broadcasted to commuters via the Find-My-Way<br>module in MyTransport mobile app.<br>• Content <br>• CreatedDate|_1710hrs: NEL – No train_<br>_service between_<br>_Harbourfront to Dhoby_<br>_Ghaut stations towards_<br>_Punggol station due to a_<br>_signalling fault. Free bus_<br>_rides are available at_<br>_designated bus stops._<br>_2017-12-01 17:54:21_|

### 2.12 CARPARK AVAILABILITY **URL **https://datamall2.mytransport.sg/ltaodataservice/CarParkAvailabilityv2

Returns no. of available lots for HDB, LTA and URA carpark data.

The LTA carpark data consist of major shopping malls and developments within **Description **Orchard, Marina, HarbourFront, Jurong Lake District.

_(Note: list of LTA carpark data available on this API is subset of those listed on_
_One.Motoring and MyTransport Portals)_**Update Freq **1 minute **Response ****LTA ** **URA ** **HDB **
**Attributes ** **Description **
**Sample ** **Sample ** **Sample **

CarParkID A unique code for this carpark _1_ _A0007_ _KB7_

Area Area of development / building: _Marina_ _(blank)_ _(blank)_

             - Orchard

             - Marina

             - Harbfront

             - JurongLakeDistrict

Development Major landmark or address where _Suntec City_ _ANGULLIA_ _BLK 69_

carpark is located _PARK OFF_ _GEYLANG_

_STREET_ _BAHRU_

Location Latitude and Longitude map _1.29375_ _1.305328…_ _1.32158.._

coordinates. _103.85718_ _103.82957..._ _103.87047…_

AvailableLots Number of lots available at point _352_ _0_ _18_

of data retrieval.

LotType Type of lots: _C_ _Y_ _C_

             - C (for Cars)

             - H (for Heavy Vehicles)

             - Y (for Motorcycles)

Agency Agencies: _LTA_ _URA_ _HDB_

             - HDB

             - LTA

             - URA

Respective agencies are responsible for the accuracy of the carpark data. If there is any data related issue, you

may contact the agency directly. There may be empty values if data is not available (e.g. Area for HDB and URA

data is unavailable hence blank value is expected).

|URL|https://datamall2.mytransport.sg/ltaodataservice/CarParkAvailabilityv2|Col3|Col4|Col5|
|---|---|---|---|---|
|**Description:**|Returns no. of available lots for HDB, LTA and URA carpark data.<br>The LTA carpark data consist of major shopping malls and developments within<br>Orchard, Marina, HarbourFront, Jurong Lake District.<br>_(Note: list of LTA carpark data available on this API issubsetof those listed on_<br>_One.Motoring and MyTransport Portals) _|Returns no. of available lots for HDB, LTA and URA carpark data.<br>The LTA carpark data consist of major shopping malls and developments within<br>Orchard, Marina, HarbourFront, Jurong Lake District.<br>_(Note: list of LTA carpark data available on this API issubsetof those listed on_<br>_One.Motoring and MyTransport Portals) _|Returns no. of available lots for HDB, LTA and URA carpark data.<br>The LTA carpark data consist of major shopping malls and developments within<br>Orchard, Marina, HarbourFront, Jurong Lake District.<br>_(Note: list of LTA carpark data available on this API issubsetof those listed on_<br>_One.Motoring and MyTransport Portals) _|Returns no. of available lots for HDB, LTA and URA carpark data.<br>The LTA carpark data consist of major shopping malls and developments within<br>Orchard, Marina, HarbourFront, Jurong Lake District.<br>_(Note: list of LTA carpark data available on this API issubsetof those listed on_<br>_One.Motoring and MyTransport Portals) _|
|**Update Freq:**|1 minute|1 minute|1 minute|1 minute|
|**Response**|**Response**|**Response**|**Response**|**Response**|
|**Attributes:**|**Description:**|**LTA**<br>**Sample:**|**URA**<br>**Sample:**|**HDB**<br>**Sample:**|
|CarParkID|A unique code for this carpark|_1 _|_A0007_|_KB7_|
|Area|Area of development / building:<br>• Orchard<br>• Marina<br>• Harbfront<br>• JurongLakeDistrict|_Marina_|_(blank)_|_(blank)_|
|Development|Major landmark or address where<br>carpark is located|_Suntec City_|_ANGULLIA_<br>_PARK OFF_<br>_STREET_|_BLK 69_<br>_GEYLANG_<br>_BAHRU_|
|Location|Latitude and Longitude map<br>coordinates.|_1.29375_<br>_103.85718_|_1.305328…_<br>_103.82957..._|_1.32158.._<br>_103.87047…_|
|AvailableLots|Number of lots available at point<br>of data retrieval.|_352_|_0 _|_18_|
|LotType|Type of lots:<br>• C (for Cars)<br>• H (for Heavy Vehicles)<br>• Y (for Motorcycles)|_C _|_Y _|_C _|
|Agency|Agencies:<br>• HDB<br>• LTA<br>• URA|_LTA_|_URA_|_HDB_|

### 2.13 ESTIMATED TRAVEL TIMES

**URL **https://datamall2.mytransport.sg/ltaodataservice/EstTravelTimes **Description **Returns estimated travel times of expressways (in segments). **Update Freq **5 minutes **Response ****Attributes ** **Description ** **Sample **

Name Expressway _AYE_

Direction Direction of travel: _1_

1 – Travelling from east to west,

or south to north.

2 – Travelling from west to east,

or north to south.

FarEndPoint The final end point of this whole

expressway in current direction

of travel

StartPoint Start point of this current

segment

EndPoint End point of this current

segment

EstTime Estimated travel time in minutes _2_

|URL|https://datamall2.mytransport.sg/ltaodataservice/EstTravelTimes|Col3|
|---|---|---|
|**Description**|Returns estimated travel times of expressways (in segments).|Returns estimated travel times of expressways (in segments).|
|**Update Freq**|5 minutes|5 minutes|
|**Response**|**Response**|**Response**|
|**Attributes**|**Description**|**Sample**|
|Name|Expressway|_AYE_|
|Direction|Direction of travel:<br>1 – Travelling from east to west,<br>or south to north.<br>2 – Travelling from west to east,<br>or north to south.|_1 _|
|FarEndPoint|The final end point of this whole<br>expressway in current direction<br>of travel|_TUAS CHECKPOINT_|
|StartPoint|Start point of this current<br>segment|_AYE/MCE INTERCHANGE_|
|EndPoint|End point of this current<br>segment|_TELOK BLANGAH RD_|
|EstTime|Estimated travel time in minutes|_2 _|

### 2.14 FAULTY TRAFFIC LIGHTS

**URL **https://datamall2.mytransport.sg/ltaodataservice/v2/FaultyTrafficLights

Returns alerts of traffic lights that are currently faulty, or currently **Description **undergoing scheduled maintenance. **Update Freq **2 minutes – whenever there are updates **Response ****Attributes ** **Description ** **Sample **

AlarmID Technical alarm ID _GL703034136_

NodeID A unique code to represent each _703034136_

unique traffic light node

Type Type of the technical alarm _13_

            - 2 (Blackout)

            - 13 (Flashing Yellow)

StartDate YYYY-MM-DD HH:MM:SS.ms

EndDate YYYY-MM-DD HH:MM:SS.ms

(empty field if this is not a

scheduled maintenance)

XCoordinate X Coordinate in SVY21 _20786.6_

coordinate system

YCoordinate Y Coordinate in SVY21 _32521.5_

coordinate system

Message Canning Message

_North Street 1 Junc._

|URL|https://datamall2.mytransport.sg/ltaodataservice/v2/FaultyTrafficLights|Col3|
|---|---|---|
|**Description**|Returns alerts of traffic lights that are currentlyfaulty, orcurrently<br>undergoing scheduled maintenance.|Returns alerts of traffic lights that are currentlyfaulty, orcurrently<br>undergoing scheduled maintenance.|
|**Update Freq**|2 minutes – whenever there are updates|2 minutes – whenever there are updates|
|**Response**|**Response**|**Response**|
|**Attributes**|**Description**|**Sample**|
|AlarmID|Technical alarm ID|_GL703034136_|
|NodeID|A unique code to represent each<br>unique traffic light node|_703034136_|
|Type|Type of the technical alarm<br>• 2 (Blackout)<br>• 13 (Flashing Yellow)|_13_|
|StartDate|YYYY-MM-DD HH:MM:SS.ms|_2014-04-12 01:58:00.0_|
|EndDate|YYYY-MM-DD HH:MM:SS.ms<br>(empty field if this is not a<br>scheduled maintenance)||
|XCoordinate|X Coordinate in SVY21<br>coordinate system|_20786.6_|
|YCoordinate|Y Coordinate in SVY21<br>coordinate system|_32521.5_|
|Message|Canning Message|_(23/1) 8:58 Flashing Yellow at_<br>_Bedok North Interchange/Bedok_<br>_North Street 1 Junc._|

### 2.15 PLANNED ROAD OPENINGS

**URL **https://datamall2.mytransport.sg/ltaodataservice/RoadOpenings **Description **Information on planned road openings. **Update Freq **24 hours – whenever there are updates **Response ****Attributes ** **Description ** **Sample **

EventID ID for this road opening event

StartDate Start date for works to be _2016-03-31_

performed for this road opening

(in YYYY-MM-DD format)

EndDate End date for works to be _2016-09-30_

performed for this road opening

(in YYYY-MM-DD format)

SvcDept Department or company

performing this road work _PROJ (EAST)_

RoadName Name of new road to be opened _AH SOO GARDEN_

Other Additional information or

messages

|URL|https://datamall2.mytransport.sg/ltaodataservice/RoadOpenings|Col3|
|---|---|---|
|**Description**|Information on planned road openings.|Information on planned road openings.|
|**Update Freq**|24 hours – whenever there are updates|24 hours – whenever there are updates|
|**Response**|**Response**|**Response**|
|**Attributes**|**Description**|**Sample**|
|EventID|ID for this road opening event|_RMAPP-201603-0900_|
|StartDate|Start date for works to be<br>performed for this road opening<br>(in YYYY-MM-DD format)|_2016-03-31_|
|EndDate|End date for works to be<br>performed for this road opening<br>(in YYYY-MM-DD format)|_2016-09-30_|
|SvcDept|Department or company<br>performing this road work|_SP POWERGRID LTD - CUSTOMER_<br>_PROJ (EAST)_|
|RoadName|Name of new road to be opened|_AH SOO GARDEN_|
|Other|Additional information or<br>messages|_For details, please call 62409237_|

### 2.16 APPROVED ROAD WORKS

**URL **https://datamall2.mytransport.sg/ltaodataservice/RoadWorks

Information on approved road works to be carried out/being carried **Description **out. **Update Freq **24 hours – whenever there are updates **Response ****Attributes ** **Description ** **Sample **

EventID ID for this road work

StartDate Start date for the works _2015-12-14_

performed for this road work

(in YYYY-MM-DD format)

EndDate End date for works performed _2016-07-31_

for this road work

(in YYYY-MM-DD format)

SvcDept Department or company

performing this road work

RoadName Name of road where work is _ADAM DRIVE_

being performed.

Other Additional information or

messages.

|URL|https://datamall2.mytransport.sg/ltaodataservice/RoadWorks|Col3|
|---|---|---|
|**Description**|Information on approved road works to be carried out/being carried<br>out.|Information on approved road works to be carried out/being carried<br>out.|
|**Update Freq**|24 hours – whenever there are updates|24 hours – whenever there are updates|
|**Response**|**Response**|**Response**|
|**Attributes**|**Description**|**Sample**|
|EventID|ID for this road work|_RMAPP-201512-0217_|
|StartDate|Start date for the works<br>performed for this road work<br>(in YYYY-MM-DD format)|_2015-12-14_|
|EndDate|End date for works performed<br>for this road work<br>(in YYYY-MM-DD format)|_2016-07-31_|
|SvcDept|Department or company<br>performing this road work|_SP POWERGRID LTD - REGIONAL_<br>_NETWORK CENTRAL_|
|RoadName|Name of road where work is<br>being performed.|_ADAM DRIVE_|
|Other|Additional information or<br>messages.|_For details, please call 67273085_|

### 2.17 TRAFFIC IMAGES

**URL **https://datamall2.mytransport.sg/ltaodataservice/Traffic-Imagesv2

Returns links to images of live traffic conditions along expressways and **Description **Woodlands & Tuas Checkpoints. **Update Freq **1 to 5 minutes **Response ****Attributes ** **Description ** **Sample **

CameraID A unique ID for this _5795_

camera

For mapping this

attribute to specific

location

descriptions, please

refer to ANNEX G.

Latitude Latitude map _1.326024822_

coordinates

Longitude Longitude map _103.905625_

coordinates

ImageLink - Link for _https://dm-traffic-camera-_

downloading _itsc.s3.amazonaws.com/2020-04-01/09-_

this image. _24/1001_0918_20200401092500_e0368e.jpg?x-_

_amz-security-_

           - Link will

_token=IQoJb3JpZ2luX2VjEBkaDmFwL..._

expire after

15 minutes.

|URL|https://datamall2.mytransport.sg/ltaodataservice/Traffic-Imagesv2|Col3|
|---|---|---|
|**Description**|Returns links to images of live traffic conditions along expressways and<br>Woodlands & Tuas Checkpoints.|Returns links to images of live traffic conditions along expressways and<br>Woodlands & Tuas Checkpoints.|
|**Update Freq**|1 to 5 minutes|1 to 5 minutes|
|**Response**|**Response**|**Response**|
|**Attributes**|**Description**|**Sample**|
|CameraID|A unique ID for this<br>camera<br>For mapping this<br>attribute to specific<br>location<br>descriptions, please<br>refer to**ANNEX G**.|_5795_|
|Latitude|Latitude map<br>coordinates|_1.326024822_|
|Longitude|Longitude map<br>coordinates|_103.905625_|
|ImageLink|• Link for<br>downloading<br>this image.<br>• Link will<br>expire after<br>15 minutes.|_https://dm-traffic-camera-_<br>_itsc.s3.amazonaws.com/2020-04-01/09-_<br>_24/1001_0918_20200401092500_e0368e.jpg?x-_<br>_amz-security-_<br>_token=IQoJb3JpZ2luX2VjEBkaDmFwL..._|

### 2.18 TRAFFIC INCIDENTS

**URL **https://datamall2.mytransport.sg/ltaodataservice/TrafficIncidents

Returns incidents currently happening on the roads, such as **Description **Accidents, Vehicle Breakdowns, Road Blocks, Traffic Diversions etc. **Update Freq **2 minutes – whenever there are updates **Response ****Attributes ** **Description ** **Sample **

Type Incident Types: _Vehicle breakdown_

             - Accident

             - Roadwork

             - Vehicle breakdown

             - Weather

             - Obstacle

             - Road Block

             - Heavy Traffic

             - Miscellaneous

             - Diversion

             - Unattended Vehicle

             - Fire

             - Plant Failure

             - Reverse Flow

Latitude Latitude map coordinates for the _1.30398068448214_

start point of this road incident

Longitude Longitude map coordinates for _103.919182834377_

the start point of this incident

Message Description message for this

incident

|URL|https://datamall2.mytransport.sg/ltaodataservice/TrafficIncidents|Col3|
|---|---|---|
|**Description**|Returns incidents currentlyhappening on the roads, such as<br>Accidents, Vehicle Breakdowns, Road Blocks, Traffic Diversions etc.|Returns incidents currentlyhappening on the roads, such as<br>Accidents, Vehicle Breakdowns, Road Blocks, Traffic Diversions etc.|
|**Update Freq**|2 minutes – whenever there are updates|2 minutes – whenever there are updates|
|**Response**|**Response**|**Response**|
|**Attributes**|**Description**|**Sample**|
|Type|Incident Types:<br>• Accident<br>• Roadwork<br>• Vehicle breakdown<br>• Weather<br>• Obstacle<br>• Road Block<br>• Heavy Traffic<br>• Miscellaneous<br>• Diversion<br>• Unattended Vehicle<br>• Fire<br>• Plant Failure<br>• Reverse Flow|_Vehicle breakdown_|
|Latitude|Latitude map coordinates for the<br>startpoint of this road incident|_1.30398068448214_|
|Longitude|Longitude map coordinates for<br>the startpoint of this incident|_103.919182834377_|
|Message|Description message for this<br>incident|_(29/3)18:22 Vehicle breakdown on_<br>_ECP (towards Changi Airport) after_<br>_Still Rd Sth Exit. Avoid lane 3._|

### 2.19 TRAFFIC SPEED BANDS

**URL **https://datamall2.mytransport.sg/ltaodataservice/v4/TrafficSpeedBands

Returns current traffic speeds on expressways and arterial roads, **Description **expressed in speed bands. **Update Freq **5 minutes **Response ****Attributes ** **Description ** **Sample **

LinkID Unique ID for this stretch of road _1_

RoadName Road Name

RoadCategory 1 – Expressways _2_

2 – Major Arterial Roads

3 – Arterial Roads

4 – Minor Arterial Roads

5 – Small Roads

6 – Slip Roads

8 – Short Tunnels

SpeedBand Speed Bands Information. Total: 8 _2_

1 – indicates speed range from 0 < 9
2 – indicates speed range from 10 < 19
3 – indicates speed range from 20 < 29
4 – indicates speed range from 30 < 39
5 – indicates speed range from 40 < 49
6 – indicates speed range from 50 < 59
7 – indicates speed range from 60 < 69
8 – speed range from 70 or more

MinimumSpeed Minimum speed in km/h _10_

MaximumSpeed Maximum speed in km/h _19_

StartLon Longitude map coordinates for start

point for this stretch of road.

|URL|https://datamall2.mytransport.sg/ltaodataservice/v4/TrafficSpeedBands|Col3|
|---|---|---|
|**Description**|Returns current traffic speeds on expressways and arterial roads,<br>expressed in speed bands.|Returns current traffic speeds on expressways and arterial roads,<br>expressed in speed bands.|
|**Update Freq**|5 minutes|5 minutes|
|**Response**|**Response**|**Response**|
|**Attributes**|**Description**|**Sample**|
|LinkID|Unique ID for this stretch of road|_1 _|
|RoadName|Road Name|_SERANGOON ROAD_|
|RoadCategory|1 – Expressways<br>2 – Major Arterial Roads<br>3 – Arterial Roads<br>4 – Minor Arterial Roads<br>5 – Small Roads<br>6 – Slip Roads<br>8 – Short Tunnels|_2 _|
|SpeedBand|Speed Bands Information. Total: 8<br>1 – indicates speed range from 0 < 9<br>2 – indicates speed range from 10 < 19<br>3 – indicates speed range from 20 < 29<br>4 – indicates speed range from 30 < 39<br>5 – indicates speed range from 40 < 49<br>6 – indicates speed range from 50 < 59<br>7 – indicates speed range from 60 < 69<br>8 –speed range from 70 or more|_2 _|
|MinimumSpeed|Minimum speed in km/h|_10_|
|MaximumSpeed|Maximum speed in km/h|_19_|
|StartLon|Longitude map coordinates for start<br>point for this stretch of road.|_103.86246461405193_|

StartLat Latitude map coordinates for start

point for this stretch of road.

EndLon Longitude map coordinates for end

point for this stretch of road.

EndLat Latitude map coordinates for start

point for this stretch of road.

|StartLat|Latitude map coordinates for start<br>point for this stretch of road.|1.3220591510051254|
|---|---|---|
|EndLon|Longitude map coordinates for end<br>point for this stretch of road.|_103.86315591911669_|
|EndLat|Latitude map coordinates for start<br>point for this stretch of road.|_1.3215993547809128_|

### 2.20 VMS / EMAS

**URL **https://datamall2.mytransport.sg/ltaodataservice/VMS

Returns traffic advisories (via variable message services) concerning **Description **current traffic conditions that are displayed on EMAS signboards

along expressways and arterial roads. **Update Freq **2 minutes **Response ****Attributes ** **Description ** **Sample **

EquipmentID EMAS equipment ID _amvms_v9104_

Latitude Latitude map coordinates of

electronic signboard.

Longitude Longitude map coordinates of

electronic signboard.

Message Variable Message being

displayed on the EMAS display. _U.THOMSON_

|URL|https://datamall2.mytransport.sg/ltaodataservice/VMS|Col3|
|---|---|---|
|**Description**|Returns traffic advisories (via variable message services) concerning<br>current traffic conditions that are displayed on EMAS signboards<br>along expressways and arterial roads.|Returns traffic advisories (via variable message services) concerning<br>current traffic conditions that are displayed on EMAS signboards<br>along expressways and arterial roads.|
|**Update Freq**|2 minutes|2 minutes|
|**Response**|**Response**|**Response**|
|**Attributes**|**Description**|**Sample**|
|EquipmentID|EMAS equipment ID|_amvms_v9104_|
|Latitude|Latitude map coordinates of<br>electronic signboard.|_1.3927176306916775_|
|Longitude|Longitude map coordinates of<br>electronic signboard.|_103.82618266340947_|
|Message|Variable Message being<br>displayed on the EMAS display.|_VEH BREAKDOWN SH,AFT_<br>_U.THOMSON_|

### 2.21 BICYCLE PARKING

**URL **https://datamall2.mytransport.sg/ltaodataservice/v3/BicycleParking

Returns bicycle parking locations within a radius. The default radius is **Description **set as 0.5km **Update Freq **Monthly **Request ****Parameters ** **Description ** **Mandatory **Latitude map

Lat coordinates of Yes

location

Longitude map

Long coordinates of Yes

location

Dist Radius in kilometre No **Response ****Attributes ** **Description **
Description Brief description of bicycle parking location.

Latitude Latitude map coordinates of bicycle parking location.

Longitude Longitude map coordinates of bicycle parking location.

RackType Ownership and type of bicycle parking facility

RackCount Total number of bicycle parking lots.

ShelterIndicator Indication if the bicycle parking lots are sheltered.

SharedBicycleParking Indication if the bicycle parking facility allows for shared bicycle parking.

Type Type of bicycle parking facility.

|URL|https://datamall2.mytransport.sg/ltaodataservice/v3/BicycleParking|Col3|Col4|
|---|---|---|---|
|**Description**|Returns bicycle parking locations within a radius. The default radius is<br>set as 0.5km|Returns bicycle parking locations within a radius. The default radius is<br>set as 0.5km|Returns bicycle parking locations within a radius. The default radius is<br>set as 0.5km|
|**Update Freq:**|Monthly|Monthly|Monthly|
|**Request**|**Request**|**Request**|**Request**|
|**Parameters**|**Description**|**Mandatory:**|**Example**|
|Lat|Latitude map<br>coordinates of<br>location|Yes|_1.364897_|
|Long|Longitude map<br>coordinates of<br>location|Yes|_103.766094_|
|Dist|Radius in kilometre|No|_Default is 0.5_|
|**Response**|**Response**|**Response**|**Response**|
|**Attributes**|**Description**|**Description**|**Example**|
|Description|Brief description of bicycle parking<br>location.|Brief description of bicycle parking<br>location.|_Bus Stop 43267_|
|Latitude|Latitude map coordinates of bicycle<br>parking location.|Latitude map coordinates of bicycle<br>parking location.|_1.3927176306916775_|
|Longitude|Longitude map coordinates of bicycle<br>parking location.|Longitude map coordinates of bicycle<br>parking location.|_103.82618266340947_|
|RackType|Ownership and type of bicycle parking<br>facility|Ownership and type of bicycle parking<br>facility|_Racks or Yellow Box_|
|RackCount|Total number of bicycle parking lots.|Total number of bicycle parking lots.|_10_|
|ShelterIndicator|Indication if the bicycle parking lots<br>are sheltered.|Indication if the bicycle parking lots<br>are sheltered.|_Y _|
|SharedBicycleParking|Indication if the bicycle parking facility<br>allows for shared bicycleparking.|Indication if the bicycle parking facility<br>allows for shared bicycleparking.|_Yes_|
|Type|Type of bicycle parking facility.|Type of bicycle parking facility.|_RACK_|

### 2.22 GEOSPATIAL WHOLE ISLAND

https://datamall2.mytransport.sg/ltaodataservice/GeospatialWholeIsla
**URL **nd **Description **Returns the SHP files of the requested geospatial layer **Update Freq **Ad hoc **Request ****Parameters ** **Description ** **Mandatory **Name of Geospatial
Layer. Refer to ANNEX **E for the list of **ID Geospatial layers Yes

(Case Sensitive, omit space.)**Response ****Attributes ** **Description **
Link - Link for downloading this file.

              - Link will expire after 15 minutes.

|URL|https://datamall2.mytransport.sg/ltaodataservice/GeospatialWholeIsla<br>nd|Col3|Col4|
|---|---|---|---|
|**Description**|Returns the SHP files of the requestedgeospatial layer|Returns the SHP files of the requestedgeospatial layer|Returns the SHP files of the requestedgeospatial layer|
|**Update Freq:**|Ad hoc|Ad hoc|Ad hoc|
|**Request**|**Request**|**Request**|**Request**|
|**Parameters**|**Description**|**Mandatory:**|**Example**|
|ID|Name of Geospatial<br>Layer. Refer to**ANNEX**<br>**E** for the list of<br>Geospatial layers<br>(Case Sensitive, omit<br>space.)|Yes|_ArrowMarking_|
|**Response**|**Response**|**Response**|**Response**|
|**Attributes**|**Description**|**Description**|**Example**|
|Link|• Link for downloading this file.<br>• Link will expire after 15 minutes.|• Link for downloading this file.<br>• Link will expire after 15 minutes.|_https://dmgeospatial.s3.ap-_<br>_southeast-_<br>_1.amazonaws.com/ArrowMa_<br>_rking.zip?X-Amz-Security-_<br>_Token=IQoJb3JpZ2luX2VjEG_|

### 2.23 FACILITIES MAINTENANCE

https://datamall2.mytransport.sg/ltaodataservice/v2/FacilitiesMaintena
**URL **nce **Description **Returns adhoc lift maintenance in MRT stations. **Update Freq **Ad hoc **Response ****Attributes ** **Description **
Line Code of train network line.
StationCode Code of train station.
StationName Name of train station.
LiftID ID of the lift which is currently under maintenance.
This value is optional.

LiftDesc Detailed description of the lift which is currently under maintenance.

|URL|https://datamall2.mytransport.sg/ltaodataservice/v2/FacilitiesMaintena<br>nce|Col3|
|---|---|---|
|**Description**|Returns adhoc lift maintenance in MRT stations.|Returns adhoc lift maintenance in MRT stations.|
|**Update Freq:**|Ad hoc|Ad hoc|
|**Response**|**Response**|**Response**|
|**Attributes**|**Description**|**Example**|
|Line|Code of train network line.|_NEL_|
|StationCode|Code of train station.|_NE12_|
|StationName|Name of train station.|_Serangoon_|
|LiftID|ID of the lift which is currently under<br>maintenance.<br>This value is optional.|_B1L01_|
|LiftDesc|Detailed description of the lift which is<br>currently under maintenance.|_Exit B Street level -_<br>_Concourse_|

### 2.24 STATION CROWD DENSITY REAL TIME

**URL **https://datamall2.mytransport.sg/ltaodataservice/PCDRealTime

Returns real-time MRT/LRT station crowdedness level of a particular train network **Description **line **Update Freq **10 minutes **Request ****Parameters ** **Description ** **Mandatory **Code of train network line.
Train lines supported:

               - CCL (for Circle Line)

               - CEL (for Circle Line Extension –
BayFront, Marina Bay)

               - CGL (for Changi Extension – Expo,
Changi Airport)

TrainLine - DTL (for Downtown Line) Yes

               - EWL (for East West Line)

               - NEL (for North East Line)

               - NSL (for North South Line)

               - BPL (for Bukit Panjang LRT)

               - SLRT (for Sengkang LRT)

               - PLRT (for Punggol LRT)

               - TEL (for Thomson-East Coast Line)**Response ****Attributes ** **Description **
Station Station code

StartTime The start of the time interval

EndTime The end of the time interval

CrowdLevel The crowdedness level indicates:

            - l: low

            - h: high

            - m: moderate

            - NA

|URL|https://datamall2.mytransport.sg/ltaodataservice/PCDRealTime|Col3|Col4|
|---|---|---|---|
|**Description**|Returns real-time MRT/LRT station crowdedness level of a particular train network<br>line|Returns real-time MRT/LRT station crowdedness level of a particular train network<br>line|Returns real-time MRT/LRT station crowdedness level of a particular train network<br>line|
|**Update Freq:**|10 minutes|10 minutes|10 minutes|
|**Request**|**Request**|**Request**|**Request**|
|**Parameters**|**Description**|**Mandatory:**|**Example**|
|TrainLine|Code of train network line.<br>Train lines supported:<br>• CCL (for Circle Line)<br>• CEL (for Circle Line Extension –<br>BayFront, Marina Bay)<br>• CGL (for Changi Extension – Expo,<br>Changi Airport)<br>• DTL (for Downtown Line)<br>• EWL (for East West Line)<br>• NEL (for North East Line)<br>• NSL (for North South Line)<br>• BPL (for Bukit Panjang LRT)<br>• SLRT (for Sengkang LRT)<br>• PLRT (for Punggol LRT)<br>• TEL(for Thomson-East Coast Line)|Yes|_EWL_|
|**Response**|**Response**|**Response**|**Response**|
|**Attributes**|**Description**|**Description**|**Example**|
|Station|Station code|Station code|EW13|
|StartTime|The start of the time interval|The start of the time interval|2021-09-<br>15T09:40:00+08:00|
|EndTime|The end of the time interval|The end of the time interval|2021-09-<br>15T09:50:00+08:00|
|CrowdLevel|The crowdedness level indicates:<br>• l: low<br>• h: high<br>• m: moderate<br>• NA|The crowdedness level indicates:<br>• l: low<br>• h: high<br>• m: moderate<br>• NA|l|

### 2.25 STATION CROWD DENSITY FORECAST

**URL **https://datamall2.mytransport.sg/ltaodataservice/PCDForecast

Returns forecasted MRT/LRT station crowdedness level of a particular train network **Description **line at 30 minutes interval **Update Freq **24 hours **Request ****Parameters ** **Description ** **Mandatory **Code of train network line.
Train lines supported:

              - CCL (for Circle Line)

              - CEL (for Circle Line Extension –
BayFront, Marina Bay)

              - CGL (for Changi Extension – Expo,
Changi Airport)

TrainLine - DTL (for Downtown Line) Yes

              - EWL (for East West Line)

              - NEL (for North East Line)

              - NSL (for North South Line)

              - BPL (for Bukit Panjang LRT)

              - SLRT (for Sengkang LRT)

              - PLRT (for Punggol LRT)

              - TEL (for Thomson-East Coast Line)**Response ****Attributes ** **Description **
Date Midnight of the forecasted date

Station Station code

Start The start of the time interval

CrowdLevel The crowdedness level indicates:

            - l: low

            - h: high

            - m: moderate

            - NA

|URL|https://datamall2.mytransport.sg/ltaodataservice/PCDForecast|Col3|Col4|
|---|---|---|---|
|**Description**|Returns forecasted MRT/LRT station crowdedness level of a particular train network<br>line at 30 minutes interval|Returns forecasted MRT/LRT station crowdedness level of a particular train network<br>line at 30 minutes interval|Returns forecasted MRT/LRT station crowdedness level of a particular train network<br>line at 30 minutes interval|
|**Update Freq:**|24 hours|24 hours|24 hours|
|**Request**|**Request**|**Request**|**Request**|
|**Parameters**|**Description**|**Mandatory:**|**Example**|
|TrainLine|Code of train network line.<br>Train lines supported:<br>• CCL (for Circle Line)<br>• CEL (for Circle Line Extension –<br>BayFront, Marina Bay)<br>• CGL (for Changi Extension – Expo,<br>Changi Airport)<br>• DTL (for Downtown Line)<br>• EWL (for East West Line)<br>• NEL (for North East Line)<br>• NSL (for North South Line)<br>• BPL (for Bukit Panjang LRT)<br>• SLRT (for Sengkang LRT)<br>• PLRT (for Punggol LRT)<br>• TEL(for Thomson-East Coast Line)|Yes|_NSL_|
|**Response**|**Response**|**Response**|**Response**|
|**Attributes**|**Description**|**Description**|**Example**|
|Date|Midnight of the forecasted date|Midnight of the forecasted date|2021-09-<br>15T00:00:00+08:00|
|Station|Station code|Station code|NS1|
|Start|The start of the time interval|The start of the time interval|2021-09-<br>15T00:00:00+08:00|
|CrowdLevel|The crowdedness level indicates:<br>• l: low<br>• h: high<br>• m: moderate<br>• NA|The crowdedness level indicates:<br>• l: low<br>• h: high<br>• m: moderate<br>• NA|l|

### 2.26 TRAFFIC FLOW

**URL **https://datamall2.mytransport.sg/ltaodataservice/TrafficFlow

Returns hourly average traffic flow, taken from a representative month of **Description **every quarter during 0700-0900 hours. **Update Freq **Quarterly **Response ****Attributes ** **Description ** **Example **

Link - Link for downloading this file.

           - Link will expire after 15 minutes.

|URL|https://datamall2.mytransport.sg/ltaodataservice/TrafficFlow|Col3|
|---|---|---|
|**Description**|Returns hourly average traffic flow, taken from a representative month of<br>every quarter during 0700-0900 hours.|Returns hourly average traffic flow, taken from a representative month of<br>every quarter during 0700-0900 hours.|
|**Update Freq**|Quarterly|Quarterly|
|**Response**|**Response**|**Response**|
|**Attributes**|**Description**|**Example**|
|Link|• Link for downloading this file.<br>• Link will expire after 15 minutes.|_https://dm-traffic-flow-_<br>_data.s3.ap-southeast-_<br>_1.amazonaws.com/trafficflow.js_<br>_on?X-Amz-Security-_<br>_Token=IQoJb3JpZ2luX2VjE..._|

### 2.27 PLANNED BUS ROUTES

**URL **https://datamall2.mytransport.sg/ltaodataservice/PlannedBusRoutes

Returns planned new/updated bus routes information. **Description **
**Important Note: Data to be released only ON/AFTER the Effective Date. **
**Update Freq **Ad hoc **Response ****Attributes ** **Description **
ServiceNo The bus service number

Operator Operator for this bus service

Direction The direction in which the bus travels (1 or 2), loop services only have 1 direction

StopSequence The i-th bus stop for this route

BusStopCode The unique 5-digit identifier for this physical bus stop

Distance Distance travelled by bus from starting location to this bus stop (in kilometres)

WD_FirstBus Scheduled arrival of first bus on weekdays

WD_LastBus Scheduled arrival of last bus on weekdays

SAT_FirstBus Scheduled arrival of first bus on Saturdays

SAT_LastBus Scheduled arrival of last bus on Saturdays

SUN_FirstBus Scheduled arrival of first bus on Sundays

SUN_LastBus Scheduled arrival of last bus on Sundays

EffectiveDate The date when the new/update bus routes will take effect.

|URL|https://datamall2.mytransport.sg/ltaodataservice/PlannedBusRoutes|Col3|
|---|---|---|
|**Description**|Returns planned new/updated bus routes information.<br>**Important Note: Data to be released only ON/AFTER the Effective Date.**|Returns planned new/updated bus routes information.<br>**Important Note: Data to be released only ON/AFTER the Effective Date.**|
|**Update Freq:**|Ad hoc|Ad hoc|
|**Response**|**Response**|**Response**|
|**Attributes**|**Description**|**Example**|
|ServiceNo|The bus service number|_107M_|
|Operator|Operator for this bus service|_SBST_|
|Direction|The direction in which the bus travels<br>(1 or 2), loop services only have 1<br>direction|_1 _|
|StopSequence|The i-th bus stop for this route|_28_|
|BusStopCode|The unique 5-digit identifier for this<br>physical bus stop|_01219_|
|Distance|Distance travelled by bus from starting<br>location to this bus stop (in kilometres)|_10.3_|
|WD_FirstBus|Scheduled arrival of first bus on<br>weekdays|_2025_|
|WD_LastBus|Scheduled arrival of last bus on<br>weekdays|_2352_|
|SAT_FirstBus|Scheduled arrival of first bus on<br>Saturdays|_1427_|
|SAT_LastBus|Scheduled arrival of last bus on<br>Saturdays|_2349_|
|SUN_FirstBus|Scheduled arrival of first bus on<br>Sundays|_0620_|
|SUN_LastBus|Scheduled arrival of last bus on<br>Sundays|_2349_|
|EffectiveDate|The date when the new/update bus<br>routes will take effect.|_20250302T00:00:00+0800_|

### 2.28 ELECTRIC VEHICLE CHARGING POINTS

**URL **https://datamall2.mytransport.sg/ltaodataservice/EVChargingPoints **Description **Returns electric vehicle charging points in Singapore and their
availabilities by Postal Code. **Update Freq **5 minutes **Request ****S/N ** **Parameters ** **Description ** **Mandatory **1 PostalCode Postal code of the location Yes **Response ****S/N ** **Attributes ** **Description **2 address Address of the charging station

3 name Name of charging station

4 longtitude Longitude map coordinates of charging

station

5 latitude Latitude map coordinates of charging

station

6 locationId Location Id of charging station

Made up from the first 6 decimal places

of longitude followed by postal code.

7 status Status of charging station

Charging station may have multiple

charging points. Please refer to statuses

of individual charging points evIds status

(S/N 21). **chargingPoints **

8 status Current status of the charger

• 0 – Occupied.

|URL|Col2|https://datamall2.mytransport.sg/ltaodataservice/EVChargingPoints|Col4|Col5|
|---|---|---|---|---|
|**Description**|**Description**|Returns electric vehicle charging points in Singapore and their<br>availabilities by Postal Code.|Returns electric vehicle charging points in Singapore and their<br>availabilities by Postal Code.|Returns electric vehicle charging points in Singapore and their<br>availabilities by Postal Code.|
|**Update Freq**|**Update Freq**|5 minutes|5 minutes|5 minutes|
|**Request**|**Request**|**Request**|**Request**|**Request**|
|**S/N:**|**Parameters**|**Description**|**Mandatory:**|**Example**|
|1|PostalCode|Postal code of the location|Yes|_123456_|
||**Response**|**Response**|**Response**|**Response**|
|**S/N:**|**Attributes**|**Description**|**Description**|**Example**|
|2|address|Address of the charging station|Address of the charging station|_123 Road A Singapore_<br>_123456_|
|3|name|Name of charging station|Name of charging station|_123 Road A_|
|4|longtitude|Longitude map coordinates of charging<br>station|Longitude map coordinates of charging<br>station|_103.123456_|
|5|latitude|Latitude map coordinates of charging<br>station|Latitude map coordinates of charging<br>station|_1.123456_|
|6|locationId|Location Id of charging station<br>Made up from the first 6 decimal places<br>of longitude followed by postal code.|Location Id of charging station<br>Made up from the first 6 decimal places<br>of longitude followed by postal code.|_123456123456_|
|7|status|Status of charging station<br>Charging station may have multiple<br>charging points. Please refer to statuses<br>of individual charging points evIds status<br>(S/N 21).|Status of charging station<br>Charging station may have multiple<br>charging points. Please refer to statuses<br>of individual charging points evIds status<br>(S/N 21).|_- _|
|**chargingPoints**|**chargingPoints**|**chargingPoints**|**chargingPoints**|**chargingPoints**|
|8|status|Current status of the charger<br>**• 0 – Occupied.**|Current status of the charger<br>**• 0 – Occupied.**|_1 _|

All charging points are occupied.

I.e. All evIds statuses (S/N 21) are

0.

• 1 – Available.
At least one charging point is

available.

I.e. At least one evIds status (S/N

21) is 1.

                 - **100 – Not Available. **All charging points are not

available.

I.e. All evIds statuses (S/N 21) are

“”.

9 operationHours Operation hours of the charger

10 operator Charging operator of the charger

11 position Position of the charger

12 name Name of the charger

13 id ID of the charger.

Charger may have multiple charging

points. Please refer to ID of individual

charging points evCpId (S/N 20). **plugTypes **

14 plugType Plug type of the charging point

15 powerRating Power rating of the charging point

16 chargingSpeed Charging speed of the charging point

Unit: kW

|Col1|Col2|All charging points are occupied.<br>I.e. All evIds statuses (S/N 21) are<br>0.<br>• 1 – Available.<br>At least one charging point is<br>available.<br>I.e. At least one evIds status (S/N<br>21) is 1.<br>• 100 – Not Available.<br>All charging points are not<br>available.<br>I.e. All evIds statuses (S/N 21) are<br>“”.|Col4|
|---|---|---|---|
|9|operationHours|Operation hours of the charger|_- _|
|10|operator|Charging operator of the charger|_EVCO A_|
|11|position|Position of the charger|_L1 Lot 123_|
|12|name|Name of the charger|_123 Road A_|
|13|id|ID of the charger.<br>Charger may have multiple charging<br>points. Please refer to ID of individual<br>charging points evCpId (S/N 20).|_- _|
|**plugTypes**|**plugTypes**|**plugTypes**|**plugTypes**|
|14|plugType|Plug type of the charging point|_Type 2_|
|15|powerRating|Power rating of the charging point|_AC_|
|16|chargingSpeed|Charging speed of the charging point<br>Unit: kW|_7.4_|

17 price Charging price, including Value Added

Tax

18 priceType Price type of the charging price

• $/h
 • $/kWh

**evIds **19 id Refer to evCpId.

20 evCpId Connector ID

Assigned by LTA during charger

registration. EV Charger Registration

Code makes up first 8 characters.

21 status Status of the charging point

• 0 – Occupied.
Includes following OCPI statuses:

`o` CHARGING
`o` RESERVED
`o` BLOCKED

• 1 – Available.
Includes the following OCPI

statuses:

`o` AVAILABLE

                 -**“” – Not Available. **
Includes the following OCPI

statuses:

`o` OUTOFORDER
`o` INOPERATIVE
`o` UNKNOWN
`o` PLANNED
`o` REMOVED

|17|price|Charging price, including Value Added<br>Tax|0.70|
|---|---|---|---|
|18|priceType|Price type of the charging price<br>**• **$/h<br>**• **$/kWh|_kWh_|
|**evIds**|**evIds**|**evIds**|**evIds**|
|19|id|Refer to evCpId.|_- _|
|20|evCpId|Connector ID<br>Assigned by LTA during charger<br>registration. EV Charger Registration<br>Code makes up first 8 characters.|_R123456A-001_|
|21|status|Status of the charging point<br>**• 0 – Occupied.**<br>Includes following OCPI statuses:<br>`o` CHARGING<br>`o` RESERVED<br>`o` BLOCKED<br>**• 1 – Available.**<br>Includes the following OCPI<br>statuses:<br>`o` AVAILABLE<br>• **“” – Not Available.**<br>Includes the following OCPI<br>statuses:<br>`o` OUTOFORDER<br>`o` INOPERATIVE<br>`o` UNKNOWN<br>`o` PLANNED<br>`o` REMOVED|_1 _|

### 2.29 ELECTRIC VEHICLE CHARGING POINTS BATCH

**URL **https://datamall2.mytransport.sg/ltaodataservice/EVCBatch

Returns all electric vehicle charging points in Singapore and their **Description **availabilities in a single file. **Update Freq **5 minutes **Response ****Attributes ** **Description ** **Example **

Link - Link for downloading this file.

           - Link will expire after 15 minutes.

_Security-_

|URL|https://datamall2.mytransport.sg/ltaodataservice/EVCBatch|Col3|
|---|---|---|
|**Description**|Returns all electric vehicle charging points in Singapore and their<br>availabilities in a single file.|Returns all electric vehicle charging points in Singapore and their<br>availabilities in a single file.|
|**Update Freq:**|5 minutes|5 minutes|
|**Response**|**Response**|**Response**|
|**Attributes**|**Description**|**Example**|
|Link|• Link for downloading this file.<br>• Link will expire after 15 minutes.|_https://dm-traffic-flow-_<br>_data.s3.ap-southeast-_<br>_1.amazonaws.com/ev-_<br>_batch/2026-02-05/EVBatch-_<br>_20260205130000.json?X-Amz-_<br>_Security-_<br>_Token=IQoJb3JpZ2luX2VjE..._|

### 2.30 FLOOD ALERTS

**URL **https://datamall2.mytransport.sg/ltaodataservice/PubFloodAlerts **Description **Returns flood alert information across Singapore, provided by PUB. **Update Freq **3 minutes **Response ****Attributes ** **Description **
alertId A number or string uniquely identifying this observation, assigned by the sender.

dateTime Date and Time the flood observation was issued by PUB.

msgType Code denoting the nature of the alert message. Possible Code Values: “Alert” Initial information requiring attention by targeted recipients, “Cancel” Cancels the earlier message(s) identified in 'references'.

event Text denoting the type of the subject event of the alert message. Event will always be 'Flood'.

responseType Alert response type. Code denoting the type of action recommended for the target audience. Default Code Value:
'Avoid'.

urgency Code denoting the severity of the subject event of the alert message.
Default Code Value: 'Immediate' Responsive action SHOULD be taken immediately.

severity Code denoting the severity of the subject event of the alert message.
Possible Code Values: 'Extreme' Extraordinary threat to life or property, 'Severe' - Significant threat to life or property, 'Moderate' - Possible threat to life or property, 'Minor' – Minimal to no known threat to life or property.

expires A flood alert automatically expires after 24 hours by default. To remove or

|URL|https://datamall2.mytransport.sg/ltaodataservice/PubFloodAlerts|Col3|
|---|---|---|
|**Description**|Returns flood alert information across Singapore, provided by PUB.|Returns flood alert information across Singapore, provided by PUB.|
|**Update Freq:**|3 minutes|3 minutes|
|**Response**|**Response**|**Response**|
|**Attributes**|**Description**|**Example**|
|alertId|A number or string uniquely identifying<br>this observation, assigned by the<br>sender.|_2.49.0.0.702.2-BCM-_<br>_17612003774680-PUBCON-_<br>_DYOONG_|
|dateTime|Date and Time the flood observation<br>was issued by PUB.|_2025-05-22T09:55:00+08:00_|
|msgType|Code denoting the nature of the alert<br>message. Possible Code Values: “Alert” -<br>Initial information requiring attention<br>by targeted recipients, “Cancel” -<br>Cancels the earlier message(s) identified<br>in 'references'.|_Alert_|
|event|Text denoting the type of the subject<br>event of the alert message. Event will<br>always be 'Flood'.|_Flood_|
|responseType|Alert response type. Code denoting the<br>type of action recommended for the<br>target audience. Default Code Value:<br>'Avoid'.|_Avoid_|
|urgency|Code denoting the severity of the<br>subject event of the alert message.<br>Default Code Value: 'Immediate' -<br>Responsive action SHOULD be taken<br>immediately.|_Immediate_|
|severity|Code denoting the severity of the<br>subject event of the alert message.<br>Possible Code Values: 'Extreme' -<br>Extraordinary threat to life or property,<br>'Severe' - Significant threat to life or<br>property, 'Moderate' - Possible threat to<br>life or property, 'Minor' – Minimal to no<br>known threat to life orproperty.|_Minor_|
|expires|A flood alert automatically expires after<br>24 hours by default. To remove or|_2025-10-24T14:19:37+08:00_|

update a flood alert before it expires, follow the cancelled alert issued. senderName Text naming the originator of the alert message. senderName will always be 'PUB'.

headline Text headline of the alert message.

description Location of Flood. Text describing the subject event of the alert message.

instruction Text describing the recommended action to be taken by recipients of the alert message.

areaDesc Area description.

circle lat/long and radius in kilometers. The radius refers to the broadcasting radius of the specific alert, it is NOT indicative of the extent of the flooding.

status Code denoting the appropriate handling of the alert message. Default Code Value: “Actual” - Actionable by all targeted recipients.

|Col1|update a flood alert before it expires,<br>follow the cancelled alert issued.|Col3|
|---|---|---|
|senderName|Text naming the originator of the alert<br>message. senderName will always be<br>'PUB'.|_PUB_|
|headline|Text headline of the alert message.|_Flash Flood Alert_|
|description|Location of Flood. Text describing the<br>subject event of the alert message.|_Flash flood at Bt Timah Rd_<br>_from Wilby Rd to Blackmore_<br>_Dr. Please avoid the area._<br>_Issued 1705 hrs._|
|instruction|Text describing the recommended<br>action to be taken by recipients of the<br>alert message.|_Please avoid this area for the_<br>_next one (1) hour._|
|areaDesc|Area description.|_Jalan Mastuli, Singapore_|
|circle|lat/long and radius in kilometers. The<br>radius refers to the broadcasting radius<br>of the specific alert, it is NOT indicative<br>of the extent of the flooding.|_1.35479,103.88611 0.05_|
|status|Code denoting the appropriate<br>handling of the alert message. Default<br>Code Value: “Actual” - Actionable by all<br>targeted recipients.|_Actual_|

### 2.31 GTFS SCHEDULE (TRAIN)

**URL **https://datamall2.mytransport.sg/ltaodataservice/GTFSScheduleTrain

GTFS Schedule (Train) is a feed specification that defines a common format for static public transportation information. It is composed of a collection of simple files, mostly text files (.txt) that are contained in a single ZIP file.

Each file describes a particular aspect of transit information such as **Description **stops, routes, trips, etc. At its most basic form, a GTFS Schedule dataset is composed of files: agency.txt, routes.txt, trips.txt, stops.txt, stop_times.txt, calendar.txt and calendar_dates.txt.

Please refer to General Transit Feed Specification documentation for more details. **Update Freq **Ad hoc **Response ****Attributes ** **Description ** **Example **

Link - Link for downloading this file.

           - Link will expire after 15 minutes.

|URL|https://datamall2.mytransport.sg/ltaodataservice/GTFSScheduleTrain|Col3|
|---|---|---|
|**Description**|GTFS Schedule (Train) is a feed specification that defines a common<br>format for static public transportation information. It is composed of a<br>collection of simple files, mostly text files (.txt) that are contained in a<br>single ZIP file.<br>Each file describes a particular aspect of transit information such as<br>stops, routes, trips, etc. At its most basic form, a GTFS Schedule dataset<br>is composed of files: agency.txt, routes.txt, trips.txt, stops.txt,<br>stop_times.txt, calendar.txt and calendar_dates.txt.<br>Please refer to General Transit Feed Specification documentation for<br>more details.|GTFS Schedule (Train) is a feed specification that defines a common<br>format for static public transportation information. It is composed of a<br>collection of simple files, mostly text files (.txt) that are contained in a<br>single ZIP file.<br>Each file describes a particular aspect of transit information such as<br>stops, routes, trips, etc. At its most basic form, a GTFS Schedule dataset<br>is composed of files: agency.txt, routes.txt, trips.txt, stops.txt,<br>stop_times.txt, calendar.txt and calendar_dates.txt.<br>Please refer to General Transit Feed Specification documentation for<br>more details.|
|**Update Freq:**|Ad hoc|Ad hoc|
|**Response**|**Response**|**Response**|
|**Attributes**|**Description**|**Example**|
|Link|• Link for downloading this file.<br>• Link will expire after 15 minutes.|_https://dmprod-_<br>_datasets.s3.ap-southeast-_<br>_1.amazonaws.com/train-gtfs-_<br>_schedule/gtfs_schedule.zip?X-_<br>_Amz-Security-_<br>_Token=IQoJb3JpZ2luX2VjE..._|

### 2.32 GTFS REALTIME (TRAIN SERVICE ALERTS)

https://datamall2.mytransport.sg/ltaodataservice/GTFSRealTimeTrain
**URL **ServiceAlerts

GTFS Realtime (Train Service Alerts) is a feed specification that allows public transportation agencies to provide up-to-date information about service alerts allowing users to smoothly plan their trips.

Examples of information provided:**Description **Service alerts - unforeseen events affecting a station, route or the entire network

Please refer to General Transit Feed Specification documentation for more details. **Update Freq **Ad hoc **Response ****Attributes ** **Description ** **Example **

Link - Link for downloading this file.

           - Link will expire after 15 minutes.

_gtfs-real-_

_.._

|URL|https://datamall2.mytransport.sg/ltaodataservice/GTFSRealTimeTrain<br>ServiceAlerts|Col3|
|---|---|---|
|**Description**|GTFS Realtime (Train Service Alerts) is a feed specification that allows<br>public transportation agencies to provide up-to-date information<br>about service alerts allowing users to smoothly plan their trips.<br>Examples of information provided:<br>Service alerts - unforeseen events affecting a station, route or the<br>entire network<br>Please refer to General Transit Feed Specification documentation for<br>more details.|GTFS Realtime (Train Service Alerts) is a feed specification that allows<br>public transportation agencies to provide up-to-date information<br>about service alerts allowing users to smoothly plan their trips.<br>Examples of information provided:<br>Service alerts - unforeseen events affecting a station, route or the<br>entire network<br>Please refer to General Transit Feed Specification documentation for<br>more details.|
|**Update Freq:**|Ad hoc|Ad hoc|
|**Response**|**Response**|**Response**|
|**Attributes**|**Description**|**Example**|
|Link|• Link for downloading this file.<br>• Link will expire after 15 minutes.|_https://dmprod-_<br>_datasets.s3.ap-southeast-_<br>_1.amazonaws.com/train-_<br>_gtfs-real-_<br>_time/gtfs_realtime.pb?X-_<br>_Amz-Security-_<br>_Token=IQoJb3JpZ2luX2VjE._<br>_.._|

### 2.33 GTFS REALTIME (TRAIN TRIP UPDATES - DISRUPTION)

https://datamall2.mytransport.sg/ltaodataservice/GTFSRealtimeTrainTrip
**URL **Updates

GTFS Realtime (Train Trip Updates - Disruption) is a feed specification that provides real-time arrival/departure predictions, delays, cancellations for scheduled trips during train service disruptions. **Description **Examples of information provided:

Trip updates – delays, cancellations

Please refer to General Transit Feed Specification documentation for more details. **Update Freq **Ad hoc **Response ****Attributes ** **Description ** **Example **

Link - Link for downloading this file. _https://dmprod-_

_datasets.s3.ap-southeast-_

           - Link will expire after 15 minutes.

_1.amazonaws.com/train-gtfs-_

_trip-_

_update/gtfs_trip_update.pb?X-_

_Amz-Security-_

_Token=IQoJb3JpZ2luX2VjE..._

|URL|https://datamall2.mytransport.sg/ltaodataservice/GTFSRealtimeTrainTrip<br>Updates|Col3|
|---|---|---|
|**Description**|GTFS Realtime (Train Trip Updates - Disruption) is a feed specification<br>that provides real-time arrival/departure predictions, delays,<br>cancellations for scheduled trips during train service disruptions.<br>Examples of information provided:<br>Trip updates – delays, cancellations<br>Please refer to General Transit Feed Specification documentation for<br>more details.|GTFS Realtime (Train Trip Updates - Disruption) is a feed specification<br>that provides real-time arrival/departure predictions, delays,<br>cancellations for scheduled trips during train service disruptions.<br>Examples of information provided:<br>Trip updates – delays, cancellations<br>Please refer to General Transit Feed Specification documentation for<br>more details.|
|**Update Freq:**|Ad hoc|Ad hoc|
|**Response**|**Response**|**Response**|
|**Attributes**|**Description**|**Example**|
|Link|• Link for downloading this file.<br>• Link will expire after 15 minutes.|_https://dmprod-_<br>_datasets.s3.ap-southeast-_<br>_1.amazonaws.com/train-gtfs-_<br>_trip-_<br>_update/gtfs_trip_update.pb?X-_<br>_Amz-Security-_<br>_Token=IQoJb3JpZ2luX2VjE..._|

### ANNEX A

**SAMPLE OUTPUT FOR 2.5 PASSENGER VOLUME BY BUS STOPS AND 2.8 PASSENGER **
**VOLUME BY TRAIN STATIONS **The batch file follows a variant of the generic comma-separated-values (CSV) format. **SYNTAX **YEAR_MONTH, DAY_TYPE, TIME_PER_HOUR, PT_TYPE, PT_CODE, TOTAL_TAP_IN_VOLUME,
TOTAL_TAP_OUT_VOLUME \n **DELIMITERS **,     common delimiter to separate values \n     not a delimiter, but the ‘next line’ character to denote the end of a record **SAMPLE FOR BUS **2018-05, WEEKDAY, 20, BUS, 50199, 853, 834
2018-05, WEEKENDS/HOLIDAY, 20, BUS, 50199, 459, 297 **SAMPLE FOR TRAIN **2018-05, WEEKDAY, 15, TRAIN, EW14-NS26, 56019, 37614
2018-05, WEEKENDS/HOLIDAY, 15, TRAIN, EW14-NS26, 13385, 10878

Note

   - Explanation of the sample Bus record: For all weekdays in May 2018, from 2000hrs to 2059hrs, at Bus
Stop 50199, Opp Shaw Plaza, the total passenger volume of tap in and tap out are 853 and 834 respectively.

   - TIME_PER_HOUR refers to the hour of the day. E.g. 15 = 1500hrs to 1559hrs

   - For some Train interchanges, the station codes will be merged and considered as one station (E.g.
EW14-NS26 refers to Raffles Place station)

   - To find out more information about bus stops, please refer to Bus Stop API.

   - To find out more information about train stations, please refer to Train Station Codes and Chinese **[Names.csv in DataMall Portal under Public Transport section.](http://www.mytransport.sg/content/mytransport/home/dataMall.html)**59

### ANNEX B **SAMPLE OUTPUT FOR 2.6 PASSENGER VOLUME BY ORIGIN DESTINATION BUS STOPS AND 2.7 PASSENGER VOLUME BY ORIGIN **
**DESTINATION TRAIN STATIONS **The batch file follows a variant of the generic comma-separated-values (CSV) format. **SYNTAX **YEAR_MONTH, DAY_TYPE, TIME_PER_HOUR, PT_TYPE, ORIGIN_PT_CODE, DESTINATION_PT_CODE, TOTAL_TRIPS \n **DELIMITERS **,     common delimiter to separate values
\n     not a delimiter, but the ‘next line’ character to denote the end of a record **SAMPLE FOR BUS **2018-05, WEEKDAY, 16, BUS, 28299, 28009, 63
2018-05, WEEKENDS/HOLIDAY, 16, BUS, 28299, 28009, 103 **SAMPLE FOR TRAIN **2018-05, WEEKDAY, 17, TRAIN, CC28, CC1-NE6-NS24, 111
2018-05, WEEKENDS/HOLIDAY, 17, TRAIN, CC28, CC1-NE6-NS24, 39

Note

   - Explanation of the sample Train record: For all weekdays in May 2018, from 1700hrs to 1759hrs, the total number of passenger trips made from CC28, Telok
Blangah station, to CC1-NE6-NS24, Dhoby Ghaut station, are 111.

   - TIME_PER_HOUR refers to the hour of the day. E.g. 16 = 1600hrs to 1659hrs

   - For some Train interchanges, the station codes will be merged and considered as one station (E.g. CC1-NE6-NS24 refers to Dhoby Ghaut station)

   - To find out more information about bus stops, please refer to Bus Stop API.

   - [To find out more information about train stations, please refer to Train Station Codes and Chinese Names.csv in DataMall Portal under Public Transport section.](http://www.mytransport.sg/content/mytransport/home/dataMall.html)

### ANNEX C **SAMPLE SCENARIOS FOR 2.11 TRAIN SERVICE ALERTS API **Once the train is unavailable, you may expect the Train Service Alert API response to be
displayed according to the steps below.

1. Activate contingency mode
2. Publish message
3. Edit activated contingency mode (optional)
4. Publish new message (optional)
5. Train Service Recover
6. Publish recover message (optional)

During normal scenario (No train Disruption)

61 **Sample Scenario #1 - Single Line affected **This scenario depicts

a. NEL – Boon Keng to Dhoby Ghaut, towards Harbourfront station

b. Free public bus services and free MRT shuttle (towards Harbourfront station)**Step 1: Activate contingency mode -** **NEL – Boon Keng to Dhoby Ghaut, towards Harbourfront station **62 **Step 2: Publish new message ****Step 3: Edit activated contingency mode – Free Public Bus Service and free MRT Shuttle Service (towards HarbourFront)**63 **Step 4: Publish new message **64 **Step 5: Train service recover with Free Public Bus and MRT shuttle still available **65 **Step 6: Publish new message **66 **Step 7: After bus rides are ceased (no new published message)**67 **Sample Scenario #2 - Multi Lines affected **This scenario depicts 3 lines: North South Line, East West Line, and Downtown Line are down.

a. North South Line – between Bishan and Woodlands, towards Jurong East Station

a. East West Line – between Paya Lebar and Pasir Ris, both direction

b. MRT Shuttle Services that run along four predefined areas in both directions

c. Downtown Line – between Downtown and Beauty World, both directions

d. Free Bus Island-wide **Step 1: Activate contingency mode – North South Line down with ** **new ** **message published **68 **Step 2: Edit activated contingency mode –East West Line and North South line are down with new message published **69 **Step 3: Edit activated contingency mode - Activate MRT shuttle services to run along four predefined areas in both directions ** **(no new message published)**70 **Step 4: Edit activated contingency mode – In addition to North South, East West lines, Downtown line is also down with new message published **71 **Step 5: Edit activated contingency mode –Activate Free bus service island-wide with new message published **72 **Step 6: Train service recover – North South and East West line recover with new message published **73 **Step 7: Train service recover – Downtown line recovers, free public bus service and MRT shuttle are still available with new message published **74 **Step 8: Train service recover – Free public bus service and MRT shuttle have ceased ****Step 9: Train service recover - After message has expired **75 **2.2 Train Delay **This scenario depicts there is a delay at Seng Kang West LRT (West Loop). **Step 1: New message published (Contingency mode is not activated)****Step 2: Train Service Resumes **76

### ANNEX D **ZONE ID ATTRIBUTE TO SPECIFIC ERP GANTRY/GANTRIES FOR ERP RATES ****ERP **
**Gantry ****Zone ID ** **No. ** **ERP Gantry Location **BMC 1 Victoria Street
BMC 2 Nicoll Highway CBD 3 Eu Tong Sen Street OC1 4 Orchard Link CBD 5 Lim Teck Kim Road CBD 6 Anson Road CBD 7 Tanjong Pagar Road BMC 9 Bencoolen Street BMC 10 Queen Street BMC 11 North Bridge Road OC1 12 Oxley Road OC1 13 Orchard Road OC1 14 Orchard Turn OC1 15 Killiney Road BMC 16 Beach Road BMC 17 Temasek Boulevard BMC 18 Republic Boulevard CBD 19 Havelock Road/Clemenceau Ave CBD 20 Havelock Road/CTE Exit OC1 21 Buyong Road OC1 22 Kramat Road BMC 23 River Valley Road CBD 24 Merchant Road/Clemenceau Ave CBD 25 Merchant Road/CTE Exit OC1 26 Clemenceau Ave OC1 27 Cairnhill Road CBD 28 Central Boulevard

Slip Road from Westbound MCE towards Maxwell CBD 29 Road EC1 30 ECP to City CT1 31 CTE after Braddell Road PE1 32 PIE after Kallang Bahru on Woodsville Flyover

|Zone ID|ERP<br>Gantry<br>No.|ERP Gantry Location|
|---|---|---|
|BMC|1|Victoria Street|
|BMC|2|Nicoll Highway|
|CBD|3|Eu Tong Sen Street|
|OC1|4|Orchard Link|
|CBD|5|Lim Teck Kim Road|
|CBD|6|Anson Road|
|CBD|7|Tanjong Pagar Road|
|BMC|9|Bencoolen Street|
|BMC|10|Queen Street|
|BMC|11|North Bridge Road|
|OC1|12|Oxley Road|
|OC1|13|Orchard Road|
|OC1|14|Orchard Turn|
|OC1|15|Killiney Road|
|BMC|16|Beach Road|
|BMC|17|Temasek Boulevard|
|BMC|18|Republic Boulevard|
|CBD|19|Havelock Road/Clemenceau Ave|
|CBD|20|Havelock Road/CTE Exit|
|OC1|21|Buyong Road|
|OC1|22|Kramat Road|
|BMC|23|River Valley Road|
|CBD|24|Merchant Road/Clemenceau Ave|
|CBD|25|Merchant Road/CTE Exit|
|OC1|26|Clemenceau Ave|
|OC1|27|Cairnhill Road|
|CBD|28|Central Boulevard|
|CBD|29|Slip Road from Westbound MCE towards Maxwell<br>Road|
|EC1|30|ECP to City|
|CT1|31|CTE after Braddell Road|
|PE1|32|PIE after Kallang Bahru on Woodsville Flyover|

CT1 33 CTE from Serangoon Road CT1 34 CTE from Balestier Road CT4 35 CTE before Braddell Road AY1 36 AYE to City before Alexandra Road PE2 37 PIE to Changi after Adam Road Exit PE2 38 PIE to Changi / Whitley Road THM 39 Thomson Road after Toa Payoh Rise OR1 40 Bendemeer Road AYT 41 AYE to Tuas Before Clementi Road PE3 42 PIE into CTE
DZ1 43 Dunearn Road / Wayang Satu Flyover DZ1 44 Dunearn Road / Whitley Road PE1 45 PIE slip road to Bendemeer Road CT5 46 CTE Northbound after PIE
OC2 47 Orchard Road after YMCA
OC3 48 Orchard Road after Handy Road OC2 49 Fort Canning Tunnel KP2 50 KPE Southbound after Defu Flyover CT6 51 CTE Northbound before exit to PIE
AYC 52 Clementi Avenue 6 into AYE (City)
AYC 53 Clementi Avenue 2 into AYE (City)

Bt Timah Expressway (Sb betw Dairy Farm Rd and BKE 54 PIE)
UBT 55 Upper Bt Timah Rd Southbound after Hume Ave TPZ 56 Toa Payoh Lorong 6
KBZ 57 Kallang Bahru GBZ 58 Geylang Bahru BKZ 59 Upper Boon Keng Road SR2 60 Eu Tong Sen Street at Central SR1 61 New Bridge Road before Upper Circular Road SR1 62 South Bridge Road before Upper Circular Road SR2 63 Fullerton Road eastbound at Fullerton Hotel SR1 64 Fullerton Road westbound at One Fullerton PE4 65 PIE westbound before Eunos Link SR2 66 Bayfront Avenue towards Raffles Avenue CT5 67 PIE to CTE Northbound before Braddell Road CT2 68 CTE slip road to PIE (Changi) / Serangoon Road SR1 69 Bayfront Avenue Towards Marina Boulevard KAL 70 Geylang Road OR1 71 Woodsville Tunnel CBD 72 Sheares Avenue towards Sheares Link EC3 73 ECP eastbound before exit to KPE

|CT1|33|CTE from Serangoon Road|
|---|---|---|
|CT1|34|CTE from Balestier Road|
|CT4|35|CTE before Braddell Road|
|AY1|36|AYE to City before Alexandra Road|
|PE2|37|PIE to Changi after Adam Road Exit|
|PE2|38|PIE to Changi / Whitley Road|
|THM|39|Thomson Road after Toa Payoh Rise|
|OR1|40|Bendemeer Road|
|AYT|41|AYE to Tuas Before Clementi Road|
|PE3|42|PIE into CTE|
|DZ1|43|Dunearn Road/ Wayang Satu Flyover|
|DZ1|44|Dunearn Road/ Whitley Road|
|PE1|45|PIE slip road to Bendemeer Road|
|CT5|46|CTE Northbound after PIE|
|OC2|47|Orchard Road after YMCA|
|OC3|48|Orchard Road after Handy Road|
|OC2|49|Fort Canning Tunnel|
|KP2|50|KPE Southbound after Defu Flyover|
|CT6|51|CTE Northbound before exit to PIE|
|AYC|52|Clementi Avenue 6 into AYE(City)|
|AYC|53|Clementi Avenue 2 into AYE(City)|
|BKE|54|Bt Timah Expressway (Sb betw Dairy Farm Rd and<br>PIE)|
|UBT|55|Upper Bt Timah Rd Southbound after Hume Ave|
|TPZ|56|Toa Payoh Lorong 6|
|KBZ|57|Kallang Bahru|
|GBZ|58|Geylang Bahru|
|BKZ|59|Upper Boon Keng Road|
|SR2|60|Eu Tong Sen Street at Central|
|SR1|61|New Bridge Road before Upper Circular Road|
|SR1|62|South Bridge Road before Upper Circular Road|
|SR2|63|Fullerton Road eastbound at Fullerton Hotel|
|SR1|64|Fullerton Road westbound at One Fullerton|
|PE4|65|PIE westbound before Eunos Link|
|SR2|66|Bayfront Avenue towards Raffles Avenue|
|CT5|67|PIE to CTE Northbound before Braddell Road|
|CT2|68|CTE slip road to PIE(Changi) / Serangoon Road|
|SR1|69|Bayfront Avenue Towards Marina Boulevard|
|KAL|70|Geylang Road|
|OR1|71|Woodsville Tunnel|
|CBD|72|Sheares Avenue towards Sheares Link|
|EC3|73|ECP eastbound before exit to KPE|

AYC 74 AYE to City Before Clementi Avenue 6
KP1 80 KPE Southbound exit to ECP (City)
MC1 90 MCE westbound exit to Marina Coastal Drive MC1 91 MCE westbound before exit to Maxwell Road MC2 92 Marina Boulevard to MCE eastbound MC2 93 MCE eastbound before exit to Central Boulevard

|AYC|74|AYE to City Before Clementi Avenue 6|
|---|---|---|
|KP1|80|KPE Southbound exit to ECP(City)|
|MC1|90|MCE westbound exit to Marina Coastal Drive|
|MC1|91|MCE westbound before exit to Maxwell Road|
|MC2|92|Marina Boulevard to MCE eastbound|
|MC2|93|MCE eastbound before exit to Central Boulevard|

### ANNEX E **GEOSPATIAL WHOLE ISLAND LAYER ID FOR 2.22 GEOSPATIAL WHOLE ISLAND ****S/No Geospatial Whole Island Layers ** **ID **1. Arrow Marking ArrowMarking
2. Bollard Bollard
3. Bus Stop Location BusStopLocation
4. Control Box ControlBox
5. Convex Mirror ConvexMirror
6. Covered Link Way CoveredLinkWay
7. Cycling Path CyclingPath
8. Detector Loop DetectorLoop
9. ERP Gantry ERPGantry
10. Footpath Footpath
11. Guard Rail GuardRail
12. Kerb Line KerbLine
13. Lamp Post LampPost
14. Lane Marking LaneMarking
15. Parking Standards Zone ParkingStandardsZone
16. Passenger Pickup Bay PassengerPickupBay
17. Pedestrain Overheadbridge / Underpass PedestrainOverheadbridge_UnderPass
18. Rail Construction RailConstruction
19. Railing Railing
20. Retaining Wall RetainingWall
21. Road Crossing RoadCrossing
22. Road Hump RoadHump
23. Road Section Line RoadSectionLine
24. School Zone SchoolZone
25. Silver Zone SilverZone
26. Speed Regulating Strip SpeedRegulatingStrip
27. Street Paint StreetPaint
28. Taxi Stand TaxiStand
29. Traffic Light TrafficLight
30. Traffic Sign TrafficSign
31. Train Station TrainStation
32. Train Station Exit TrainStationExit
33. Vehicular Bridge / Flyover / Underpass VehicularBridge_Flyover_Underpass
34. Word Marking WordMarking

|S/No|Geospatial Whole Island Layers|ID|
|---|---|---|
|1.|Arrow Marking|ArrowMarking|
|2.|Bollard|Bollard|
|3.|Bus Stop Location|BusStopLocation|
|4.|Control Box|ControlBox|
|5.|Convex Mirror|ConvexMirror|
|6.|Covered Link Way|CoveredLinkWay|
|7.|Cycling Path|CyclingPath|
|8.|Detector Loop|DetectorLoop|
|9.|ERP Gantry|ERPGantry|
|10.|Footpath|Footpath|
|11.|Guard Rail|GuardRail|
|12.|Kerb Line|KerbLine|
|13.|Lamp Post|LampPost|
|14.|Lane Marking|LaneMarking|
|15.|Parking Standards Zone|ParkingStandardsZone|
|16.|Passenger Pickup Bay|PassengerPickupBay|
|17.|Pedestrain Overheadbridge / Underpass|PedestrainOverheadbridgeUnderPass|
|18.|Rail Construction|_<br>RailConstruction|
|19.|Railing|Railing|
|20.|Retaining Wall|RetainingWall|
|21.|Road Crossing|RoadCrossing|
|22.|Road Hump|RoadHump|
|23.|Road Section Line|RoadSectionLine|
|24.|School Zone|SchoolZone|
|25.|Silver Zone|SilverZone|
|26.|Speed Regulating Strip|SpeedRegulatingStrip|
|27.|Street Paint|StreetPaint|
|28.|Taxi Stand|TaxiStand|
|29.|Traffic Light|TrafficLight|
|30.|Traffic Sign|TrafficSign|
|31.|Train Station|TrainStation|
|32.|Train Station Exit|TrainStationExit|
|33.|Vehicular Bridge / Flyover/ Underpass|VehicularBridgeFlyoverUnderpass|
|34.|Word Marking|__<br>WordMarking|

### ANNEX F **DESCRIPTION OF ROAD CATEGORIES FOR 2.26 TRAFFIC FLOW ****S/No Road Category ** **Description **1. CAT1 Expressways
Form the primary network where all long-distance traffic movements should be directed. It is planned to optimise long distance mobility from one part of the island to another
2. CAT2 Major Arterials
Predominantly carry through traffic from one region to another, forming principal avenues of communication for urban traffic movements. It interconnects expressways and minor arterial as well as with other major arterial roads
3. CAT3 Minor Arterials
Distribute traffic within the major residential and industrial areas. It is planned to optimise circulation within the area and facilitate through traffic between adjacent towns
4. CAT4 Primary Accesses
Form the link between local accesses and arterial roads. It provides access to developments and through traffic is discouraged. However, where a development is also accessible by a local access road, the access shall be located at the local access road
5. CAT5 Local Accesses
Give direct access to buildings and other developments and should connect only with primary access
6. SLIP_ROAD Slip Roads
Connect roads to allow motorists to change roads without entering an intersection

|S/No|Road Category|Description|
|---|---|---|
|1.|CAT1|Expressways<br>Form the primary network where all long-distance traffic<br>movements should be directed. It is planned to optimise<br>long distance mobility from onepart of the island to another|
|2.|CAT2|Major Arterials<br>Predominantly carry through traffic from one region to<br>another, forming principal avenues of communication for<br>urban traffic movements. It interconnects expressways and<br>minor arterial as well as with other major arterial roads|
|3.|CAT3|Minor Arterials<br>Distribute traffic within the major residential and industrial<br>areas. It is planned to optimise circulation within the area<br>and facilitate through traffic between adjacent towns|
|4.|CAT4|Primary Accesses<br>Form the link between local accesses and arterial roads. It<br>provides access to developments and through traffic is<br>discouraged. However, where a development is also<br>accessible by a local access road, the access shall be located<br>at the local access road|
|5.|CAT5|Local Accesses<br>Give direct access to buildings and other developments and<br>should connect only withprimary access|
|6.|SLIP_ROAD|Slip Roads<br>Connect roads to allow motorists to change roads without<br>entering an intersection|

### ANNEX G **LOCATION DESCRIPTION OF CAMERA ID FOR 2.17 TRAFFIC IMAGES ****Camera ID ** **Location Description **
2701 Woodlands Causeway (Towards Johor)
2702 Woodlands Checkpoint 2704 BKE (Woodlands Checkpoint) - Woodlands F/O
4703 Tuas Second Link 4712 AYE(Tuas) - Tuas Ave 8 Exit 4713 Tuas Checkpoint 4798 Sentosa Tower 1
4799 Sentosa Tower 2

|Camera ID|Location Description|
|---|---|
|2701|Woodlands Causeway (Towards Johor)|
|2702|Woodlands Checkpoint|
|2704|BKE(Woodlands Checkpoint) - Woodlands F/O|
|4703|Tuas Second Link|
|4712|AYE(Tuas) - Tuas Ave 8 Exit|
|4713|Tuas Checkpoint|
|4798|Sentosa Tower 1|
|4799|Sentosa Tower 2|
