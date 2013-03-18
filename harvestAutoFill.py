#\
# Created with PyCharm.
# User: mkelly
# Date: 3/15/13
# Time: 4:19 PM
# 
# Description:  Autopopulates Harvest Timesheet for current day.
#
#/
__author__ = 'mkelly'


import harvest
import random

DEBUG=False

Tasks = {
    'Architecture':'1842336',
    'Documentation':'1842326',
    'Research': '1842317',
    'Strategy':'1842352',
    'Admin':'1819029',
    'Planning':'1842319',
    'Vendor Management':'1842320'
}

#Project ID for Cloud Platform (Shared Platforms)
ProjectID = '3339844'

MaxHoursPerDay=8
HarvestURL="https://scrippsnetworksdigital.harvestapp.com"
HarvestEmail="mark.kelly@scrippsnetworks.com"
HarvestPassword="mek26811"

ValidTimeEntries = [0, .5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8]

try:
    mytime=harvest.Harvest(HarvestURL,HarvestEmail,HarvestPassword)
    print mytime.status()
except:
    print "Cannot connect to Harvest"

#Sample add line:
#data = {"notes":"test note", "project_id":"3339844","hours":"1.0", "task_id": "1842326","spent_at": "2013-03-14" }

# data = {"project_id":"3339844","hours":"1.0", "task_id": "1842326"}
# if DEBUG is False:
#     success=mytime.add(data)
#     if success=None:
#         print "Error Adding data to Harvest"
#     print success

#Determine Split for the day
# set .5 hours to admin time
#
#Total for the Day should be this:
TotalTime=8
AdminTime=.5
#Track hours allocated so far
MaxUsedTime=0+AdminTime
AvailableTime=TotalTime-AdminTime

data = {"project_id":"3339844","hours":str(AdminTime), "task_id": Tasks['Admin']}
if DEBUG is False:
    success=mytime.add(data)
    if success is None:
        print "Error Adding data to Harvest"
    print success
print data
#Documentation
# Set it to be 0 - 1 hours for now
DocumentationRange=random.randint(0, 2)
#Maximum possible = 1.5 hours so far
DocumentationTime=ValidTimeEntries[DocumentationRange]
AvailableTime=AvailableTime-DocumentationTime
data = {"project_id":"3339844","hours":str(DocumentationTime), "task_id": Tasks['Documentation']}
if DEBUG is False and DocumentationTime > 0:
    success=mytime.add(data)
    if success is None:
        print "Error Adding data to Harvest"
    print success
print data
# Architecture
# Set it to be .5 - 1.5 hours for now
ArchitectureRange=random.randint(1, 3)
#Maximum possible = 3 hours so far
ArchitectureTime=ValidTimeEntries[ArchitectureRange]
AvailableTime=AvailableTime-ArchitectureTime
data = {"project_id":"3339844","hours":str(ArchitectureTime), "task_id": Tasks['Architecture']}
if DEBUG is False and ArchitectureTime > 0:
    success=mytime.add(data)
    if success is None:
        print "Error Adding data to Harvest"
    print success
print data
# Planning
# Set it to be 1 - 3 hours for now
PlanningRange=random.randint(2, 6)
#Maximum possible = 6 hours so far
PlanningTime=ValidTimeEntries[PlanningRange]
AvailableTime=AvailableTime-PlanningTime
data = {"project_id":"3339844","hours":str(PlanningTime), "task_id": Tasks['Planning']}
if DEBUG is False and PlanningTime > 0:
    success=mytime.add(data)
    if success is None:
        print "Error Adding data to Harvest"
    print success
print data
# Strategy
# Set it to be .5 - 2 hours for now
StrategyRange=random.randint(1, 4)
#Maximum possible = 8 hours so far
StrategyTime=ValidTimeEntries[StrategyRange]
AvailableTime=AvailableTime-StrategyTime
data = {"project_id":"3339844","hours":str(StrategyTime), "task_id": Tasks['Strategy']}
if DEBUG is False and StrategyTime > 0:
    success=mytime.add(data)
    if success is None:
        print "Error Adding data to Harvest"
    print success
print data
if AvailableTime>0:
    # Research
    # Set it to be .5 - 2 hours for now
    ResearchRange=random.randint(1, 4)
    #Maximum possible = 11 hours so far
    ResearchTime=ValidTimeEntries[ResearchRange]
    if ResearchTime>AvailableTime:
        ResearchTime=AvailableTime
    AvailableTime=AvailableTime-ResearchTime
    data = {"project_id":"3339844","hours":str(ResearchTime), "task_id": Tasks['Research']}
    if DEBUG is False and ResearchTime > 0:
       success=mytime.add(data)
       if success is None:
        print "Error Adding data to Harvest"
       print success
    print data
if AvailableTime>0:
    # Vendor Management
    # Set it to be 0 - 2 hours for now
    VendorManagementRange=random.randint(0, 4)
    #Maximum possible = 13 hours so far
    VendorManagementTime=ValidTimeEntries[VendorManagementRange]
    if VendorManagementTime>AvailableTime:
        VendorManagementTime=AvailableTime
    AvailableTime=AvailableTime-VendorManagementTime

    data = {"project_id":"3339844","hours":str(VendorManagementTime), "task_id": Tasks['Vendor Management']}
    if DEBUG is False and VendorManagementTime > 0:
        success=mytime.add(data)
        if success is None:
            print "Error Adding data to Harvest"
        print success
    print data

# All Tasks have been used, now need to check and see if any left over time
if AvailableTime>0:
    #Let's add left over time to Architecture for the day
    data = {"project_id":"3339844","hours":str(AvailableTime), "task_id": Tasks['Architecture']}
    if DEBUG is False and AvailableTime > 0:
        success=mytime.add(data)
        if success is None:
            print "Error Adding data to Harvest"
        print success
    print data
print AvailableTime