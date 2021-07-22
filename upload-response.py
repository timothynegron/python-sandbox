def uploadResponse(data):
    
    jsonData = json.loads(data)
    registrants = jsonData['registrants']
    
    newRegistrantsList = createCompleteRegistrantList(registrants)
    
    # Create temporary file and csv writer object
    f = open("/tmp/csv_file.csv", "w+")
    temp_csv_file = csv.writer(f)
    
    # writing the column names
    temp_csv_file.writerow(['firstname', 
                            'lastname', 
                            'company', 
                            'zip',
                            'workphone',
                            'companyindustry',
                            'eventid',
                            'eventuserid',
                            'std1',
                            'std2',
                            'std3',
                            'std4',
                            'std5',
                            'std6',
                            'std7',
                            'std8',
                            'std9',
                            'std10',
                            'marketingemail',
                            'eventemail',
                            'userprofileurl',
                            'createtimestamp',
                            'lastactivity',
                            'ipaddress',
                            'os',
                            'browser',
                            'emailformat',
                            'engagementprediction',
                            'compaigncode',
                            'sourcecampaigncode',
                            'sourceeventid',
                            'userstatus'])
    
    for registrant in newRegistrantsList:
        temp_csv_file.writerow([registrant['firstname'],
                                registrant['lastname'],
                                registrant['company'],
                                registrant['zip'],
                                registrant['workphone'],
                                registrant['companyindustry'],
                                registrant['eventid'],
                                registrant['eventuserid'],
                                registrant['std1'],
                                registrant['std2'],
                                registrant['std3'],
                                registrant['std4'],
                                registrant['std5'],
                                registrant['std6'],
                                registrant['std7'],
                                registrant['std8'],
                                registrant['std9'],
                                registrant['std10'],
                                registrant['marketingemail'],
                                registrant['eventemail'],
                                registrant['userprofileurl'],
                                registrant['createtimestamp'],
                                registrant['lastactivity'],
                                registrant['ipaddress'],
                                registrant['os'],
                                registrant['browser'],
                                registrant['emailformat'],
                                registrant['engagementprediction'],
                                registrant['compaigncode'],
                                registrant['sourcecampaigncode'],
                                registrant['sourceeventid'],
                                registrant['userstatus']
                                ])
    
    f.close()
    
    client = boto3.client('s3')
    client.upload_file('/tmp/csv_file.csv', 'S3 BUCKET NAME','FILENAMETOBUCKET.csv')
    
    return ''

def createCompleteRegistrantList(registrants):
    
    newRegistrantsList = []
    
    kList = ['firstname', 
            'lastname', 
            'company', 
            'zip',
            'workphone',
            'companyindustry',
            'eventid',
            'eventuserid',
            'std1',
            'std2',
            'std3',
            'std4',
            'std5',
            'std6',
            'std7',
            'std8',
            'std9',
            'std10',
            'marketingemail',
            'eventemail',
            'userprofileurl',
            'createtimestamp',
            'lastactivity',
            'ipaddress',
            'os',
            'browser',
            'emailformat',
            'engagementprediction',
            'compaigncode',
            'sourcecampaigncode',
            'sourceeventid',
            'userstatus']
    
    index = -1
    
    for registrant in registrants:
        index += 1
        newRegistrantsList.append({})
        for i in range(0, len(kList)):
            for key in registrant:
                if kList[i] == key:
                    newRegistrantsList[index][key] = registrant[key]
                    break
                elif key == 'userstatus':
                    newRegistrantsList[index][kList[i]] = ''
        
    return newRegistrantsList
